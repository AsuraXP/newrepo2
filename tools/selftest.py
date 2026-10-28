#!/usr/bin/env python3
"""
Offline selftest for the pipeline: fake TTS + synthetic frames, real ffmpeg.

Proves the parts that Kaggle depends on without needing Azure or a Kaggle run:
  * anchor matching (exact / occurrence / ordering errors)
  * hold validation + merge
  * xfade timeline math (cuts land on anchor timestamps)
  * ffmpeg render, muxed audio, correct duration

    python tools/selftest.py                 # full run in a temp dir
    python tools/selftest.py --keep          # keep the temp dir for inspection
    python tools/selftest.py --ffmpeg /path/to/ffmpeg

Needs: pyyaml, pillow, numpy, ffmpeg (imageio-ffmpeg's binary is fine).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RUN_PY = REPO / "kaggle" / "run.py"
CONFIG = REPO / "kaggle" / "config.yaml"

SCRIPT = """<!-- TTS:START -->
Every glacier in the Alps is shrinking, and the pace is accelerating. That is not a forecast. It is a measurement, taken twice a year by the same team.

A glacier does not melt from the top down, like an ice cube on a counter. It loses mass where the sun hits the snowline and gains mass where storms pile snow above it. The difference between those two numbers is the glacier's entire budget.

When the budget goes negative the glacier gets thinner, then slower, then darker. Darker ice absorbs more sunlight. More sunlight means more melt, and that loop is why a glacier can look healthy for a decade.

Glaciologists call that threshold the runaway. It will still be there. It will simply no longer be a glacier.
<!-- TTS:END -->

