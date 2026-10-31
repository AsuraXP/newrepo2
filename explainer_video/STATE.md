# Production state

- Current state: **5 — 61 frames accepted; batch 8 has a pending repair**.
- AUTOPILOT: off.
- Branch: `arena/9714bb12-newrepo2`.
- Discovery: completed; existing `vidsync/`, `kaggle/`, and `tools/` inventoried for reuse.
- Project initialization: completed under provisional slug `explainer`.
- Confirmed: explainer, YouTube, five-minute target, second-person narration.
- Planning target: approximately 930 spoken words; approved script is 971 words, with runtime not measured.
- Topic selected: how standardized screw threads helped build the Crystal Palace. Preliminary channel and competitor checks are recorded in brief.md; completeness is limited.
- Visual style selected: user-supplied hand-drawn 2D stick-figure references, copied into `refs/`. Generated character and location anchors are approved.
- Visual hook: 1, The wrong bolt (stylized metaphor).
- Thumbnail direction: 1 / A, TINY SCREW, HUGE PALACE.
- Defaults: confirmed (16:9, no captions, en-US-AndrewNeural +10%, Kaggle-only audio).
- Narration: drafted in `script.md`; second-person POV; 971 words; projected runtime 313.2 seconds at 3.1 words/second, not measured. Explicitly approved by the user.
- The old ship-survival premise is not selected.
- `visuals.csv`: 177 provisional word-reactive rows, covering the approved script in order. Frame 01 shows the selected mismatched-bolt hook. Prompts require refinement and the approved anchor blocks before frame generation.
- Reference tests: `refs/character_test.png` and `refs/location_test.png` generated successfully after the earlier HTTP 403 errors. Both explicitly approved as anchors. Original user-provided style inputs are intact.
- Sequence frames: 61 accepted of 177; 116 remain. `beat10m04` shipped as a declared exception after three failed repairs; `beat10m05` is pending after one failed repair. Review sheets: `refs/reviews/batch01_contact.png` through `batch08_contact.png`.
- Thumbnail and Kaggle runner: not started.
- Audio: none generated; all synthesis/mixing/encoding is reserved for Kaggle.

## Gate ledger

| Gate | Status | Required next decision |
|---|---|---|
| 1A — core concept | COMPLETE | Topic, runtime, POV and style selected |
| 1B — hooks/thumbnails | COMPLETE | Hook 1, thumbnail A, and defaults confirmed |
| 2 — script | COMPLETE | Explicitly approved by user |
| 3 — word-reactive spine | DRAFTED | 177 rows; refine prompts against approved anchor before generation |
| 4 — references | COMPLETE | Character and location tests explicitly approved |
| 5 — frames/thumbnail | IN PROGRESS | 61 accepted; repair `beat10m05` and generate the next 7; thumbnail pending |
| 6 — Kaggle runner | NOT STARTED | Reuse existing code where compatible; validate offline |
| 7 — handoff | NOT STARTED | Provide ready-to-run Kaggle cell |

## Next action

The user chose the recommended history topic and supplied style images. Commit and push batches 7 and 8. On continuation, repair `beat10m05` for the second time, then generate seven new frames beginning with `slide_12m01`. No thumbnail yet.
