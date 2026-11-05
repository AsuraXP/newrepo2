# STATE — ancient_travel_video

Machine: STATE 0 → 7 (single-agent producer spec).
**Current: STATE 4 — ANCHOR LOCK (STOPPED, awaiting user's winning-style pick).**

| State | Status |
|---|---|
| 0 — Repo discovery & init | DONE 2026-11-05 (folder renamed ship_outbreak_video → ancient_travel_video on topic pivot) |
| 1 — Brief | DONE 2026-11-05 — user confirmed: 6 min (can be longer), default voice, 2nd person, style-only refs, no hard rules, no captions, 16:9, YouTube |
| 2 — Script | DONE 2026-11-05 — user approved ("apprive"). 1,210 words ≈ 6.5 min (estimate). |
| 3 — visuals.csv spine | DONE 2026-11-05 — N=182 rows, 42 slides, 23 batches; moment_text concatenation verified == narration word-for-word (build_visuals.py). |
| 4 — Master anchor lock | IN PROGRESS — 3 style test refs generated (A cozy / B cinematic / C comic), exact prompts + QC logged in continuity.md, comparison sheet built. **Awaiting user's winning pick.** |
| 5 — Frame batches | pending (8 frames + 2 repairs per turn; QC + contact sheet) |
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
