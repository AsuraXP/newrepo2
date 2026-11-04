# Production state

- State: 5 — frame generation in progress.
- Project slug: provisional (story).
- Topic: unfinished tasks as a metaphorical waiting room.
- Script: approved; second person; 942 words; projected runtime 5:04 at 3.1 words/second (estimate only).
- Visual spine: 159 rows in `visuals.csv`, covering the complete narration in sequence. Earlier provisional count was 192; awkward phrase boundaries were merged before frame generation. This projects to 20 batches of up to 8 frames. Future prompts remain drafts and require anchor blocks and explicit story states before generation.
- Approved anchors: `refs/character_test.png`, `refs/location_test.png`. Exact reference prompts and invariants in `continuity.md`. Accepted `frames/beat03m01.png` is an additional task-visitor design reference.
- Accepted frames: 16/159, contiguous through `beat03m03`; remaining: 143.
- Batch contact sheets: `contact_sheets/batch01.png`, `contact_sheets/batch02.png`; rejected attempts are included and retained under `contact_sheets/rejects/`.
- Batch 1 QC correction: `beat02m01` attempt 2 was initially incorrectly rejected. On closer review it contains both the envelope thought bubble and the blank second speech bubble, and the protagonist is seated. Restored as accepted; contact sheet corrected. Original `beat01m07` and `beat02m01` attempts showed the protagonist sitting in midair; changed their seating clauses to require hips on the sofa cushion, and rerolls passed.
- Batch 2 rejects: `beat02m05` attempt 1 gave task visitors ghost tails instead of legs; changed only the visitor clause to specify two stick legs and feet, reroll accepted. `beat02m06` attempt 1 made visitors adult-sized versus the small visitors of `beat03m01`; changed only the crowd clause to specify tiny stick visitors, reroll accepted.
- Drift: `beat01m03` has two lamps vs one in `refs/location_test.png`; `beat01m07` and `beat02m06` show an extra cup versus the single held cup in `refs/character_test.png`. `beat02m05` has white tunic-like visitor torsos vs bare stick-line torso in `beat03m01`. Set dressing is low priority; future prompts should explicitly avoid duplication and favor visitor reference. No declared exceptions.
- Next batch: `beat03m04` through `beat05m03`, covering the visitors' eagerness, the waiting-room question, and the historical claim. Refine each prompt before generating.
- Thumbnail and Kaggle runner not started. No workspace audio or video rendering.
