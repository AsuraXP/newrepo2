# STATE MACHINE LOG — ONE OF THEM Ep.1 "The Bite"

Branch: arena/65278339-newrepo2

## 2026-11-01

- STATE 0 ✅ Repo discovered (existing vidsync/kaggle/tools pipeline noted;
  no prior *_video/ project). Scaffold created: one_of_them_video/.
- STATE 1 ✅ Brief locked from user response: series premise (bitten-but-
  survived, zombies see you as their own, hide from survivors; series of
  episodes), ~8–10 min per episode, en-US-AndrewNeural @ +10%, second-person,
  16:9 YouTube, no captions. Art style: PENDING — user pasting style image.
- STATE 2 ✅ script.md written: 1,667 words, POV second-person present,
  projected runtime 8:58 @ 3.1 wps (estimate). Full text shown to user in
  chat. AWAITING USER APPROVAL.
- Style refs received (3 user screenshots, stick-figure storytime look) and
  saved to refs/style_user_01..03.png. Style analysis logged in
  continuity.md. Satisfies the STATE 4 style input; anchor still locked only
  after test-ref approval.

## 2026-11-01 (STATE 3-4)

- STATE 3 ✅ visuals.csv built: 345 rows (12 slides), strict micro-beat split,
  validated: moment_text tiles script.md exactly (1,667/1,667 words). Frame
  naming beat{NN}m{NN}.png. Projected: 44 batches of 8 (repair budget 2/turn).
- STATE 4 ✅ Style test refs generated (2 candidates); user picked option 1 →
  refs/style_test_winner.png = MASTER ANCHOR (prompt logged VERBATIM in
  continuity.md). Moderation log + invariants + composition rule + anchor
  recipe + style/negative blocks recorded in continuity.md.
- Swarm math: N=345 → 4 worker chats (slide-aligned chunks):
  W1 rows 1-92 (slides 01-03, 92 frames) · W2 rows 93-190 (slides 04-06, 98)
  · W3 rows 191-262 (slides 07-09, 72) · W4 rows 263-345 (slides 10-12, 83).
- Briefing packets written: packets/worker_1..4.md (each self-contained:
  full master prompt + branch checkout + row range + script excerpt +
  continuity summary).
- Git: one_of_them_video/ committed + pushed to session branch
  arena/65278339-newrepo2 (spec says "main"; session rules require the
  session branch — flagged to user).

## 2026-11-01 (STATE 4 gate resolution)

- DEPLOY MODE: HYBRID (user choice). Producer chat = Worker 4: rows 263-345
  (slides 10-12, 83 frames), generated here via STATE 5 loop (B=8/turn,
  R=2, QC + contact sheet each turn). Workers 1-3 = external chats fed
  packets/worker_1..3.md by the user (rows 1-262).
- Branch note: producer frames commit to session branch
  arena/65278339-newrepo2 (session rules; worker-4 branch not used here).
- STATE 5 started: batch 1 = rows 263-270 (beat10m01-m08).
- Then workers run STATE 5 on their branches; STATE 5.5 thumbnail after merge;
  STATE 6 Kaggle runner; STATE 7 handoff cell.
- Exceptions: none yet.

## 2026-11-01 (Worker 4, batch 1 QC)

- Attempted rows 263-270 (beat10m01-08); accepted 10m01, 03, 04, 05,
  07, 08 (6/83 Worker 4 frames). Remaining 77, including 10m02 and 10m06.
- Rejected 10m02: survivors' gaze directions are scattered rather than
  clearly snapping toward the street. Reroll pending; the two-repair budget
  for this turn was exhausted by 10m06. Contact sheet includes the reject.
- 10m06: initial generation and two repair attempts were blocked by image
  moderation; no image was returned, so there is no closest version to ship.
  Scene clause softened from survivors fighting zombies with bats and boards
  to swinging boards as figures approach, then waving boards while figures
  gather. Not declared a completed frame; retry in a future batch. No rejected
  image exists for these blocked attempts.
- Continuity: 10m07 shows a gray-green, droopy-eyed woman in an olive coat
  with short dark hair; 10m08 maintains her coat, hair and complexion while
  grabbing Hector's charcoal jacket. Use 10m07 as the green-coat reference
  for subsequent appearances. Master style reference remains unchanged.
