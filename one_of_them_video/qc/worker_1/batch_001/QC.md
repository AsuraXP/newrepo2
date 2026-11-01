# Worker 1 — Batch 001 visual QC

Date: 2026-11-01
Scope: CSV rows 1–8, all in slide 01; assignment remains rows 1–92 only.
Working branch: `arena/62425825-newrepo2` (session-fixed).
Source: `arena/65278339-newrepo2`, commit `b05fb9530ccc0d27e660ce6a7a4281a370da4c18`.

## Result

- Accepted: 6 frames — rows 1, 2, 3, 4, 6, 7.
- Pending: row 5, `beat01m05` (neither attempt shows the required physical bump), and row 8, `beat01m08` (post-sheet edge inspection found a zombie-colored limb emerging from the protagonist's brown sleeve).
- Assignment progress: 6/92 accepted; 86 not accepted (2 pending + 84 not started).
- Image generations: 10/10 — 8 initial + 2 repairs. No further generation this turn.
- Failed repair attempts: row 5 = 1; row 7 = 1, followed by an accepted repair. Row 8 has had no repair attempt yet.
- Declared exceptions: none. Neither pending frame has reached the three-failed-repairs threshold; neither has been shipped as an exception.
- New master anchors: none. `refs/style_test_winner.png` remains the sole master anchor.
- Audio/TTS/FFmpeg: not run. No durations assigned.

## Anchor and continuity checks

The locked anchor specifies a “white-headed stick figure with simple dot eyes,” “gray-green zombie stick figures with droopy half-lidded eyes,” “Bold wobbly black outlines, flat muted colors, warm cream background.” The accepted frames retain those subject, palette and line-weight cues.

The anchor image depicts short sleeves, conflicting with the later locked rule “Sleeve covers the forearm ALWAYS except explicit wound/scar close-ups.” The story-state rule takes precedence: visible protagonist sleeves cover the forearms in the accepted frames. The anchor file and its verbatim prompt were not altered. The accepted `beat01m01.png` was used only as an optional sleeve-continuity reference for the row 5 repair; it is not a replacement master anchor.

Slide 01 remains present-day: no visible bite, wound, wrap or scar; no zombie attacks or pursuit. The accidental shoulder bump is still pending an accurate frame.

## Per-frame review

| Row / frame | Narrated beat | Visual and anchor comparison | Decision |
|---|---|---|---|
| 001 / beat01m01 | The dead walk past you | Calm white-headed walker among gray-green, half-lidded zombies on the anchor's cream/dusty-pink sidewalk. Long brown sleeves, blue trousers; no carried cup and no visible wound. | ACCEPTED, attempt 1 |
| 002 / beat01m02 | on the sidewalk. | Feet-level crop clearly shows blue-trousered black shoes among gray-green feet on sidewalk tiles. No upper-body or wound continuity risk. | ACCEPTED, attempt 1 |
| 003 / beat01m03 | Shoulder to shoulder. | One white head centered between two distinct gray-green heads; adjacent shoulders convey the packed street. Brown sleeves remain long; no grabbing. | ACCEPTED, attempt 1 |
| 004 / beat01m04 | Close enough to touch. | Separate brown-sleeved black hand and gray-green arm, with a small visible gap. Proximity reads without contact; no exposed forearm. | ACCEPTED, attempt 1 |
| 005 / beat01m05 | One of them bumps your arm | Attempt 1 has exposed forearms and no contact. Attempt 2 corrects the sleeves but still has a gap between the nearest zombie shoulder and protagonist arm. Motion ticks do not substitute for the action. | REJECTED; pending next repair |
| 006 / beat01m06 | and keeps going. | The gray-green walker has moved ahead with head forward; a clear gap separates it from the long-sleeved protagonist. No acknowledgment or pursuit. | ACCEPTED, attempt 1 |
| 007 / beat01m07 | It does not stop. | Attempt 2 shows a rear-facing gray-green zombie leaving and exactly one white-headed protagonist. Other pedestrians are gray-green. The duplicated living protagonists from attempt 1 are gone. | ACCEPTED, attempt 2 |
| 008 / beat01m08 | It does not snarl. | The gray-green face has heavy half-lids and a slack mouth, so the facial beat passes. However, the edge close-up shows a gray-green limb emerging from the brown protagonist sleeve, mixing zombie and living character design. This violates the locked character separation despite the otherwise correct expression. | REJECTED after edge inspection; pending first repair |

All accepted images were opened individually, then reviewed together on the contact sheet. An additional edge close-up caught the row 8 sleeve/limb defect before commit. No gibberish lettering, watermark, merged face or extra-limb defect was found in the final six accepted frames. They retain native generator dimensions (1376 × 768); no manual timing, interpolation or post-generation scaling was applied.

## Repair ledger — one prompt-text change per reroll

### beat01m05 — repair 1, rejected

Specific faults: “short sleeves” expose the forearms; the zombie's shoulder is separated from the protagonist's arm rather than bumping it.

Only the opening scene-description sentence was changed:

- Before: “A zombie's shoulder bumps the figure's arm mid-stride.”
- After: “In a medium two-shot, the zombie's gray-green shoulder visibly presses against the protagonist's brown long-sleeved upper arm mid-stride, their bodies adjacent at the point of contact.”

The remaining direction, story-state, style and negative text stayed unchanged. The optional prior-approved sleeve reference was added under the anchor recipe. Outcome: sleeves fixed; physical contact still absent. Keep both rejects out of `frames/`.

Next repair should replace only the opening sentence again with an explicit tight crop of a gray-green shoulder touching a brown-covered upper arm, keeping all other prompt text unchanged. This will be attempt 3 / repair 2 for this frame.

### beat01m07 — repair 1, accepted

Specific fault: several identical white-headed, brown-shirted protagonists appear, instead of one living protagonist among gray-green zombies.

Only the opening scene-description sentence was changed:

- Before: “Rear view: the zombie keeps walking away, head forward.”
- After: “Rear view: one zombie walks away with its back to the camera and head forward, with exactly one white-headed protagonist and otherwise only gray-green zombie pedestrians on the sidewalk.”

The remaining direction, story-state, style and negative text stayed unchanged. The accepted `beat01m06.png` was added as the optional prior-frame reference. Outcome: one protagonist; rear-facing zombie and forward head retained.

## Artifacts and moderation

- `prompts.json`: exact sent prompt text, reference paths, attempt status, native dimensions and SHA-256 for all 10 candidates.
- `contact_sheet.jpg`: all 10 candidates, including four rejects, with approximately 380-pixel-wide thumbnails and row/attempt labels. Labels exist only on the QC sheet, not in episode frames.
- `rejects/`: preserved rejected source candidates; intentionally excluded from Git. Their thumbnail evidence remains in the committed contact sheet.
- No image-tool moderation block occurred. Existing prompt-safe replacements in `continuity.md` and `visuals.csv` remain unchanged.

## Next turn

Resume row 5 first (attempt 3 / repair 2), then repair row 8 (attempt 2 / repair 1), then generate rows 9–16 (`beat01m09`–`beat01m16`) in narration order. For row 8, change only the opening scene sentence to exclude the brown-sleeved figure entirely from the face crop. These ten planned generations reach the next turn's cap; if another repair is needed, defer the last new row instead of exceeding it. Do not generate slides 04–12, alter the locked script/CSV, create a thumbnail, or run audio/render stages.
