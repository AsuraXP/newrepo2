#!/usr/bin/env bash
# ==============================================================================
# STATE 6 KAGGLE RUNNER — apocalypse_day3_video
# Branch: arena/24ef2530-newrepo2
#
# Performs (ONLY on Kaggle):
#   1. Installs ffmpeg, edge-tts, and pillow
#   2. Clones / updates branch arena/24ef2530-newrepo2
#   3. Strict preflight checks (files, all 90 PNG frames, Edge-TTS voice)
#   4. Per-beat grouping from visuals.csv + ONE continuous Edge-TTS take
#      (en-US-AndrewNeural, --rate=+10%, explicit WordBoundary timestamps)
#   5. PIL pre-pad of all frames onto even-dimension max-W/H black RGB canvas
#      at (0,0) saved as PNG (optimize=False, compress_level=6)
#   6. FFmpeg concat stitch at native pre-padded resolution without post-concat
#      video resizing or letterboxing filters, -14 LUFS loudnorm, AAC 192k,
#      30fps, libx264 yuv420p
#   7. Packages VIDEO.mp4, thumbnail.jpg, metadata.json, script.md, youtube.txt
#      into apocalypse_day3_DELIVERABLE.zip
# ==============================================================================
set -euo pipefail

SLUG="apocalypse_day3"
PROJECT_SUBDIR="${SLUG}_video"
REPO_URL="https://github.com/AsuraXP/newrepo2.git"
BRANCH="arena/24ef2530-newrepo2"
VOICE="en-US-AndrewNeural"
RATE="+10%"

echo "=================================================================="
echo " [${SLUG}] Step 1/6: Installing system & Python dependencies..."
echo "=================================================================="
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg
  else
    echo "FATAL: ffmpeg/ffprobe not found and apt-get is unavailable." >&2
    exit 1
  fi
fi

python3 -m pip install -q --upgrade edge-tts pillow

echo "=================================================================="
echo " [${SLUG}] Step 2/6: Resolving / updating repository (${BRANCH})..."
echo "=================================================================="
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -d "${SCRIPT_DIR}/${PROJECT_SUBDIR}" ]; then
  REPO_DIR="${SCRIPT_DIR}"
  if [ -d "${REPO_DIR}/.git" ]; then
    git -C "${REPO_DIR}" pull --ff-only origin "${BRANCH}" || \
      echo "INFO: Using current local checkout at ${REPO_DIR}"
  fi
else
  BASE_WORK="/kaggle/working"
  if [ ! -d "${BASE_WORK}" ]; then
    BASE_WORK="$(pwd)"
  fi
  REPO_DIR="${BASE_WORK}/newrepo2"
  if [ -d "${REPO_DIR}/.git" ]; then
    git -C "${REPO_DIR}" fetch --depth 1 origin "${BRANCH}"
    git -C "${REPO_DIR}" checkout -f "${BRANCH}"
    git -C "${REPO_DIR}" reset --hard "origin/${BRANCH}"
  else
    rm -rf "${REPO_DIR}"
    git clone --depth 1 --branch "${BRANCH}" "${REPO_URL}" "${REPO_DIR}"
  fi
fi

if [ -d "/kaggle/working" ]; then
  OUT_ROOT="/kaggle/working"
else
  OUT_ROOT="$(pwd)"
fi

BUILD_DIR="${OUT_ROOT}/${SLUG}_build"
STAGE_DIR="${BUILD_DIR}/deliverable_stage"
PAD_DIR="${BUILD_DIR}/padded_frames"
rm -rf "${BUILD_DIR}"
mkdir -p "${STAGE_DIR}" "${PAD_DIR}"

export REPO_DIR PROJECT_SUBDIR SLUG VOICE RATE BUILD_DIR STAGE_DIR PAD_DIR OUT_ROOT

echo "=================================================================="
echo " [${SLUG}] Steps 3–6: Preflight, Edge-TTS, PIL Pre-Pad & FFmpeg..."
echo "=================================================================="

