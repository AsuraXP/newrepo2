# STATE — ship_survival

State-machine ledger. One line per transition, append-only. Owned by the master
chat; workers read it and never edit it (except the `DECLARED EXCEPTION` lines
they are instructed to append).

| # | State | Status | Date | Notes |
|---|---|---|---|---|
| 0 | Repo discovery + init | DONE | 2026-11-06 | Layout inspected; folder scaffolded on `arena/c25b4281-newrepo2`. |
| 1 | Brief | PARTIAL | 2026-11-06 | Ship premise retired. Voice/pace/POV/captions/format locked. Channel researched; 3 topics issued; awaiting pick (also awaiting style choice at State 4). |
| 2 | Scripting | BLOCKED | - | Needs topic pick. |
| 3 | Spine (`visuals.csv`) | BLOCKED | - | Row count is an output, never an input. |
| 4 | Anchor lock + worker packets | BLOCKED | - | Needs a written script. |
| 5 | Swarm frame generation | BLOCKED | - | Needs worker deployment approval. |
| 5.5 | Thumbnail | BLOCKED | - | Needs merged frames. |
| 6 | Kaggle runner | BLOCKED | - | Script exists in repo root only after State 5.5. |
| 7 | Handoff | BLOCKED | - | - |

## Declared exceptions

None yet. Format: `beat{slide}m{moment} — fault — 3 re-rolls failed — shipping closest`.

## Audio boundary

No TTS, no voice auditioning, no FFmpeg preview, no audio mix in this
workspace. Those happen only on Kaggle (see `run_ship_survival_kaggle.sh`,
written in State 6).
