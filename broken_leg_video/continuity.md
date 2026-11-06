# CONTINUITY — broken_leg

Anchor lock ledger. Blocks below are copied **VERBATIM** into every generation
prompt. Do not paraphrase, do not reorder, do not "improve" them.

Your three supplied images are ART STYLE ONLY: line quality, palette, texture,
character design language. Nothing of their subjects, furniture, rooms or
compositions enters this film.

Round 1 was rejected by the user ("no images matched my style"). The diagnosis
was correct: round 1 came out sepia-monochrome with a full halftone dot grid
over the ground. Round 2 removes the brown wash, restores sage/mustard/
terracotta/navy, thins the line, and limits halftone to small accent patches.

## LOCKED STYLE BLOCK (paste verbatim)

```
Hand-drawn 2D animation still, clean confident ink line in deep warm brown-black with slightly varied marker weight, flat gouache fills and soft paper grain on warm cream paper, palette of cream, sage green-blue, mustard yellow, terracotta, deep navy with brick-red accents, halftone dot patches used sparingly as small accent shadows only, simple round-headed stick figures with dot eyes and thin expressive brows, soft warm light with gentle bloom, muted film grain, locked-off camera, 16:9 widescreen.
```

## LOCKED NEGATIVE BLOCK (paste verbatim)

```
sepia monochrome, brown-only palette, full dot grid across the ground, photorealistic, 3D render, CGI, gradients, airbrush, anime, chibi, detailed anatomy, gore, blood, open wounds, broken skin, text, letters, numbers, captions, watermark, logo, signature, frame border, extra limbs, melted faces, deformed hands, motion blur, lens flare, neon colours, dense background detail
```

## CHARACTER ANCHOR — "YOU" (protagonist)

```
YOU: round white head, two black dot eyes, thin arched brows, three or four ink strands of hair at the crown, one ink-stroke body, fringed hide tunic to mid-thigh in mustard, simple three-finger hands, thick dark-brown mitten boots. Seen from behind, in profile, from above, or as a small figure in wide shots; face shown when the beat needs it.
```

Never give YOU a wound, a cast, a splint, a bandage or blood. The bad leg is a
wrong angle and a flat shape, nothing more.

## CHARACTER ANCHOR — THE BAND (four)

```
BAND MEMBER: same design language as YOU, darker shaggy hair in a few ink strands, hide garments in sage green-blue or cream, brows and posture carry all emotion, no other facial detail. Weapons only when the beat asks for them.
```

Elder (Shanidar 1): grey-streaked hair, heavy brow, hide across the shoulders,
right forearm ended smooth below the elbow, left eye socket flattened.

## LIGHT KEYS (pick per beat, do not blend them)

- **DAY** — cream paper sky, sage and sand ground, soft warm sun, no dark vignette.
- **FIRELIT** — deep navy darks, orange fire light on faces and rock, cream highlights, one halftone shadow patch behind the group.
- **MUSEUM / LAB** — cold white light, sage-grey shadows, no warm cast.
- **DIAGRAM** — plain cream paper, thin even line, one small halftone contact shadow per object, generous margins.

## LOCATION ANCHORS

No `location_ref` exists yet. Workers build fresh backgrounds per beat in the
locked style and light keys. Per-location refs get cut from the first approved
frames and logged here before any worker reuses them.

## ERA RULES

Palaeolithic only: no metal, no pottery, no woven cloth, no architecture beyond
hide shelters. The single exception is the final still life, which is explicitly
listing inventions (fire drill, spear, wooden wheel disc). No text anywhere in
this film, not even on museum labels.

## CONTENT MODERATION LOG

| Script word | Prompt language | Why |
|---|---|---|
| crushing blow / broken eye socket | "flattened left eye socket on a clean fossil skull" | no injury gore on a living face |
| blood (bone healing) | "warm red wash inside a diagram gap" | internal diagram, not a wound |
| skeleton | "fossil skeleton drawn as clean bone shapes" | stylised, museum-clean |
| grave / saying goodbye | "shallow scrape in the earth with one flat stone, no body visible" | avoid death imagery |
| leg folds the wrong way | "one lower leg folded at a wrong angle, drawn as a flat wedge" | no gore, no bone showing |
| predator eyes | "two pairs of eyes low in the dark, shapes barely readable" | threat without violence |
| childbirth | "woman supported upright by two others, hands gripping forearms, no gore" | clinical, non-explicit |

## COMPOSITION RULE

Figures behind glass or a barrier: camera on the viewer's side, figure seen from
behind, hands on the viewer's side of the surface, interior visible through it.

## ANCHOR LOG

| Date | Ref | Status |
|---|---|---|
| 2026-11-06 | `refs/style_ref_A_cozy_textured.jpg` | user-supplied, style direction only |
| 2026-11-06 | `refs/style_ref_B_cinematic_storytime.jpg` | user-supplied, style direction only |
| 2026-11-06 | `refs/style_ref_C_expressive_comic.jpg` | user-supplied, style direction only |
| 2026-11-06 | `refs/test_A_warm_daylight.jpg`, `test_B_cinematic_dusk.jpg`, `test_C_paper_comic.jpg` | round 1 — REJECTED by user (sepia, over-textured) |
| 2026-11-06 | `refs/proof1_day_hillside.jpg` | round 2 day key — awaiting approval |
| 2026-11-06 | `refs/proof2_night_cave.jpg` | round 2 firelit key — awaiting approval |
| 2026-11-06 | `refs/proof3_diagram_bone.jpg` | round 2 diagram key — awaiting approval |

## MASTER ANCHOR PROMPT

PENDING — written from the approved round-2 proof, then reused unchanged as the
first line of every worker prompt.
