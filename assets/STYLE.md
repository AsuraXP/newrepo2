# STYLE — ancient_travel_video (LOCKED)

User-selected 2026-11-05: **anchor B (cinematic)**. Reference:
`ancient_travel_video/refs/anchor_B_cinematic.png` (also reused as the approved
opening frame `beat01m01`). User refs are STYLE ONLY — never literal scenes/props.

## Verbatim style + character block (in every prompt; never rephrase)

> Cinematic storytime style: dramatic atmospheric lighting, deep desaturated blues with a warm amber accent, heavy film grain, bold expressive shading, moody depth, hand-drawn 2D illustration with slightly wobbly ink contours. Match ONLY the rendering style, palette, grain and line weight of the reference image; do not copy its scene or composition. Recurring protagonist, when present: a stick-figure human with a large round white head, messy spiky dark-brown hair, a minimal expressive face with two dot eyes, simple brows and a small mouth, thin black stick limbs, and a simple ragged brown hide tunic.

## Verbatim negative block (in every prompt)

> No text, no letters, no numbers, no watermark, no signature, no extra limbs, no melted faces, no photorealism, no 3D render.

## Prompt formula

`Wide 16:9 cinematic frame. {scene} {STYLE} {NEG}`

Full character/location locks, anti-drift clauses and QC lessons live in
`ancient_travel_video/continuity.md`. Camera is locked off: no Ken Burns, no
zoom, no drift. Transitions are visible fades (config: 1.0 s default, 0.8 s min).
