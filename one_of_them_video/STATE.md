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

## Next at anchor lock (historical)
- AWAITING USER: approval of winning style anchor + DEPLOY of 4 worker chats.
- Then workers run STATE 5 on their branches; STATE 5.5 thumbnail after merge;
  STATE 6 Kaggle runner; STATE 7 handoff cell.
- Exceptions: none yet.

## 2026-11-01 — WORKER 1 / STATE 5 / BATCH 001

- Deployment received: Worker 1 is assigned CSV rows 1–92 (slides 01–03).
  The briefing confirms the user-selected master anchor; no new style vote,
  script approval gate, anchor generation or other-worker work was repeated.
- Source project imported unchanged from `arena/65278339-newrepo2` at
  `b05fb9530ccc0d27e660ce6a7a4281a370da4c18`. Protected source SHA-256:
  - script.md: `943d572bf000446fb187fb42a6be95c99faed874c94f751f30d67cb2f8fa2eea`
  - visuals.csv: `8f8f4b69f2385e7f23f0ee57bae0344a7d0640bc8e078edc34a3231b0c12d8d5`
- Branch override: Arena requires all work and pushes on the session-fixed
  `arena/62425825-newrepo2`. The requested `one_of_them-worker-1` branch was
  not created or checked out. Scope remains Worker 1 paths only.
- Batch coverage: rows 1–8. Generated 8 candidates + 2 repairs = 10/10 images.
- ACCEPTED (6): beat01m01, beat01m02, beat01m03, beat01m04, beat01m06,
  beat01m07 (attempt 2). Every accepted image was opened and checked against
  its moment_text, the locked anchor and present-day sleeve rules.
- PENDING (2): beat01m05 and beat01m08. Row 5 attempt 1 exposed forearms and
  missed the bump; repair 1 fixed the sleeves but still missed shoulder-to-arm
  contact. Row 8 passed the facial-beat check initially, but a subsequent edge
  close-up found a gray-green limb emerging from the protagonist's brown
  sleeve; it was rejected before commit. All rejected candidates are preserved
  locally and included in the QC sheet. No declared exceptions; do not ship
  either pending frame yet.
- beat01m07 attempt 1 duplicated the protagonist; its single-sentence repair
  produced exactly one living protagonist and passed QC.
- Progress: 6/92 accepted; 86 remaining to accept (rows 5 and 8 pending +
  rows 9–92 not started).
- New master anchors: none. The locked winner is unchanged. The accepted
  beat01m01 is only an optional local sleeve-continuity reference.
- Contact sheet includes all 10 candidates, including rejects, at ~380 px:
  `qc/worker_1/batch_001/contact_sheet.jpg`. Exact prompts and hashes are in
  `qc/worker_1/batch_001/prompts.json`; diagnoses are in `QC.md` beside them.
- No TTS, voice audition, audio mix, FFmpeg, thumbnail or Kaggle-stage work.
  No manual frame durations. script.md and visuals.csv remain byte-identical
  to the supplied source branch.

### Worker 1 next action after batch 001 (completed in batch 002)
- Repair row 5 first (attempt 3 / repair 2), changing only its opening scene
  sentence to require a tight crop with actual shoulder-to-sleeved-arm contact.
- Repair row 8 next (attempt 2 / repair 1), changing only its opening scene
  sentence to keep the brown-sleeved figure entirely outside the face crop.
- Then continue rows 9–16 in order. These ten planned generations reach the
  next turn's image cap; if another repair is needed, defer the last new row
  rather than exceed the cap. Stay inside rows 1–92.

## 2026-11-01 — WORKER 1 / STATE 5 / BATCH 002

- Coverage: carry-over rows 5 and 8, then new rows 9–16 in narration order.
  Ten image-tool calls: nine saved candidates and one moderation block.
  Both repair slots were consumed by the carry-over rows.
- ACCEPTED THIS BATCH (8): beat01m08 (attempt 2), beat01m09, beat01m10,
  beat01m11, beat01m12, beat01m13, beat01m15, beat01m16. Every saved candidate
  was opened individually and the contact sheet reviewed end to end.
- Row 8's face-only repair removes the brown-sleeve/gray-green-limb defect;
  the neutral half-lidded face now passes without character contamination.
- Row 5 attempt 3 / failed reroll 2: the foreground zombie inherits a brown
  protagonist sleeve and cuff, merging character designs instead of showing
  a clean shoulder-to-arm bump. REJECTED; no declared exception yet because
  the threshold is three failed rerolls, not two.
- Row 14 attempt 1: MODERATION BLOCKED, no image saved. The tool did not
  disclose a trigger token. Attempted wording and a safer replacement are
  logged in continuity.md and batch_002/prompts.json; replacement NOT_SENT.
  The CSV and script were not edited.
- Hypothetical memory frames use desaturated doodle bubbles and a generic
  pale-gray figure, not the actual protagonist. Row 15 passes with no contact;
  row 16 returns to the present-day palette and a still, calm protagonist.
- CUMULATIVE: 14/92 accepted; 78 remaining to accept (rows 5 and 14 pending,
  rows 17–92 not started). Accepted files now cover rows 1–4 and 6–13,
  15–16. No other worker's rows were generated.
- New master anchors: none. Locked winner unchanged. No TTS, voice audition,
  FFmpeg, audio mix, thumbnail, runtime measurement or Kaggle-stage work.
- Protected script.md and visuals.csv remain byte-identical to the source
  hashes recorded in batch 001. Native accepted PNGs are 1376 × 768; no
  manual durations, scaling or post-generation frame edits were applied.
- QC: `qc/worker_1/batch_002/contact_sheet.jpg` includes all nine saved
  candidates and a labelled blocked-attempt placeholder; `QC.md`,
  `prompts.json` and `validation.txt` record diagnoses and exact prompts.

### Current Worker 1 next action
- Row 5: attempt 4 / reroll 3, changing only the opening sentence again.
  If this third reroll fails, ship the closest existing candidate and log
  the precise DECLARED EXCEPTION here, then move on as the spec requires.
- Row 14: send the logged prompt-safe replacement, keeping the locked style
  and negative blocks verbatim and the generic memory figure distinct from
  the protagonist. Do not alter visuals.csv.
- Then rows 17–24 in order. Ten planned calls reach the cap; defer the last
  new row if another repair is needed. Stay inside assigned rows 1–92.
