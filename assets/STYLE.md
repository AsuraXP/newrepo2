# STYLE — frozen tokens (user-supplied references, 2026-10-31)

Status: SELECTED BY USER (reference images supplied). No anchor frame is
approved yet — Phase 3 style gate still requires an explicit approval of a
generated reference frame.

Source references (read-only, committed as user intent, not as episode frames):

- `style_refs/ref_source_01_cave_campfire.png` — exterior night, campfire lighting, ragged-cloth costume
- `style_refs/ref_source_02_stick_figure.png` — clean white field, full-body figure
- `style_refs/ref_source_03_couch_phone.png` — interior, furniture, props, wide shot

Palette sampled from the references (flat fills, no gradients):

| Role | Hex |
|---|---|
| Paper / sky background | `#F8F8F8` |
| Warm wall cream | `#F0E0C8` |
| Sand wall shadow | `#E0D0B8` |
| Warm floor brown | `#705038` |
| Cave rock | `#585050` |
| Cave rock shadow | `#403838` |
| Night sky navy | `#182850` |
| Slate sofa blue-grey | `#788090` |
| Ink outline | `#000000` |
| Accent mustard | `#D8A838` |
| Accent flame orange | `#F08018` |
| Accent rust | `#A85038` |
| Accent olive | `#6B7A44` |

## TOKEN BLOCK — copy VERBATIM into every prompt, character for character

```
STYLE: 2D hand-drawn digital cartoon, deadpan stick-figure animation still.
Line: single uniform-weight black ink contour, ~4px at 1280px wide, slightly
wobbly hand-drawn edges, no line tapering, no cross-hatching, no sketch texture.
Fill: flat opaque color areas only, no gradients, no airbrush, no soft shadow,
no bloom; one flat shadow tone per surface at most.
Face: perfect circle head, blank off-white fill, two small solid black dot eyes,
one simple curved black mouth line; no nose, no ears, no eyebrows unless the
beat needs them; expression carried by mouth curve and eye placement alone.
Body: pure black stick limbs of even thickness with solid black round dot hands
and dot feet; torso is a single line unless clothing is specified.
Color: restrained flat palette — paper #F8F8F8, cream #F0E0C8, sand #E0D0B8,
floor brown #705038, cave rock #585050 / #403838, navy #182850, slate #788090,
with at most two warm accents from #D8A838 / #F08018 / #A85038 / #6B7A44.
Composition: wide 16:9 locked-off camera, eye-level or slightly above, figure
composed off-center with generous empty background, background furniture and
props drawn as simple flat blocks with black outlines.
Mood: dry, calm, matter-of-fact; comedy from understatement, never from
cartoon squash-and-stretch.
NEGATIVE: photorealistic, 3D render, CGI, painterly brushwork, oil paint,
watercolor wash, gradient mesh, lens flare, bokeh, depth-of-field blur, film
grain, motion blur, anime, manga speed lines, chibi, caricature, oversized
googly eyes, extra limbs, extra fingers, malformed hands, melted features,
duplicate heads, text, letters, captions, watermark, signature, UI chrome,
busy detail, ornate background, dramatic chiaroscuro, gore, blood spatter.
```

## Character invariants (episode anchor, established at Phase 3)

- HEAD: perfect circle, off-white (#F8F8F8) fill, black outline, always same diameter relative to frame.
- EYES: two solid black dots, fixed spacing, no whites, no highlights.
- MOUTH: single curved stroke; neutral = short flat curve, worry = downward arc, conviction = upward arc.
- LIMBS: uniform black strokes, dot hands (filled circles), dot feet; limbs bend only at the implied joint.
- SILHOUETTE: figure reads clearly at 336px thumbnail width.
- WARDROBE: one outfit per episode, stated once in the anchor recipe and repeated verbatim.
- CREATURE RULE: any non-human threat is a flat black silhouette with the same dot eyes, never detailed or gory.

## Notes on generation hygiene

- The reference images are the style authority; the token block is the portable
  restatement. When a re-render drifts, re-paste the block rather than editing it.
- Never describe the character with a different head shape or different eye
  count; those are the two fastest ways to lose the look.
- Text in frame is banned (the references contain UI/text blocks; the episode
  frames must not).
