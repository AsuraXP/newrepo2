# Continuity & Visual Invariants — Episode 2 (`apocalypse_day2_video`)

## 1. Master Style & Carried-Forward Day One References (`refs/`)
- `refs/user_style_ref_01_couch.png`, `refs/user_style_ref_02_pose.png`, `refs/user_style_ref_03_scene.png` — User's 3 canonical minimalist 2D stick-figure style references (`#FFFFFF` pure-white circle head, `#111111` uniform black ink outline, two solid black oval dot eyes, minimal single-stroke brows/mouth, thin black stick limbs, flat muted colors with single-step cel-shading).
- `refs/anchor_01_protagonist_gear.png` — Geared Day One survivor continuity reference.
- `refs/anchor_03_lookout_cabin_night.png` & `refs/day1_ending_cabin.png` — Elevated 30-foot stilt forestry fire-lookout cabin exterior & interior (bunk cot, storm shutters, iron woodstove, overhead wooden roof-vent hatch, slate-grey wool blanket).

## 2. Generated Day Two STATE 4 Anchors & Exact Prompts (`refs/`)

### `refs/anchor_d2_01_maya_paramedic.png` (Geared Protagonist + County Paramedic Maya Duo Anchor)
- **Reference Inputs**: `["apocalypse_day2_video/refs/anchor_01_protagonist_gear.png", "apocalypse_day2_video/refs/user_style_ref_02_pose.png", "apocalypse_day2_video/refs/user_style_ref_03_scene.png"]`
- **Exact Prompt**:
  > 2D minimalist stick-figure cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on backgrounds and clothing, zero 3D rendering, zero gradients, zero photorealism, zero text, zero letters, 16:9 widescreen. Full-body two-character survival duo reference shot on a misty mountain pine forest trail (#35463D pines, muted brown dirt path): on the left stands the exact geared minimalist stick-figure protagonist from the first reference (large round solid pure-white #FFFFFF circle head, bald, two small solid black oval dot eyes, determined single-stroke brows and line mouth, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and brown boots, wearing his flat olive-tan canvas jacket #9A8F62 with grey duct-taped forearm wraps #8D9297, compact dark charcoal backpack #36393C, holding his curved dark-grey steel crowbar #5C646D). Standing beside him on the right is county paramedic Maya drawn in the exact same minimalist stick-figure anatomy: large round solid pure-white circle head (#FFFFFF) with zero skin tint, short dark-black hair tied back in a neat crisp black stick-strand ponytail, two small solid black oval dot eyes, alert single-stroke brows and line mouth, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and dark boots, wearing a flat faded slate-blue paramedic jacket (#4F6D8A) with a tiny plain white medical cross patch on the shoulder (strictly zero words or letters) and a compact muted-red medical trauma bag (#A63D38) with a tiny white cross icon slung diagonally across her chest.

### `refs/anchor_d2_02_ranger_quad.png` (Green-Roofed Forestry Ranger Station + Olive Utility Quad Bike Anchor)
- **Reference Inputs**: `["apocalypse_day2_video/refs/user_style_ref_01_couch.png", "apocalypse_day2_video/refs/user_style_ref_03_scene.png", "apocalypse_day2_video/refs/anchor_03_lookout_cabin_night.png"]` (plus 1 story-state edit stowing the twin perforated steel loading ramps horizontally beneath the rear cargo rack)
- **Exact Prompt**:
  > 2D minimalist cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on buildings and vehicle, zero 3D rendering, zero gradients, zero photorealism, zero text, zero letters, zero signs, 16:9 widescreen. Wide morning mountain forest clearing scene surrounded by tall muted-green pine trees (#35463D): on the left stands a rustic tan-plank and log forestry ranger station cabin with a pitched dark forest-green metal roof (#2F5241), a tilted dark-blue rooftop solar panel, and a wooden front porch with a plain pine-tree emblem plaque (strictly zero words or letters); on the right inside a fenced gravel equipment yard with a padlocked chain-link gate sits a rugged flat olive-drab four-wheel utility quad ATV (#5B6347) with black knobby tires, black tubular front and rear cargo racks, and two flat silver-grey perforated steel loading ramps (#8C949C) stowed horizontally right underneath the rear cargo rack, zero people in frame.

### `refs/anchor_d2_03_gorge_bridge.png` (Twin Creek Gorge + Broken Suspension Footbridge + Distant Dam Anchor)
- **Reference Inputs**: `["apocalypse_day2_video/refs/user_style_ref_01_couch.png", "apocalypse_day2_video/refs/user_style_ref_03_scene.png", "apocalypse_day2_video/refs/anchor_03_lookout_cabin_night.png"]`
- **Exact Prompt**:
  > 2D minimalist cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on canyon cliffs and bridge, zero 3D rendering, zero gradients, zero photorealism, zero text, zero letters, 16:9 widescreen. Dramatic wide afternoon mountain canyon landscape: Twin Creek Gorge cuts eighty feet deep between sheer grey-brown granite cliff walls down to churning white-foaming slate-blue rapids below; spanning the canyon from left to right hangs an old weathered brown wooden plank suspension footbridge hung from dark steel cables between wooden end posts, with a fresh rockslide having smashed a clean five-foot-wide open gap completely missing wooden planks near the far right cliff ledge; miles away on the northern pine horizon gleams a clean pale-grey concrete hydroelectric dam wall holding back calm dark mountain water, zero people in frame.

## 3. Verbatim Style & Subject Invariant Blocks (Copy Verbatim in STATE 5)
- **Verbatim Style Block**:
  `2D minimalist stick-figure cartoon illustration strictly matching the reference art style, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on backgrounds and furniture, zero 3D rendering, zero gradients, zero photorealism, zero text or watermarks, 16:9 widescreen.`
- **Verbatim Protagonist (`CHAR_PROTAG`)**:
  `Protagonist is a minimalist stick figure with a large round solid flat pure-white (#FFFFFF) circle head with zero peach or beige tint, bald, two small solid black oval dot eyes, simple single-stroke black line mouth and brows, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and brown boots, wearing a flat olive-tan canvas jacket (#9A8F62) with grey duct-taped forearm wraps (#8D9297) and a compact dark charcoal backpack (#36393C).`
- **Verbatim Maya (`CHAR_MAYA`)**:
  `Maya is a minimalist stick figure with a large round solid flat pure-white (#FFFFFF) circle head with zero peach or beige tint, short dark-black tied-back ponytail drawn in crisp black stick strands, two small solid black oval dot eyes, expressive single-stroke brows and line mouth, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and dark boots, wearing a flat faded slate-blue paramedic jacket (#4F6D8A) with a tiny plain white cross shoulder patch and a compact red medical trauma bag (#A63D38) with a tiny white cross icon slung diagonally across her chest.`
- **Verbatim Infected (`CHAR_INFECTED`)**:
  `Infected figures use the exact same minimalist stick-figure anatomy with round chalk-pale circle heads (#EAEBE6), hollow dark dot eyes, tense open line mouths, crooked posture, and thin black stick limbs with flat torn sleeve accents.`
- **Palette Invariants**:
  - Protagonist: `#FFFFFF` head, `#9A8F62` olive-tan jacket, `#8D9297` grey forearm tape, `#36393C` dark backpack, `#5C646D` curved steel crowbar.
  - Maya: `#FFFFFF` head, `#111111` black stick ponytail, `#4F6D8A` faded slate-blue paramedic jacket, `#A63D38` red trauma bag.
  - Vehicles & Props: `#5B6347` olive utility quad ATV, `#8C949C` perforated silver-grey steel loading ramps, `#2F5241` green ranger roof, `#35463D` mountain pines.

## 4. Composition & Anchor Recipe Rules
- **Glass / Windows / Barriers**: Camera on viewer's side, figures seen from behind, hands on viewer's side of surface, interior/exterior visible through it.
- **Character-Free Shots**: Pass ONLY character-free scene anchors on empty landscape/object shots (`anchor_d2_02`, `anchor_d2_03`) so extra stick figures never bleed into empty environments.
- **Anchor Recipe**: Every STATE 5 `generate_image` call passes `images=[character_ref, location_ref, optional_prior_approved_frame]`, copies style/subject blocks VERBATIM from this file, and states explicit lighting + open/closed/bolted story states.

## 5. Content Moderation Log (Carried Forward + Episode 2)
| Blocked Term / Clause | Approved Replacement | Frame / Ref ID |
|---|---|---|
| `lunges at [character]'s shoulder with tense open mouth` | `reaches abruptly toward [character]'s sleeve as [character] steps back startled` | `day1:beat01m16` |
| `point the tip of his silver-grey aluminum baseball bat straight toward the windshield` | `stands blocking the lane, holding a silver-grey cylindrical sports bat raised diagonally in one stick hand toward the car hood while gesturing palm-out with his other stick hand to stop` | `day1:beat06m07` |
