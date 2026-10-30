# Continuity

## User-provided style references

- `refs/user-style-reference-01.png`
- `refs/user-style-reference-02.png`
- `refs/user-style-reference-03.png`

Approved style direction: hand-drawn 2D; stick-figure-like bodies; pale round faces; bold, slightly irregular black outlines; sparse facial marks; flat restrained colors with vivid blue/orange accents; clear silhouettes; sharp, expressive brows, eyes, mouths, and poses. Adapt props, setting, and clothing to the story. Readable in-frame text is allowed only when the story calls for it.

Draft character continuity for review: traveler has tousled dark hair, pale round face, slim black-line limbs, rough ochre tunic, brown belt; Tavi is a shorter child with short dark hair and a rust-orange tunic; Keeper is tall/angular with a charcoal-violet robe and black crystal. These generated designs are **not approved anchors yet**.

## State 4 style-test candidates — awaiting user selection/approval

### Candidate 1 — protagonist character reference
File: `refs/style-test-01-protagonist.png`
Exact prompt:
> Create ONE standalone hand-drawn 2D character reference image, not a sheet or collage. Show a single full-body traveler character for a whimsical fantasy story, centered against a simple warm cream background. The traveler has a pale round face, tousled dark-brown hair, very simple black dot eyes, a sharply expressive raised brow, and a small confident half-smile; slim stick-figure-like black-line limbs; a simple rough ochre tunic and brown belt. Give the pose lively intelligence and alert curiosity, with a clear silhouette and expressive hands. Match the supplied style references: bold slightly irregular black outlines, minimal face details, flat restrained color, lightly imperfect hand-drawn lines, clean uncluttered composition. No text, labels, border, watermark, or extra characters. This is a style test, not a finished story frame.

### Candidate 2 — first-miracle action/style reference
File: `refs/style-test-02-first-miracle.png`
Exact prompt:
> Create ONE standalone 16:9 hand-drawn 2D story illustration, not a sheet or collage: the first-miracle moment in a completely imaginary city. The recurring traveler—pale round face, tousled dark hair, bold expressive brows, slim stick-like limbs, rough ochre tunic—leans with focused effort on a long crooked beam balanced over a small rounded stone; an enormous stone gate has just shifted and a bright blue stream bursts into a dry canal. Nearby townspeople react with astonishment; a small child watches the mechanism closely. Show an energetic readable action and sharp expressions, with Orra’s leaning fantasy towers behind them. Match the supplied references: bold imperfect black ink outlines, minimal facial marks, expressive stick-figure bodies, flat muted cream/charcoal/umber colors with strong blue and orange accents, simple backgrounds. No captions, labels, watermark, or decorative text. This is a style test, not final frame art.

### Candidate 3 — bell-tower/location reference
File: `refs/style-test-03-bell-tower.png`
Exact prompt:
> Create ONE standalone 16:9 hand-drawn 2D fantasy story illustration, not a sheet or collage: at dusk in an entirely imagined world, a tall angular Keeper in a charcoal-violet robe stands inside a simple floating-stone bell tower, clutching a dark crystal at his throat as a huge suspended stone bell begins to ring. Below, the tiny fantasy city of Orra sits in a valley beneath a green-ringed sun and three pale moons. Make the Keeper’s expression sharply possessive and uneasy; use dramatic but simple silhouettes, expressive face and hands. Match the supplied style references: bold slightly irregular black outlines, stick-figure-like forms, pale round faces, minimal facial details, flat restrained colors with blue and orange highlights, uncluttered hand-drawn 2D composition. No text, labels, watermark, or collage elements. This is a style test, not final frame art.

No moderation blocks or prompt substitutions so far.

## Approved anchors

None yet. Await user approval of the style-test candidates before batch 1. After approval, use the selected protagonist and location references in every frame prompt; add the optional previous approved frame only when continuity requires it. Copy the approved style/subject blocks verbatim.

## Anchor approval

The user approved all three style-test images as anchors on 2026-10-30:
- Character anchor: `refs/style-test-01-protagonist.png`
- First-miracle/action anchor: `refs/style-test-02-first-miracle.png`
- Bell-tower/location anchor: `refs/style-test-03-bell-tower.png`

Use these approved references for frame prompts; preserve the traveler's pale round face, tousled dark hair, ochre tunic, the blue gate/water motif, Orra's leaning towers, and the Keeper's charcoal-violet robe/black crystal. Story-state rules (especially gate position and the bell's active/inactive state) must be explicit in each frame prompt.

## Frame batch 01 QC (rows 1–8)

Accepted: `beat01m01.png` through `beat01m08.png`. Composition follows the “First Miracle” hook, then the bell/dawn memory-reset beat. No visible text artifacts, watermark, or major anatomy/perspective defects observed.

- Drift checks: `b01m01` traveler ochre tunic + tousled dark hair matches protagonist anchor; `b01m03` upbeat face is an intentional expression shift from anchor’s half-smile; `b01m06` Tavi rust-orange scarf/tunic matches the approved child direction; `b01m04` bell silhouette and floating tower follow location anchor.
- Rejection: `beat01m06` v1 incorrectly introduced the Keeper into the memory-reset shot. Re-rolled by changing only one clause: added “Only the traveler, Tavi, and background townspeople are present; do not include the Keeper, guards, or other named characters.” V2 passes. The first v1 image was overwritten, so the contact sheet includes a clearly labeled QC card for that rejected attempt rather than its thumbnail.
- Contact sheet: `frames/contact-sheet-batch01.jpg` (380px thumbnails; accepted frames plus rejection QC card).
