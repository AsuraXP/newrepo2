# WORKER ASSIGNMENT 3 — The Rewilding

- Branch: `git checkout -b rewilding-worker-3` (from arena/c251d7fe-newrepo2)
- Target CSV: `rewilding_video/visuals.csv` — **Assigned rows 224 to 335** (112 frames to generate)
- Slides covered: 10, 11, 12, 13, 14, 15
- Output dir: `rewilding_video/frames/` — filename `beat{slide:02d}m{moment:02d}.png` (already encoded in the table below)
- Batch: **6 frames per turn**, repair budget **R=2 per turn** (re-roll changing ONE clause only)
- QC each frame: shows its moment_text? invariants intact? no melted limbs/merged faces/gibberish text? Reject → name the fault, re-roll, ≤3 tries then ship closest as DECLARED EXCEPTION (log in STATE.md).
- Contact sheet of every batch (~380px thumbs, rejects included). Commit + push branch after EVERY batch.
- Pacing: each frame holds for the exact spoken duration of its moment_text; word-level TTS timestamps place cuts — never hand-place durations

## LOCKED STYLE & CHARACTER (copy/paste VERBATIM into every prompt)

**Style & Medium:**
Hand-drawn 2D stick-figure cartoon — thick wobbly black ink outlines, round white head, dot eyes with expressive black brows, thin black stick body and limbs with small oval hands and simple stick feet, painterly gouache-style brush shading with subtle film grain, warm-cool color separation (amber practical light vs cold blue-gray mist), muted earthy palette, high-contrast readable silhouettes, no photorealism, no 3D render, no anime.

**Protagonist
round white head, three-strand hair sprig under a weathered olive wide-brim hat, heavy-lidded tired dot eyes under straight brows; thin black oval torso; STICK arms and legs with oval hands and flat stick feet; olive-green ranger vest over charcoal shirt, olive trousers, small olive backpack, chest tag reading SECTOR SEVEN, brass tally counter on belt; dart gun holstered, ALWAYS with the red UNFIRED tape intact; dark boots.

**The calf
round white head, smaller than adult hands, single hair sprig, huge bright dot eyes, enormous brave smile; oversized red flannel work jacket with painted-on check/plaid, sleeves rolled and cupped over her hands; tiny stick limbs; barefoot. NEVER shown older than two. NEVER harmed.

**The turned
round pale blue-gray heads, blank soft-white dot eyes (never red), tattered layered coats in ash gray, slate and bark brown, hunched posture, heels dragging toe-clawing gait; move ONLY at a slow walk; NEVER run, NEVER speak, NEVER attack. No wounds, no blood, no rot — always weathered and dry.

## INSTRUCTIONS
1. Pull branch, open `visuals.csv` (rows pre-numbered in the table below for convenience), load `refs/`.
2. For EVERY assigned row: image prompt = [visual_prompt] + [LOCKED STYLE & CHARACTER verbatim above]. Attach character_ref whenever ranger/calf/herd appears.
3. Attach location_ref ONLY while the beat occurs in the same continuous setting. When the setting changes (see Slides column), DROP location_ref and generate a fresh background in the locked style.
4. Camera LOCKED OFF — no Ken Burns/zoom/drift. Fire/candle = warm light only. No text beyond diegetic signage ≤5 words. Wanderers never run, never red-eye, never glow.

## ASSIGNED FRAMES — 112 prompts

