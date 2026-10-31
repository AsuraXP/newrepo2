# STATE — zombie_72h

Current state: **STATE 2 COMPLETE — WAITING FOR SCRIPT APPROVAL**

| State | Status |
|---|---|
| 0 Repo discovery + folder | done 2026-10-31 |
| 1 Brief | done — see `brief.md` |
| 2 Scripting | written, 1,513 words, awaiting explicit approval |
| 3 Spine (`visuals.csv`) | not started — blocked on script approval |
| 4 Consistency setup | refs pending — anchors must be approved before any frame |
| 5 Frame generation | not started |
| 6 Kaggle runner | not started (planned: `run_zombie_72h_kaggle.sh`) |
| 7 Handoff | not started |

## Numbers

- Narration words: 1,513 (speakable passage only, markers excluded)
- Projected runtime: 8.13 min = 488 s, from 3.1 words per second. Projection,
  not a measurement. Real runtime comes from the Kaggle TTS pass.
- Frame count: unknown by design. It is an output of STATE 3.
- Frames accepted: 0
- Batches run: 0

## Frame batch log

| Batch | Rows | Accepted | Rejected | Notes |
|---|---|---|---|---|
| — | — | — | — | not started |

## Declared exceptions

None yet. A frame is only listed here after three failed re-rolls, with the
exact clause that was changed and the reason the closest version shipped.

## Blockers

1. Script approval.
2. Style anchors: 2 to 3 test refs must be generated and one approved before
   the first episode frame. The user's reference images define the look but do
   not count as an approved episode anchor.
