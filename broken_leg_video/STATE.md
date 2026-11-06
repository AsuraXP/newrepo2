# STATE — broken_leg

State-machine ledger. One line per transition, append-only. Owned by the master
chat; workers read it and never edit it (except the `DECLARED EXCEPTION` lines
they are instructed to append).

| # | State | Status | Date | Notes |
|---|---|---|---|---|
| 0 | Repo discovery + init | DONE | 2026-11-06 | Layout inspected; folder scaffolded on `arena/c25b4281-newrepo2`. |
| 1 | Brief | DONE | 2026-11-06 | Ship premise retired. Topic A chosen; voice/pace/POV/no-captions/16:9 locked; no hard rules. Art style still open (State 4). |
| 2 | Scripting | DONE | 2026-11-06 | Approved by user. 1,478 words, ~7:57 estimated (uncalibrated). |
| 3 | Spine (`visuals.csv`) | DONE | 2026-11-06 | 200 rows, 32 slides, 7.4 words/beat. `python tools/spine.py check` passes: every beat verbatim, unique, in order, non-overlapping. |
| 4 | Anchor lock + worker packets | ROUND 2 TESTING | 2026-11-06 | Round 1 test refs rejected by user (sepia, over-textured). Style block rewritten: sage/mustard/terracotta/navy, thin confident line, halftone accents only. 3 round-2 proofs (day / firelit / diagram) awaiting approval. Split revised to 4 workers x 50 rows; master chat is Worker 1. |
| 5 | Swarm frame generation | IN PROGRESS | 2026-11-06 | Anchor locked (proof1, full backgrounds). Worker 1 (master): 5/50 frames accepted. Batch 1 QC: 3 defects found, 2 repaired in-budget, `01m03` held for next turn's repair budget. |
| 5.5 | Thumbnail | BLOCKED | - | Needs merged frames. |
| 6 | Kaggle runner | BLOCKED | - | Script exists in repo root only after State 5.5. |
| 7 | Handoff | BLOCKED | - | - |

## Deviations from the swarm spec (deliberate, recorded)

1. **Worker branches target the session branch, not `main`.** `main` does not
   contain this episode; workers branch from `arena/c25b4281-newrepo2` and PR
   back into it.
2. **Frames are `.jpg` at quality 90, not `.png`.** The repository hard-rules
   GitHub to "no large binaries"; 200 lossless PNGs would be 200-400 MB. The
   naming pattern (`beat{slide:02d}m{moment:02d}`) is unchanged; the Kaggle
   runner must accept `.jpg` and `.png`.
3. **No `location_ref` exists yet.** Workers attach the winning style test ref
   only, and build fresh backgrounds per beat until per-location refs are cut
   from the first approved frames.
4. **The Kaggle runner takes `.jpg` frames** for the canvas pad step; the pad is
   still done in PIL before concat, never with `-vf pad=`/`-vf scale=`.

## Spine QC

```
python tools/spine.py check --repo .     # -> PASS, 200 rows, 32 slides
```

Validator enforces: verbatim substring of the narration, unique occurrence,
correct order, no overlap, non-empty prompt, and reports punctuation-only gaps.

## Worker split (4-way, 2026-11-06)

| Worker | Rows | Frames | Range |
|---|---|---|---|
| 1 (master chat) | 1-50 | 50 | 01m01 .. 09m02 |
| 2 | 51-100 | 50 | 09m03 .. 16m02 |
| 3 | 101-150 | 50 | 16m03 .. 24m05 |
| 4 | 151-200 | 50 | 24m06 .. 32m09 |

## Style rejection record (round 1 -> round 2)

Round 1 was rejected: "no images you showed matched my style at all". The
round-1 block produced sepia-monochrome paper with a dot grid over every
surface. Round 2 fix: removed the brown wash, restored sage green-blue / mustard
/ terracotta / deep navy, thinned the ink line to a confident marker weight,
restricted halftone to small accent shadows, and kept backgrounds flat and
uncluttered. The rejected files stay in refs/ for the record but are never used
as references.

## Frame QC log — Worker 1

| Batch | Frames | Accepted | Repaired | Held / notes |
|---|---|---|---|---|
| 1 | 01m01-01m06 | 01m01, 01m02, 01m04, 01m05, 01m06 | 01m01 (featureless figures + built stone wall), 01m02 (rubber-tread boot, laces) | 01m03 rejected: black silhouettes with a modern backpack and a hat, off-model identity |

Drift patterns to watch in every batch: modern footwear, backpacks and hats;
masonry walls; figures losing their dot eyes and hide tunics at distance. The
locked negative block now carries all four. Model still gives the close-up eyes
white sclera with black pupils instead of bare dots - accepted as an expressive
variant, logged rather than fought.

## Declared exceptions

None yet. Format: `beat{slide}m{moment} — fault — 3 re-rolls failed — shipping closest`.

## Audio boundary

No TTS, no voice auditioning, no FFmpeg preview, no audio mix in this
workspace. Those happen only on Kaggle (see `run_broken_leg_kaggle.sh`,
written in State 6).
