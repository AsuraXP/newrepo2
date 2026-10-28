#!/usr/bin/env python3
"""Offline integration test for sync, static imagery, transitions, duration and audio muxing."""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is required: python -m pip install pillow", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("narration_pipeline", ROOT / "kaggle" / "run.py")
pipeline = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pipeline
assert spec.loader is not None
spec.loader.exec_module(pipeline)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ffmpeg_binary() -> str:
    binary = pipeline.ffmpeg_executable()
    if not binary:
        raise RuntimeError("ffmpeg is unavailable")
    return binary


def media_info(path: Path) -> tuple[float, str]:
    result = subprocess.run([ffmpeg_binary(), "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    info = result.stderr
    match = __import__("re").search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", info)
    if not match:
        raise RuntimeError(f"Could not inspect media info for {path}: {info}")
    hours, minutes, seconds = map(float, match.groups())
    return hours * 3600 + minutes * 60 + seconds, info


def frame_at(video: Path, time_s: float, target: Path) -> tuple[int, int, int]:
    subprocess.run([ffmpeg_binary(), "-y", "-hide_banner", "-loglevel", "error", "-ss", str(time_s), "-i", str(video), "-frames:v", "1", str(target)], check=True)
    with Image.open(target) as image:
        return image.convert("RGB").getpixel((image.width // 2, image.height // 2))


def main() -> int:
    if not pipeline.ffmpeg_executable():
        print("FAIL: selftest needs ffmpeg (system binary or imageio-ffmpeg)", file=sys.stderr)
        return 2
    try:
        with tempfile.TemporaryDirectory(prefix="narration-selftest-") as temp_name:
            temp = Path(temp_name)
            text = ("Amber lanterns glow above the quiet station tonight. "
                    "Blue shadows gather beyond the wooden bridge at dusk. "
                    "White windows shine across the sleeping town below.")
            frames = [
                {"id": "a", "anchor_phrase": "Amber lanterns glow", "occurrence": 1},
                {"id": "b", "anchor_phrase": "Blue shadows gather", "occurrence": 1},
                {"id": "c", "anchor_phrase": "White windows shine", "occurrence": 1},
            ]
            rows, errors = pipeline.resolve_anchors(text, frames, 0.5)
            check(not errors, f"expected clean anchor check, got: {errors}")
            check(len(rows) == 3 and all(row["status"] == "ok" for row in rows), "not every anchor resolved")
            check([row["word_index"] for row in rows] == [0, 8, 17], "anchor word positions drifted")
            check(all(3 <= row["hold_s"] <= 12 for row in rows), "synthetic holds outside 3–12s")
            sentence_chunks = [
                {"type": "SentenceBoundary", "offset_s": 0.0, "text": "Amber lanterns glow above the quiet station tonight."},
                {"type": "SentenceBoundary", "offset_s": 4.0, "text": "Blue shadows gather beyond the wooden bridge at dusk."},
                {"type": "SentenceBoundary", "offset_s": 8.5, "text": "White windows shine across the sleeping town below."},
            ]
            measured, measured_errors, _ = pipeline.measured_rows(text, frames, sentence_chunks, 12.5, 0.5)
            check(not measured_errors and all(row["anchor_precision"] == "exact" for row in measured), "sentence-boundary events were not recovered as exact sentence starts")
            repeated, repeat_errors = pipeline.resolve_anchors("Red birds circle above the river. Later, red birds circle above the bridge.", [{"id": "last", "anchor_phrase": "red birds circle", "occurrence": -1}], 0.5)
            check(repeated[0]["word_index"] == 7 and any("FIRST anchor" in error for error in repeat_errors), "negative occurrence did not select the final repeated phrase")
            collision, collision_errors = pipeline.resolve_anchors(text, [frames[0], {"id": "same_sentence", "anchor_phrase": "above the quiet", "occurrence": 1}], 0.5)
            check(any("SENTENCE collision" in error for error in collision_errors), "same-sentence anchor collision was not rejected")
            missing, missing_errors = pipeline.resolve_anchors(text, [{"id": "bad", "anchor_phrase": "this phrase does not exist", "occurrence": 1}], 0.5)
            check(bool(missing_errors) and missing[0]["status"] == "missing", "missing anchor did not fail loudly")

            config = {"render": {"width": 320, "height": 180, "fps": 24, "transition_seconds": 1.0, "transition": "fade"}}
            colors = {"a": (230, 20, 20), "b": (20, 220, 20), "c": (20, 20, 230)}
            for fid, color in colors.items():
                Image.new("RGB", (320, 180), color).save(temp / f"{fid}.jpg", quality=100)
            audio = temp / "silence.wav"
            subprocess.run([ffmpeg_binary(), "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", "12.5", "-c:a", "pcm_s16le", str(audio)], check=True)
            repo = temp / "repo"
            (repo / "assets" / "frames").mkdir(parents=True)
            for fid in colors:
                shutil.copyfile(temp / f"{fid}.jpg", repo / "assets" / "frames" / f"{fid}.jpg")
            video = temp / "transition.mp4"
            pipeline.render(repo, frames, rows, audio, video, config)
            total_duration, info = media_info(video)
            check("Audio:" in info, "render is missing audio")
            check("Video:" in info and "320x180" in info, "render dimensions incorrect")
            check(abs(total_duration - 12.5) < 0.25, f"duration {total_duration:.3f}s != 12.5s")
            start = frame_at(video, 0.5, temp / "start.png")
            blend = frame_at(video, 3.5, temp / "blend.png")
            green = frame_at(video, 4.5, temp / "green.png")
            check(start[0] > start[1] * 2, f"first anchor not visible at 0.5s: {start}")
            check(green[1] > green[0] * 2, f"second anchor not visible after transition: {green}")
            check(blend[0] > 30 and blend[1] > 30 and blend[0] < start[0] - 30, f"transition did not visibly blend: {blend}")

            static_video = temp / "static.mp4"
            pipeline.render(repo, frames[:1], [rows[0]], audio, static_video, config)
            static_a = frame_at(static_video, 1.0, temp / "static-a.png")
            static_b = frame_at(static_video, 3.0, temp / "static-b.png")
            check(max(abs(a - b) for a, b in zip(static_a, static_b)) <= 2, f"static image moved/changed: {static_a} vs {static_b}")
        print("PASS: anchors, missing-anchor failure, static frame, visible transition, duration, and audio mux")
        return 0
    except (AssertionError, OSError, subprocess.CalledProcessError, ValueError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
