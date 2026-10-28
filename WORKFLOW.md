# Narration-First Video Production Workflow (channel-agnostic)

## Core principle
**Narration is the master timeline. Frames react to the words — never the other way around.**

- Frame count = number of anchors in the script (`len(frames.json)`) — decided at authoring time, never by the audio
- Frame duration = time between anchor timestamps, **measured** from TTS word boundaries — derived, never hand-set
- Audio is synthesized as ONE continuous narration (natural prosody) — never chopped into per-beat clips
- We never pre-decide frame counts or how long frames last; the narration words determine both

## TTS spec
- Engine: `edge-tts` (Microsoft Edge neural voices)
- Voice: `en-US-AndrewNeural` ("Andrew"), rate: **+10%**
- Timing source: **WordBoundary events** (per-word, 100ns precision) captured during synthesis
- edge-tts needs internet + Azure endpoint → runs **only in Kaggle** (assistant sandbox cannot reach it)

## Division of labor (3 locations)

### 1. ASSISTANT WORKSPACE — authoring + frame production
- Research → narration script (pure speakable text + source list)
- `frames.json`: one entry per frame: `{id, anchor_phrase, occurrence, image_prompt, negative_prompt, transition}`
- Frame count known instantly = `len(frames.json)`
- **Frames are generated HERE and visually VERIFIED HERE**: the assistant views every image, rejects/regenerates failures, and holds one locked artstyle across the whole video
- Pipeline code + config authored here
- Estimator QC here: ~0.33 s/word (Andrew @ +10% ≈ 180 wpm) + punctuation pauses (period ≈ 0.3s, comma ≈ 0.2s) → flags flash-frames (< ~1.2s holds) and sanity-checks total runtime
- Optional: silent estimated-timing draft preview for pacing eyeball

### 2. GITHUB — source of truth
- Everything pushed here: narration, `frames.json`, verified frame images, `run.py`, `config.yaml`, README
- Public repo → Kaggle clones without auth (private repo → store PAT in Kaggle Secrets)

### 3. KAGGLE — compute only (timing + render), single short entrypoint
```
!git clone <repo> && pip install -q edge-tts && python run.py --repo . --out final.mp4
```
(Enable Internet in the Kaggle sidebar — it's off by default.)
- **PASS 1**: edge-tts whole narration (Andrew, +10%) → capture WordBoundary stream → match anchors (phrase + occurrence index) into word stream → exact start/end per frame → validate (warn/clamp/merge holds outside min/max) → write `timings.csv` → `--dry-run` stops here for review
- **PASS 2**: ffmpeg places each frame at its exact offset, transitions land on word timestamps, mux with narration → `final.mp4` in `/kaggle/working`

## Repo layout
```
repo/
  WORKFLOW.md
  README.md
  narration/narration.md        # pure TTS text (+ sources section)
  narration/frames.json         # anchors + image prompts (frame count lives here)
  assets/frames/                # generated, visually verified frames (compressed)
  kaggle/config.yaml            # voice, rate, resolution, fps, transitions, min/max hold
  kaggle/run.py                 # the single entrypoint (two-pass)
  output/                       # timings.csv, drafts (git-ignored)
```

## Iteration loop
1. Author script + `frames.json` → push
2. Workspace: generate frames → visually verify each → style-consistency pass → push
3. Kaggle run with `--dry-run` → review `timings.csv`
4. Bad holds / misplaced anchors → adjust anchors in authoring → push → rerun
5. Render final → review → ship

## Calibration
- Workspace estimator ≈ 0.33 s/word (Andrew @ +10%) + punctuation pauses — **authoring QC only**
- After every real Kaggle run: diff `timings.csv` vs estimates → refine the constant so future pre-checks get sharper
- Final sync ALWAYS = Kaggle's measured word boundaries

## Hard rules
- Never chunk TTS per scene/beat; never hand-set frame durations; never generate frames before anchors exist
- Every frame generated and visually verified in the workspace before it's pushed
- Kaggle never authors — it only measures and stitches
- `frames.json` is the single source of truth for frame count

## New-conversation kickoff (paste this plan +)
"Follow this narration-first video workflow exactly. You handle research, the narration script, anchors/frames.json, professional frame generation with visual verification, and push everything to GitHub. I run one Kaggle script for edge-tts (Andrew +10%) timings and final stitch. Frame count and durations are always derived — never authored."
