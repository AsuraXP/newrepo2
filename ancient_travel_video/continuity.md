# Continuity — ancient_travel_video

STATUS: **MASTER ANCHOR LOCKED 2026-11-05 — winner B (cinematic), user-selected.**
Verbatim style/character/negative blocks frozen below and injected into all 182
visual_prompts via build_visuals.py. Frame generation may proceed (STATE 5).

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

## LOCKED MASTER ANCHOR — B (cinematic)
- Anchor file: `refs/anchor_B_cinematic.png` (also reused as frames/beat01m01.png,
  the approved opening shot).
- Character decision: B's fuller look is LOCKED (spiky dark-brown hair + ragged
  brown hide tunic) — era-appropriate and matches the user's cinematic reference.
  The earlier tuft/bare baseline is superseded.

### VERBATIM STYLE + CHARACTER BLOCK (in every prompt; never rephrase)
> Cinematic storytime style: dramatic atmospheric lighting, deep desaturated blues with a warm amber accent, heavy film grain, bold expressive shading, moody depth, hand-drawn 2D illustration with slightly wobbly ink contours. Match ONLY the rendering style, palette, grain and line weight of the reference image; do not copy its scene or composition. Recurring protagonist, when present: a stick-figure human with a large round white head, messy spiky dark-brown hair, a minimal expressive face with two dot eyes, simple brows and a small mouth, thin black stick limbs, and a simple ragged brown hide tunic.

### VERBATIM NEGATIVE BLOCK (in every prompt)
> No text, no letters, no numbers, no watermark, no signature, no extra limbs, no melted faces, no photorealism, no 3D render.

### Locked invariants
- Palette: deep desaturated blue base + warm amber focal accent; night = near-navy;
  day = muted blue-grey with amber light; ice = pale cold blue.
- Line weight: medium-bold black ink contour on figures, thinner on environment.
- Medium: hand-drawn 2D, heavy film grain, bold expressive shading, moody depth.
- Protagonist: round white head, messy spiky dark-brown hair, minimal face (dot
  eyes, simple brows, small mouth), thin black stick limbs, ragged brown hide tunic.
- Crowd figures: same stick construction, smaller, varied head sizes, same hides.
- Animals: same ink-contour + flat-fill treatment, recognizable silhouettes.
- Kudu (established beat07m03, recurs in slide 9 persistence hunt): spiral
  horns, white-striped tan coat, same ink-contour treatment.
- Feet: simple black stick-line feet, never shoes/boots (beat06m02 repair) —
  applies to the ANCIENT protagonist only; the modern walker wears hiking boots.
- Pacific coast (established beat31m02): ice-free green-brown shore, rocky
  headlands, kelp beds, amber horizon south; cold blue sea. Skin boats
  (beat31m05): open skin-covered hulls with visible wooden ribs, paddles,
  no sails — distinct from the Sahul bamboo raft; reuse slides 31–33.
- Beringia fauna (established beat28m02): woolly mammoths (brown, domed heads,
  curved tusks) + steppe bison herds, same ink-contour treatment; reuse in
  slides 28–31 hunting/landscape beats. Wild horses added beat29m05 (small,
  brown, simple ink) — part of the Beringia fauna set.
- Bamboo raft (Sahul crossing, beat22m07–beat25m01): lashed bamboo poles +
  cordage, wooden paddles, no sail, no wheel — pre-wheel era. Distinct from
  the Pacific skin boats.
- Modern walker (Paul Salopek, present-day, established beat37m01): separate
  from the ancient protagonist — round white head, short cropped dark hair,
  trimmed dark beard, dot eyes, muted olive long-sleeve hiking shirt, dark grey
  trekking trousers, worn brown hiking boots, small olive backpack, wooden
  walking stick; no logos. Reuse slides 37–42.
- Set dressing: LOW priority.