## Sources
1. selftest fixture
"""

FRAMES = [
    ("01_open", "Every glacier in the Alps", 1, "fade:0.6"),
    ("02_forecast", "That is not a forecast", 1, "fade:0.5"),
    ("03_budget", "is the glacier's entire budget", 1, "dissolve:0.5"),
    ("04_darker", "gets thinner, then slower, then darker", 1, "wipeleft:0.4"),
    ("05_runaway", "the runaway", 1, "cut"),
    ("06_end", "no longer be a glacier", 1, "fade:0.6"),
]

STUB = '''
"""stand-in for edge-tts: synthesises silent audio of the right length"""
import asyncio, os, subprocess, tempfile
TICKS = 10_000_000
FFMPEG = os.environ.get("FFMPEG_BIN", "ffmpeg")

class Communicate:
    def __init__(self, text, voice="", rate="", volume="", pitch=""):
        self.text = text
    def _words(self):
        spw, pauses = 0.33, {".": 0.3, ",": 0.2, "?": 0.3, "!": 0.3, ":": 0.2}
        t, out = 0.0, []
        for raw in self.text.split():
            out.append((raw, t, spw))
            t += spw + pauses.get(raw.strip('"').rstrip()[-1:], 0.0)
        return out, t
    async def stream(self):
        words, total = self._words()
        tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
        subprocess.run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                        "-t", f"{total:.3f}", "-q:a", "9", tmp],
                       check=True, capture_output=True)
        with open(tmp, "rb") as fh:
            yield {"type": "audio", "data": fh.read()}
        os.unlink(tmp)
        for raw, start, dur in words:
            yield {"type": "wordboundary" if False else "WordBoundary",
                   "offset": int(start * TICKS), "duration": int(dur * TICKS),
                   "text": raw.strip(".,?!:;\\"\'")}
'''


def make_frames(assets: Path) -> None:
    from PIL import Image, ImageDraw
    import colorsys
    for i, (slug, *_rest) in enumerate(FRAMES):
        img = Image.new("RGB", (1920, 1080))
        draw = ImageDraw.Draw(img)
        for y in range(0, 1080, 4):
            t = y / 1080
            r, g, b = (int(255 * c) for c in
                       colorsys.hsv_to_rgb(((i / len(FRAMES)) + t * 0.1) % 1, 0.6,
                                           0.35 + 0.4 * t))
            draw.rectangle([0, y, 1920, y + 4], fill=(r, g, b))
        draw.rectangle([60, 60, 720, 170], fill=(0, 0, 0))
        draw.text((80, 100), f"{i + 1:02d} {slug}", fill=(255, 255, 255))
        img.save(assets / f"{slug}.png")


def build_project(root: Path) -> dict:
    (root / "narration").mkdir(parents=True)
    (root / "assets" / "frames").mkdir(parents=True)
    (root / "kaggle").mkdir(parents=True)
    (root / "tools").mkdir(parents=True)
    (root / "stub").mkdir(parents=True)
    shutil.copy(RUN_PY, root / "kaggle" / "run.py")
    shutil.copy(CONFIG, root / "kaggle" / "config.yaml")
    shutil.copy(REPO / "tools" / "prep_frames.py", root / "tools" / "prep_frames.py")
    (root / "narration" / "narration.md").write_text(SCRIPT, encoding="utf-8")
    frames = [{"id": slug, "anchor_phrase": phrase, "occurrence": occ,
               "image_prompt": "selftest", "negative_prompt": "text, watermark",
               "transition": trans}
              for slug, phrase, occ, trans in FRAMES]
    (root / "narration" / "frames.json").write_text(json.dumps(frames, indent=2),
                                                    encoding="utf-8")
    (root / "stub" / "edge_tts.py").write_text(STUB, encoding="utf-8")
    make_frames(root / "assets" / "frames")
    return {"frames": len(frames)}


def sh(cmd: list[str], env: dict, cwd: Path, label: str) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"\nFAIL {label}\n{proc.stdout}\n{proc.stderr}")
        sys.exit(1)
    return proc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ffmpeg", default=None)
    ap.add_argument("--keep", action="store_true")
    args = ap.parse_args()

    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        sys.exit("needs pillow + numpy: pip install -q pillow numpy")

    ffmpeg = args.ffmpeg or shutil.which("ffmpeg")
    if not ffmpeg:
        try:
            import imageio_ffmpeg
            ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        except ImportError:
            sys.exit("ffmpeg not found (install ffmpeg or imageio-ffmpeg)")
    ffmpeg = str(Path(ffmpeg).resolve())

    root = Path(tempfile.mkdtemp(prefix="nfv-selftest-"))
    bindir = root / "bin"
    bindir.mkdir(exist_ok=True)
    link = bindir / "ffmpeg"                      # run.py looks for the name "ffmpeg"
    if not link.exists():
        link.symlink_to(ffmpeg)
    env = dict(os.environ, PATH=f"{bindir}:{os.environ.get('PATH', '')}",
               FFMPEG_BIN=str(link), PYTHONPATH=str(root / "stub"))
    print(f"selftest in {root}")

    info = build_project(root)
    py = sys.executable
    base = [py, "kaggle/run.py", "--repo", "."]

    print("[1/5] compress frames")
    sh([py, "tools/prep_frames.py", "--repo", ".", "--strict", "--sheet"], env, root,
       "prep_frames")

    print("[2/5] estimator (offline QC path)")
    proc = sh(base + ["--estimate"], env, root, "estimate")
    est_csv = root / "output" / "estimates.csv"
    assert est_csv.is_file(), "estimates.csv not written"
    for line in proc.stdout.splitlines():
        if "estimated" in line:
            print("      " + line.strip())
            break

    print("[3/5] PASS 1 with stand-in TTS")
    sh(base + ["--dry-run"], env, root, "dry-run")
    rows = [r for r in csv.DictReader(open(root / "output" / "timings.csv"))
            if not r["status"].startswith("merged")]
    assert len(rows) == info["frames"], f"{len(rows)} rendered frames of {info['frames']}"

    print("[4/5] PASS 2 render")
    sh(base + ["--out", "final.mp4"], env, root, "render")
    video = root / "output" / "final.mp4"
    assert video.is_file(), "final.mp4 not written"

    # --- assertions ------------------------------------------------------
    probe = subprocess.run([ffmpeg, "-i", str(video)], capture_output=True, text=True)
    err = probe.stderr
    duration = None
    for line in err.splitlines():
        if "Duration:" in line:
            hms = line.split("Duration:")[1].split(",")[0].strip().split(":")
            duration = int(hms[0]) * 3600 + int(hms[1]) * 60 + float(hms[2])
    assert duration, "no duration in ffmpeg output"
    counts = subprocess.run([ffmpeg, "-i", str(video), "-map", "0:v", "-f", "null", "-"],
                            capture_output=True, text=True).stderr
    frames_out = int(counts.rsplit("frame=", 1)[1].strip().split()[0])
    last_end = float(rows[-1]["end_s"])
    assert abs(duration - (last_end + 0.8)) < 0.25, \
        f"duration {duration:.2f}s vs expected {last_end + 0.8:.2f}s"
    assert abs(frames_out - duration * 30) < 40, \
        f"{frames_out} video frames for {duration:.2f}s at 30fps"
    assert "Audio: aac" in err, "no aac audio stream"

    # every measured boundary must actually show the right frame
    def grab(t: float):
        out = root / "_grab.jpg"
        subprocess.run([ffmpeg, "-y", "-v", "error", "-ss", f"{t:.3f}", "-i",
                        str(video), "-frames:v", "1", "-q:v", "2", str(out)],
                       check=True)
        return np.asarray(Image.open(out).convert("RGB").resize((160, 90)), dtype=float)

    refs = {r["frame_id"]: np.asarray(
        Image.open(root / "assets" / "frames" / r["image"]).convert("RGB")
        .resize((160, 90)), dtype=float) for r in rows}
    mismatches = []
    for r in rows:
        t = min(float(r["start_s"]) + 0.6, float(r["end_s"]) - 0.15)
        shot = grab(max(t, 0.5))
        best = min(refs, key=lambda k: float(np.abs(shot - refs[k]).mean()))
        if best != r["frame_id"]:
            mismatches.append(f"{r['frame_id']} @{t:.2f}s showed {best}")
    assert not mismatches, "sync failures: " + "; ".join(mismatches)

    print("[5/5] error paths")
    good = (root / "narration" / "frames.json").read_text(encoding="utf-8")
    bad_frames = json.loads(good)
    bad_frames[2]["anchor_phrase"] = "this phrase is not in the script at all"
    broken = root / "narration" / "frames.bad.json"
    broken.write_text(json.dumps(bad_frames, indent=2), encoding="utf-8")
    bad = subprocess.run(base + ["--estimate", "--frames", str(broken)],
                         cwd=root, env=env, capture_output=True, text=True)
    assert bad.returncode != 0, "a missing anchor should fail the run"
    assert "not found" in (bad.stderr + bad.stdout), "missing-anchor message unclear"
    broken.unlink()

    print(f"\nPASS  all {len(rows)} frames land on their anchor timestamps, "
          f"{duration:.2f}s, {frames_out} frames, audio muxed")
    if args.keep:
        print(f"     kept {root}")
    else:
        shutil.rmtree(root, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
