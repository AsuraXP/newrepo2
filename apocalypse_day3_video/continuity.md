# Continuity & Visual Invariants — Episode 3 (`apocalypse_day3_video`)

## 1. Master Style & Carried-Forward Series References (`refs/`)
- `refs/user_style_ref_01_couch.png`, `refs/user_style_ref_02_pose.png`, `refs/user_style_ref_03_scene.png` — User's 3 canonical minimalist 2D stick-figure style references (`#FFFFFF` pure-white circle head, `#111111` uniform black ink outline, two solid black oval dot eyes, minimal single-stroke brows/mouth, thin black stick limbs, flat muted colors with single-step cel-shading).
- `refs/anchor_01_protagonist_gear.png` — Solo geared Protagonist continuity reference.
- `refs/maya_solo_ref.png` — Solo Paramedic Maya full-body continuity reference (prevents second-character bleed on solo Maya shots).
- `refs/anchor_d2_01_maya_paramedic.png` — Geared Protagonist + Paramedic Maya duo continuity reference.
- `refs/infected_crowd_ref.png` — Crooked chalk-pale (`#EAEBE6`) hollow-eyed stick-figure infected crowd continuity reference.
- `refs/day2_dam_panorama.png` & `refs/day2_ending_ridge_dam.png` — Clearwater Dam curved pale-grey concrete wall & mountain reservoir continuity references from Episode 2's ending.

## 2. Generated Day Three STATE 4 Anchors & Exact Prompts (`refs/`)

