# PROMPT — narration-first explainer video (production spec)

A workflow for producing one explainer episode: research → script → anchors → frames →
measured render. Every phase ends with a **gate**. Do not start the next phase until the
current gate passes. Gates exist so that no phase proceeds on an assumption the next
phase depends on.

---

## 0. CORE PRINCIPLE

Narration is the master timeline. Frames react to the words.

- **Frame count** = the number of anchors in `frames.json`. Decided at authoring time.
- **Frame duration** = measured time between anchor timestamps. Derived, never hand-set.
- **Audio** = one continuous narration, synthesized in a single request. Never chunked
  per scene, per beat, or per paragraph.
- **Runtime** is an output, not an input. Never trim the script to hit a target length.

Nothing downstream may change the frame count. If an anchor has to move, the frame
count is re-derived from `frames.json`, not adjusted by hand.

---

## 1. THREE LOCATIONS

| location | owns | must never do |
| --- | --- | --- |
| **Workspace** | research, script, anchors, frame generation + visual QC, all code and config | run TTS (needs Azure) |
| **GitHub** | source of truth: everything the render needs, cloneable without auth | hold large binaries |
| **Kaggle** | TTS + measured timing, and stitching | author content, edit prompts, regenerate frames |

Kaggle never authors. The workspace never synthesizes. Keep that boundary absolute.

---

## PHASE 0 — PREFLIGHT CALIBRATION (Kaggle, before any authoring)

**Purpose:** replace assumptions about the TTS engine with measurements. This phase runs
before a single word of narration is written, because everything after it depends on two
numbers.

### Do

1. Create `narration/preflight.md` containing roughly 60 words of plain prose with
   several sentences, wrapped in the standard `<!-- TTS:START -->` / `<!-- TTS:END -->`
   markers.
2. On Kaggle, with Internet enabled, run:

   ```python
   !pip install -q --upgrade --force-reinstall edge-tts pyyaml
   !python -c "import edge_tts; print('edge-tts', edge_tts.__version__)"
   ```

   Always force-reinstall. A cached wheel is the single most common cause of a TTS pass
   producing nothing.
3. Run the preflight render with `--tts-debug`:

   ```python
   !python newrepo2/kaggle/run.py --repo newrepo2 --dry-run --tts-debug
   ```

4. Read three numbers out of the output and record them:

   | number | where it appears | goes into |
   | --- | --- | --- |
   | **word-boundary granularity** | `N boundary events (X words each)` | `WORKFLOW.md` production log |
   | **seconds per word** | `suggested sec_per_word` | `kaggle/config.yaml → estimate.sec_per_word` |
   | **edge-tts version** | first line of PASS 1 | `WORKFLOW.md` production log |

### Record it

Write the three values into `PRODUCTION.md` at the repo root:

```markdown
## Calibration (episode N)
- edge-tts: 7.3.1
- granularity: 1 boundary event per 10.2 words (sentence-level)
- sec_per_word: 0.246
- measured with: preflight.md, 60 words, voice en-US-AndrewNeural @ +10%
```

### Gate 0

- [ ] `sync_source` is printed and understood
- [ ] Granularity is recorded — **if it is anything other than `measured`
      (one event per word), then Phase 2's anchor rules change. Read them before writing.**
- [ ] `estimate.sec_per_word` in `config.yaml` matches the measured value
- [ ] Audio duration is non-zero and the word count recovered matches the preflight text

---

## PHASE 1 — RESEARCH AND SCRIPT

### Do

1. Research the topic. Collect sources as you go, with URLs.
2. Write `narration/narration.md`:
   - Speakable text only between `<!-- TTS:START -->` and `<!-- TTS:END -->`
   - No headings, bullets, links, markdown emphasis, or parenthetical stage directions
     inside the markers
   - A `## Sources` section after the end marker — it is stripped before synthesis
3. Write for the ear, not the page: short sentences, concrete nouns, one idea per
   sentence. A sentence break is a natural breath and a good place for a frame anchor.