- Batch contact sheet saved outside the repository for QC at
  /home/user/one_of_them_qc/batch10_01_sheet.jpg.
- Next: retry pending 10m02 and 10m06 within the per-turn cap, then continue
  rows 271 onward (10m09 and later); never skip the missing frames silently.

## 2026-11-01 (Worker 4, batch 2 QC)

- Attempted the two pending frames 10m02 and 10m06 plus 10m09-14. Accepted
  10m02 and 10m09-14: 7 new frames, 13/83 Worker 4 frames total, 70 remaining.
- 10m02 repair: specified three survivors looking in the same direction
  toward the street corner, fixing the scattered gaze of the prior reject.
- 10m14 initial image rejected: protagonist's face appeared disconnected
  from the held arm, suggesting a third person. Changed the composition
  clause to show the head attached to the held-arm body; repaired version
  accepted. Rejected and accepted versions appear in the contact sheet.
- DECLARED EXCEPTION, 10m06: third reroll was also blocked by moderation
  (four blocked attempts total, across two turns). There is no image to ship
  as the closest version. Frame remains MISSING and must be resolved before
  the final video. Changed scene clause to survivors holding boards in
  defensive poses while distant figures approach; no image was returned.
- Recurring-character drift check: 10m09-14 green-coat woman's olive coat,
  short dark hair and gray-green skin match 10m07; Hector's charcoal jacket
  matches 10m08. No new anchor; use 10m07/08 as references.
- Contact sheet: /home/user/one_of_them_qc/batch10_02_sheet.jpg (includes
  the 10m14 reject and a placeholder for blocked 10m06; no blocked image exists).
- Next coverage: 10m15-22. 10m06 remains explicitly outstanding.

## 2026-11-01 (Worker 4, batch 3 QC)

- Rows 277-284, 10m15-22: all eight images accepted, no rejects or
  rerolls. Worker 4 total: 21/83 frames; 62 remain, including missing 10m06.
- Continuity check: 10m15-21 green-coat woman's olive coat, short dark hair,
  gray-green skin and droopy eyes match 10m07/08; 10m20-21 Hector's charcoal
  jacket matches 10m08. The protagonist's brown sleeves cover their forearms.
  The image in 10m22 uses a clock without lettering or numerals.
- No new anchor. Batch contact sheet:
  /home/user/one_of_them_qc/batch10_03_sheet.jpg.
- Next coverage: rows 285-292 (10m23-29 and 11m01). 10m06 remains an
  explicitly missing declared exception that must be resolved before delivery.

## 2026-11-01 (Worker 4, batch 4 QC)

- Rows 285-292 attempted (10m23-29, 11m01); accepted 10m24-28 and
  11m01, six new frames. Worker 4 total 27/83; 56 remain, including
  missing 10m06, 10m23 and 10m29.
- 10m23 initial and first reroll blocked by moderation; no image returned.
  Changed the scene clause from a stylized knife swing and impact to a raised
  knife with a motion line and abstract impact star. Still missing; no closest
  image exists, retry later within the cap.
- 10m29 first image rejected because sleeves stopped above the forearms;
  changed sleeve clause to say sleeves cover shoulders through wrists. Reroll
  covered sleeves but placed zombies inside the night shelter rather than
  showing the protagonist safely in camp. Rejected both, frame remains
  missing. Both attempts are in the contact sheet, saved outside the repo.
- 10m25 green-coat woman's short hair and olive coat match 10m08;
  10m26-27 Hector's charcoal jacket matches 10m08. No new anchor.
- Contact sheet: /home/user/one_of_them_qc/batch10_04_sheet.jpg (blocked
  placeholder and both 10m29 rejects included).
- Next coverage: 11m02 onward, with 10m06, 10m23, 10m29 explicitly pending
  and required before delivery.

## 2026-11-01 (Worker 4, batch 5 QC)

- Rows 293-300 attempted, 11m02-09. Accepted 11m03, 04, 06, 07, 08,
  09: six new frames, 33/83 Worker 4 frames total, 50 remain.
- 11m02 initial reject: protagonist was sitting on the bunk rather than lying
  awake. Changed the pose clause to specify lying flat, head on pillow. The
  reroll showed an uncovered forearm despite the sleeve rule; rejected it too.
  Both are in the contact sheet; 11m02 remains missing.
