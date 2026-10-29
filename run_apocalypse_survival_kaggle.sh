#!/usr/bin/env bash
# run_apocalypse_survival_kaggle.sh — Fixed v2
# Run in a Kaggle notebook cell (internet ON):
#   !rm -rf newrepo2
#   !git clone --depth 1 --branch arena/138cc5e0-newrepo2 https://github.com/AsuraXP/newrepo2.git
#   !bash newrepo2/run_apocalypse_survival_kaggle.sh

set -euo pipefail

REPO="newrepo2"
PROJECT="${REPO}/apocalypse_survival_video"
BUILD="${PROJECT}/build"
FRAMES="${PROJECT}/frames"

echo "=== APOCALYPSE SURVIVAL KAGGLE RUNNER v2 ==="
echo ""

# ---- Step 1: Install dependencies ----
echo "[1/7] Installing dependencies..."
pip install -q --upgrade --force-reinstall edge-tts pyyaml pillow
apt-get update -qq && apt-get install -y -qq ffmpeg > /dev/null 2>&1
echo "  edge-tts: $(python3 -c 'import edge_tts; print(edge_tts.__version__)')"
echo "  ffmpeg: $(ffmpeg -version 2>&1 | head -1)"
echo ""

# ---- Step 2: Create build directory ----
mkdir -p "$BUILD"
echo "[2/7] Build directory ready: $BUILD"
echo ""

# ---- Step 3: Run TTS with word-level timestamps ----
echo "[3/7] Synthesizing narration (ONE continuous request with WordBoundary)..."
python3 << 'PYEOF'
import asyncio, json, os, sys, re

async def main():
    import edge_tts

    # Read narration from script.md — extract plain speakable text
    with open("newrepo2/apocalypse_survival_video/script.md") as f:
        text = f.read()

    # Extract speakable text: skip markdown headers, blank lines between paragraphs
    lines = text.split('\n')
    paragraphs = []
    current_para = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
            continue
        if not stripped:
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
            continue
        current_para.append(stripped)
    if current_para:
        paragraphs.append(' '.join(current_para))

    narration = ' '.join(paragraphs).strip()
    # Clean any remaining markdown artifacts
    narration = re.sub(r'\*+', '', narration)
    narration = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', narration)

    print(f"  Narration: {len(narration)} chars, ~{len(narration.split())} words")

    voice = "en-US-AndrewNeural"
    rate = "+10%"

    communicate = edge_tts.Communicate(narration, voice, rate=rate)

    audio_path = "newrepo2/apocalypse_survival_video/build/narration.mp3"
    events_path = "newrepo2/apocalypse_survival_video/build/word_events.json"

    # Use save_with_audio_file to get both audio and metadata
    submaker = edge_tts.SubMaker()
    audio_chunks = []
    boundary_events = []

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            boundary_events.append({
                "offset": chunk["offset"],
                "duration": chunk["duration"],
                "text": chunk["text"],
            })

    # Write audio
    with open(audio_path, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)
    audio_size = os.path.getsize(audio_path)
    print(f"  Audio: {audio_path} ({audio_size} bytes)")

    # Write boundary events
    with open(events_path, "w") as f:
        json.dump(boundary_events, f, indent=2)
    print(f"  Word boundaries captured: {len(boundary_events)}")

    if len(boundary_events) == 0:
        print("  WARNING: No WordBoundary events! Check edge-tts version compatibility.")

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
    if img.mode != 'RGB':
        img = img.convert('RGB')
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

events_path = "newrepo2/apocalypse_survival_video/build/word_events.json"
num_frames = 68

# Try to use word boundary events for timing
total_s = None
use_word_timing = False

if os.path.exists(events_path):
    with open(events_path) as f:
        events = json.load(f)

    if events and len(events) > 0:
        # Calculate total duration from last event
        last = events[-1]
        # edge-tts offset and duration are in 100-nanosecond units
        total_s = (last["offset"] + last["duration"]) / 10_000_000.0
        use_word_timing = True
        print(f"  Word-timed total: {total_s:.2f}s ({len(events)} boundaries)")

if total_s is None:
    # Fallback: estimate from word count
    total_s = 272.0
    print(f"  Fallback estimate: {total_s:.2f}s")

frame_duration = total_s / num_frames
print(f"  Per-frame duration: {frame_duration:.3f}s")

# Write concat list
concat_path = "newrepo2/apocalypse_survival_video/build/concat.txt"
with open(concat_path, "w") as f:
    for i in range(1, num_frames + 1):
        sid = f"s{i:02d}"
        img = f"newrepo2/apocalypse_survival_video/build/padded/{sid}.jpg"
        abs_img = os.path.abspath(img)
        f.write(f"file '{abs_img}'\n")
        f.write(f"duration {frame_duration:.4f}\n")
    # FFmpeg concat demuxer requires last entry repeated
    last_img = f"newrepo2/apocalypse_survival_video/build/padded/s{num_frames:02d}.jpg"
    f.write(f"file '{os.path.abspath(last_img)}'\n")

print(f"  Concat list: {concat_path}")
PYEOF
echo ""

# ---- Step 6: Render video with FFmpeg ----
echo "[6/7] Rendering video (libx264, aac 192k, 30fps, yuv420p)..."
CONCAT_FILE="newrepo2/apocalypse_survival_video/build/concat.txt"
AUDIO_FILE="newrepo2/apocalypse_survival_video/build/narration.mp3"
OUTPUT_FILE="newrepo2/apocalypse_survival_video/build/VIDEO.mp4"

# First pass: normalize audio loudness
NORMALIZED_AUDIO="newrepo2/apocalypse_survival_video/build/narration_normalized.mp3"
echo "  Pass 1: Measuring loudness..."
ffmpeg -y -i "$AUDIO_FILE" -af loudnorm=I=-14:LRA=11:TP=-1.5:print_format=json -f null - 2>&1 | tail -20 > "$BUILD/loudnorm_stats.json" || true

echo "  Pass 2: Applying loudness normalization + rendering..."
ffmpeg -y \
  -f concat -safe 0 -i "$CONCAT_FILE" \
  -i "$AUDIO_FILE" \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -r 30 \
  -c:a aac -b:a 192k \
  -af loudnorm=I=-14:LRA=11:TP=-1.5 \
  -shortest \
  "$OUTPUT_FILE" 2>&1 | tail -10

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
