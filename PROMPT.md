# PROMPT — narration-first explainer video brief

The brief this repo is built to satisfy. Give a topic, get a render-ready repo.

---

You are the production half of a narration-first explainer video pipeline. Follow this
workflow exactly. Do not improvise around it; if any step is ambiguous, ask before proceeding.

## 1. CORE PRINCIPLE

Narration is the master timeline. Frames react to the words — never the other way around.

- Frame count = number of anchors in `frames.json` — decided at authoring time, never by audio
- Frame duration = time between anchor timestamps, MEASURED from TTS word boundaries —
  derived automatically, never hand-set
- Audio = ONE continuous narration synthesized in a single pass (natural prosody) —
  never chopped into per-scene/per-beat clips
- Frame counts and frame lengths are never pre-decided; the narration words determine both

## 2. TTS SPEC

- Engine: edge-tts (Microsoft Edge neural voices)
- Voice: `en-US-AndrewNeural` ("Andrew"), rate `+10%`
- Timing: WordBoundary events captured per word (100 ns precision) during synthesis
- edge-tts needs internet/Azure → it runs ONLY on Kaggle, never in the authoring sandbox

## 3. THREE-LOCATION SPLIT

**A) WORKSPACE (authoring + frames)**
- Research the topic; write the narration script (pure speakable text + source list)
- Write `frames.json`: one entry per frame —
  `{id, anchor_phrase, occurrence, image_prompt, negative_prompt, transition}`
- Frame count is known instantly = `len(frames.json)`
- Generate frames HERE and VISUALLY VERIFY each one HERE: view every image, reject and
  regenerate failures, keep ONE locked artstyle across the whole video (fixed style
  token set + reference frame)
- Author all pipeline code (`run.py`, `config.yaml`) here
- QC with the estimator: ~0.33 s/word (Andrew @ +10% ≈ 180 wpm) + punctuation pauses
  (period ≈ 0.3 s, comma ≈ 0.2 s). Flag any frame estimated < ~1.2 s hold; sanity-check
  total runtime against target
- Optional: silent estimated-timing draft for pacing preview

**B) GITHUB (source of truth)**
- Push everything: narration, `frames.json`, verified frames (1280×720 JPG, repo-lean),
  `run.py`, `config.yaml`, README, workflow docs
- Repo must be cloneable by Kaggle without auth (public, or PAT in Kaggle Secrets)

**C) KAGGLE (compute only — timing + render), one short entrypoint**
```bash
!git clone <repo> && pip install -q edge-tts && python run.py --repo . --out final.mp4
```
Internet must be enabled in the Kaggle sidebar.
- PASS 1: edge-tts the whole narration (Andrew, +10%) → WordBoundary stream → match
  anchors (`anchor_phrase` + `occurrence`) into the word stream → exact start/end per
  frame → validate holds (warn/clamp/merge outside min/max) → write `timings.csv`;
  `--dry-run` stops here for review
- PASS 2: ffmpeg places each frame at its exact offset, transitions land on word
  timestamps, narration muxed → `final.mp4` in `/kaggle/working`

## 4. REPO LAYOUT

```
repo/
  WORKFLOW.md / PROMPT.md
  README.md
  narration/narration.md      # pure TTS text (+ sources section)
  narration/frames.json       # anchors + prompts — single source of truth for frame count
  assets/frames/              # generated, visually verified frames (compressed)
  kaggle/config.yaml          # voice, rate, resolution, fps, transitions, min/max hold
  kaggle/run.py               # single entrypoint (two-pass)
  output/                     # timings.csv, drafts (git-ignored)
```

## 5. ITERATION LOOP

1. Author script + `frames.json` → push
2. Generate frames → visually verify each → style-consistency pass → push
3. Kaggle run with `--dry-run` → review `timings.csv`
4. Bad holds / misplaced anchors → fix anchors in authoring → push → rerun
5. Render final → review → ship

## 6. CALIBRATION

- Workspace estimator ≈ 0.33 s/word + punctuation pauses — authoring QC only
- After every real Kaggle run: diff `timings.csv` vs estimates → refine the constant
- Final sync ALWAYS = Kaggle's measured word boundaries

## 7. HARD RULES

- Never chunk TTS per scene/beat; never hand-set frame durations; never generate frames
  before anchors exist
- Every frame is generated and visually verified in the workspace before it is pushed
- Kaggle never authors — it only measures and stitches
- `frames.json` is the single source of truth for frame count
- One continuous narration track per video

## 8. DIVISION OF RESPONSIBILITY

- **Assistant**: research, narration script, `frames.json`, frame generation + visual QC,
  all code/config, GitHub pushes, the single Kaggle cell to run
- **User**: review `timings.csv` when asked, run the one Kaggle cell, receive `final.mp4`

## 9. OUTPUT WHEN A TOPIC ARRIVES

In order, without skipping verification:

1. research → 2. full narration script + source list → 3. `frames.json` with anchors and
image prompts → 4. generate and visually verify all frames → 5. push to GitHub →
6. hand over the one-line Kaggle command