- 11m05 original and first reroll blocked by moderation. Changed the scene
  clause from silhouette survivors with boards and stick rifles to raised
  arms and wooden boards; no image returned. 11m05 remains missing.
- Drift: 11m03 and 11m06-07 protagonist's brown shirt matches 10m14; 11m04
  zombies' gray-green appearance matches the master anchor. No new anchor.
- Contact sheet: /home/user/one_of_them_qc/batch11_01_sheet.jpg (both 11m02
  rejects and the blocked 11m05 placeholder included).
- Next coverage: 11m10 onward; pending frames 10m06, 10m23, 10m29, 11m02,
  11m05 must be resolved before delivery.

## 2026-11-01 (Worker 4, batch 6 QC)

- Rows 301-308 attempted (11m10-17). Accepted 11m10-12 and 11m15:
  four new frames. Worker 4 total 37/83; 46 remain.
- 11m13 rejected: portrait shows short sleeves with uncovered forearms,
  inconsistent with the protagonist's covered-arm rule. Reroll pending.
- 11m14 rejected: a zombie reaches toward the protagonist instead of clearly
  drifting past without reacting. Reroll pending.
- 11m16 first image rejected for bare forearms; changed sleeve clause to
  insist on fabric from shoulder to wrist. Reroll rejected: three arms appear
  at the tap. Both versions remain out of frames/.
- 11m17 first image rejected: sleeve ends in an empty tube with no hand;
  changed composition clause to show a hand emerging from that sleeve.
  Reroll rejected: a third arm intrudes from the left. Both versions remain
  out of frames/. The text of this row refers to crescent marks; the current
  story-state rule requires the forearm to stay covered in this shot.
- No new anchor. 11m10-12 zombie figures match master gray-green palette;
  11m15 retains the wire gate established in 11m09. Contact sheet including
  all rejected candidates: /home/user/one_of_them_qc/batch11_02_sheet.jpg.
- Next coverage: 12m01 onward, with pending 10m06, 10m23, 10m29, 11m02,
  11m05, 11m13, 11m14, 11m16, 11m17 to resolve before delivery.

## 2026-11-01 (Worker 4, batch 7 QC)

- Rows 309-316, 12m01-08: eight frames accepted; Worker 4 total 45/83,
  38 remain. Both repair attempts succeeded.
- 12m07 first image rejected because Ollie put a hand on the protagonist's
  mouth instead of simply speaking softly; changed the pose clause to keep
  Ollie's hands in his lap. Accepted reroll shows him whispering beside them.
- 12m08 first image rejected because the protagonist was standing despite
  the ongoing shared breakfast; changed the pose clause to seat both on the
  bench. Accepted reroll preserves the shared breakfast and Ollie's gaze.
- Provisional Ollie reference: 12m02, small white-headed child with tiny dark
  hair tuft and muted blue-gray shirt; 12m03/06-08 follow this appearance.
  Reconcile this with Worker 3's earlier Ollie frames when they arrive; no
  final cross-worker character anchor has been established. Protagonist's
  brown long sleeves match 10m14. Master anchor remains unchanged.
- Batch contact sheet including both rejects and repairs:
  /home/user/one_of_them_qc/batch12_01_sheet.jpg.
- Next coverage: 12m09-16. Nine prior frames remain explicitly pending:
  10m06, 10m23, 10m29, 11m02, 11m05, 11m13, 11m14, 11m16, 11m17.

## 2026-11-01 (Worker 4, batch 8 QC)

- Rows 317-324 (12m09-16): eight images accepted, no rejects or rerolls.
  Worker 4 total 53/83, 30 remain, including the nine previously pending.
- Continuity: 12m10-11 and 12m13-14 green-coat woman retains the short dark
  hair, gray-green skin and olive coat of 10m07/08; 12m14 is desaturated as
  a flashback. 12m09/12/15 Ollie retains the small white head, hair tuft and
  blue-gray top from provisional reference 12m02. Protagonist's brown
  sleeves remain down. 12m15 uses one question-mark doodle as specified by
  the row; no words or captions. No new anchor.
- Batch contact sheet: /home/user/one_of_them_qc/batch12_02_sheet.jpg.
- Next coverage: 12m17-24. Prior pending 10m06, 10m23, 10m29, 11m02,
  11m05, 11m13, 11m14, 11m16, 11m17 must be resolved before delivery.
