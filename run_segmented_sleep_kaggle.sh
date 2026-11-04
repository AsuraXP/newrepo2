#!/usr/bin/env bash
set -euo pipefail

# ==============================================================================
# KAGGLE RUNNER: segmented_sleep_video
# Topic: "Why Did Ancient Humans Stop Sleeping Twice a Night?"
# Pipeline: Edge-TTS -> PIL Pre-Padding -> FFmpeg Concat & LUFS Normalization -> Deliverable ZIP
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PROJECT="segmented_sleep"
PROJECT_DIR="${PROJECT}_video"
WORK_DIR="$(pwd)"

echo "=== [1/7] Environment Setup ==="
export DEBIAN_FRONTEND=noninteractive
command -v ffmpeg >/dev/null 2>&1 || {
    echo "Installing ffmpeg..."
    apt-get update -qq && apt-get install -y -qq ffmpeg
}

python3 -m pip install --upgrade --quiet pip
python3 -m pip install --quiet edge-tts pillow

echo "=== [2/7] Preflight Checks ==="
if [ ! -d "$PROJECT_DIR" ]; then
    echo "ERROR: Project directory $PROJECT_DIR not found in $(pwd)!"
    exit 1
fi

if [ ! -f "$PROJECT_DIR/visuals.csv" ] || [ ! -f "$PROJECT_DIR/script.md" ] || [ ! -f "$PROJECT_DIR/thumbnail.jpg" ]; then
    echo "ERROR: Missing required project files in $PROJECT_DIR"
    exit 1
fi

FRAME_COUNT=$(ls -1 "$PROJECT_DIR/frames/"*.png 2>/dev/null | wc -l)
echo "Verified $FRAME_COUNT frames present in $PROJECT_DIR/frames/"
if [ "$FRAME_COUNT" -ne 134 ]; then
    echo "ERROR: Expected 134 frames, found $FRAME_COUNT"
    exit 1
fi

mkdir -p build/padded_frames

echo "=== [3/7] Edge-TTS Narration & Word-Level Timing Synthesis ==="
python3 - << 'EOF'
import json
import subprocess
import edge_tts

VOICE = "en-US-AndrewNeural"
RATE = "+10%"

with open("segmented_sleep_video/script.md", "r", encoding="utf-8") as f:
    script_text = f.read().strip()

print(f"Synthesizing narration take ({len(script_text.split())} words) via Edge-TTS [{VOICE}, {RATE}, boundary=WordBoundary]...")

# Request boundary=WordBoundary explicitly as per edge-tts 7.x specification
comm = edge_tts.Communicate(script_text, voice=VOICE, rate=RATE, boundary="WordBoundary")

word_events = []
with open("build/narration.mp3", "wb") as f:
    for chunk in comm.stream_sync():
        ctype = chunk.get("type")
        if ctype == "audio":
            f.write(chunk["data"])
        elif ctype == "WordBoundary":
            offset_s = chunk["offset"] / 10_000_000
            duration_s = chunk["duration"] / 10_000_000
            word_events.append({
                "word": chunk.get("text", ""),
                "start": offset_s,
                "end": offset_s + duration_s
            })

# Measure precise audio file duration via ffprobe
probe_cmd = [
    "ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1", "build/narration.mp3"
]
audio_dur_str = subprocess.check_output(probe_cmd).decode("utf-8").strip()
audio_duration_s = float(audio_dur_str)

with open("build/word_timings.json", "w", encoding="utf-8") as f:
    json.dump({
        "audio_duration_s": audio_duration_s,
        "words": word_events
    }, f, indent=2)

print(f"TTS synthesis complete: build/narration.mp3 ({audio_duration_s:.2f}s), {len(word_events)} word timestamps captured.")
EOF

echo "=== [4/7] Calculate Frame Timings Matching Micro-Beats ==="
python3 - << 'EOF'
import csv
import json

