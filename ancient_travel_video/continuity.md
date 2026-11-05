# Continuity — ancient_travel_video

STATUS: style direction received from user (2026-11-05); anchor lock happens at
STATE 4 after script approval.

## User-provided style refs (STYLE ONLY — never literal)
| File | What to take from it | What NOT to take |
|---|---|---|
| `refs/style_ref_cozy_textured.png` | paper-grain texture, soft muted fills, wobbly hand-drawn contour, cozy lamp-glow lighting option | couch/TV/living-room scene, phone, blanket props |
| `refs/style_ref_cinematic_storytime.png` | dramatic night lighting, fire glow, grainy cinematic shading, expressive worried face | cave scene, fur garment literal, campfire composition |
| `refs/style_ref_expressive_comic.png` | bold black stick limbs, round white head, minimal expressive face, accent-color splash behind figure, halftone ground shadow | yellow idea-spark pose, plain white void background |

User instruction (verbatim): "the images i proved are art sytle only do not take
them literally and reuse them continuously" → the STYLE is reused continuously
across every frame; the literal scenes/props are never copied.

## STATE 4 style test refs (generated 2026-11-05, awaiting user selection)
Same opening-beach scene, three style leanings. Exact generation prompts:

### anchor_A_cozy.png (ref: style_ref_cozy_textured.png)
> Wide 16:9 establishing shot. A lone small stick-figure traveler with a large round white head, thin black stick limbs, a small black hair tuft on top, and a minimal expressive face with two dot eyes, simple brows, and a small mouth, standing on an empty prehistoric beach at dawn, facing a calm vast ocean, soft warm light, untouched ancient shore with wild grasses, no modern objects. Cozy textured storytime style: warm cream and muted blue palette, visible paper-grain texture, soft wobbly hand-drawn ink contours, gentle flat fills with soft grain shading, cozy warm dawn glow. Match the provided reference image's rendering style, palette and line weight. No text, no letters, no numbers, no watermark, no signature, no extra limbs, no photorealism, no 3D render.

QC: style on-model; DEFECT — modern blue backpack added (anachronism). If A wins,
locked block replaces backpack with a simple hide bundle or bare figure.

### anchor_B_cinematic.png (ref: style_ref_cinematic_storytime.png)
> Wide 16:9 establishing shot. A lone small stick-figure traveler with a large round white head, thin black stick limbs, a small black hair tuft on top, and a minimal expressive face with two dot eyes, simple brows, and a small mouth, standing on an empty prehistoric beach at dawn, facing a calm vast ocean, soft warm light, untouched ancient shore with wild grasses, no modern objects. Cinematic storytime style: dramatic atmospheric lighting, deep desaturated blues with a warm amber dawn accent, heavy film grain, bold expressive shading, moody depth. Match the provided reference image's rendering style, palette and line weight. No text, no letters, no numbers, no watermark, no signature, no extra limbs, no photorealism, no 3D render.

QC: style on-model; character drift — spiky brown hair + fur tunic instead of
hair tuft + bare stick body. If B wins, decide whether to lock that fuller look
or correct toward the tuft/bare baseline.

### anchor_C_comic.png (ref: style_ref_expressive_comic.png)
> Wide 16:9 establishing shot. A lone small stick-figure traveler with a large round white head, thin black stick limbs, a small black hair tuft on top, and a minimal expressive face with two dot eyes, simple brows, and a small mouth, standing on an empty prehistoric beach at dawn, facing a calm vast ocean, soft warm light, untouched ancient shore with wild grasses, no modern objects. Expressive comic style: bold clean black stick limbs, round white head, flat warm cream background with a single amber accent splash behind the figure, halftone dot ground shadow, punchy high-contrast comic energy, minimal detail. Match the provided reference image's rendering style, palette and line weight. No text, no letters, no numbers, no watermark, no signature, no extra limbs, no photorealism, no 3D render.

QC: on-model character (tuft, bare stick limbs, minimal face), halftone shadow,
amber splash, no anachronisms. Cleanest baseline of the three.

## Candidate invariants (to be frozen verbatim at STATE 4)
- Medium: hand-drawn 2D storytime illustration, visible paper grain, slightly
  wobbly ink contours, flat muted fills with soft grain shading.
- Protagonist ("you"): large round white head, thin black stick limbs, small
  black hair tuft, minimal expressive face (dot/line eyes, simple brows/mouth),
  no clothing or a simple muted tunic when the era demands; same silhouette in
  every frame.
- Palette: warm cream/tan base, muted blue + ochre + olive secondaries, one warm
  accent (amber) for focal light; night scenes deep desaturated blue.
- Line weight: medium-bold black contour on figures, thinner on environments.
- Crowd figures: same stick-figure construction, smaller, varied head sizes.
- Animals (kudu, mammoth, seals): same ink-contour + flat-fill treatment,
  simplified but recognizable silhouettes.
- Set dressing: LOW priority — varies shot to shot.

## Location reference scope
Refs above are ARTISTIC STYLE anchors only. A `location_ref` is passed ONLY for
beats inside the same continuous setting; on location shifts (savanna → coast →
desert → sea → ice → rainforest → Andes → Tierra del Fuego) generate a NEW
environment in the locked style/palette. Never force an old location ref.

| Location | Ref file | Beats (slide ids) |
|---|---|---|
| PENDING (assigned at STATE 4/5) | — | — |

## Standing composition rule (spec)
Figures pressing against glass/windows/barriers: camera on the viewer's side;
figures seen from behind; hands on the viewer's side of the surface; interior
visible through it. (Rarely applicable to this episode; kept for rule parity.)

## Moderation log (blocked term → replacement)
(empty — no hard rules from user; standard image-model moderation applies:
persistence-hunt kill rendered as hunter approaching an exhausted, lying kudu,
no wound/blood detail.)