### `refs/anchor_d3_01_red_parka_scavengers.png` (Hostile Red-Parka Scavengers + High Steel Dam Catwalk)
- **Reference Inputs**: `["apocalypse_day3_video/refs/anchor_01_protagonist_gear.png", "apocalypse_day3_video/refs/user_style_ref_02_pose.png", "apocalypse_day3_video/refs/day2_dam_panorama.png"]`
- **Exact Prompt**:
  > 2D minimalist stick-figure cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on backgrounds and clothing, zero 3D rendering, zero gradients, zero photorealism, zero text, zero letters, 16:9 widescreen. Full-body two-character antagonist reference shot on an elevated grey steel grating dam catwalk lined with olive-tan sandbags high on the pale-grey concrete dam wall in cool grey morning light: standing behind the sandbags are TWO hostile scavengers drawn in the exact same minimalist stick-figure anatomy as the first two references — large round solid flat pure-white (#FFFFFF) circle heads with zero skin tint, TWO SMALL SOLID BLACK OVAL DOT EYES (strictly solid black dots with zero white sclera rings), sharp scowling single-stroke black brows and tense line mouths, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and dark boots, wearing flat muted dark-red hooded parkas (#8E3532) and snug dark charcoal knit beanies (#2B2E33). The left scavenger rests a simple flat-black hunting rifle horizontally sideways across the top of the sandbags (not aimed at viewer) while the right scavenger stands beside a neat pile of three stolen hiking backpacks on the steel grating, strictly TWO characters total.

### `refs/anchor_d3_02_concrete_drainage_tunnel.png` (Character-Free Dam Concrete Drainage Gallery, Brass Valve & Bulkhead Door)
- **Reference Inputs**: `["apocalypse_day3_video/refs/user_style_ref_01_couch.png", "apocalypse_day3_video/refs/user_style_ref_03_scene.png"]`
- **Exact Prompt**:
  > 2D minimalist cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on concrete walls and pipes, zero 3D rendering, zero gradients, zero photorealism, zero text, zero letters, 16:9 widescreen. Atmospheric character-free interior architecture reference down a narrow damp cool-grey concrete inspection drainage tunnel inside a hydroelectric dam: shallow ankle-deep dark slate water covers the floor with subtle pale-green reflections (#76C893); heavy bolted dark-grey iron water pipes run horizontally along the right concrete wall; on the left wall sits a circular tarnished brass overflow valve wheel (#B08D57) right above a recessed iron bar floor culvert grate; at the far end of the corridor stands a heavy grey steel bulkhead door with a central circular dogging wheel and a plain white upward arrow stencil (strictly zero words or letters, strictly zero people in frame).

### `refs/anchor_d3_03_reservoir_boathouse_pier.png` (Character-Free Reservoir Pier, Grey Transformers, Chained Aluminum Boat & Pine Island)
- **Reference Inputs**: `["apocalypse_day3_video/refs/user_style_ref_01_couch.png", "apocalypse_day3_video/refs/user_style_ref_03_scene.png", "apocalypse_day3_video/refs/day2_dam_panorama.png"]`
- **Exact Prompt**:
  > 2D minimalist cartoon illustration strictly matching the exact art style of the reference images, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on buildings, boat, and mountains, zero 3D rendering, zero gradients, zero photorealism, zero text, zero letters, 16:9 widescreen. Wide morning mountain reservoir shoreline reference scene beside the upper edge of the pale-grey concrete dam: on the left sit three boxy grey industrial power transformers (#6E747C) and a weathered grey corrugated-metal boathouse shed on a concrete-and-timber pier; floating against black rubber dock bumpers on the right sits a rugged unpainted silver-grey aluminum utility motorboat (#9EA6AE) with wooden bench seats and a compact black rear outboard motor, chained at its bow by an iron link chain and rusted brass padlock (#B08D57) to a brown wooden dock piling; out across the misty calm dark slate-blue mountain reservoir lake rises an isolated dark-green pine-covered island (#35463D) with a tiny wooden ranger cabin, strictly zero people in frame.

## 3. Verbatim Style & Subject Invariant Blocks (Copy Verbatim in STATE 5)
- **Verbatim Style Block**:
  `2D minimalist stick-figure cartoon illustration strictly matching the reference art style, clean medium-weight uniform black ink outlines (#111111) with subtle hand-drawn feel, flat muted colors with minimal simple single-step cel-shading on backgrounds and furniture, zero 3D rendering, zero gradients, zero photorealism, zero text or watermarks, 16:9 widescreen.`
- **Verbatim Protagonist (`CHAR_PROTAG`)**:
  `Protagonist is a minimalist stick figure with a large round solid flat pure-white (#FFFFFF) circle head with zero peach or beige tint, bald, two small solid black oval dot eyes (strictly solid black dots with zero white sclera rings), simple single-stroke black line mouth and brows, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and brown boots, wearing a flat olive-tan canvas jacket (#9A8F62) with rolled cuffs meeting grey duct-taped forearm wraps (#8D9297) and a compact dark charcoal backpack (#36393C).`
- **Verbatim Maya (`CHAR_MAYA`)**:
  `Maya is a minimalist stick figure with a large round solid flat pure-white (#FFFFFF) circle head with zero peach or beige tint, short dark-black tied-back ponytail drawn in crisp black stick strands, two small solid black oval dot eyes (strictly solid black dots with zero white sclera rings), expressive single-stroke brows and line mouth, EXACTLY TWO thin solid black stick arms and legs with rounded black nub hands and dark boots, wearing a flat faded slate-blue paramedic jacket (#4F6D8A) with a tiny plain white cross shoulder patch and a compact red medical trauma bag (#A63D38) with a tiny white cross icon slung diagonally across her chest.`
- **Verbatim Hostile Scavengers (`CHAR_SCAV`)**:
  `Hostile scavengers use the exact same minimalist stick-figure anatomy with large round solid flat pure-white (#FFFFFF) circle heads, two small solid black oval dot eyes (zero white sclera), sharp scowling single-stroke brows, thin solid black stick limbs with black nub hands and dark boots, wearing flat muted dark-red hooded parkas (#8E3532) and dark charcoal knit beanies (#2B2E33).`
- **Verbatim Infected (`CHAR_INFECTED`)**:
  `Infected figures use the exact same minimalist stick-figure anatomy with round chalk-pale circle heads (#EAEBE6), hollow dark dot eyes, tense open line mouths, crooked posture, and thin black stick limbs.`
- **Palette Invariants**:
  - Protagonist: `#FFFFFF` head, `#9A8F62` olive-tan jacket, `#8D9297` grey forearm wraps, `#36393C` dark backpack, `#5C646D` curved steel crowbar.
  - Maya: `#FFFFFF` head, `#4F6D8A` slate-blue paramedic jacket, `#A63D38` red cross trauma bag, `#76C893` pale-green chemical glow stick.
  - Scavengers: `#FFFFFF` head, `#8E3532` dark-red hooded parka, `#2B2E33` dark charcoal knit beanie.
  - Dam & Boat Environments: `#C9B04E` muted-yellow utility vests (yard infected), `#5A5343` olive-brown rubber waders (tunnel technician), `#B08D57` brass binoculars/valve/padlock, `#6E747C` grey transformers, `#9EA6AE` unpainted aluminum motorboat.

## 4. Composition & Anchor Recipe Rules
- **Solo vs. Duo Character Refs**: Use `anchor_01_protagonist_gear.png` on solo Protagonist shots, `maya_solo_ref.png` on solo Maya shots, and `anchor_d2_01_maya_paramedic.png` ONLY on two-character Protagonist+Maya shots (prevents extra character bleed).
- **Character-Free Shots**: Pass ONLY character-free scene anchors (`day2_dam_panorama.png`, `anchor_d3_02_concrete_drainage_tunnel.png`, `anchor_d3_03_reservoir_boathouse_pier.png`) on empty landscape/object shots.
- **Firearms & Action Framing**: Always frame the scavenger's hunting rifle in side-profile or angled diagonally toward the boathouse roof/sandbags — never pointed toward the camera.

## 5. Content Moderation Log (Carried Forward + Episode 3)
| Blocked Term / Clause | Approved Replacement | Frame / Ref ID |
|---|---|---|
| `lunges at [character]'s shoulder with tense open mouth` | `reaches abruptly toward [character]'s sleeve as [character] steps back startled` | `day1:beat01m16` |
| `point the tip of his silver-grey aluminum baseball bat straight toward the windshield` | `stands blocking the lane, holding a silver-grey cylindrical sports bat raised diagonally in one stick hand toward the car hood while gesturing palm-out with his other stick hand to stop` | `day1:beat06m07` |