with open("build/word_timings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

audio_duration = data["audio_duration_s"]
words = data["words"]

with open("segmented_sleep_video/visuals.csv", "r", encoding="utf-8") as f:
    beats = list(csv.DictReader(f))

frame_segments = []

if len(words) > 0:
    # Use exact word-level timestamps when provided by engine
    current_word_idx = 0
    for idx, beat in enumerate(beats):
        m_words = len(beat["moment_text"].split())
        start_t = words[min(current_word_idx, len(words) - 1)]["start"]
        end_word_idx = min(current_word_idx + m_words - 1, len(words) - 1)
        
        if idx == len(beats) - 1:
            end_t = audio_duration
        else:
            end_t = words[min(end_word_idx + 1, len(words) - 1)]["start"]
            
        dur = max(0.4, end_t - start_t)
        frame_file = f"beat{int(beat['slide_id']):02d}m{int(beat['moment']):02d}.png"
        frame_segments.append({"frame": frame_file, "duration": dur})
        current_word_idx += m_words
else:
    # Robust fallback: proportional allocation by beat word count
    print("Notice: Word boundary events empty from engine, allocating frame holds proportionally to beat word count...")
    total_words = sum(len(b["moment_text"].split()) for b in beats)
    for beat in beats:
        w_count = len(beat["moment_text"].split())
        dur = (w_count / total_words) * audio_duration
        frame_file = f"beat{int(beat['slide_id']):02d}m{int(beat['moment']):02d}.png"
        frame_segments.append({"frame": frame_file, "duration": max(0.4, dur)})

# Generate FFmpeg concat demuxer file
with open("build/concat_list.txt", "w", encoding="utf-8") as f:
    for seg in frame_segments:
        f.write(f"file 'padded_frames/{seg['frame']}'\n")
        f.write(f"duration {seg['duration']:.4f}\n")
    # Concat demuxer requirement: repeat last file once
    f.write(f"file 'padded_frames/{frame_segments[-1]['frame']}'\n")

total_visual_time = sum(s["duration"] for s in frame_segments)
print(f"Timing list generated: {len(frame_segments)} frames, total visual time: {total_visual_time:.2f}s (audio: {audio_duration:.2f}s)")
EOF

echo "=== [5/7] PIL Canvas Pre-Padding Snap ==="
python3 - << 'EOF'
import glob
import os
from PIL import Image

src_frames = sorted(glob.glob("segmented_sleep_video/frames/*.png"))
max_w, max_h = 0, 0

for f in src_frames:
    with Image.open(f) as img:
        max_w = max(max_w, img.width)
        max_h = max(max_h, img.height)

# Snap to even dimensions
max_w = max_w + (max_w % 2)
max_h = max_h + (max_h % 2)
print(f"Max canvas resolved across all frames: {max_w}x{max_h}")

for f in src_frames:
    fname = os.path.basename(f)
    out_path = os.path.join("build/padded_frames", fname)
    with Image.open(f) as img:
        img_rgb = img.convert("RGB")
        canvas = Image.new("RGB", (max_w, max_h), (0, 0, 0))
        offset_x = (max_w - img_rgb.width) // 2
        offset_y = (max_h - img_rgb.height) // 2
        canvas.paste(img_rgb, (offset_x, offset_y))
        canvas.save(out_path, format="PNG", optimize=False, compress_level=6)

print(f"All {len(src_frames)} frames padded and written to build/padded_frames/")
EOF

echo "=== [6/7] FFmpeg Video Render & Audio Normalization (-14 LUFS) ==="
ffmpeg -y -hide_banner -loglevel warning \
    -f concat -safe 0 -i build/concat_list.txt \
    -i build/narration.mp3 \
    -af "loudnorm=I=-14:LRA=7:tp=-1" \
    -c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 \
    -c:a aac -b:a 192k \
    -shortest \
    "build/VIDEO.mp4"

echo "Video render complete: build/VIDEO.mp4"

echo "=== [7/7] Deliverable Packaging ==="
cp build/VIDEO.mp4 "${PROJECT}_video/"
cd "${PROJECT}_video"
zip -q -r "../${PROJECT}_DELIVERABLE.zip" \
    VIDEO.mp4 \
    thumbnail.jpg \
    metadata.json \
    script.md \
    youtube.txt \
    visuals.csv \
    README.md

cd ..
echo "======================================================================"
echo "DELIVERABLE READY: ${WORK_DIR}/${PROJECT}_DELIVERABLE.zip"
echo "======================================================================"
ls -lh "${PROJECT}_DELIVERABLE.zip" build/VIDEO.mp4
