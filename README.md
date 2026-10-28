# narration-first video pipeline

Narration is the master timeline. Frames react to words — never the other way round.

- **Frame count** = number of anchors in `narration/frames.json`. Fixed at authoring time.
- **Frame duration** = measured time between anchor word boundaries from TTS. Never hand-set.
- **Audio** = one continuous narration, synthesized in a single request. Never chopped per scene.

```
script words ──► edge-tts WordBoundary stream ──► anchor match ──► timings.csv ──► ffmpeg
   (authoring)            (Kaggle, PASS 1)         (exact)         (measured)     (PASS 2)
```

## Quick start

Authoring side (this repo, any machine with python + pillow):

```bash
python tools/prep_frames.py --repo . --sheet --strict   # compress frames + QC sheet
python kaggle/run.py --estimate --repo .                # offline pacing check
python tools/selftest.py                                # prove the pipeline offline
```

Render side (Kaggle notebook, internet ON, one cell):

```bash
!git clone -b arena/9c89fb1f-newrepo2 https://github.com/AsuraXP/newrepo2.git && pip install -q edge-tts pyyaml && python newrepo2/kaggle/run.py --repo newrepo2 --out final.mp4
```

(The `-b` pins the working branch; drop it once this lands on `main`.)

Dry run first — it stops after PASS 1 so you can read `timings.csv`:

```bash
!python newrepo2/kaggle/run.py --repo newrepo2 --dry-run
```

`final.mp4` and `timings.csv` land in `/kaggle/working`.

## Repo layout

```
narration/narration.md     speakable text only (+ sources section, stripped before TTS)
narration/frames.json      anchors + image prompts — single source of truth for frame count
assets/frames/             generated, visually verified frames (1280x720 JPG)
kaggle/config.yaml         voice, rate, resolution, fps, transitions, min/max hold, estimator
kaggle/run.py              single two-pass entrypoint
tools/prep_frames.py       JPG compression + contact sheet for the style pass
tools/selftest.py          fake-TTS end-to-end test: sync, duration, error paths
output/                    timings.csv, estimates.csv, drafts (git-ignored)
WORKFLOW.md                the production loop, in order
PROMPT.md                  authoring brief for a fresh agent
```

## frames.json

```json
[
  {
    "id": "01_cold_open",
    "anchor_phrase": "every glacier in the Alps is shrinking",
    "occurrence": 1,
    "image_prompt": "cinematic wide establishing shot ...",
    "negative_prompt": "text, watermark, extra limbs ...",
    "transition": "fade:0.6"
  }
]
```

- `anchor_phrase` must be copied **verbatim** from `narration.md` — matching is
  token-level, so punctuation and case are ignored but word choice is not.
- `occurrence` selects the *n*-th appearance of that phrase (1-based; negative
  values count from the end). Use it whenever a phrase repeats.
- Frames must appear in narration order. `run.py` fails loudly if they don't.
- `transition` is **how this frame enters**: `name:seconds` with an ffmpeg
  `xfade` name (`fade`, `dissolve`, `wipeleft`, `circleopen`, …), `cut` for a
  2-frame blend that reads as a hard cut, or omitted for the config default.
  The blend *ends* on the anchor word, so the picture settles exactly as the
  phrase is spoken.

## Timing rules

| rule | value | behaviour |
| --- | --- | --- |
| min hold | `1.2 s` | shorter frame merges into its neighbour (`under_min_policy`) |
| max hold | `12 s` | warning only — clamping would break word sync |
| first frame | starts at 0.0 s | warns if the first anchor lands after `lead_in_max_s` |
| last frame | +`0.8 s` tail | holds after the last word so the audio can breathe |
| transitions | complete on the anchor word | xfade offset = anchor start − transition duration |
| spare frame | +1 frame per clip | xfade always has material at the boundary |

Frame *n* ends exactly where frame *n+1*'s anchor word begins, so every cut, wipe
or dissolve lands on a spoken word.

## Calibration

`--estimate` uses `0.33 s/word` (Andrew @ +10% ≈ 180 wpm) plus punctuation
pauses. That estimator is **authoring QC only**. Every real Kaggle run prints

```
calibration: est 148.2s vs measured 151.6s -> suggested sec_per_word 0.3371
```

and writes the same numbers to `/kaggle/working/calibration.json`. Paste the new
constant into `kaggle/config.yaml → estimate.sec_per_word` so the next script's
pacing check is sharper. Final sync is always the measured word boundaries.

## Requirements

Kaggle: `edge-tts`, `pyyaml`, `ffmpeg` (preinstalled on Kaggle images).
Authoring: `pillow`, `pyyaml` (+ `numpy` for the selftest). No TTS and no
network needed for `--estimate`.

`run.py` finds ffmpeg on `PATH`; set `FFMPEG_BIN=/path/to/ffmpeg` to point at a
specific binary (that is how `tools/selftest.py` runs here).
