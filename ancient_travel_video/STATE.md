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
| 5 — Frame batches | IN PROGRESS — batches 1–6 DONE. 48/182 frames done, 134 remain. |
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

## Frame storage pipeline (decided batch 1)
Native generated PNGs (~2.3 MB each) would exceed the ~128 MB patchset cap at 182
frames (~387 MB). Pipeline: resize to 1280×720 (render target) + quantize to
256-color PNG (optimize=True) → ~550 KB/frame, ~98 MB projected total. Keeps the
spec's `.png` naming and stays under cap. QC confirmed grain/gradients/character
survive quantization (contact_batch01.jpg). Contact sheets in sheets/ (~380px
thumbs) are QC-only; the STATE 6 runner globs frames/beat*.png only.

## Batch log
- Batch 1 (2026-11-05): beat01m01–beat02m04. 8/8 accepted, 0 rejects, 0 repairs.
  beat01m01 = reused approved anchor B. Location shifts (beach → S. headland →
  map) generated fresh in locked style. Contact sheet: sheets/contact_batch01.jpg.
  Next: batch 2 = beat03m01–beat05m02.
- Batch 2 (2026-11-05): beat03m01–beat05m02. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch02.jpg (incl. rejects). Rejects:
  beat03m01_r0 (paved cobblestone path + forest → changed path clause to dirt
  footpath on open grassland); beat05m02_r0 (Stonehenge-like megalith → changed
  environment clause to natural rocky ledge, no standing stones). Both repairs
  passed first re-roll. Next: batch 3 = beat05m03–beat07m05.
- Batch 3 (2026-11-05): beat05m03–beat07m05. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch03.jpg (incl. rejects). Rejects:
  beat06m02_r0 (tan boot-like feet → bare black stick feet, no shoes);
  beat07m01_r0 (extra corner limb-lines → exactly two legs, nothing else).
  Both repairs passed first re-roll. New location: savanna (acacia). Kudu
  design established (spiral horns, white-striped tan coat) for slide 9.
  Next: batch 4 = beat07m06–beat08m04.
- Batch 4 (2026-11-05): beat07m06–beat08m04. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch04.jpg (incl. rejects). Rejects:
  beat08m01_r0 (baked-in letterbox bars → full-bleed 16:9); beat08m02_r0
  (gibberish pseudo-text annotations → wordless coil, no labels/arrows).
  Both repairs passed first re-roll. Anatomy-diagram beats use amber glow
  highlights, no text. Next: batch 5 = beat08m05–beat09m07.
- Batch 5 (2026-11-05): beat08m05–beat09m07. 8/8 accepted, 0 QC rejects.
  Contact sheet: sheets/contact_batch05.jpg. 2 moderation blocks re-worded
  (not QC rejects): beat09m02 "hunters jogging after"→"figures jogging behind
  a running kudu"; beat09m07 "hunter toward exhausted kudu, relentless"→
  "figure toward a kudu lying down resting". Both accepted first try. New
  location locked: Kalahari (red sand, dry scrub, blazing white sun, mesas).
  Kudu design consistent across all hunt beats. Next: batch 6 =
  beat09m08–beat12m02.
- Batch 6 (2026-11-05): beat09m08–beat12m02. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks (neutral hunt phrasing per continuity.md
  worked). Contact sheet: sheets/contact_batch06.jpg. Hunt resolved respectfully
  (lying kudu, calm approach, no gore). New location locked: camp (A-frame hide
  lean-tos with crossed poles, central fire, savanna edge, acacia silhouettes).
  Next: batch 7 = beat12m03–beat13m06.

## Declared exceptions / reject log
- beat03m01_r0: REJECTED (anachronistic paving + forest drift). Fixed r1, accepted.
- beat05m02_r0: REJECTED (anachronistic megalith monument). Fixed r1, accepted.
- beat06m02_r0: REJECTED (feet drifted to tan boot-like shapes). Fixed r1, accepted.
- beat07m01_r0: REJECTED (extra limb-like lines in frame corners). Fixed r1, accepted.
- beat08m01_r0: REJECTED (baked-in black letterbox bars). Fixed r1, accepted.
- beat08m02_r0: REJECTED (gibberish pseudo-text annotations/arrows). Fixed r1, accepted.
- Reject sources kept locally in frames/rejects/ (gitignored); audit trail in
  contact sheets. No DECLARED EXCEPTIONS (all frames eventually passed).
