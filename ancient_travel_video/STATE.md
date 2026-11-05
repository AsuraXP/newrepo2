# STATE — ancient_travel_video

Machine: STATE 0 → 7 (single-agent producer spec).
**Current: STATE 5 — FRAME GENERATION (batch 1 in progress).**

| State | Status |
|---|---|
| 0 — Repo discovery & init | DONE 2026-11-05 (folder renamed ship_outbreak_video → ancient_travel_video on topic pivot) |
| 1 — Brief | DONE 2026-11-05 — user confirmed: 6 min (can be longer), default voice, 2nd person, style-only refs, no hard rules, no captions, 16:9, YouTube |
| 2 — Script | DONE 2026-11-05 — user approved ("apprive"). 1,210 words ≈ 6.5 min (estimate). |
| 3 — visuals.csv spine | DONE 2026-11-05 — N=182 rows, 42 slides, 23 batches; moment_text concatenation verified == narration word-for-word (build_visuals.py). |
| 4 — Master anchor lock | DONE 2026-11-05 — user picked **B (cinematic)**. Verbatim style/character/negative blocks frozen in continuity.md + build_visuals.py, injected into all 182 prompts. anchor_B reused as beat01m01. |
| 5 — Frame batches | IN PROGRESS — batch 1 (beat01m01–beat02m04, 8 frames). 8/turn + 2 repairs; QC + contact sheet each batch. |
| 5.5 — Thumbnail | pending |
| 6 — Kaggle runner | pending (`run_ancient_travel_kaggle.sh`) |
| 7 — Handoff cell | pending |

## Standing notes
- All git ops on `arena/1cbb32ec-newrepo2` (session-pinned; no other branch).
- NO AUDIO in this workspace. TTS / mix / FFmpeg / ZIP only on Kaggle.
- User refs are STYLE ONLY: reuse the style continuously, never the literal
  scenes/props (logged in continuity.md).
- Title hook: "It took them ___ days…" → 2,000 walking-days vs 50,000 years
  (42,000 km Out of Eden route ÷ ~20 km/day; sources in script.md).
- Repo Gate 0 calibration still PENDING (`sec_per_word: null`); Kaggle run
  measures word-level timing. Workspace numbers are labelled estimates.
- Reuse at STATE 6: `vidsync/` (tts, timing, stitch, media), `kaggle/run.py`,
  `tools/prep_frames.py` where compatible with the CSV spine.

## Declared exceptions / reject log
(empty)
