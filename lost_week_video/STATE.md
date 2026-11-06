# STATE — lost_week_video

Project slug: `lost_week_video`
Working title: "The Week You Lost"
Branch: `arena/1200f0d8-newrepo2`

## State machine

| State | Name | Status | Entry |
|---|---|---|---|
| 0 | Repo discovery | DONE | Repo is the narration-first pipeline (`vidsync/`, `kaggle/`, `tools/`, `docs/`). No project folders existed. |
| 0.5 | Resume check | DONE | No prior `<slug>_video/` folder found; user chose start-fresh with a new story beat. |
| 1 | Brief | DONE | `brief.md` written from the user's supplied opening + rules; style ref deferred by user. |
| 2 | Script | **STOPPED — awaiting approval** | `script.md`, 1,917 narration words ≈ 10:18 projected. |
| 3 | Spine (`visuals.csv`) | NOT STARTED | Micro-beat split after script approval. |
| 4 | Anchors + worker packets | BLOCKED | Waiting on the user's art-style reference image. |
| 5 | Swarm frames | NOT STARTED | — |
| 5.1 | Swarm merge | NOT STARTED | — |
| 5.5 | Thumbnail | NOT STARTED | — |
| 6 | Kaggle runner | NOT STARTED | — |
| 7 | Handoff cell | NOT STARTED | — |

## Story decisions locked

- 2026-11-06: Opening kept in the user's order (hunger → food → phone → seven days gone → bite).
- 2026-11-06: The shove is treated as ordinary self-defence so the audience files it away; it pays
  off in Act IV.
- 2026-11-06: Twist locked — the protagonist is a *carrier*: no fever, no turn, memory gaps,
  self-repairing body. He walked the missing week.
- 2026-11-06: Ending locked — padlock on the *inside* of the door, sister on the other side. No
  rescue, no cure, no chase.

## Declared exceptions

None yet.

## Audio

No TTS, no auditioning, no preview renders in this workspace. Kaggle only.
