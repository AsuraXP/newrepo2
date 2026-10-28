#!/usr/bin/env python3
"""Narration-first Edge TTS timing and static-frame renderer.

Use --estimate for the offline authoring check. All synthesis/rendering belongs on Kaggle.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None

MARKER_RE = re.compile(r"<!--\s*TTS:START\s*-->(.*?)<!--\s*TTS:END\s*-->", re.S | re.I)
WORD_RE = re.compile(r"[\w]+(?:['’][\w]+)?", re.UNICODE)
SENTENCE_RE = re.compile(r"[^.!?]+(?:[.!?]+|$)", re.S)


def marked_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    matches = MARKER_RE.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one TTS marker pair in {path}; found {len(matches)}")
    content = matches[0].strip()
    if not content:
        raise ValueError(f"TTS markers in {path} are empty")
    return content


def load_config(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML is required. On Kaggle: pip install -q --upgrade --force-reinstall edge-tts pyyaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data


def sentence_index(text: str) -> tuple[list[str], list[int]]:
    words = [m.group(0) for m in WORD_RE.finditer(text)]
    starts: list[int] = []
    for match in SENTENCE_RE.finditer(text):
        if WORD_RE.search(match.group(0)):
            char_offset = match.start()
            word_index = sum(1 for m in WORD_RE.finditer(text, 0, char_offset))
            starts.append(word_index)
    return words, starts


def find_phrase(words: list[str], phrase: str, occurrence: int) -> int | None:
    pwords = [w.casefold() for w in WORD_RE.findall(phrase)]
    if not 3 <= len(pwords) <= 8:
        raise ValueError(f"anchor_phrase must contain 3–8 words: {phrase!r}")
    haystack = [w.casefold() for w in words]
    hits = [i for i in range(len(haystack) - len(pwords) + 1) if haystack[i:i + len(pwords)] == pwords]
    if not hits:
        return None
    if occurrence == 0:
        raise ValueError(f"occurrence is 1-based and cannot be 0: {phrase!r}")
    n = occurrence - 1 if occurrence > 0 else len(hits) + occurrence
    return hits[n] if 0 <= n < len(hits) else None


def resolve_anchors(text: str, frames: list[dict[str, Any]], sec_per_word: float) -> tuple[list[dict[str, Any]], list[str]]:
    words, starts = sentence_index(text)
    sentence_for_word: dict[int, int] = {}
    for si, begin in enumerate(starts):
        end = starts[si + 1] if si + 1 < len(starts) else len(words)
        for wi in range(begin, end):
            sentence_for_word[wi] = si + 1
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    previous = -1
    seen_sentence: set[int] = set()
    seen_ids: set[str] = set()
    for entry in frames:
        fid = str(entry.get("id", ""))
        if not fid:
            errors.append("FRAME error: every frame needs a non-empty id")
        elif fid in seen_ids:
            errors.append(f"FRAME error: duplicate id {fid!r}")
        seen_ids.add(fid)
        phrase = str(entry.get("anchor_phrase", ""))
        if "occurrence" not in entry:
            errors.append(f"FRAME error: {fid or '<no id>'} must set occurrence explicitly (1-based)")
        occurrence = int(entry.get("occurrence", 1))
        idx = find_phrase(words, phrase, occurrence)
        base = {"id": entry.get("id", ""), "anchor_phrase": phrase, "matched_text": "", "word_index": "", "sentence": "", "start_s": "", "hold_s": "", "est_hold_s": "", "anchor_precision": "", "status": ""}
        if idx is None:
            errors.append(f"MISSING anchor: {entry.get('id', '<no id>')} — {phrase!r} occurrence={occurrence}")
            base["status"] = "missing"
            rows.append(base)
            continue
        si = sentence_for_word.get(idx, 1)
        exact_sentence_start = idx in starts
        if idx <= previous:
            errors.append(f"ORDER error: {entry.get('id', '<no id>')} is not after the previous anchor")
        if si in seen_sentence:
            errors.append(f"SENTENCE collision: multiple anchors in sentence {si} ({entry.get('id', '<no id>')})")
        previous = idx
        seen_sentence.add(si)
        base.update(matched_text=" ".join(words[idx:idx + len(WORD_RE.findall(phrase))]), word_index=idx,
                    sentence=si, start_s=round(idx * sec_per_word, 3),
                    anchor_precision="exact" if exact_sentence_start else "in-sentence", status="ok")
        rows.append(base)
    total_s = len(words) * sec_per_word
    valid = [r for r in rows if r["status"] == "ok"]
    if valid and int(valid[0]["word_index"]) != 0:
        errors.append("FIRST anchor must start at the beginning of narration so the measured timeline has a frame at t=0")
    for j, row in enumerate(valid):
        start = float(row["start_s"])
        end = float(valid[j + 1]["start_s"]) if j + 1 < len(valid) else total_s
        hold = end - start
        row["hold_s"] = round(hold, 3)
        row["est_hold_s"] = round(hold, 3)
        if hold < 3 or hold > 12:
            row["status"] = "warn_hold"
            errors.append(f"HOLD warning: {row['id']} = {hold:.2f}s (required 3–12s)")
    return rows, errors


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["id", "anchor_phrase", "matched_text", "word_index", "sentence", "start_s", "hold_s", "est_hold_s", "anchor_precision", "status"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def print_estimate(repo: Path, config: dict[str, Any], text: str, frames: list[dict[str, Any]]) -> int:
    spw = (config.get("estimate") or {}).get("sec_per_word")
    if not isinstance(spw, (float, int)) or spw <= 0:
        print("ERROR: estimate.sec_per_word is not calibrated. Complete Phase 0 on Kaggle, then update kaggle/config.yaml.", file=sys.stderr)
        return 2
    rows, errors = resolve_anchors(text, frames, float(spw))
    words = WORD_RE.findall(text)
    path = repo / "kaggle" / "output" / "timings.csv"
    write_csv(path, rows)
    print(f"Estimated narration: {len(words)} words, {len(words) * float(spw):.2f}s ({len(words) * float(spw) / 60:.2f} min)")
    print(f"frames.json entries: {len(frames)}; estimate rows: {len(rows)}; timings: {path.relative_to(repo)}")
    if not frames:
        print("ERROR: frames.json has no anchors", file=sys.stderr)
        return 1
    for error in errors:
        print(error)
    return 1 if errors else 0


def ffmpeg_executable() -> str | None:
    found = shutil.which("ffmpeg")
    if found:
        return found
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return None


def run_ffprobe(path: Path) -> float:
    probe = shutil.which("ffprobe")
    if probe:
        result = subprocess.run([probe, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)], check=True, capture_output=True, text=True)
        return float(result.stdout.strip())
    binary = ffmpeg_executable()
    if not binary:
        raise RuntimeError("ffprobe is required (or install imageio-ffmpeg for its ffmpeg fallback)")
    result = subprocess.run([binary, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    match = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match:
        raise RuntimeError(f"Could not read media duration from {path}")
    hours, minutes, seconds = map(float, match.groups())
    return hours * 3600 + minutes * 60 + seconds


async def synthesize(text: str, voice: str, rate: str, boundary: str, audio_path: Path) -> list[dict[str, Any]]:
    try:
        import edge_tts
    except ImportError as exc:
        raise RuntimeError("edge-tts is missing; force-reinstall it on Kaggle before the TTS pass") from exc
    if boundary not in ("WordBoundary", "SentenceBoundary"):
        raise ValueError("boundary must be WordBoundary or SentenceBoundary")
    communicator = edge_tts.Communicate(text, voice, rate=rate, boundary=boundary)
    boundaries: list[dict[str, Any]] = []
    audio_path.parent.mkdir(parents=True, exist_ok=True)
    with audio_path.open("wb") as out:
        async for chunk in communicator.stream():
            if chunk["type"] == "audio":
                out.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                boundaries.append({"type": chunk["type"],
                                   "offset_s": float(chunk.get("offset", 0)) / 10_000_000,
                                   "duration_s": float(chunk.get("duration", 0)) / 10_000_000,
                                   "text": chunk.get("text", "")})
    return boundaries


def measured_rows(text: str, frames: list[dict[str, Any]], boundaries: list[dict[str, Any]], duration: float, sec_per_word: float) -> tuple[list[dict[str, Any]], list[str], float]:
    words = WORD_RE.findall(text)
    rows, errors = resolve_anchors(text, frames, sec_per_word)
    errors = [error for error in errors if not error.startswith("HOLD warning:")]
    events = [b for b in boundaries if b.get("text", "").strip()]
    # Edge voices may emit word, phrase, or sentence boundaries. Match anchor starts against
    # the event sequence where possible; otherwise interpolate within the audio duration.
    boundary_words: list[tuple[int, float]] = []
    cursor = 0
    for event in events:
        event_words = WORD_RE.findall(event["text"])
        if event_words:
            boundary_words.append((cursor, event["offset_s"]))
            cursor += len(event_words)
    boundary_word_indices = {index for index, _ in boundary_words}
    exact_word_events = (
        len(boundary_words) >= len(words)
        and all(event.get("type") == "WordBoundary" and len(WORD_RE.findall(event["text"])) == 1 for event in events)
    )
    def timestamp(word_index: int) -> float:
        if exact_word_events:
            return boundary_words[min(word_index, len(boundary_words) - 1)][1]
        if boundary_words:
            before = [b for b in boundary_words if b[0] <= word_index]
            after = [b for b in boundary_words if b[0] > word_index]
            if before and after:
                left, right = before[-1], after[0]
                fraction = (word_index - left[0]) / max(1, right[0] - left[0])
                return left[1] + (right[1] - left[1]) * fraction
            if before:
                return before[-1][1] + sec_per_word * (word_index - before[-1][0])
        return duration * word_index / max(1, len(words))
    starts: list[tuple[dict[str, Any], float]] = []
    for row in rows:
        if row["status"] in ("missing",):
            continue
        wi = int(row["word_index"])
        t = timestamp(wi)
        row["start_s"] = round(t, 3)
        row["anchor_precision"] = "exact" if wi in boundary_word_indices else "in-sentence"
        starts.append((row, t))
    for i, (row, start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else duration
        hold = max(0, end - start)
        row["hold_s"] = round(hold, 3)
        row["status"] = "ok" if 3 <= hold <= 12 else "warn_hold"
        if row["status"] != "ok":
            errors.append(f"HOLD warning: {row['id']} = {hold:.2f}s (required 3–12s)")
    per_word = duration / max(1, len(words))
    return rows, errors, per_word


def render(repo: Path, frames: list[dict[str, Any]], rows: list[dict[str, Any]], audio: Path, out_path: Path, config: dict[str, Any]) -> None:
    if not frames:
        raise ValueError("Cannot render: frames.json is empty")
    if ffmpeg_executable() is None:
        raise RuntimeError("ffmpeg is required for rendering")
    duration = run_ffprobe(audio)
    row_by_id = {str(r["id"]): r for r in rows}
    image_paths = []
    durations = []
    for frame in frames:
        fid = str(frame.get("id", ""))
        image = repo / "assets" / "frames" / f"{fid}.jpg"
        if not image.is_file():
            raise FileNotFoundError(f"Missing reviewed JPG for frame {fid}: {image}")
        image_paths.append(image)
        durations.append(float(row_by_id[fid]["hold_s"]))
    # Align final segment to the measured audio end to avoid a silent/black tail.
    durations[-1] = max(0.1, duration - sum(durations[:-1]))
    settings = config.get("render", {})
    width, height, fps = int(settings.get("width", 1280)), int(settings.get("height", 720)), int(settings.get("fps", 30))
    transition = float(settings.get("transition_seconds", 1.0))
    if transition < 0.8:
        raise ValueError("transition_seconds must be at least 0.8")
    mode = str(settings.get("transition", "fade"))
    cmd = [ffmpeg_executable() or "ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    for i, (image, hold) in enumerate(zip(image_paths, durations)):
        seg = hold if i == 0 else hold + (transition if i < len(durations) else 0)
        # The final chain also needs the overlap extension on its input.
        if i == len(durations) - 1 and i > 0:
            seg = hold + transition
        cmd += ["-loop", "1", "-framerate", str(fps), "-t", f"{seg:.6f}", "-i", str(image)]
    cmd += ["-i", str(audio)]
    filters = []
    for i in range(len(frames)):
        filters.append(f"[{i}:v]scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={fps},format=yuv420p[v{i}]")
    if len(frames) == 1:
        filters.append("[v0]null[vout]")
    else:
        current = "v0"
        elapsed = durations[0]
        for i in range(1, len(frames)):
            offset = max(0.0, elapsed - transition)
            next_label = f"vx{i}"
            filters.append(f"[{current}][v{i}]xfade=transition={mode}:duration={transition:.3f}:offset={offset:.6f}[{next_label}]")
            current = next_label
            elapsed += durations[i]
        filters.append(f"[{current}]null[vout]")
    cmd += ["-filter_complex", ";".join(filters), "-map", "[vout]", "-map", f"{len(frames)}:a:0", "-t", f"{duration:.6f}", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_path)]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--estimate", action="store_true", help="offline timing/anchor check; no TTS or network")
    parser.add_argument("--dry-run", action="store_true", help="synthesize once and write measured timings; do not render video")
    parser.add_argument("--tts-debug", action="store_true", help="print measured boundary granularity and rate")
    parser.add_argument("--preflight", action="store_true", help="synthesize narration/preflight.md instead of episode narration")
    parser.add_argument("--out", type=Path, help="render measured video to this path")
    args = parser.parse_args()
    repo = args.repo.resolve()
    try:
        config = load_config(repo / "kaggle" / "config.yaml")
        script_path = repo / "narration" / ("preflight.md" if args.preflight else "narration.md")
        text = marked_text(script_path)
        frames = json.loads((repo / "frames.json").read_text(encoding="utf-8"))
        if not isinstance(frames, list):
            raise ValueError("frames.json must contain a JSON array")
        if args.estimate:
            print("sync_source: calibrated estimate (offline; no synthesis)")
            return print_estimate(repo, config, text, frames)
        if not (args.dry_run or args.out):
            parser.error("choose --estimate, --dry-run, or --out")
        output_dir = repo / "kaggle" / "output"
        audio = output_dir / ("preflight.mp3" if args.preflight else "narration.mp3")
        voice, rate = str(config.get("voice", "en-US-AndrewNeural")), str(config.get("rate", "+0%"))
        boundary = str(config.get("boundary", "SentenceBoundary"))
        print("PASS 1 — Edge TTS")
        try:
            import edge_tts
            print(f"edge-tts {edge_tts.__version__}")
        except Exception:
            print("edge-tts version unavailable")
        boundaries = asyncio.run(synthesize(text, voice, rate, boundary, audio))
        measured_duration = run_ffprobe(audio)
        if measured_duration <= 0:
            raise RuntimeError("TTS produced zero-duration audio")
        spw = (config.get("estimate") or {}).get("sec_per_word")
        fallback_spw = float(spw) if isinstance(spw, (int, float)) and spw > 0 else measured_duration / max(1, len(WORD_RE.findall(text)))
        rows, errors, suggested = measured_rows(text, frames, boundaries, measured_duration, fallback_spw)
        source_words = WORD_RE.findall(text)
        recovered_words = sum(len(WORD_RE.findall(event.get("text", ""))) for event in boundaries)
        if recovered_words != len(source_words):
            errors.append(f"WORD COUNT mismatch: script has {len(source_words)} words but boundary text recovers {recovered_words}")
        boundary_types = {event.get("type") for event in boundaries}
        if boundary_types == {"WordBoundary"}:
            sync_source = "word-boundary timestamps"
        elif boundary_types == {"SentenceBoundary"}:
            sync_source = "sentence-boundary timestamps; words within sentences interpolated"
        elif boundary_types:
            sync_source = "mixed boundary timestamps with interpolation"
        else:
            sync_source = "no boundary metadata; timing unavailable"
            errors.append("BOUNDARY error: Edge TTS returned no word or sentence boundary metadata")
        print(f"sync_source: {sync_source}")
        print(f"Audio duration: {measured_duration:.3f}s; script words: {len(source_words)}; words recovered from boundaries: {recovered_words}")
        print(f"{len(boundaries)} boundary events ({recovered_words / max(1, len(boundaries)):.2f} words each)")
        print(f"suggested sec_per_word: {suggested:.4f}")
        if args.tts_debug:
            print("TTS DEBUG boundary samples:")
            for event in boundaries[:12]:
                print(f"  {event.get('type', 'boundary')} @ {event['offset_s']:.3f}s | {event['text']}")
        timings_path = output_dir / "timings.csv"
        write_csv(timings_path, rows)
        print(f"timings: {timings_path}")
        if errors:
            for error in errors:
                print(error)
        if args.out:
            render(repo, frames, rows, audio, args.out.resolve(), config)
            print(f"rendered: {args.out}")
        return 1 if errors else 0
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
