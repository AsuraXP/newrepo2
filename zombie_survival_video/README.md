# zombie_survival_video — THE LIST

Animated short, ~5 minutes, 16:9, YouTube. Fictional zombie survival narration.

## Status

| Stage | State |
|---|---|
| 1. Brief | done (style ref pending) |
| 2. Script | **draft 3 (procedural rewrite) — awaiting go** |
| 3. Spine (`visuals.csv`) | stale, archived — rebuild after go |
| 4. Consistency set (refs) | done — 4 anchors locked, reusable |
| 5. Frames | 0 |
| 6. Kaggle runner | not written |
| 7. Deliverable | in Kaggle only |

## Layout

```
zombie_survival_video/
├── README.md        this file
├── brief.md         locked parameters + hard rules
├── script.md        narration, one line = one spoken beat
├── visuals.csv      the spine (slide_id,moment,moment_text,visual_prompt)
├── metadata.json    consumed by the runner for packaging
├── youtube.txt      title, description, tags, chapters
├── STATE.md         batch log: frames done, rejects, anchors
├── continuity.md    style lock, anchors, moderation substitutions
├── frames/          beatNNmNN.png
└── refs/            style + character + location anchors
```

## The pipeline

1. **Script** is the only place duration is decided. Frame count and per-frame
   duration are *outputs*: the script's beats set the number of frames, and TTS
   word timestamps set how long each one holds.
2. **`visuals.csv`** carries one row per visual moment, with `moment_text` being
   the exact words spoken under that frame.
3. **Frames** are generated here, named `beat{slide:02d}m{moment:02d}.png`, QC'd
   against anchors in `refs/`, and committed every 8–16 accepted frames.
4. **`run_<slug>_kaggle.sh`** (repo root) is the only place sound exists: it
   clones the branch, runs one continuous TTS take with word timestamps, derives
   each frame's duration from those timestamps, pads frames to a uniform even
   canvas with PIL, stitches at native resolution with ffmpeg, and zips
   `VIDEO.mp4 + thumbnail.jpg + metadata.json + script.md + youtube.txt`.

## Audio boundary

No TTS, no mixing, no ffmpeg encoding happens in this workspace. Runtime numbers
in `brief.md` and `metadata.json` are projections: script words ÷ 3.1 wps.

## Running it

One Kaggle cell, no edits:

```python
!rm -rf newrepo2
!git clone --depth 1 --branch arena/ffbfba80-newrepo2 https://github.com/AsuraXP/newrepo2.git
!bash newrepo2/run_zombie_survival_video_kaggle.sh
```

Output: `/kaggle/working/zombie_survival_video_DELIVERABLE.zip`
