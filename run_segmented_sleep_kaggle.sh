#!/usr/bin/env bash
set -euo pipefail

# ==============================================================================
# KAGGLE RUNNER: segmented_sleep_video
# Topic: "Why Did Ancient Humans Stop Sleeping Twice a Night?"
# Pipeline: Edge-TTS (WordBoundary) -> PIL Padding -> FFmpeg Stitch -> Deliverable ZIP
# ==============================================================================

PROJECT="segmented_sleep"
PROJECT_DIR="${PROJECT}_video"
BRANCH="arena/41c2bd65-newrepo2"
REPO_URL="https://github.com/AsuraXP/newrepo2.git"
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
    echo "ERROR: Project directory $PROJECT_DIR not found!"
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
import asyncio
import csv
import json
import re
import edge_tts

VOICE = "en-US-AndrewNeural"
RATE = "+10%"

with open("segmented_sleep_video/script.md", "r", encoding="utf-8") as f:
    script_text = f.read().strip()

print(f"Synthesizing narration take ({len(script_text.split())} words) via Edge-TTS [{VOICE}, {RATE}]...")

communicate = edge_tts.Communicate(script_text, voice=VOICE, rate=RATE)

word_events = []
audio_chunks = bytearray()

async def run_tts():
    async for event in communicate.stream():
        if event["type"] == "audio":
            audio_chunks.extend(event["data"])
        elif event["type"] == "WordBoundary":
            # offset and duration in 100ns units
            offset_s = event["offset"] / 10_000_000
            duration_s = event["duration"] / 10_000_000
            word_events.append({
                "word": event["text"],
                "start": offset_s,
                "end": offset_s + duration_s
            })

asyncio.run(run_tts())

with open("build/narration.mp3", "wb") as f:
    f.write(audio_chunks)

with open("build/word_timings.json", "w", encoding="utf-8") as f:
    json.dump(word_events, f, indent=2)

print(f"TTS synthesis complete: build/narration.mp3 ({len(audio_chunks)} bytes), {len(word_events)} words timed.")
EOF

echo "=== [4/7] Calculate Frame Timings Matching Micro-Beats ==="
python3 - << 'EOF'
import csv
import json
import os
import re

with open("build/word_timings.json", "r", encoding="utf-8") as f:
    timings = json.load(f)

# Total audio duration from last word end + 1.2s tail buffer
audio_duration = timings[-1]["end"] + 1.2

with open("segmented_sleep_video/visuals.csv", "r", encoding="utf-8") as f:
    beats = list(csv.DictReader(f))

# Match each beat to timestamps proportionally based on word count
total_words = sum(len(b["moment_text"].split()) for b in beats)
current_word_idx = 0
frame_segments = []

for idx, beat in enumerate(beats):
    m_words = len(beat["moment_text"].split())
    # find corresponding time
    start_t = timings[min(current_word_idx, len(timings)-1)]["start"]
    end_word_idx = min(current_word_idx + m_words - 1, len(timings)-1)
    
    if idx == len(beats) - 1:
        end_t = audio_duration
    else:
        end_t = timings[min(end_word_idx + 1, len(timings)-1)]["start"]
    
    duration = max(0.4, end_t - start_t)
    frame_file = f"beat{int(beat['slide_id']):02d}m{int(beat['moment']):02d}.png"
    
    frame_segments.append({
        "frame": frame_file,
        "duration": duration
    })
    current_word_idx += m_words

# Generate FFmpeg concat demuxer file
with open("build/concat_list.txt", "w", encoding="utf-8") as f:
    for seg in frame_segments:
        f.write(f"file 'padded_frames/{seg['frame']}'\n")
        f.write(f"duration {seg['duration']:.4f}\n")
    # Concat demuxer requirement: repeat last file once
    f.write(f"file 'padded_frames/{frame_segments[-1]['frame']}'\n")

print(f"Timing list generated: {len(frame_segments)} frames, total video time: {sum(s['duration'] for s in frame_segments):.2f}s")
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
        # Create uniform canvas
        canvas = Image.new("RGB", (max_w, max_h), (0, 0, 0))
        # Center frame on canvas
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
