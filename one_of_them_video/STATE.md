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

## Next
- AWAITING USER: approval of winning style anchor + DEPLOY of 4 worker chats.
- Then workers run STATE 5 on their branches; STATE 5.5 thumbnail after merge;
  STATE 6 Kaggle runner; STATE 7 handoff cell.
- Exceptions: none yet.

## Worker 2 frame exceptions
- DECLARED EXCEPTION — beat04m08: after three failed re-rolls, the closest
  candidate depicts eight gray-green zombies rather than the seven specified
  by the narration. Retained for continuity of production; replace if a
  correctly counted frame becomes available.
- DECLARED EXCEPTION — beat04m09: after three failed re-rolls, closest
  candidate shows twelve zombies rather than eleven, including one cropped
  at the edge. Replace with an accurately counted shot when possible.
- DECLARED EXCEPTION — beat04m10: after three failed re-rolls, closest
  candidate shows thirteen zombies rather than fifteen. Replace with an
  accurately counted shot when possible.
- DECLARED EXCEPTION — beat04m11: after three failed re-rolls, the best
  stopped-zombie shot has dot eyes rather than the anchor's droopy eyes.
  Replace with an anchor-consistent stopped zombie when possible.

## Worker 2 moderation notes
- beat05m03: original close-up prompt was blocked; retry with "two clean
  crescent marks" and "two faint pale curved lines" was accepted.
- beat05m02: private scar close-up retry was blocked; frame remains pending.
- DECLARED EXCEPTION — beat05m02: after three failed re-rolls (including
  one blocked attempt), the closest private over-shoulder image puts the
  crescent marks near the elbow rather than clearly on the forearm. Replace
  with an anatomically clear forearm view when possible.
- beat05m18: retry of the imagined weapon scene was blocked by content
  moderation; frame remains pending.
- beat05m18: a second reworded attempt was blocked; no replacement was
  produced, and the scene remains pending.
- beat05m18: a later symbolic thought-bubble prompt was accepted; the frame
  is no longer pending.