python3 - <<'PYEOF'
import asyncio
import csv
import difflib
import inspect
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

from PIL import Image
import edge_tts

TICKS_PER_SECOND = 10_000_000.0
EDGE_PUNCT = ".,;:!?\"'()[]{}<>\u2014\u2013\u201c\u201d\u2018\u2019\u00ab\u00bb\u2026*#|/\\"


def die(msg: str) -> None:
    print(f"\n[PREFLIGHT / PIPELINE FATAL] {msg}", file=sys.stderr)
    sys.exit(1)


def norm_word(token: str) -> str:
    w = token.casefold().strip(EDGE_PUNCT)
    w = w.replace("\u2019", "'").replace("\u2018", "'")
    w = w.replace("\u2014", "-").replace("\u2013", "-")
    return w


def probe_duration(media_path: Path) -> float:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(media_path),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        die(f"ffprobe failed on {media_path}: {res.stderr.strip()}")
    try:
        dur = float(res.stdout.strip())
    except ValueError:
        die(f"ffprobe returned non-numeric duration for {media_path}: {res.stdout!r}")
    if dur <= 0:
        die(f"ffprobe measured non-positive duration ({dur}) for {media_path}")
    return dur


def fmt_mmss(sec: float) -> str:
    total = max(0, int(round(sec)))
    m, s = divmod(total, 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


repo_dir = Path(os.environ["REPO_DIR"]).resolve()
proj_dir = repo_dir / os.environ["PROJECT_SUBDIR"]
slug = os.environ["SLUG"]
voice = os.environ["VOICE"]
rate = os.environ["RATE"]
build_dir = Path(os.environ["BUILD_DIR"]).resolve()
stage_dir = Path(os.environ["STAGE_DIR"]).resolve()
pad_dir = Path(os.environ["PAD_DIR"]).resolve()
out_root = Path(os.environ["OUT_ROOT"]).resolve()

# ------------------------------------------------------------------------------
# 1. STRICT PREFLIGHT CHECKS
# ------------------------------------------------------------------------------
for bin_name in ("ffmpeg", "ffprobe"):
    if shutil.which(bin_name) is None:
        die(f"Required binary '{bin_name}' is missing from PATH.")

required_files = [
    proj_dir / "visuals.csv",
    proj_dir / "script.md",
    proj_dir / "metadata.json",
    proj_dir / "youtube.txt",
    proj_dir / "thumbnail.jpg",
]
for rf in required_files:
    if not rf.is_file() or rf.stat().st_size == 0:
        die(f"Missing or empty required project file: {rf}")

with open(proj_dir / "visuals.csv", "r", encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    expected_cols = {"slide_id", "moment", "moment_text", "visual_prompt"}
    if not reader.fieldnames or not expected_cols.issubset(set(reader.fieldnames)):
        die(f"visuals.csv missing required columns {expected_cols}; got {reader.fieldnames}")
    rows = list(reader)

if len(rows) != 90:
    die(f"Expected 90 rows in visuals.csv, found {len(rows)}.")

frames_dir = proj_dir / "frames"
missing_frames = []
raw_sizes = []
frame_records = []

for idx, r in enumerate(rows):
    try:
        slide_id = int(r["slide_id"])
        moment_id = int(r["moment"])
    except (KeyError, ValueError) as exc:
        die(f"Invalid slide_id/moment at visuals.csv row {idx + 1}: {exc}")

    text = (r.get("moment_text") or "").strip()
    if not text:
        die(f"Empty moment_text at beat{slide_id:02d}m{moment_id:02d}")

    fpath = frames_dir / f"beat{slide_id:02d}m{moment_id:02d}.png"
    if not fpath.is_file() or fpath.stat().st_size == 0:
        missing_frames.append(str(fpath))
        continue

    try:
        with Image.open(fpath) as im:
            im.verify()
        with Image.open(fpath) as im2:
            raw_sizes.append(im2.size)
    except Exception as exc:
        die(f"Corrupt PNG frame {fpath}: {exc}")

    frame_records.append(
        {
            "idx": idx,
            "slide_id": slide_id,
            "moment": moment_id,
            "frame_name": fpath.name,
            "src_path": fpath,
            "moment_text": text,
        }
    )

if missing_frames:
    die(f"Missing {len(missing_frames)} frame(s): {missing_frames[:10]}")

print(f"[PREFLIGHT OK] Verified {len(frame_records)} frames and all project files.")


async def verify_and_synthesize(full_text: str, raw_audio_path: Path):
    voices = await edge_tts.list_voices()
    available = {v.get("ShortName") for v in voices}
    if voice not in available:
        die(f"Requested Edge-TTS voice '{voice}' not found in edge_tts.list_voices().")
    print(f"[PREFLIGHT OK] Voice '{voice}' verified available ({len(available)} total voices).")

    comm_kwargs = {"rate": rate}
    sig_params = inspect.signature(edge_tts.Communicate.__init__).parameters
    if "boundary" in sig_params:
        comm_kwargs["boundary"] = "WordBoundary"

    comm = edge_tts.Communicate(full_text, voice, **comm_kwargs)
    _texts = getattr(comm, "texts", None)
    if _texts is not None:
        try:
            _ = len(_texts)
        except TypeError:
            _, comm.texts = itertools.tee(_texts)

    events = []
    with open(raw_audio_path, "wb") as out_f:
        async for chunk in comm.stream():
            ctype = chunk.get("type")
            if ctype == "audio":
                out_f.write(chunk["data"])
            elif ctype in ("WordBoundary", "SentenceBoundary"):
                events.append(
                    {
                        "type": ctype,
                        "offset_s": float(chunk["offset"]) / TICKS_PER_SECOND,
                        "duration_s": float(chunk["duration"]) / TICKS_PER_SECOND,
                        "text": str(chunk.get("text", "")),
                    }
                )
    return events


# ------------------------------------------------------------------------------
# 2. PER-BEAT GROUPING & ONE CONTINUOUS EDGE-TTS TAKE
# ------------------------------------------------------------------------------
beats = defaultdict(list)
for rec in frame_records:
    beats[rec["slide_id"]].append(rec)

ordered_slide_ids = sorted(beats.keys())
slide_paragraphs = []
source_words = []  # list of dicts: {global_idx, row_idx, raw, norm}

for sid in ordered_slide_ids:
    beat_rows = beats[sid]
    para_parts = []
    for rec in beat_rows:
        para_parts.append(rec["moment_text"])
        tokens = [t for t in re.findall(r"\S+", rec["moment_text"]) if norm_word(t)]
        if not tokens:
            die(f"Row {rec['frame_name']} has zero speakable tokens: {rec['moment_text']!r}")
        rec["word_start_idx"] = len(source_words)
        for tok in tokens:
            source_words.append(
                {
                    "global_idx": len(source_words),
                    "row_idx": rec["idx"],
                    "raw": tok,
                    "norm": norm_word(tok),
                }
            )
        rec["word_end_idx"] = len(source_words) - 1
    slide_paragraphs.append(" ".join(para_parts))

full_narration_text = "\n\n".join(slide_paragraphs)
print(
    f"[TTS] Synthesizing ONE continuous take ({len(ordered_slide_ids)} beats, "
    f"{len(frame_records)} micro-moments, {len(source_words)} words) "
    f"with {voice} at {rate}..."
)

raw_mp3 = build_dir / "narration_raw.mp3"
events = asyncio.run(verify_and_synthesize(full_narration_text, raw_mp3))
if not raw_mp3.is_file() or raw_mp3.stat().st_size == 0:
    die("Edge-TTS produced empty audio output.")
if not events:
    die("Edge-TTS returned zero timing boundary events.")

# Normalize audio loudness to -14 LUFS BEFORE final duration lock so video and
# normalized audio durations match identically.
norm_wav = build_dir / "narration_loudnorm_14lufs.wav"
loudnorm_cmd = [
    "ffmpeg",
    "-hide_banner",
    "-loglevel",
    "error",
    "-y",
    "-i",
    str(raw_mp3),
    "-af",
    "loudnorm=I=-14:TP=-1.5:LRA=11",
    "-ar",
    "48000",
    "-ac",
    "2",
    str(norm_wav),
]
ln_res = subprocess.run(loudnorm_cmd, capture_output=True, text=True)
if ln_res.returncode != 0:
    die(f"FFmpeg loudnorm failed: {ln_res.stderr.strip()}")

total_audio_s = probe_duration(norm_wav)
print(
    f"[AUDIO OK] Raw TTS + -14 LUFS loudnorm complete: {total_audio_s:.3f}s "
    f"({total_audio_s / 60.0:.2f} min), {len(events)} boundary events."
)

# Expand boundary events into atomic normalized word tokens with timestamps
event_tokens = []
for ev in events:
    parts = [p for p in re.split(r"[\s\-]+", ev["text"]) if norm_word(p)]
    if not parts:
        continue
    n_p = len(parts)
    for k, p in enumerate(parts):
        t0 = ev["offset_s"] + ev["duration_s"] * (k / n_p)
        t1 = ev["offset_s"] + ev["duration_s"] * ((k + 1) / n_p)
        event_tokens.append({"norm": norm_word(p), "t_start": t0, "t_end": t1})

src_norms = [sw["norm"] for sw in source_words]
ev_norms = [et["norm"] for et in event_tokens]

matcher = difflib.SequenceMatcher(a=src_norms, b=ev_norms, autojunk=False)
word_starts = [None] * len(source_words)
matched_count = 0

for block in matcher.get_matching_blocks():
    for offset in range(block.size):
        s_i = block.a + offset
        e_i = block.b + offset
        word_starts[s_i] = event_tokens[e_i]["t_start"]
        matched_count += 1

coverage = matched_count / max(1, len(source_words))
print(f"[ALIGNMENT] Direct word-boundary match: {matched_count}/{len(source_words)} ({coverage * 100:.2f}%)")
if coverage < 0.70:
    die(f"Word-boundary alignment coverage too low ({coverage * 100:.2f}%).")

# Interpolate any unmatched words cleanly between neighboring measured anchors
if word_starts[0] is None:
    word_starts[0] = 0.0

i = 0
n_w = len(word_starts)
while i < n_w:
    if word_starts[i] is not None:
        i += 1
        continue
    j = i
    while j < n_w and word_starts[j] is None:
        j += 1
    left_t = word_starts[i - 1] if i > 0 else 0.0
    right_t = word_starts[j] if j < n_w else total_audio_s
    span = j - i + 1
    for step in range(i, j):
        frac = (step - i + 1) / span
        word_starts[step] = left_t + (right_t - left_t) * frac
    i = j

# Compute exact hold_start_s / hold_end_s for all 90 micro-moments
MIN_HOLD_S = 0.08
for idx, rec in enumerate(frame_records):
    if idx == 0:
        rec["hold_start_s"] = 0.0
    else:
        raw_t = float(word_starts[rec["word_start_idx"]])
        prev_t = frame_records[idx - 1]["hold_start_s"]
        rec["hold_start_s"] = min(max(raw_t, prev_t + MIN_HOLD_S), total_audio_s - MIN_HOLD_S * (len(frame_records) - idx))

for idx, rec in enumerate(frame_records):
    if idx < len(frame_records) - 1:
        rec["hold_end_s"] = frame_records[idx + 1]["hold_start_s"]
    else:
        rec["hold_end_s"] = total_audio_s
    rec["duration_s"] = rec["hold_end_s"] - rec["hold_start_s"]
    if rec["duration_s"] <= 0:
        die(f"Non-positive hold duration on {rec['frame_name']}: {rec['duration_s']}")

timings_csv = build_dir / "timings.csv"
with open(timings_csv, "w", encoding="utf-8", newline="") as tf:
    writer = csv.writer(tf)
    writer.writerow(["slide_id", "moment", "frame", "hold_start_s", "hold_end_s", "duration_s", "moment_text"])
    for rec in frame_records:
        writer.writerow(
            [
                rec["slide_id"],
                rec["moment"],
                rec["frame_name"],
                f"{rec['hold_start_s']:.6f}",
                f"{rec['hold_end_s']:.6f}",
                f"{rec['duration_s']:.6f}",
                rec["moment_text"],
            ]
        )

print("[TIMINGS] Per-beat measured start timestamps:")
slide_starts = {}
for sid in ordered_slide_ids:
    s_start = beats[sid][0]["hold_start_s"]
    s_end = beats[sid][-1]["hold_end_s"]
    slide_starts[sid] = s_start
    print(f"  Beat {sid:02d} ({len(beats[sid]):2d} frames): {fmt_mmss(s_start)} -> {fmt_mmss(s_end)} ({s_end - s_start:.2f}s)")

# ------------------------------------------------------------------------------
# 3. PIL PRE-PAD TO EVEN MAX-W / MAX-H BLACK RGB CANVAS (optimize=False, compress_level=6)
# ------------------------------------------------------------------------------
max_w = max(w for w, _ in raw_sizes)
max_h = max(h for _, h in raw_sizes)
if max_w % 2 != 0:
    max_w += 1
if max_h % 2 != 0:
    max_h += 1

print(f"[PIL PRE-PAD] Pre-padding {len(frame_records)} frames onto ({max_w}x{max_h}) RGB black canvas at (0,0)...")
for rec in frame_records:
    out_png = pad_dir / rec["frame_name"]
    with Image.open(rec["src_path"]) as src_im:
        rgb_im = src_im.convert("RGB")
        canvas = Image.new("RGB", (max_w, max_h), (0, 0, 0))
        canvas.paste(rgb_im, (0, 0))
        canvas.save(out_png, format="PNG", optimize=False, compress_level=6)
    rec["padded_path"] = out_png

concat_txt = build_dir / "ffconcat_frames.txt"
with open(concat_txt, "w", encoding="utf-8") as cf:
    cf.write("ffconcat version 1.0\n")
    for rec in frame_records:
        escaped = str(rec["padded_path"]).replace("'", "'\\''")
        cf.write(f"file '{escaped}'\n")
        cf.write(f"duration {rec['duration_s']:.6f}\n")
    # Repeat final frame entry so FFmpeg concat demuxer honors last duration
    last_escaped = str(frame_records[-1]["padded_path"]).replace("'", "'\\''")
    cf.write(f"file '{last_escaped}'\n")

# ------------------------------------------------------------------------------
# 4. FFMPEG STITCH (NATIVE RES, ZERO POST-CONCAT FILTERS, 30fps, libx264 yuv420p, AAC 192k)
# ------------------------------------------------------------------------------
video_out = stage_dir / "VIDEO.mp4"
print(f"[FFMPEG] Stitching {video_out} at native {max_w}x{max_h} @ 30fps (direct pre-padded concat)...")
ffmpeg_cmd = [
    "ffmpeg",
    "-hide_banner",
    "-loglevel",
    "warning",
    "-y",
    "-f",
    "concat",
    "-safe",
    "0",
    "-i",
    str(concat_txt),
    "-i",
    str(norm_wav),
    "-map",
    "0:v:0",
    "-map",
    "1:a:0",
    "-r",
    "30",
    "-c:v",
    "libx264",
    "-preset",
    "medium",
    "-crf",
    "18",
    "-pix_fmt",
    "yuv420p",
    "-c:a",
    "aac",
    "-b:a",
    "192k",
    "-ar",
    "48000",
    "-movflags",
    "+faststart",
    str(video_out),
]
ff_res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
if ff_res.returncode != 0:
    die(f"FFmpeg concat stitch failed (exit {ff_res.returncode}):\n{ff_res.stderr}")

if not video_out.is_file() or video_out.stat().st_size == 0:
    die("VIDEO.mp4 was not created or is empty.")

measured_video_s = probe_duration(video_out)
print(
    f"[VIDEO OK] VIDEO.mp4 rendered: {measured_video_s:.3f}s "
    f"(audio={total_audio_s:.3f}s, delta={abs(measured_video_s - total_audio_s):.3f}s, "
    f"size={video_out.stat().st_size / (1024 * 1024):.2f} MB)"
)

# ------------------------------------------------------------------------------
# 5. STAGE DELIVERABLES & PACKAGE <slug>_DELIVERABLE.zip
# ------------------------------------------------------------------------------
with Image.open(proj_dir / "thumbnail.jpg") as th_im:
    th_im.convert("RGB").save(stage_dir / "thumbnail.jpg", format="JPEG", quality=95)

shutil.copy2(proj_dir / "script.md", stage_dir / "script.md")

with open(proj_dir / "metadata.json", "r", encoding="utf-8") as mf:
    meta = json.load(mf)
meta["measured_audio_seconds"] = round(total_audio_s, 3)
meta["measured_video_seconds"] = round(measured_video_s, 3)
meta["resolution"] = f"{max_w}x{max_h}"
meta["fps"] = 30
meta["loudness_target_lufs"] = -14
meta["status"] = "RENDERED_DELIVERABLE_READY"
with open(stage_dir / "metadata.json", "w", encoding="utf-8") as mf:
    json.dump(meta, mf, indent=2)
    mf.write("\n")

chapter_titles = {
    1: "05:50 AM - The Ambush Trap at Clearwater Dam",
    2: "06:20 AM - Sneaking Into the Concrete Drainage Gallery",
    3: "06:45 AM - The Flooded Bulkhead & Silent Valve Trick",
    4: "07:10 AM - Chained Motorboat & Spotted From Above",
    5: "07:15 AM - The Warning Shot That Wakes the Horde",
    6: "07:20 AM - Snapping the Padlock & Crossing Deep Water",
}
chapter_lines = [
    f"{fmt_mmss(0.0 if sid == 1 else slide_starts[sid])} {chapter_titles[sid]}"
    for sid in ordered_slide_ids
]
yt_content = (
    "TITLE:\n"
    "Can You Survive Day Three of the Apocalypse?\n\n"
    "DESCRIPTION:\n"
    "At 5:50 AM on Day Three, cold mist curls off the mountain reservoir above Clearwater Dam—"
    "and one look through your brass binoculars reveals forty infected in the lower yard and "
    "two armed scavengers waiting in ambush on the high steel catwalk. Continue this second-person "
    "survival story as you and Maya sneak beneath the dam, outsmart an armed trap, and fight to "
    "launch a chained boat into deep water.\n\n"
    f"Runtime: {fmt_mmss(measured_video_s)}\n\n"
    + "\n".join(chapter_lines)
    + "\n\nTAGS:\n"
    "can you survive day three, zombie apocalypse story part 3, second person survival story, "
    "stick figure survival story, day three outbreak, animated survival story, "
    "how to survive a zombie apocalypse\n"
)
with open(stage_dir / "youtube.txt", "w", encoding="utf-8") as yf:
    yf.write(yt_content)

zip_path = out_root / f"{slug}_DELIVERABLE.zip"
deliverable_names = ["VIDEO.mp4", "thumbnail.jpg", "metadata.json", "script.md", "youtube.txt"]

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for dname in deliverable_names:
        fpath = stage_dir / dname
        if not fpath.is_file() or fpath.stat().st_size == 0:
            die(f"Deliverable file missing before ZIP packaging: {fpath}")
        zf.write(fpath, arcname=dname)

with zipfile.ZipFile(zip_path, "r") as zf_verify:
    namelist = set(zf_verify.namelist())
    if set(deliverable_names) != namelist:
        die(f"ZIP verification mismatch: expected {deliverable_names}, got {sorted(namelist)}")

print("==================================================================")
print(f" [SUCCESS] Package ready: {zip_path} ({zip_path.stat().st_size / (1024 * 1024):.2f} MB)")
print(f" Contents: {', '.join(deliverable_names)}")
print("==================================================================")
PYEOF
