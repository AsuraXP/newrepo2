# CONTINUITY — broken_leg

Anchor lock ledger. Blocks below are copied **VERBATIM** into every generation
prompt. Do not paraphrase, do not reorder, do not "improve" them.

The three supplied images (`refs/style_ref_A..C`) are ART STYLE ONLY. Do not
reproduce their subjects, furniture, rooms or compositions. Nothing from them
enters this film except line, palette, texture and character design language.

## LOCKED STYLE BLOCK (paste verbatim)

```
Hand-inked 2D animation still on warm cream paper, thick slightly wobbly dark-brown outlines, flat gouache fills with soft paper grain, limited earthy palette of mustard ochre, sage blue-grey, warm sand, deep navy and one brick-red accent, halftone dot shading only in contact shadows, simple round-headed figures with dot eyes and thin expressive brows, soft daylight or firelight bloom, muted film grain, locked-off camera, 16:9 widescreen.
```

## LOCKED NEGATIVE BLOCK (paste verbatim)

```
photorealistic, 3D render, CGI, gradients, airbrush, anime, chibi, detailed anatomy, gore, blood, open wounds, broken skin, text, letters, numbers, captions, watermark, logo, signature, frame border, extra limbs, melted faces, deformed hands, motion blur, lens flare, neon colours, dense background detail
```

## CHARACTER ANCHOR — "YOU" (protagonist)

```
YOU: round white head, two black dot eyes, thin arched brows, a small ink tuft of hair at the crown, one ink-stroke body, fringed hide tunic to mid-thigh, simple three-finger hands, thick dark-brown mitten boots. Seen from behind, in profile, from above, or as a small figure in wide shots; face shown only when the beat needs it.
```

Never give YOU a wound, a cast, a splint, or blood. The bad leg is drawn as a
wrong angle and a flat shape, nothing more.

## CHARACTER ANCHOR — THE BAND (four)

```
BAND MEMBER: same design language as YOU, darker shaggy hair, hide garments in sage grey or warm sand, brows and posture carry the emotion, no other facial detail.
```

Four adults, one elder (Shanidar 1: grey-streaked hair, heavy brow, hide across
the shoulders, right forearm ended smooth below the elbow, left eye socket
flattened).

## LOCATION ANCHORS (attach `location_ref` ONLY inside that continuous setting)

- **HILLSIDE** — loose grey scree, dry grass, bare ridge line, low sun. Attach
  only for slides 1-8, 20, 29-32. Never for cave, museum or plain beats.
- **CAVE CAMP** — dark warm interior, low fire at the mouth, hides, stone tools,
  smoke. Attach only for slides 3-5, 9, 15-16, 22-28.
- **MUSEUM / LAB** — cold white light, grey foam, glass cases. Attach only for
  slides 8-9, 11-14, 18, 20-27, 32.
- On any setting change: no `location_ref`, generate a fresh background in the
  locked style.

## ERA RULES

Palaeolithic: no metal, no pottery, no woven cloth, no wheels except in the
final still life (which is explicitly listing inventions), no architecture
beyond hide shelters. America/Europe absent from signage — there is no text in
this film at all.

## CONTENT MODERATION LOG

| Script word | Prompt language | Why |
|---|---|---|
| crushing blow / broken eye socket | "flattened left eye socket on a clean fossil skull" | no injury gore on a living face |
| blood (bone healing) | "warm red wash inside a diagram gap" | internal diagram, not a wound |
| skeleton | "fossil skeleton drawn as clean bone shapes" | stylised, museum-clean |
| grave / saying goodbye | "shallow scrape in the earth with one flat stone, no body visible" | avoid death imagery |
| leg folds the wrong way | "one lower leg bent at a wrong angle, drawn as flat shapes" | no gore, no bone showing |
| predator eyes | "two pairs of eyes low in the dark, shapes barely readable" | threat without violence |
| childbirth | "woman supported upright by two others, hands gripping forearms, no gore" | clinical, non-explicit |

## COMPOSITION RULE

If a beat ever puts a figure behind glass or a barrier: camera stays on the
viewer's side, figure seen from behind, hands on the viewer's side of the
surface, interior visible through it. (Applies to museum-case beats only.)

## ANCHOR LOG

| Date | Ref | Status |
|---|---|---|
| 2026-11-06 | `refs/style_ref_A_cozy_textured.jpg` | user-supplied, style direction only |
| 2026-11-06 | `refs/style_ref_B_cinematic_storytime.jpg` | user-supplied, style direction only |
| 2026-11-06 | `refs/style_ref_C_expressive_comic.jpg` | user-supplied, style direction only |
| 2026-11-06 | `refs/test_A_warm_daylight.jpg` | generated from the locked blocks, awaiting pick |
| 2026-11-06 | `refs/test_B_cinematic_dusk.jpg` | generated from the locked blocks, awaiting pick |
| 2026-11-06 | `refs/test_C_paper_comic.jpg` | generated from the locked blocks, awaiting pick |

Winning test ref becomes the master anchor: its exact prompt is logged below and
reused, unchanged, as the first line of every worker prompt.

## MASTER ANCHOR PROMPT

PENDING — written only after the user picks a winning test ref.
