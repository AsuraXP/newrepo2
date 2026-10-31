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
| beat04m01 | rounded filled torso ≠ line anatomy; only 6 X marks for "seven days" | line torso clause + "exactly seven boxes crossed off" | ✅ repaired (7 X's, line torso), PASS |
| beat04m02 | rounded filled torso ≠ line anatomy | line torso clause | queued |
| beat09m03 | tan skin-filled forearm vs line-limb invariant; red marks oversized scribbles | "arm is a single thin black line, no skin fill; marks small" | queued |
| beat09m02 | USER-FLAGGED: head detached — floating head behind mugs + headless body on stool (impossible anatomy; assistant QC missed it) | "EXACTLY ONE connected figure — head sitting directly on the spine, never detached" | ✅ repaired, PASS |

USER CORRECTION (batch 19): "latest generation zombies don't look like zombies,
frames don't match reference, some are using mobile phones". ROOT CAUSE: weak
block "pale grey stick figure, faint dot eyes" → grey people standing idly;
model adds phones to idle figures. FIX — ZOMBIE BLOCK MANDATORY in every frame
containing the undead, from batch 20 on:
"the SAME pale-grey stairwell zombie: sickly pale grey-green skin, HUNCHED
forward, head lolling to one side, slack jaw hanging open, big GLASSY
UNFOCUSED eyes with a wet white glint staring at nothing (ref beat77m02),
torn ragged shirt with jagged uneven hem (ref beat84m01), arms dangling loose
or swaying half-lifted, dragging its feet in an uneven stagger — clearly the
undead: never upright, never attentive, never holding any object, no phone,
no device, no bag, no weapon; non-graphic, no blood, no gore, no wounds".
Reference frames: beat77m02 (glassy eyes), beat84m01 (ragged clothing).
Re-roll list (un-accepted): 84m02, 86m01, 87m01, 87m02, 88m02, 89m01, 89m02,
92m01, 92m02, 92m03, 93m01, 93m02, 93m03, 94m01, 95m01 (never made).
ACCEPTED (168, QC'd by eye): rows slide_01..slide_84m01 + zombie-block re-rolls
84m02, 85m01, 86m01, 87m01, 87m02, 88m01, 88m02, 89m01, 89m02, 92m01, 92m02,
92m03, 93m01, 93m02, 93m03, 94m01, 94m02, 95m01 + no-zombie frames 85m02,
90m01, 90m02, 91m01, 96m01, 96m02, 97m01, 98m01, 98m02, 99m01, 99m02
(batch 23: 10/10 zero rejects, zero blocks).
QUEUE: none.
Next rows: slide_100+ (CSV read through slide_117; 100 couch/TV lab →
statue/cell → lock down → paperwork → freedom/life gone → sunrise bars →
sneaky cure thought → blood/drop → maybe cure → planet → nice/wrong →
everyone needs it → drawer → rules).
Tolerated (additions): 89m01 white-outlined legs read as light trousers
(zombie side + line torso now correct); 99m02 richer rendered still-life
(style exception for dark object frames); 97m01 silhouettes wear neckties
(corporate menace, reads fine); parallel read_file display can shuffle —
verify disk mapping with a sequential read when in doubt (97m01/98m01
confirmed correct this way).
MODERATION NOTE (batch 21): 7 blocks in 10 attempts on the standing zombie
block — flaky, same recipe passed 7/7 in batch 20. Recipe that re-passed
88m01 att: "harmless comedy scene" opener + "cartoon zombie figure" + "no
biting" in negatives + two separate figure descriptions without interaction
verbs between them.
Zombie tint drift tolerated: grey-green to greener across cuts — same type.
88m01 flash-panel border tolerated (established class, cf. 78m02).
OUTSTANDING repairs (R=4):
- beat87m02 attempt 3: now hollow outlined robe-torso → "torso is ONE single
  vertical black stick line like a classic stick-figure drawing, no outline,
  no robe/peanut enclosure, no fill"
- beat88m02 REJECT: duplicate white-headed stick man (two-shot shows 3 figures)
  → "exactly two figures in frame: him + the grey figure, nobody else"
- beat92m02 REJECT: readable SFX/speech text "Heh heh!"/"FLICK!" added
  (captions-none production) → same composition, "no words, no lettering,
  no speech bubbles, no sound-effect text anywhere"
- beat92m03 REJECT: same — "HURRAY!" text added → hero pose, "no words, no
  lettering, no speech bubbles, no sound-effect text anywhere"
QUEUE: those 4.
Next rows: slide_93+ (CSV unread) — likely tail of immune beat / Episode-2 hook.
Tolerated (additions): 84m02/86m01/87m01 landing zombie reads plain pale-grey
after ragged 84m01 (same figure, wardrobe under-specified in text);
87m01 paper-bag prop recurrence (established comic motif);
89m02 wave lands a step away from its head instead of inches (beat reads).
Tolerated notes: 05m02 dashed arm + mitten-index; 09m03/18m01/28m02 red marks
on both forearms (close-up class); 15m01 paper bag; 19m01/20m01/21m01/31m01
close-up face detail; 22m01 shadow shape; 26m01 darker pants under light;
27m02 stranger slumped against low sidewalk ledge (costume correct); 30m02
forearm warm-tinted by streetlight.
Tolerated notes: 05m02 dashed arm + mitten-index; 09m03 stray mark; 15m01
paper bag; 18m01 marks both forearms; 19m01/20m01/21m01 close-up face detail
register; 22m01 shadow shape; 26m01 stranger pants darker under night light.