4. State estimates as estimates ("perhaps one person in a hundred"). Never invent a
   precise figure to sound authoritative.
5. Let the runtime be whatever the script honestly takes. Do not pad, do not compress.

### Gate 1

- [ ] Script contains no markdown characters that TTS would read aloud
- [ ] Every factual claim has a source in `## Sources`
- [ ] Estimated duration is reported, and is treated as an estimate only
- [ ] Read it aloud once. Any sentence you stumble over is rewritten, not kept

---

## PHASE 2 — ANCHORS (`frames.json`)

This is where timing is won or lost. Anchor placement decides whether the final video is
word-accurate or approximately right.

### The granularity rule (read Gate 0 before this)

Ask what the engine reports for one boundary event:

| Granularity | Meaning | What you must do |
| --- | --- | --- |
| **one event per word** | every word has a measured timestamp | anchors may sit anywhere; word-accurate sync is achievable |
| **one event per sentence** | only sentence starts are measured; words inside are interpolated | **place every anchor at a sentence start**, one anchor per sentence, no exceptions |

On sentence-level engines an anchor placed mid-sentence is interpolated, so its timing is
approximate and two anchors in the same sentence can collapse onto the same instant. Both
are avoidable by construction: anchor on the first word of a sentence.

### Anchor rules

- `anchor_phrase` is copied **verbatim** from the narration — 3 to 8 words
- **One anchor per sentence.** Never two anchors inside the same sentence.
- Anchor on the **first words of a sentence** wherever the sentence could plausibly open a frame
- Anchor cadence: one frame per **5–10 seconds** of narration. Under 3 s and the image never
  registers; over 12 s and the picture goes stale
- Frames appear in narration order; anchors never overlap
- `occurrence` selects *which* appearance of a repeated phrase (1-based, negative counts
  from the end). Use it whenever a phrase repeats — never rely on the first match by accident
- `transition` is **optional**. Omit it and the config default applies. Only override when a
  specific beat needs a different move

### Frame entry

```json
{
  "id": "07_no_year",
  "anchor_phrase": "Nobody here will tell you the year",
  "occurrence": 1,
  "image_prompt": "<subject>, <verbatim style token block>",
  "negative_prompt": "<verbatim negative token block>"
}
```

### Gate 2

Run the offline check — no network, no Azure:

```bash
python kaggle/run.py --estimate --repo .
```

- [ ] Every anchor matched; no `MISSING` or order errors
- [ ] `frames rendered` equals the number of entries in `frames.json` — nothing merged
- [ ] Shortest hold ≥ 3 s, longest ≤ 12 s, no warnings
- [ ] Estimated runtime is within the intended range for this topic
- [ ] On a sentence-level engine: no two anchors share a sentence

---

## PHASE 3 — FRAMES AND VISUAL QC (workspace)

### Do

1. Fix the style token set once, in `assets/STYLE.md`. Generate a reference frame and
   inspect it before generating anything else.
2. Append the style token block **verbatim** to every prompt. Same negative block every
   time. Consistency across the episode is the channel's identity; per-frame creativity
   breaks it.
3. Generate in small batches. **Open every image and look at it.** Reject and regenerate on:
   - wrong subject or action
   - off-model character (face, hands, proportions)
   - palette drift
   - text, watermarks, extra limbs
   - anything that reads as a different film
4. Keep the reference frame open beside each batch and compare directly.
5. Compress to 1280×720 JPG and build a contact sheet:

   ```bash
   python tools/prep_frames.py --repo . --sheet --strict
   ```

6. Review the contact sheet as one document. Any frame that stands out is regenerated.

**Never push a frame you have not looked at.** Compressed JPGs only; source PNGs stay out
of the repo.

### Gate 3

- [ ] `prep_frames.py --strict` reports every frame present
- [ ] Contact sheet reviewed end-to-end in one pass
- [ ] Every frame on-model: same character, same palette, same line weight
- [ ] Repo weight is reasonable (target: well under 5 MB of frames)

---

