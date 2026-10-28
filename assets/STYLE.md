# LOCKED ART STYLE — stick-figure explainer series

Reference frames: `assets/frames/01_wake_light.jpg`, `06_working_town.jpg`

Every prompt in `narration/frames.json` is composed from the subject + this exact
token set. Do not paraphrase it per frame — the flat look is the channel's identity.

## Style token set (verbatim, appended to every subject)

```
flat 2D cartoon illustration, thick slightly uneven black ink outlines, simple
round-headed stick figure character with a blank white circular head, two small
black dot eyes and a small straight mouth, thin black line limbs, matte flat
colour fills with no gradients, no shading and no texture, muted limited palette
of cream, pale grey-blue, warm brown, tan and mustard yellow, plain uncluttered
background, hand-drawn animation still, 16:9 widescreen
```

## Negative token set (verbatim)

```
photograph, photorealistic, 3d render, gradient shading, soft shadows, texture,
realistic anatomy, extra limbs, extra fingers, anime, manga, detailed background,
neon colours, text, letters, words, caption, watermark, logo, signature
```

## The rules

1. **Flat.** Solid fills, one weight of black outline, no gradients, no lighting,
   no texture, no cast shadows beyond a simple flat shape.
2. **The hero is one stick figure, always the same.** White circular head, two dot
   eyes, small straight mouth. Ragged brown fur tunic, bare line legs. Never
   redesign the head or the eyes.
3. **The head always faces the viewer.** No side profiles, no head-on-pillow
   angles, no looking straight up — the model collapses the eyes and mouth onto
   each other and the character goes off-model. Convey action with limbs, body
   angle and props; keep the face frontal.
4. **Hands are simple line mittens, three fingers.** Detailed hands read as a
   different cartoon and break the style.
5. Face is allowed and encouraged — expression is carried by the eyebrows and the
   mouth line, nothing else. Deadpan is the default; surprise is two dots and an
   open oval.
6. Backgrounds are **props, not scenery**: a wall, a floor line, a fire, a jar, a
   horizon. Three or four shapes maximum. Nothing that needs detail.
7. Palette is closed: cream paper, grey-blue, warm brown, tan, mustard, plus one
   accent (fire orange or night navy). No other hues.
8. Composition is simple and centred, read at a glance in under a second.
9. Modern-day gags may appear as a cold open or a cutaway (couch, phone, TV) —
   these stay in the same flat style and same palette.

## Per-episode continuity

- Same head, same eyes, same tunic, same palette, same line weight, every episode.
- Night scenes: navy field, cream stars, one orange fire.
- Cut on the word: the picture settles as the phrase is spoken (see `WORKFLOW.md`).