## Candidate invariants (superseded by the lock above)
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
| Beach / coast at dusk (deep blue sea, amber sky) | — (style anchor only) | 1–6 |
| Savanna (acacia trees, dry gold grass, dusk gradient) | — (style anchor only) | 6–8 |
| Kalahari (red sand, dry scrub, blazing white sun, distant mesas) | — (style anchor only) | 9–10 |
| Camp (A-frame hide lean-tos, crossed poles, central fire, savanna edge, acacias) | — (style anchor only) | 11–16 |
| Australian outback (red sand, spinifex grass, flat-topped monoliths, glowing amber songlines) | — (style anchor only) | 19–20 |
| Lush Asian coastline (tropical palms, dense jungle, open sea, amber dusk) | — (style anchor only) | 21–25 |
| Ice-age north (snow, advancing ice sheets, frozen ridges, cold blue palette) | — (style anchor only) | 26–31 |
| Pacific coast (ice-free green-brown shore, rocky headlands, kelp beds, cold blue sea) | — (style anchor only) | 31–33 |
| White Sands (pale white gypsum flats, ancient lake, mud, fossil trackways) | — (style anchor only) | 33 |
| Tropical Panama / rainforest (dense green, buttressed giants, vines, humid amber light, dirt footpath) | — (style anchor only) | 34 |
| Andes / continental spine (cold rocky passes, snow peaks, condors, breath puffs, cloud layers below) | — (style anchor only) | 34–35 |
| Tierra del Fuego (cold wind-scoured tip, grey sea, Antarctica hint) | — (style anchor only) | 35 |
| Present-day Salopek walk (gravel roads, open hills, Ethiopian rift valley, seasonal passing landscapes; modern hiking gear) | — (style anchor only) | 37–38 |

No dedicated location_ref files exist; each setting is re-described in scene
clauses using the locked style. Established frames serve as visual continuity
memory (see contact sheets).

DRIFT LESSON (batch 8): "camp firelight / dusk" prompts default to temperate
conifer/pine forest unless the scene clause explicitly says "flat savanna
horizon with acacia silhouettes and no forest". ALWAYS include that clause for
camp beats (slides 11–16). Repaired beat15m01 + beat15m06 this way.

DRIFT LESSON (batch 20): wordless map beats default to modern political borders
(internal country lines) unless the scene clause explicitly says "plain solid
landmass silhouettes, no internal lines of any kind, no country borders, no
grid". ALWAYS include that clause for map/diagram beats. Repaired beat36m02
this way (first re-roll PASS).

DRIFT LESSON (batch 21): portrait beats default to full-body landscape unless
the scene clause says "close-up portrait bust, cropped at the chest, plain
background". Lifetime-vs-route map beats need explicit "full faint route spans
Africa to Tierra del Fuego; only one short bright segment highlighted" or the
route collapses to a single continent. Repaired beat37m02 + beat38m01 this way
(first re-roll PASS).

## Standing composition rule (spec)
Figures pressing against glass/windows/barriers: camera on the viewer's side;
figures seen from behind; hands on the viewer's side of the surface; interior
visible through it. (Rarely applicable to this episode; kept for rule parity.)

## Moderation log (blocked term → replacement)
Standard image-model moderation applies (no hard rules from user).
Persistence-hunt kill rendered as hunter approaching an exhausted, lying kudu;
no wound/blood detail.
- beat09m02 (batch 5): "Hunters jogging after a kudu" BLOCKED →
  "Three stick figures jogging ... behind a running kudu" — accepted.
- beat09m07 (batch 5): "A lone hunter jogging ... toward a resting exhausted
  kudu ..., relentless" BLOCKED → "A lone stick figure jogging steadily ...
  toward a kudu ... lying down resting in the distance" — accepted.
- Lesson: avoid "hunter/chase/relentless/exhausted" pursuit framing in scene
  clauses; use neutral "figures jogging behind / toward a resting kudu".
  Narration (moment_text) is unaffected — only the visual scene clause changes.