## PHASE 4 — VERIFY THE PIPELINE, THEN MEASURE

### Do

1. Run the selftest **before** trusting a render. It uses a stand-in TTS backend and
   synthetic frames, so it needs no network:

   ```bash
   python tools/selftest.py
   ```

   It asserts: sync at every anchor, a genuinely static picture, transitions that actually
   blend, correct duration, audio muxed, and that a missing anchor fails loudly.

2. Dry pass on Kaggle:

   ```python
   !python newrepo2/kaggle/run.py --repo newrepo2 --dry-run
   ```

3. Read `timings.csv` and check:
   - `status` — no `merged_*`, no `warn_*`
   - `anchor_precision` — `exact` where possible; any `in-sentence` row is a candidate to
     move to a sentence start
   - `hold_s` vs `est_hold_s` — if these drift systematically, update `sec_per_word`
   - `matched_text` — confirms which words the anchor actually landed on

### Gate 4

- [ ] Selftest passes
- [ ] `frames rendered` equals the frame count
- [ ] No merged or warned frames
- [ ] `in-sentence` anchors are either moved to sentence starts or accepted knowingly
- [ ] Calibration updated in `config.yaml` if the estimator drifted

---

## PHASE 5 — RENDER

```python
!python newrepo2/kaggle/run.py --repo newrepo2 --out final.mp4
```

Static camera. No zoom, no drift, ever — a slow zoom on a still image steps in whole-pixel
jumps and reads as shake. Transitions are long enough to be seen: **0.8 s minimum, 1.0 s
default** for flat 2D art, which has no motion cues to imply a gradual change.

### Gate 5

- [ ] Duration matches the measured narration length within a second
- [ ] Picture is static when the frame is static
- [ ] Every cut is visible as a transition, not a snap
- [ ] Audio present and synchronised

---

## PHASE 6 — PUBLISH ASSETS (only after Gate 5)

Order matters: title, thumbnail and chapter timestamps are all downstream of the **measured**
runtime. Writing them earlier means rewriting them.

1. **Thumbnail** — generate the art with any text baked in; never composite text afterwards.
   Keep overlay wording to three or four words. Proof it at 336 px wide: if the words are
   not legible there, they do not exist.
2. **Title** — concrete, first person, matches the channel's voice.
3. **Description** — hook, honest summary, then chapters cut directly from `timings.csv`
   (not from estimates), then sources.
4. **Chapters** — verified against `timings.csv` line by line.

### Gate 6

- [ ] Thumbnail legible at 336 px
- [ ] Chapter timestamps derived from `timings.csv`, not estimated
- [ ] Runtime in the description matches the rendered file

---

## HARD RULES

1. Calibrate the engine before authoring. Never author against an assumed rate.
2. One continuous narration request per video. Never chunk TTS.
3. Never hand-set a frame duration. Durations are measured.
4. Never generate a frame before its anchor exists.
5. One anchor per sentence. Two anchors in one sentence collapse on sentence-level engines.
6. Every frame is viewed before it is pushed.
7. The style token block is copied, never paraphrased.
8. The camera is locked off. No ken burns.
9. Transitions are at least 0.8 s.
10. Kaggle measures and stitches; it never authors.
11. `frames.json` is the only source of truth for frame count.
12. Publish assets are written from measured output, never from predictions.

---

## DIVISION OF RESPONSIBILITY

**Assistant:** research, script, anchors, frame generation and visual QC, all code and
config, the Kaggle cells, verification of every gate.

**User:** run the Kaggle cells, review `timings.csv` when asked, review the render, ship.

---

## ACCEPTANCE SUMMARY

A finished episode satisfies all of these at once:

| check | expected |
| --- | --- |
| frames rendered | equals frame count in `frames.json` |
| merged or warned frames | zero |
| holds | 3–12 s, no outliers |
| anchor precision | `exact`, or `in-sentence` by informed choice |
| selftest | passing, including static-frame and blend assertions |
| runtime | measured, and quoted in the description |
| thumbnail | text legible at 336 px |
