# Production record and gates

This checkout is a production in progress. Phases 0–2 have passed: calibration is recorded, the 913-word narration has user read-aloud approval, and 43 sentence-start anchors pass the offline estimate. Phase 3 is in progress; the user-selected style is locked, and frames 01–10 have been generated and visually reviewed. Frames 11–43 remain.

## Episode premise

A second-person, explicitly fictional survival scenario in Rome around 200 CE. The outbreak rules are slow-moving undead and bite transmission; the episode focuses on immediate decisions available to an ordinary renter: leave a dense neighborhood, find water and food, avoid bottlenecks, and seek a defensible shelter. This is not a claim about a real historical event.

## Calibration (episode 1)

- edge-tts: 7.3.1
- granularity: sentence-level; 7 boundary events for 65 words (9.29 words/event)
- sec_per_word: 0.3268 (set in `kaggle/config.yaml`)
- measured with: `narration/preflight.md`, 65 words, `en-US-AndrewNeural` @ `+10%`; audio duration 21.240s
- sync_source: sentence-boundary timestamps; words within sentences interpolated
- recovered word count: 65/65

## Phase 0 — preflight calibration (Kaggle)

The workspace must not run TTS. In a Kaggle notebook with Internet enabled, clone this public repo and run these cells from the notebook working directory:

```python
!pip install -q --upgrade --force-reinstall edge-tts pyyaml
!python -c "import edge_tts; print('edge-tts', edge_tts.__version__)"
!python newrepo2/kaggle/run.py --repo newrepo2 --dry-run --tts-debug --preflight
```

The script reports boundary event count, words per event, suggested seconds per word, and the installed Edge TTS version. `kaggle/config.yaml` explicitly requests `SentenceBoundary` by default; you may select `WordBoundary` before calibration, but keep that setting unchanged for the episode render. Inspect the output and preflight audio; record the observed values above, then copy the measured rate into `kaggle/config.yaml`. Keep the actual observed boundary granularity wording; do not label sentence-level timing as word-level. `--preflight` synthesizes the marked preflight passage in exactly one request. It writes runtime artifacts under `kaggle/output/`.

### Gate 0

- [x] `sync_source` is printed and understood
- [x] Boundary granularity and words/event recorded; Phase 2 rules follow the measured granularity (sentence-level)
- [x] `estimate.sec_per_word` equals the measured value (0.3268)
- [x] Non-zero audio duration (21.240s); recovered words match marked preflight text (65/65)

## Phase 1 — research and script

Research the selected topic and retain source URLs. Put speakable prose only between the TTS markers in `narration/narration.md`; put citations in `## Sources` after the end marker. No markup, headings, bullets, links, or stage directions inside the markers. Write for speech, use estimates honestly, and do not pad or compress for a target runtime.

### Gate 1

- [x] No markdown characters or non-spoken material inside the TTS markers
- [x] Every historical factual claim has a source in `## Sources`
- [x] Estimated duration reported as an estimate, not a target (about 4:58)
- [x] Read aloud once; user approved the draft as sounding good

## Phase 2 — anchors

For word-boundary timing, anchors can land on any word. For sentence-level timing, every anchor must be the first words of a distinct sentence; there can be no two anchors in one sentence. In all cases use 3–8 verbatim words, one anchor per sentence, ordered in narration, with explicit `occurrence` for repeated phrases. Aim for 5–10 seconds per frame; holds under 3 seconds or over 12 seconds fail. A frame entry has this shape:

```json
{
  "id": "01_example",
  "anchor_phrase": "Copied words from the script",
  "occurrence": 1,
  "image_prompt": "subject and action, followed by the exact style token block",
  "negative_prompt": "the exact negative token block"
}
```

Do not add a hand-set duration. `frames.json` alone determines the number of frames; measured anchor timestamps determine their holds. The first anchor must begin the narration so the first measured image starts at time zero.

Run the offline check (no network, no Azure):

```bash
python kaggle/run.py --estimate --repo .
```

### Gate 2

Offline estimate (`python kaggle/run.py --estimate --repo .`): 43/43 anchors matched; estimated runtime 298.37 s (4:58); estimated holds 5.882–8.170 s; zero warnings. `timings.csv` contains 43 rows for 43 entries in `frames.json`.

- [x] Every anchor matched, in order; no missing/duplicate ambiguity
- [x] Frame/anchor count is 43 entries; no entries merged
- [x] Shortest estimated hold ≥3 s, longest ≤12 s, no warnings
- [x] Estimated runtime is plausible for the topic; estimate only
- [x] Sentence-level engine: one anchor at the start of each distinct sentence

## Phase 3 — frames and visual QC (workspace)

The style token block in `assets/STYLE.md` is frozen to the user's three cartoon references. The 16:9 reference frame was inspected and accepted; frames 01–10 were generated in small batches and visually checked against it. The image-generation allowance for this turn is exhausted, so frames 11–43 remain pending. Continue in small batches and inspect every image before compression. Regenerate any wrong subject/action, off-model character, palette drift, text/watermark, extra limbs, or different-film look. Keep only reviewed compressed 1280×720 JPGs; uncompressed/source images stay out of Git.

```bash
python tools/prep_frames.py --repo . --sheet --strict
```

### Gate 3

- [ ] Strict prep reports all frames present
- [ ] Contact sheet reviewed end-to-end
- [ ] Every frame is on-model: same character, palette and line weight
- [ ] Frame repo weight is reasonable (target well under 5 MB)

## Phase 4 — verify, then measure (Kaggle)

Run the offline selftest before trusting a render:

```bash
python tools/selftest.py
```

Then, on Kaggle, force-reinstall as above and run:

```python
!python newrepo2/kaggle/run.py --repo newrepo2 --dry-run
```

Inspect `kaggle/output/timings.csv`: no `merged_*` or `warn_*` status, inspect `anchor_precision` and `matched_text`, and compare `hold_s` with `est_hold_s`. Update the rate only when measured evidence warrants it.

### Gate 4

- [ ] Selftest passes
- [ ] Rendered frame count equals `frames.json`
- [ ] No merged or warned frames
- [ ] Any in-sentence anchors moved to sentence starts or knowingly accepted
- [ ] Calibration updated if estimator drifted

## Phase 5 — render

```python
!python newrepo2/kaggle/run.py --repo newrepo2 --out final.mp4
```

Static camera only; no zoom or drift. Transitions are at least 0.8 seconds, with 1.0 second default.

### Gate 5

- [ ] Duration matches measured narration within one second
- [ ] Picture is static when the frame is static
- [ ] Every cut is a visible transition, not a snap
- [ ] Audio present and synchronized

## Phase 6 — publish assets (only after Gate 5)

Generate thumbnail art with text baked in; proof at 336 px. Then write a concrete first-person title, honest description, chapters from measured `timings.csv`, and sources.

### Gate 6

- [ ] Thumbnail text legible at 336 px
- [ ] Chapter timestamps verified against `timings.csv` line by line
- [ ] Description runtime matches rendered file
