#!/usr/bin/env bash
# run_apocalypse_survival_kaggle.sh — v3 (uses vidsync library for word-accurate TTS)
# Run in a Kaggle notebook cell (internet ON):
#   !rm -rf newrepo2
#   !git clone --depth 1 --branch arena/138cc5e0-newrepo2 https://github.com/AsuraXP/newrepo2.git
#   !bash newrepo2/run_apocalypse_survival_kaggle.sh

set -euo pipefail

REPO="newrepo2"
PROJECT="${REPO}/apocalypse_survival_video"
BUILD="${PROJECT}/build"
FRAMES="${PROJECT}/frames"

echo "=== APOCALYPSE SURVIVAL KAGGLE RUNNER v3 ==="
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

# ---- Step 3: Run TTS with word-level timestamps using vidsync library ----
echo "[3/7] Synthesizing narration with WordBoundary (via vidsync.RealEdgeTTS)..."
python3 << 'PYEOF'
import sys, re
sys.path.insert(0, "newrepo2")

from vidsync.tts import RealEdgeTTS, TTSError

# Read narration from script.md
with open("newrepo2/apocalypse_survival_video/script.md") as f:
    text = f.read()

# Extract speakable text: skip headers, join paragraphs
lines = text.split('\n')
paragraphs = []
current = []
for line in lines:
    s = line.strip()
    if s.startswith('#'):
        if current:
            paragraphs.append(' '.join(current))
            current = []
        continue
    if not s:
        if current:
            paragraphs.append(' '.join(current))
            current = []
        continue
    current.append(s)
if current:
    paragraphs.append(' '.join(current))

narration = ' '.join(paragraphs).strip()
narration = re.sub(r'\*+', '', narration)
narration = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', narration)

word_count = len(narration.split())
print(f"  Narration: {len(narration)} chars, ~{word_count} words")

audio_path = "newrepo2/apocalypse_survival_video/build/narration.mp3"

tts = RealEdgeTTS(voice="en-US-AndrewNeural", rate="+10%")
result = tts.synthesize(narration, audio_path, boundary="WordBoundary")

print(f"  Audio: {result.audio_path} ({result.audio_duration_s:.2f}s)")
print(f"  Word boundaries: {len(result.events)}")
print(f"  Requested boundary: {result.requested_boundary}")
print(f"  Returned types: {result.returned_boundary_types}")
for note in result.notes:
    print(f"  NOTE: {note}")

# Save events as JSON for downstream use
import json
events_data = []
for e in result.events:
    events_data.append({
        "type": e.type,
        "offset_s": e.offset_s,
        "duration_s": e.duration_s,
        "text": e.text,
    })
with open("newrepo2/apocalypse_survival_video/build/word_events.json", "w") as f:
    json.dump(events_data, f, indent=2)

if len(result.events) == 0:
    print("  ERROR: No word boundaries returned! Check Kaggle internet is ON.")
    sys.exit(1)

print("  Word-level TTS complete.")
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

# ---- Step 5: Build frame timing from word boundaries ----
echo "[5/7] Computing per-frame durations from word boundaries..."
python3 << 'PYEOF'
import json, os

events_path = "newrepo2/apocalypse_survival_video/build/word_events.json"
with open(events_path) as f:
    events = json.load(f)

num_frames = 68
total_s = events[-1]["offset_s"] + events[-1]["duration_s"]
print(f"  Total audio: {total_s:.2f}s ({len(events)} word boundaries)")

# Compute word-indexed timeline: each word has a start time
# Map each frame to the words it should cover (even distribution)
words_per_frame = len(events) / num_frames

# For each frame, compute start/end from the word boundaries
frame_timings = []
for i in range(num_frames):
    start_word_idx = int(i * words_per_frame)
    end_word_idx = int((i + 1) * words_per_frame)
    if end_word_idx >= len(events):
        end_word_idx = len(events) - 1

    start_s = events[start_word_idx]["offset_s"]
    end_s = events[end_word_idx]["offset_s"] + events[end_word_idx]["duration_s"]
    duration = end_s - start_s
    frame_timings.append({
        "frame_id": f"s{i+1:02d}",
        "start_s": start_s,
        "end_s": end_s,
        "duration_s": duration,
        "words_covered": end_word_idx - start_word_idx + 1,
    })

# Write timings
timings_path = "newrepo2/apocalypse_survival_video/build/frame_timings.json"
with open(timings_path, "w") as f:
    json.dump(frame_timings, f, indent=2)
print(f"  Timings written: {num_frames} frames")

# Write FFmpeg concat list
concat_path = "newrepo2/apocalypse_survival_video/build/concat.txt"
with open(concat_path, "w") as f:
    for ft in frame_timings:
        sid = ft["frame_id"]
        img = f"newrepo2/apocalypse_survival_video/build/padded/{sid}.jpg"
        abs_img = os.path.abspath(img)
        f.write(f"file '{abs_img}'\n")
        f.write(f"duration {ft['duration_s']:.4f}\n")
    # FFmpeg concat requirement: repeat last entry
    last_img = f"newrepo2/apocalypse_survival_video/build/padded/s{num_frames:02d}.jpg"
    f.write(f"file '{os.path.abspath(last_img)}'\n")

print(f"  Concat list written")
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
cd "$PROJECT"
DELIVERABLE="apocalypse_survival_DELIVERABLE.zip"

zip -j "$DELIVERABLE" \
  build/VIDEO.mp4 \
  build/narration.mp3 \
  build/word_events.json \
  build/frame_timings.json \
  metadata.json \
  script.md \
  youtube.txt \
  visuals.csv \
  brief.md \
  README.md
echo "  Deliverable: $PROJECT/$DELIVERABLE"
echo ""

echo "=== DONE ==="
echo "Download $DELIVERABLE from Kaggle output."
