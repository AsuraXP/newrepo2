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
| 4 | Anchor lock + worker packets | AWAITING PICK | 2026-11-06 | Locked style blocks written. 3 test refs generated from the user's 3 style refs; 3 worker packets published in `worker_packets.md`. STOPPED for winning anchor + deployment approval. |
| 5 | Swarm frame generation | BLOCKED | - | Needs anchor pick + deployment approval. Budget: 6 frames/turn, 2 repairs/turn. |
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

## Declared exceptions

None yet. Format: `beat{slide}m{moment} — fault — 3 re-rolls failed — shipping closest`.

## Audio boundary

No TTS, no voice auditioning, no FFmpeg preview, no audio mix in this
workspace. Those happen only on Kaggle (see `run_broken_leg_kaggle.sh`,
written in State 6).
