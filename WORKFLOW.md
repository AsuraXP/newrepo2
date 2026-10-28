# WORKFLOW — narration-first production loop

Narration is the master timeline. Frames react to the words.

## 0. Preflight — calibrate the engine first

Before writing a word, measure what the TTS engine actually does. See `PROMPT.md` Phase 0.

```python
!pip install -q --upgrade --force-reinstall edge-tts pyyaml
!python newrepo2/kaggle/run.py --repo newrepo2 --dry-run --tts-debug
```

Record three things in `PRODUCTION.md`: edge-tts version, boundary granularity
(words per event), and the suggested `sec_per_word`. Put the rate into
`kaggle/config.yaml`. If granularity is sentence-level rather than per-word, place every
anchor at a sentence start — one per sentence — before authoring `frames.json`.

Do not proceed on an assumed rate or an assumed granularity.

## The three locations

| location | owns | never does |
| --- | --- | --- |
| **workspace** | research, script, `frames.json`, frame generation + visual QC, all code | TTS (needs Azure) |
| **GitHub** | source of truth; every artifact the render needs | — |
| **Kaggle** | PASS 1 TTS + anchoring, PASS 2 stitch | authoring, prompt edits, frame regeneration |

## Loop

### 1. Research → script

Write `narration/narration.md` as **pure speakable text**, wrapped in markers:

```
<!-- TTS:START -->
The speakable narration lives here. Plain sentences, no headings, no bullets,
no markdown emphasis, no links, no parenthetical asides.
<!-- TTS:END -->

## Sources
- ...
```

Everything between the markers is what gets synthesized, verbatim. Everything
after `## Sources` is stripped. Wrap it anyway — the markers are authoritative.

Rules that matter for timing later:
- 90–160 words per minute of target runtime; Andrew @ +10% ≈ 180 wpm raw.
- Anchor phrases should be **short (3–8 words)** and **unique**, or count the
  repeats with `occurrence`.
- **One anchor per sentence, placed at the sentence start.** Two anchors inside one
  sentence collapse onto the same instant on sentence-level engines.
- Never put an anchor inside a sentence you also anchor mid-way through — keep
  anchors in reading order and non-overlapping.
- One anchor per frame. A 2-minute video is typically 20–30 frames.

### 2. Frames spec

`narration/frames.json` — one entry per frame, in narration order:

| field | notes |
| --- | --- |
| `id` | stable, ordered, `NN_slug` |
| `anchor_phrase` | verbatim from the script; the frame starts on this word |
| `occurrence` | which appearance of the phrase (1-based; negative = from end) |
| `image_prompt` | subject + action + light + lens, ending with the style token |
| `negative_prompt` | what must never appear (text, watermark, etc.) |
| `transition` | how the frame **enters**: `fade:0.6`, `dissolve:0.5`, `wipeleft:0.4`, `cut`, … |

Frame count is known the instant this file is valid: `len(frames.json)`.
Nothing downstream is allowed to change it.

### 3. Generate + verify frames (workspace only)

1. Fix the **style token set** once (see `PROMPT.md`), generate a reference frame,
   and reuse the token block verbatim in every prompt.
2. Generate every frame. Then **look at each one**. Reject and regenerate:
   wrong subject, mangled anatomy, text/watermark, off-palette, wrong aspect.
3. Style-consistency pass: build the contact sheet and compare side by side.
   Anything that reads as a different film gets regenerated.
4. Compress and normalise:

```bash
python tools/prep_frames.py --repo . --sheet --strict
```

Output: `assets/frames/NN_slug.jpg` at 1280×720, ~120–250 KB each.
The contact sheet goes to `output/contact_sheet.jpg` (git-ignored, QC only).

### 4. Offline pacing check

```bash
python kaggle/run.py --estimate --repo .
```

First green light: `python tools/selftest.py` exercises the whole pipeline
(fake TTS, synthetic frames, real ffmpeg) and asserts three things:

1. every frame lands on its anchor timestamp
2. **the picture is static** — mean frame-to-frame change under 0.15, which fails
   if `ken_burns` is ever switched back on (zoompan judders on still frames)
3. **transitions actually blend** — 60%+ of sampled frames inside a transition
   window must match neither source image; otherwise the cut is snapping

Run it after touching `run.py` or the transition/camera settings.

Reads the same script, same anchors, and reports estimated holds +
`output/estimates.csv`. Fix here, not on Kaggle:

- a frame estimated **< 1.2 s** → merge it with a neighbour or extend the anchor
- a frame **> 12 s** → add an anchor to split it
- total runtime wildly off target → rewrite, don't pad
- any `match_quality=loose` → the anchor text drifted from the script

### 5. Push

```bash
git add -A && git commit -m "..." && git push
```

Repo must be public (or clone with a PAT from Kaggle Secrets).

### 6. Kaggle — dry run

```bash
!git clone https://github.com/AsuraXP/newrepo2.git && pip install -q edge-tts pyyaml && python newrepo2/kaggle/run.py --repo newrepo2 --dry-run
```

Review `/kaggle/working/timings.csv`:

- `status` — any `merged_*` / `warn_*` rows
- `hold_s` vs `est_hold_s` — big deltas mean the estimator constant needs updating
- `matched_text` — the words the anchor actually landed on
- `start_s` monotonic, last `end_s` ≈ narration length

Bad holds or misplaced anchors → fix anchors **in authoring**, push, rerun.

### 7. Render

```bash
!python newrepo2/kaggle/run.py --repo newrepo2 --out final.mp4
```

PASS 2 writes `/kaggle/working/final.mp4`, plus `render_manifest.json` and
`ffmpeg_cmd.txt` for reproducibility. Review, then ship.

### 8. Calibrate

Take `suggested_sec_per_word` from the run output and put it in
`kaggle/config.yaml → estimate.sec_per_word`. Commit.

## Hard rules

- Never chunk TTS per scene or beat. One request, one track, one prosody.
- Never hand-set frame durations or frame counts.
- Never generate frames before the anchors exist.
- Never push a frame you have not looked at.
- Kaggle never authors — it measures and stitches.
- `frames.json` is the only source of frame count.
