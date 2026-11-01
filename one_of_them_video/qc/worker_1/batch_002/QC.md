# Worker 1 — Batch 002 visual QC

Date: 2026-11-01
Branch: `arena/62425825-newrepo2`
Coverage: carry-over repairs for rows 5 and 8, then new rows 9–16 in narration order.
Assignment remains CSV rows 1–92 only.

## Result

- Accepted this batch: 8 frames — rows 8, 9, 10, 11, 12, 13, 15, 16.
- Cumulative accepted: 14/92.
- Remaining to accept: 78 — rows 5 and 14 pending, rows 17–92 not started.
- Image-tool calls: 10/10. Nine calls saved images; one was moderation-blocked without a file.
- Repair slots: 2/2, used by the two carry-over repairs.
- New master anchors: none. The locked winner remains unchanged.
- Declared exceptions: none. Row 5 has had two failed rerolls, not three; do not invoke the closest-version exception yet.
- No TTS, voice audition, audio mixing, FFmpeg, thumbnail or Kaggle-stage work.

## Frame review

| Row / frame | moment_text | Specific QC diagnosis | Decision |
|---|---|---|---|
| 005 / beat01m05, attempt 3 | One of them bumps your arm | The foreground zombie inherits a brown protagonist-style sleeve and cuff, with a gray-green hand emerging. The protagonist's torso is partly occluded. This merges character designs rather than depicting a clean zombie-shoulder bump against a brown-covered arm. | REJECTED; second failed reroll |
| 008 / beat01m08, attempt 2 | It does not snarl. | The face-only crop now excludes all brown clothing, other people and stray arms. Gray-green skin, heavy half-lids and a slack mouth match the anchor; no teeth or aggressive brow. The prior sleeve/limb defect is gone. | ACCEPTED |
| 009 / beat01m09 | It does not even look. | The zombie stays behind the walking protagonist, with a vacant half-lidded expression and no eye contact or acknowledgment. Both figures remain distinct; brown sleeves cover the forearms. The intended indifference reads clearly. | ACCEPTED |
| 010 / beat01m10 | You keep walking. | One calm white-headed walker maintains an even stride among gray-green pedestrians. Long brown sleeves, blue trousers and the established sidewalk match the approved present-day frames. No zombie reaches or reacts. | ACCEPTED |
| 011 / beat01m11 | Your heart is hammering, | A small flat red heart on the brown shirt has an offset echo and vibration ticks. It reads as a non-anatomical heartbeat doodle. Sleeves and black hands remain on-model; no wound or gray-green limb contamination. | ACCEPTED |
| 012 / beat01m12 | but your face is calm. | One white round head, two dot eyes, relaxed brows and a flat mouth. The face-only composition deliberately contrasts with the preceding racing-heart shot. No extra figure, sleeve defect or lettering. | ACCEPTED |
| 013 / beat01m13 | Three weeks ago, | The same doorway, blank shopfront, planters and sidewalk are empty, desaturated and enclosed by a wobbly memory border. The location remains recognizable while the time-state changes. | ACCEPTED |
| 014 / beat01m14 | this street would have killed you | Image moderation blocked the generated result and saved no file. There is no image to QC or accept. The tool did not identify a specific trigger token. A safer prompt is logged but NOT SENT this turn. | PENDING SAFE RETRY |
| 015 / beat01m15 | in ten seconds. | A desaturated thought bubble contains a generic pale-gray figure, not the brown-shirted/blue-trousered protagonist. Gray-green silhouettes converge with speed ticks but make no contact. This communicates hypothetical danger without showing the actual protagonist being chased or attacked. | ACCEPTED |
| 016 / beat01m16 | Right now, | The normal cream/dusty-pink palette returns and the memory bubble disappears. One long-sleeved protagonist stands still while the gray-green crowd walks past. The present-state contrast is clear. | ACCEPTED |

Every saved candidate was opened individually. The final contact sheet was then reviewed as a whole. Accepted frames preserve the anchor's “white-headed stick figure with simple dot eyes,” “gray-green zombie stick figures with droopy half-lidded eyes,” and “Bold wobbly black outlines, flat muted colors, warm cream background.” The explicit long-sleeve override remains in force where the protagonist's arms appear. No accepted frame exposes a bite, wrap or scar in slide 01.

## Repair ledger

### Row 5 — attempt 3 / reroll 2

Only the opening scene sentence changed from attempt 2:

- Before: “In a medium two-shot, the zombie's gray-green shoulder visibly presses against the protagonist's brown long-sleeved upper arm mid-stride, their bodies adjacent at the point of contact.”
- After: “Tight upper-body side view with no gap at the contact point: a gray-green zombie shoulder physically touches the outside of the protagonist's brown long-sleeved upper arm as both pass mid-stride.”

All subsequent prompt text and reference paths remained unchanged. The result still fails the character-separation and contact checks. Preserve it as a reject. The next turn may use attempt 4 / reroll 3, changing only the opening sentence again. If that third reroll also fails, select the closest existing candidate and record the specific DECLARED EXCEPTION in STATE.md as the spec requires.

### Row 8 — attempt 2 / reroll 1

Only the opening scene sentence changed from attempt 1:

- Before: “Close on a zombie face: droopy half-lidded eyes, slack mouth, no snarl.”
- After: “Close on a zombie face alone, with no other person, arm, hand, or brown clothing anywhere in the frame: droopy half-lidded eyes, slack mouth, no snarl.”

All subsequent prompt text and reference paths remained unchanged. The brown-sleeve/gray-green-limb defect is removed. Accepted.

## Moderation event — row 14

Exact tool result: “Failed to generate image: The generated image was blocked by content moderation and was not saved.”

The tool did not disclose which words triggered the block. Do not label guesses as confirmed blocked words. The attempted prompt included “cornered by lunging zombies,” “backed against a wall,” and repeated attack/chase prohibitions. The next retry replaces the scene with a quiet hypothetical diagram: a pale doodle figure inside a ring of separated gray-green silhouettes, all stationary and making no contact. The actual protagonist is absent. The locked style and negative blocks stay unchanged; `visuals.csv` is not edited.

The complete attempted prompt and complete planned replacement are recorded in `prompts.json`. The replacement is marked NOT_SENT. The blocked attempt is represented by a labelled placeholder on the contact sheet, not by a fabricated image.

## Artifacts and next action

- `contact_sheet.jpg`: all nine saved candidates plus the blocked-attempt placeholder, approximately 380 pixels wide per thumbnail.
- `prompts.json`: exact prompts, references, attempts, decisions, file hashes and native dimensions; planned row 14 safe retry.
- `rejects/`: row 5 attempt 3, kept out of Git; its thumbnail is retained on the sheet.
- `staging/` and `scratch/`: local-only work areas, ignored by Git.
- `validation.txt`: offline integrity and scope checks.

Next turn: attempt row 5's third reroll first, send row 14's logged safe retry second, then generate rows 17–24. This uses ten calls if all save. If an additional repair becomes necessary, defer the last new row rather than exceed the cap. Remain within rows 1–92.
