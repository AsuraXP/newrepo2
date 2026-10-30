# STATE MACHINE — apocalypse_ship

Current state: **STATE 5 — batch 1 in progress (frames 1–8 of 346)**
Anchors FROZEN: B2 (character+palette) + C2 (interior/composition) ✅

| State | Status | Notes |
|---|---|---|
| 0 — Repo discovery & init | DONE (2026-10-30) | existing pipeline found: `vidsync/`, `kaggle/`, `tools/`; episode record in `PRODUCTION.md` |
| 1 — Concept brief & visual strategy | DONE | premise v2 amendments (knockout, secrecy, blood-cure fear, day-one series scope) |
| 2 — Scripting | DONE | Day One v4, 1,903 words ≈ 10:14, user approved |
| 3 — visuals.csv spine | DONE | N=346 rows, coverage exact vs script; B = floor(10×0.75) = 7 (batches of 8 at cap, R=2) |
| 4 — Consistency setup | DONE | round-1 rejected (fat limbs/grey head/cold palette); round-2: **B2 + C2 approved = anchors**, blocks frozen in continuity.md |
| 5 — Frame loop + thumbnail | IN PROGRESS | batch 1 = slide_01..slide_04; thumbnail state: not started (T1 concept locked) |
| 2 — Scripting | not started | stop for explicit approval (or AUTOPILOT) |
| 3 — visuals.csv spine | not started | |
| 4 — Consistency setup | not started | stop for anchor approval |
| 5 — Frame loop + thumbnail | not started | cap 10/turn: batch 8 + repair 2 |
| 6 — Kaggle runner | not started | `run_apocalypse_ship_kaggle.sh` |
| 7 — Handoff | not started | |

## Declared exceptions

(none)

## QC rejects — batch 1–2 (repair queue, R=2/turn)

| Frame | Fault (specific) | Clause to change on re-roll | Status |
|---|---|---|---|
| beat01m01 | tan filled torso vs anchor B2 pure-line torso | add: "torso is a single thin black line, no shirt, no body fill" | ✅ repaired, PASS |
| beat01m02 | moderation block ×2 (punch scene) | 3rd attempt: swing-only staging, no second figure | ✅ repaired attempt 3, PASS |
| beat04m01 | rounded filled torso ≠ line anatomy; only 6 X marks for "seven days" | line torso clause + "exactly seven boxes crossed off" | queued |
| beat04m02 | rounded filled torso ≠ line anatomy | line torso clause | queued |
| beat09m03 | tan skin-filled forearm vs line-limb invariant; red marks oversized scribbles | "arm is a single thin black line, no skin fill; marks small" | queued |

ACCEPTED (13, QC'd by eye): 01m01 01m02 01m03 01m04 02m01 03m01 05m01 05m02 06m01 07m01 08m01 09m01 09m02
Minor tolerated notes: 05m02 dashed upper-arm stroke + mitten-with-index (gesture legible), kept.
