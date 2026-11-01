# Worker 1 — Batch 003 visual QC

Date: 2026-11-01
Branch: `arena/62425825-newrepo2`
Coverage: pending rows 5 and 14, then rows 17–24.

## Result

- 10 image calls, 10 saved candidates, 9 accepted.
- Accepted rows: 5, 14, 17, 18, 19, 21, 22, 23, 24.
- Pending: row 20, storefront continuity repair.
- Cumulative: 23/92 accepted; 69 remaining (row 20 pending + rows 25–92).
- New master anchors: none.
- Declared exceptions: none. Row 5 passed on its third reroll.
- No audio, TTS, FFmpeg or manual frame durations.

## Review

| Row | Frame | Decision and diagnosis |
|---|---|---|
| 5 | beat01m05, attempt 4 | ACCEPTED. Tight crop shows the sage-gray zombie shoulder touching the brown-covered upper arm. Garment outlines remain separate; no brown sleeve is transferred to the zombie and no limb is merged. Motion ticks support the incidental bump. |
| 14 | beat01m14, attempt 2 | ACCEPTED. The logged prompt-safe retry saved successfully. A generic pale figure is surrounded by separated gray-green figures inside a desaturated thought bubble. The actual brown-shirted/blue-trousered protagonist is absent; no contact occurs. |
| 17 | beat01m17 | ACCEPTED. Low viewpoint and blue sky frame the untouched protagonist while zombies leave space around them. Long sleeves and indifferent zombie behavior are preserved. |
| 18 | beat01m18 | ACCEPTED. Sideways glance and hand-over-sleeved-forearm gesture read clearly. Both forearms remain covered; no wound is visible and zombies do not react. |
| 19 | beat02m01 | ACCEPTED. Compact pharmacy with blank signboard, medical cross, broken window and door on the left. No lettering or people. This is the local storefront reference for row 20. |
| 20 | beat02m02, attempt 1 | REJECTED. The door/window layout mirrors row 19: door moves from left to right, window from right to left; facade proportions change and the green cross disappears. Memory palette and smoke pass, but “Same storefront” does not. |
| 21 | beat02m03 | ACCEPTED. Bent pole and completely blank sign at an empty corner; no invented Fifth street lettering. |
| 22 | beat02m04 | ACCEPTED. Wide rooftop skyline with distinct flat black smoke columns, matching the city-collapse beat. |
| 23 | beat02m05 | ACCEPTED. Bridge, river and thick drifting smoke are all readable; no premature focus on abandoned cars. |
| 24 | beat02m06 | ACCEPTED. Abandoned cars fill the bridge bumper to bumper; doors remain closed for the next narrated reveal. No readable plates or people. |

Every candidate was opened individually and the contact sheet was reviewed end to end. Accepted frames retain the locked wobbly-outline, flat-muted-color style. Slide 01 remains unwounded with sleeves down; slide 02 begins before the bite, with no premature wound or bandage.

## Row 5 repair record

Only the opening sentence changed from attempt 3:

“Extreme close-up cropped from neck to waist of two separate walking bodies touching at exactly one point: the zombie's sage-gray-shirted shoulder on the left meets the protagonist's brown-sleeved upper arm on the right, with a continuous black outline separating their garments.”

The rest of the prompt and reference paths remained unchanged. The result passes, so the three-failed-rerolls exception rule was not invoked.

## Row 20 queued repair

The next call changes only the opening scene sentence to:

“Same storefront with the door on the left and the broken window on the right exactly as in the approved reference, in desaturated memory tone with smoke on the horizon.”

It adds accepted `frames/beat02m01.png` as the optional prior-frame reference alongside the unchanged master anchor. The full prompt is logged as NOT_SENT in `prompts.json`. Do not alter the CSV.

## Next turn

Repair row 20 first, then generate rows 25–32 in order. Nine planned calls leave one repair slot under the ten-image cap. Stay within Worker 1 rows 1–92.
