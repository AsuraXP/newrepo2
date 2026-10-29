# Continuity & Visual Invariants

## 1. User-Supplied Master Style References (`refs/`)
- `refs/user_style_ref_01_couch.png` — Home protagonist Anchor: minimalist white-circle-head black-stick-figure slouched on slate-blue two-cushion couch (`#768999`) with mustard-yellow blanket (`#F2C649`), holding dark smartphone, wall-mounted flatscreen TV on warm cream wall (`#EBD8BE`), flat medium-brown floor (`#6E472B`), wooden end table with brown mug.
- `refs/user_style_ref_02_pose.png` — Facial expression & stick-anatomy Anchor: large round white/cream circle head, uniform medium-weight black ink outline (`#111111`), expressive minimal single-stroke brows/mouth, two small solid black oval dot eyes, thin black stick limbs, solid black silhouette hand.
- `refs/user_style_ref_03_scene.png` — Night & environment Anchor: dark environment cel-shading, deep midnight-blue starry sky (`#192841` with crisp tiny white dot stars), warm orange firelight (`#F27D16`), flat hand-drawn garment layering over thin black stick limbs.

## 2. Generated STATE 4 Candidate Anchors & Exact Prompts (`refs/`)

### `refs/anchor_01_protagonist_gear.png` (Geared Protagonist + Apartment Hallway Anchor)
- **Reference Inputs**: `["apocalypse_day1_video/refs/user_style_ref_01_couch.png", "apocalypse_day1_video/refs/user_style_ref_02_pose.png", "apocalypse_day1_video/refs/user_style_ref_03_scene.png"]`
- **Exact Prompt**:
  > 2D minimalist stick-figure cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on backgrounds and props, zero 3D rendering, zero gradients, zero photorealism, zero text or watermarks, 16:9 widescreen. Full-body character shot in a dim warm-beige apartment hallway (#EBD8BE walls, #6E472B floor, closed wooden apartment door on the right, flickering small yellow ceiling bulb overhead). The protagonist is the exact minimalist stick figure from the references: large round pure-white circle head (#FFFFFF), completely bald, two small solid black oval dot eyes, simple single-stroke black eyebrows angled with alert determination, thin single-line black mouth, thin solid black stick legs and thin solid black stick arms ending in small rounded black silhouette nub hands and feet. Over the stick torso, the protagonist wears a simple flat olive-tan canvas jacket with rolled sleeves revealing grey duct-taped magazine wraps strapped snugly around both thin black stick forearms, a compact dark charcoal backpack on the shoulders, and holds a dark-grey curved steel crowbar in one black nub hand.

### `refs/anchor_02_city_outbreak_sedan.png` (Compact Grey Sedan + Urban Outbreak + Infected Rules Anchor)
- **Reference Inputs**: `["apocalypse_day1_video/refs/user_style_ref_01_couch.png", "apocalypse_day1_video/refs/user_style_ref_02_pose.png", "apocalypse_day1_video/refs/user_style_ref_03_scene.png"]`
- **Exact Prompt**:
  > 2D minimalist stick-figure cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on vehicles and buildings, zero 3D rendering, zero gradients, zero photorealism, zero text or watermarks, 16:9 widescreen. Wide urban morning outbreak scene on a muted grey city avenue: in the left foreground sits a clean compact flat-grey four-door sedan with closed doors; further up the road in the background, rows of flat-colored sedans sit bumper-to-bumper in motionless gridlock beneath thick black smoke plumes rising behind simple flat grey downtown towers under a pale hazy morning sky. Near a concrete subway stairwell entrance on the right sidewalk, three infected figures stagger crookedly—drawn in the exact same minimalist stick-figure anatomy with round chalk-pale grey-white circle heads, small hollow dark dot eyes, open single-line mouths, thin solid black stick arms and legs, and simple flat muted torn shirt sleeves, with zero gore.

### `refs/anchor_03_lookout_cabin_night.png` (Elevated Stilt Fire-Lookout Cabin + Starry Night Anchor)
- **Reference Inputs**: `["apocalypse_day1_video/refs/user_style_ref_01_couch.png", "apocalypse_day1_video/refs/user_style_ref_02_pose.png", "apocalypse_day1_video/refs/user_style_ref_03_scene.png"]` (plus 1 story-state cleanup pass removing lower post rungs and placing detached ladder flat on deck)
- **Exact Prompt**:
  > 2D minimalist stick-figure cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading, zero 3D rendering, zero gradients, zero photorealism, zero text or watermarks, 16:9 widescreen. Wide atmospheric nighttime mountain forest scene matching the exact deep navy-blue starry night sky (#192841 with crisp tiny white dot stars) of the third reference image: a rustic square brown wooden forestry fire-lookout cabin perched thirty feet high on four tall X-braced bare smooth wooden stilts above dark muted green-grey pine tree silhouettes. The detached lower wooden boarding ladder lies flat horizontally on top of the cabin's wraparound wooden deck beside the railing, leaving all four lower timber posts completely bare and unreachable from the forest floor; the deck trapdoor and wooden cabin window shutters are closed tight with zero light leaking out, and the minimalist round-white-circle-head black-stick-figure protagonist in a flat olive-tan jacket and dark backpack crouches quietly on the elevated deck holding a grey steel crowbar.

## 3. Verbatim Style & Subject Invariant Blocks (Copy Verbatim in STATE 5)
- **Verbatim Style Block**:
  `2D minimalist stick-figure cartoon illustration strictly matching the reference art style, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on backgrounds and furniture, zero 3D rendering, zero gradients, zero photorealism, zero text or watermarks, 16:9 widescreen.`
- **Verbatim Protagonist (Home — Slide 1 & Slide 2 m01–m09)**:
  `Protagonist is a minimalist stick figure with a large round pure-white circle head (#FFFFFF), bald, two small solid black oval dot eyes, simple single-stroke black line mouth and brows, thin solid black stick torso, thin solid black stick arms and legs, and rounded black nub hands and feet.`
- **Verbatim Protagonist (Geared — Slide 2 m10 through Slide 9)**:
  `Protagonist is a minimalist stick figure with a large round pure-white circle head (#FFFFFF), bald, two small solid black oval dot eyes, simple single-stroke black line mouth and brows, thin solid black stick arms and legs with rounded black nub hands and feet, wearing a flat olive-tan canvas jacket with grey duct-taped forearm wraps and a compact dark charcoal backpack.`
- **Verbatim Infected / Creature Rule**:
  `Infected figures use the exact same minimalist stick-figure anatomy with round chalk-pale circle heads, hollow dark dot eyes, tense open line mouths, crooked posture, and thin black stick limbs with flat torn sleeve accents.`
- **Palette Invariants**:
  - Apartment walls: `#EBD8BE` warm cream/beige; floors: `#6E472B` flat medium-brown; couch: `#768999` muted slate-blue; blanket: `#F2C649` mustard-yellow.
  - Protagonist jacket: flat olive-tan (`#9A8F62`); forearm tape: cool grey (`#8D9297`); backpack: dark charcoal (`#36393C`); crowbar: slate steel (`#5C646D`).
  - Sedan: compact flat neutral grey (`#A8AEB5`).
  - Foothills & Cabin: muted pine green (`#35463D`), rustic wood brown (`#6F4E37`), midnight sky (`#192841`) with crisp white dot stars (`#FFFFFF`), valley campfire (`#F27D16`).

## 4. Composition & Anchor Recipe Rules
- **Glass / Windows / Barriers**: Camera on viewer's side, figures seen from behind, hands on viewer's side of surface, interior/exterior visible through it.
- **Anchor Recipe**: Every STATE 5 `generate_image` call passes `images=[character_ref, location_ref, optional_prior_approved_frame]`, copies style/subject blocks VERBATIM from this file, and states explicit lighting + open/closed story states.

## 5. Content Moderation Log
| Blocked Term / Clause | Approved Replacement | Frame / Ref ID |
|---|---|---|
| `lunges at Marcus's shoulder with tense open mouth` | `reaches abruptly toward Marcus's blue sleeve as Marcus steps back startled` | `beat01m16` |
