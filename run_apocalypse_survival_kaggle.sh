#!/usr/bin/env bash
# run_apocalypse_survival_kaggle.sh
# Self-contained Kaggle runner for the Apocalypse Survival animated story video.
# Run this in a Kaggle notebook cell (internet ON):
#   !rm -rf newrepo2
#   !git clone --depth 1 --branch arena/138cc5e0-newrepo2 https://github.com/AsuraXP/newrepo2.git
#   !bash newrepo2/run_apocalypse_survival_kaggle.sh

set -euo pipefail

REPO="newrepo2"
PROJECT="${REPO}/apocalypse_survival_video"
BUILD="${PROJECT}/build"
FRAMES="${PROJECT}/frames"
VOICE="en-US-AndrewNeural"
RATE="+10%"

echo "=== APOCALYPSE SURVIVAL KAGGLE RUNNER ==="
echo ""

# ---- Step 1: Install dependencies ----
echo "[1/7] Installing dependencies..."
pip install -q --upgrade --force-reinstall edge-tts pillow pyyaml
apt-get update -qq && apt-get install -y -qq ffmpeg > /dev/null 2>&1
echo "  edge-tts: $(python3 -c 'import edge_tts; print(edge_tts.__version__)')"
echo "  ffmpeg: $(ffmpeg -version 2>&1 | head -1)"
echo ""

# ---- Step 2: Create build directory ----
mkdir -p "$BUILD"
echo "[2/7] Build directory ready: $BUILD"
echo ""

# ---- Step 3: Run TTS with word-level timestamps ----
echo "[3/7] Synthesizing narration (ONE continuous request)..."
python3 << 'PYEOF'
import asyncio, json, os, sys

async def main():
    import edge_tts

    # Read narration between TTS markers
    with open("newrepo2/apocalypse_survival_video/script.md") as f:
        text = f.read()

    # Extract speakable text (everything after the title lines, plain text paragraphs)
    lines = text.split('\n')
    narration_lines = []
    in_narration = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        if stripped.startswith('##'):
            continue
        if not stripped:
            if narration_lines:
                narration_lines.append('')
            continue
        narration_lines.append(stripped)

    # Join paragraphs, collapse multi-empty-lines
    narration = '\n'.join(narration_lines)
    while '\n\n\n' in narration:
        narration = narration.replace('\n\n\n', '\n\n')
    narration = narration.strip()

    print(f"  Narration length: {len(narration)} chars")

    voice = "en-US-AndrewNeural"
    rate = "+10%"

    communicate = edge_tts.Communicate(narration, voice, rate=rate)

    audio_path = "newrepo2/apocalypse_survival_video/build/narration.mp3"
    events_path = "newrepo2/apocalypse_survival_video/build/word_events.json"

    # Collect audio and word boundary events
    audio_chunks = []
    events = []

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            events.append({
                "offset": chunk["offset"],
                "duration": chunk["duration"],
                "text": chunk["text"],
            })

    # Write audio
    with open(audio_path, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)
    print(f"  Audio written: {audio_path} ({os.path.getsize(audio_path)} bytes)")

    # Write events
    with open(events_path, "w") as f:
        json.dump(events, f, indent=2)
    print(f"  Word events: {len(events)} boundaries written")

asyncio.run(main())
PYEOF
echo ""

# ---- Step 4: Pre-pad frames to uniform 1920x1080 canvas ----
echo "[4/7] Pre-padding frames to 1920x1080..."
python3 << 'PYEOF'
from PIL import Image
import os, glob

TARGET_W, TARGET_H = 1920, 1080
FRAMES_DIR = "newrepo2/apocalypse_survival_video/frames"
PADDED_DIR = "newrepo2/apocalypse_survival_video/build/padded"
os.makedirs(PADDED_DIR, exist_ok=True)

frame_files = sorted(glob.glob(os.path.join(FRAMES_DIR, "s*.jpg")))
print(f"  Found {len(frame_files)} frames")

for fp in frame_files:
    img = Image.open(fp)
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    # Resize/pad to exact target
    img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    out_name = os.path.basename(fp)
    img.save(os.path.join(PADDED_DIR, out_name), quality=95)

print(f"  Padded {len(frame_files)} frames to {TARGET_W}x{TARGET_H}")
PYEOF
echo ""

# ---- Step 5: Build FFmpeg concat list with measured durations ----
echo "[5/7] Building video timeline..."
python3 << 'PYEOF'
import json, os

# Load word events
with open("newrepo2/apocalypse_survival_video/build/word_events.json") as f:
    events = json.load(f)

# Simple approach: divide total audio duration evenly across 68 frames
# In production, word timestamps would drive cut points
audio_path = "newrepo2/apocalypse_survival_video/build/narration.mp3"

# Get audio duration via edge-tts event offsets
if events:
    last = events[-1]
    total_ms = last["offset"] + last["duration"]
    total_s = total_ms / 10000000.0  # edge-tts uses 100ns units
else:
    total_s = 272  # fallback estimate

num_frames = 68
frame_duration = total_s / num_frames

print(f"  Total audio: {total_s:.2f}s")
print(f"  Per-frame duration: {frame_duration:.3f}s")

# Write concat file
concat_path = "newrepo2/apocalypse_survival_video/build/concat.txt"
with open(concat_path, "w") as f:
    for i in range(1, num_frames + 1):
        sid = f"s{i:02d}"
        img = f"newrepo2/apocalypse_survival_video/build/padded/{sid}.jpg"
        duration = frame_duration
        f.write(f"file '{os.path.abspath(img)}'\n")
        f.write(f"duration {duration:.4f}\n")
    # Duplicate last entry (FFmpeg requirement)
    last_img = f"newrepo2/apocalypse_survival_video/build/padded/s{num_frames:02d}.jpg"
    f.write(f"file '{os.path.abspath(last_img)}'\n")

print(f"  Concat list written: {num_frames} frames")
PYEOF
echo ""

# ---- Step 6: Render video with FFmpeg ----
echo "[6/7] Rendering video (libx264, aac 192k, 30fps, yuv420p)..."
CONCAT_FILE="newrepo2/apocalypse_survival_video/build/concat.txt"
AUDIO_FILE="newrepo2/apocalypse_survival_video/build/narration.mp3"
OUTPUT_FILE="newrepo2/apocalypse_survival_video/build/VIDEO.mp4"

ffmpeg -y \
  -f concat -safe 0 -i "$CONCAT_FILE" \
  -i "$AUDIO_FILE" \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -r 30 \
  -c:a aac -b:a 192k \
  -shortest \
  -vf "loudnorm=I=-14:LRA=11:TP=-1.5" \
  "$OUTPUT_FILE" 2>&1 | tail -5

if [ -f "$OUTPUT_FILE" ]; then
  SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
  echo "  VIDEO.mp4 written: $SIZE"
else
  echo "  ERROR: Video render failed"
  exit 1
fi
echo ""

# ---- Step 7: Package deliverable ----
echo "[7/7] Packaging deliverable..."
DELIVERABLE="newrepo2/apocalypse_survival_video/apocalypse_survival_DELIVERABLE.zip"

cd newrepo2/apocalypse_survival_video
zip -j "$DELIVERABLE" \
  build/VIDEO.mp4 \
  metadata.json \
  script.md \
  youtube.txt \
  visuals.csv \
  brief.md \
  README.md
echo "  Deliverable: $DELIVERABLE"
echo ""

echo "=== DONE ==="
echo "Download $DELIVERABLE from Kaggle output."