| # | frame file | moment_text | visual_prompt |
|---|---|---|---|
| 224 | beat10m15.png | You have a radio. | close-up: the radio on the belt, mic button worn shiny with thumbs |
| 225 | beat10m16.png | You have a rule. | close-up: the manual open on a palm — Rule 1: OBSERVE. DO NOT INTERFERE. |
| 226 | beat11m01.png | You climb down from the ridge. | wide: figure picking down the shale slide, arms out for balance |
| 227 | beat11m02.png | You do not aim the gun. | close-up: a hand hovering over the dart gun grip — not drawing |
| 228 | beat11m03.png | You never even draw it. | close-up: an empty holster snap flicked open |
| 229 | beat11m04.png | You walk into the open with your hands loose at your sides, | wide: figure walking into the open meadow, hands loose at the sides |
| 230 | beat11m05.png | and the herd stops. | wide: the herd stops — dozens of legs halting as one |
| 231 | beat11m06.png | Eleven heads come around. | close-up: eleven heads come around, slow and level |
| 232 | beat11m07.png | That tidal gait halts. | wide: the halt rippling down the line — a wave on a sea wall |
| 233 | beat11m08.png | The forest goes so quiet you can hear the creek. | wide total silence: only the creek, no birds anywhere |
| 234 | beat11m09.png | And then the small shape in the flannel jacket turns, | direct view: the small shape in flannel spins to face the figure |
| 235 | beat11m10.png | and looks at you with eyes that have never known a wall, | close-up: her upturned face — eyes wide, zero fear in them |
| 236 | beat11m11.png | and does the one thing nobody has done at you in nine years. | close-up: same eyes building to something enormous |
| 237 | beat11m12.png | She smiles. | close-up: her smile breaks across her whole face |
| 238 | beat11m13.png | You are fifty yards closer. | medium wide: figure advancing slowly — fifty yards of open meadow |
| 239 | beat11m14.png | Thirty. | close-up: eyes narrowed, calm measured steps, breath even |
| 240 | beat11m15.png | You do not run. | medium: figure low in a coiled stance — not charging, never charging |
| 241 | beat11m16.png | You do not shout. | close-up: mouth closed, words shaped without volume |
| 242 | beat11m17.png | You talk, | medium: figure crouching into a parent's stance, palms open |
| 243 | beat11m18.png | the way the manual says you must never talk in the field — | close-up: the manual's corner poking from the vest pocket — Rule 1 showing |
| 244 | beat11m19.png | you talk like a person, | close-up: lips moving against warm backlight |
| 245 | beat11m20.png | because you are a person | close-up: her huge pupils filling with him |
| 246 | beat11m21.png | and she should learn it. | close-up: her absorbing him like gospel, utterly without walls |
| 247 | beat11m22.png | You tell her your name. | close-up: his face level with hers, close and gentle |
| 248 | beat11m23.png | You tell her the sky is real. | medium: he points straight up at the racing clouds |
| 249 | beat11m24.png | You tell her the water is coming up | close-up: her face tipping skyward, awed |
| 250 | beat11m25.png | and you are going to help her over. | close-up: one open palm extended — an offering, not a reach |
| 251 | beat12m01.png | The herd watches. | wide: the herd holds still — eleven statues mid-turn |
| 252 | beat12m02.png | The herd does not advance. | medium wide: turners motionless, heads tilted like curious deer |
| 253 | beat12m03.png | The herd does not flee. | close-up: a turner blinking once, long and slow |
| 254 | beat12m04.png | They turn, | wide: eleven turners rotating east as one body |
| 255 | beat12m05.png | slowly, | close-up: one bare foot planting uphill on shale |
| 256 | beat12m06.png | all of them, | wide: the pivot — slow as a season changing |
| 257 | beat12m07.png | the way they turn at the season, | wide: golden light on the ridge behind them, the year turning |
| 258 | beat12m08.png | and they begin — | wide: first eastward steps — unhurried, unanimous |
| 259 | beat12m09.png | not toward you, | wide: the column moving — not one step toward the figure |
| 260 | beat12m10.png | not away from you — | wide: the column tracking the contour — not fleeing either |
| 261 | beat12m11.png | they begin toward the high ground, | wide: the column stringing out toward the rocky shoulder of the ridge |
| 262 | beat12m12.png | up the rocky spine the old survey maps call Hawk's Back, | wide: Hawk's Back — a dark rocky spine against the dawn sky |
| 263 | beat12m13.png | where the water cannot reach. | wide: the spine high and dry above the brown flood line |
| 264 | beat12m14.png | And you understand, | close-up: figure's face registering something enormous |
| 265 | beat12m15.png | standing there in the cold with your heart hammering, | close-up: chest heaving, high color flooding his round cheeks |
| 266 | beat12m16.png | that they are not attacking. | same face — impossibility breaking loose: not an attack |
| 267 | beat12m17.png | They are not retreating. | same face — not a retreat either — something older |
| 268 | beat12m18.png | They are leading. | wide: the column cresting Hawk's Back — leading, unmistakably leading |
| 269 | beat13m01.png | The calf does not understand roads. | close-up: the toddler's head pivoting toward the moving column |
| 270 | beat13m02.png | She understands the herd. | close-up: her eyes tracking them, deciding |
| 271 | beat13m03.png | She takes three unsteady steps after them, | low angle: flannel hem sweeping, sneakers tipping on shale |
| 272 | beat13m04.png | up the shale. | close-up: one small shoe coming down on a loose stone |
| 273 | beat13m05.png | And you — | medium: figure frozen mid-gesture, arm still out |
| 274 | beat13m06.png | you sit down in the mud, | wide: figure dropping straight down, sitting hard in the mud |
| 275 | beat13m07.png | and you laugh, | close-up: a laugh cracking through wet cheeks |
| 276 | beat13m08.png | and you cry, | close-up: simple tear streaks on a round white head |
| 277 | beat13m09.png | and you do not follow, | medium: figure with fists open on his knees, emptied out |
| 278 | beat13m10.png | because some part of you, | wide from behind: figure small in the meadow, the herd tiny on the ridge |
| 279 | beat13m11.png | the part that has been a clerk for nine years, | close-up: a torn brochure scrap in the mud, the missing page |
| 280 | beat13m12.png | knows you cannot walk a child out of the wilderness into a world that has a page missing. | close-up: open hands flat on knees — empty, and knowing it |
| 281 | beat13m13.png | You climb back to the ridge. | wide: figure scrambling up the shale route, far behind them |
| 282 | beat13m14.png | You watch them cross Hawk's Back as the water takes the low ground behind them. | wide: the column crossing Hawk's Back, flood swallowing the low ground behind |
| 283 | beat13m15.png | You watch the flannel jacket disappear into the fog above the timberline, | wide: a red flannel dot swallowed by fog above the timberline |
| 284 | beat13m16.png | eleven shadows | close-up: eleven distant shadows strung along the spine |
| 285 | beat13m17.png | and one small light, | close-up: one warm red-plaid ember of motion among the gray |
| 286 | beat13m18.png | all walking the same tide-road east. | wide: all of them shrinking east into fog, one by one gone |
| 287 | beat14m01.png | That evening you key the radio. | medium: dusk porch — the figure lifts the radio handset |
| 288 | beat14m02.png | Your voice is very calm. | close-up: face lit low amber by the porch bulb — utterly calm |
| 289 | beat14m03.png | "Base. | close-up: the handset grille, voice flat and even |
| 290 | beat14m04.png | Sector Seven. | medium: same hand steady on the handset, wind stirring the porch |
| 291 | beat14m05.png | Count complete at the crossing. | close-up: ledger page — COUNT COMPLETED — typed header |
| 292 | beat14m06.png | Eleven confirmed, | close-up: pen writing ELEVEN CONFIRMED, |
| 293 | beat14m07.png | heading northeast, | same hand writing heading northeast, |
| 294 | beat14m08.png | condition good." A pause. | same hand finishing condition good. — pen stopping mid-line |
| 295 | beat14m09.png | "Eleven? | radio burst — static crackle from the grille |
| 296 | beat14m10.png | Last month you logged eleven." | close-up: the handset silent in the amber light, waiting for the reply |
| 297 | beat14m11.png | "Confirmed," you say. | medium: breath moving in, out — slow and deliberate |
| 298 | beat14m12.png | "Same eleven." Another pause, | close-up: crickets on the porch rail, legs jumping |
| 299 | beat14m13.png | longer. | same stillness stretched — fireflies rising over the yard |
| 300 | beat14m14.png | Then: | close-up: a finger hovering near the cradle hook — not hanging up |
| 301 | beat14m15.png | "Copy, | close-up: the handset lowering slow — Base's voice breaking in |
| 302 | beat14m16.png | Sector Seven. | close-up: the ledger, pen hanging above it — pause mid-sentence |
| 303 | beat14m17.png | Ledger updated. | close-up: stamp coming down — LEDGER UPDATED |
| 304 | beat14m18.png | Base out." | medium: figure at the rail, the yard going black around him |
| 305 | beat15m01.png | You sit on the porch of the station as the dark comes down, | wide: the station silhouette against violet dusk, porch bulb one warm eye |
| 306 | beat15m02.png | and the first stars come out over a country that forgot itself | close-up: first stars piercing the dark over the ridgeline |
| 307 | beat15m03.png | and grew back anyway, | wide: arms of night opening over a country that forgot itself |
| 308 | beat15m04.png | green over concrete, | wide: same hills gone gentle, grass over concrete ghosts |
| 309 | beat15m05.png | deer in the parking lots, | close-up: deer browsing the rust husk of a parking-lot sedan |
| 310 | beat15m06.png | trumpet vine up the overpasses, | close-up: trumpet vine spilling over an overpass rail |
| 311 | beat15m07.png | and somewhere east of here, | wide: eastern horizon glow — the direction of all walking |
| 312 | beat15m08.png | walking, | wide: eastern fog with a tiny figure-shape mid-march, ghost-image shimmer |
| 313 | beat15m09.png | a child who belongs to the last wild thing that remembers how to keep a calf. | through memory: one red flannel center — pendulum of stolen cloth |
| 314 | beat15m10.png | You do not know her name. | close-up: open hands, at rest and empty — no name known, none needed |
| 315 | beat15m11.png | You are her ranger. | close-up: the ranger patch over his heart, worn soft with nine years |
| 316 | beat15m12.png | You will come back in the spring. | close-up: wall calendar — SPRING circled hard in red grease pencil |
| 317 | beat15m13.png | Because that is what the Rewilding Authority | close-up: AUTHORITY brochure cover — heron emblem, REWILDING |
| 318 | beat15m14.png | never got around to printing on the brochures: | close-up: the brochure's blank back page, gloss gone dull |
| 319 | beat15m15.png | the wild does not decide what is broken. | close-up: a fern spear punching through cracked asphalt — life wins |
| 320 | beat15m16.png | It only decides what survives. | close-up: a droplet falling leaf to leaf, morning world reborn |
| 321 | beat15m17.png | And sometimes, | wide: the tide-road east at dawn, fog rolling slow as surf |
| 322 | beat15m18.png | walking the slow tide-road through the green, | wide: the slow tide of dark shapes drifting over green ridges |
| 323 | beat15m19.png | survival looks like eleven of the dead, | wide: eleven silhouettes on the far ridge, backlit by cracked dawn |
| 324 | beat15m20.png | and one living girl in a stolen jacket, | through memory: one red flannel center — the only warm note on the ridge |
| 325 | beat15m21.png | and a man on a ridge pretending very hard not to cry. | wide reversal: from the herd's side — a tiny man-shape on the far ridge |
| 326 | beat15m22.png | Your radio clicks. | wide: dawn porch rail, the radio clicking on all by itself into morning |
| 327 | beat15m23.png | Base, | medium: figure back at the rail at daybreak, coffee untouched |
| 328 | beat15m24.png | one more time. | close-up: the handset rising again toward the face |
| 329 | beat15m25.png | "Sector Seven. | close-up: the eastern ridge again — blank and patient |
| 330 | beat15m26.png | Confirm — | close-up: the same ridge — fog swelling out and in, breathing slow |
| 331 | beat15m27.png | same eleven?" You look at the eastern hills. | wide: fog folding over the ridge like a long exhale |
| 332 | beat15m28.png | The fog moves over them like a breath. | same fog close in — one held heartbeat of white |
| 333 | beat15m29.png | "Same eleven," you say. | close-up: mouth close to the grille, words barely spoken |
| 334 | beat15m30.png | And you leave the channel open, | close-up: handset set gently on the rail — channel light left green and open |
| 335 | beat15m31.png | in case she ever needs to hear a human voice say her own name back to her. | wide: the station alone under a spill of stars, one window warm and gold |
