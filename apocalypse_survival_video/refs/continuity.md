# Continuity — Apocalypse Survival Video

## Style Anchors (refs/)

| File | Description | Use |
|---|---|---|
| `Screenshot Capture - 2026-10-28 - 08-14-55.png` | Figure on couch, phone, TV, blanket — modern apartment | Indoor/casual scenes, neutral expression |
| `Screenshot Capture - 2026-10-28 - 08-14-40.png` | Figure pointing up, smug expression, white BG | Teaching/explaining moments, clean BG |
| `Screenshot Capture - 2026-10-28 - 08-14-25.png` | Figure in cave, campfire, animal skins, night sky | Survival/wilderness scenes, dramatic lighting |

## Style Token Block (VERBATIM — copy into every prompt)

```
Stick-figure cartoon, 16:9. White round head (large circle), dot eyes (small black filled circles), line mouth (thin black line, expression via curve). Bold black stick body (thick lines, not thin). Simple circle or filled-shape hands. Bold black outlines on ALL elements. Flat colored backgrounds, no gradients, no shading. Minimal shadow under objects only. Environments are simple geometric shapes with flat color fills. Expressions carried by eye/mouth shape only — no eyebrows needed unless emphasizing.
```

## Negative Prompt (VERBATIM — every prompt)

```
photorealistic, 3D render, CGI, anime, chibi, watercolor, pixel art, gradients, drop shadows, complex anatomy, realistic proportions, text labels, watermarks, signatures, extra limbs, deformed hands, blurry, low resolution, jpeg artifacts, ken burns, zoom, motion blur, camera movement
```

## Visual Invariants

| Element | Rule |
|---|---|
| Head | Large white/cream circle, always the same size ratio to body |
| Eyes | Two small black filled circles, evenly spaced |
| Mouth | Thin black line — straight (neutral), curved up (happy), curved down (sad), slight smirk (confident), small O (surprised) |
| Body | Bold black stick lines — arms, legs, torso as simple lines |
| Hands | Small filled circles or simple glove shapes |
| Hair | Messy short black lines on top of head when shown (not always present) |
| Outlines | Bold black outlines on EVERYTHING — characters, objects, furniture, backgrounds |
| Colors | Flat fills only. No gradients, no shading, no texture overlays |
| Backgrounds | Simple geometric rooms/landscapes. Walls are flat color rectangles |
| Camera | LOCKED OFF. No zoom, no pan, no ken burns, no drift |
| Expression | Dot eyes + line mouth carry all emotion. Exaggerate slightly for clarity |

## Content Moderation Notes

- Apocalypse/violence themes: keep non-graphic. No blood, no weapons in action, no injury detail
- Threats shown as shadows/silhouettes only, never realistic
- "Monsters" abstracted as shadowy figures with red X marks
- Survival tension conveyed through expression and composition, not graphic content

## Anchor Recipes

| Scene type | Prompt pattern |
|---|---|
| Indoor casual | Stick figure + simple room + flat wall color + minimal props |
| Teaching moment | Stick figure + white/light BG + gesture (pointing, holding) |
| Wilderness/survival | Stick figure + natural setting + campfire/shelter + dramatic flat colors |
| Crowd scene | Multiple identical stick figures + simple BG + motion lines |
| Object focus | Stick figure interacting with specific item + item clearly rendered in same style |
| Split panel | Two or three panels with bold dividers, each showing different scenario |
| Icon/diagram | Simple icons (clock, shield, lock) in bold outline style matching character |
