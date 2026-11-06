# WORKER ASSIGNMENT 3 — The Rewilding

- Worker: branch `rewilding-worker-3`
- Target CSV: `rewilding_video/visuals.csv` — **Assigned rows 169 to 252** (84 frames to generate)
- Slides covered: 7, 8, 9, 10, 11, 12
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

## ASSIGNED FRAMES — 84 prompts

| # | frame file | moment_text | visual_prompt |
|---|---|---|---|
| 169 | beat07m24.png | and the team would do what teams do, | wide daydream: hazy ranger trucks pulling up at the crossing, light shimmer |
| 170 | beat07m25.png | and the ledger would close over this like water over a stone. | close-up: the ledger slamming shut — motion blur, black cover |
| 171 | beat07m26.png | You tell yourself a dozen other things. | montage: a burning scrap of tally sheet curling in the stove flame |
| 172 | beat07m27.png | The truth is simpler. | close-up: nine ledger spines lined on a shelf — YEAR 1 through YEAR 9 |
| 173 | beat07m28.png | You have spent nine years cataloguing things that cannot be helped, | close-up: nine years in the eyes — canyon lines, flat calm |
| 174 | beat07m29.png | and you are so tired, | same eyes, fire-gleam small and steady |
| 175 | beat07m30.png | so tired, | close-up: jaw set — a private resolve taking shape |
| 176 | beat07m31.png | and this is the first thing in nine years that might be helped. | close-up: the photo pressed against the chest, held like a coal |
| 177 | beat08m01.png | You follow the herd. | wide: figure tucking the photo away, turning east toward the trail |
| 178 | beat08m02.png | It is not hard. | wide: the herd plain ahead in morning sun, unhurried, unhidden |
| 179 | beat08m03.png | They are not hiding. | medium: figure lowering from the ridge into the boulder-dotted basin |
| 180 | beat08m04.png | They move at the pace of growing things, | wide: the herd along the old rail grade, vines falling like curtains |
| 181 | beat08m05.png | east along the old rail line, | wide: the rail line curving east into pine forest, fog bank waiting |
| 182 | beat08m06.png | into the upper valley where the fog never quite lifts | wide: the upper valley wall of fog, light gone milky |
| 183 | beat08m07.png | and the trees grow so close their trunks touch. | close-up: parallel trunks almost touching overhead, a cathedral nave |
| 184 | beat08m08.png | You keep to the ridge. | wide: the ridge spine above the valley, figure a lone dot on skyline |
| 185 | beat08m09.png | You watch through the binoculars. | close-up: binocular circle — the herd below, small and deliberate |
| 186 | beat08m10.png | You log nothing. | close-up: logbook tucked away, pencil unused behind one ear |
| 187 | beat09m01.png | On the second day you see it with your own eyes, | wide: second day, high golden light, figure set up at the scope |
| 188 | beat09m02.png | through the glasses, | close-up: scope lenses catching sun, a hard glint |
| 189 | beat09m03.png | from three hundred yards. | wide: three hundred yards of open slope between figure and herd |
| 190 | beat09m04.png | The calf walking. | through the scope: toddler legs in red flannel hem, first wobbling gait |
| 191 | beat09m05.png | Swaying, | through the scope: sway and windmill arms, deep concentration |
| 192 | beat09m06.png | toddling, | close-up through scope: a scrunched face, furious with effort |
| 193 | beat09m07.png | furious, | same face, the rage-cute determination right at the center |
| 194 | beat09m08.png | alive. | close-up through scope: eyes bright, blazing, undeniably alive |
| 195 | beat09m09.png | A girl, | through the scope: a tiny body drowning in the oversized jacket |
| 196 | beat09m10.png | maybe two years old, | close-up through scope: flannel collar past the chin, sleeves cupped over hands |
| 197 | beat09m11.png | wrapped in a flannel jacket too big for anyone living. | medium through scope: still wobbling upright against the world |
| 198 | beat09m12.png | The herd walks around her the way a river moves around a stone. | through the scope: the herd arcing around her like a river around a stone |
| 199 | beat09m13.png | The turners do not touch her. | through the scope: nearest turner walking wide of her, giving no notice at all |
| 200 | beat09m14.png | They do not seem to see her as food, | through the scope: dead eyes fixed forward, steps never breaking rhythm |
| 201 | beat09m15.png | or as threat, | through the scope: nothing in her posture registers as threat to them |
| 202 | beat09m16.png | or as anything. | through the scope: nothing registers as anything — equal, blank regard |
| 203 | beat09m17.png | They see her the way geese see a borrowed gosling. | wide real view: geese high above in a V over the fog line |
| 204 | beat09m18.png | A thing in the middle of the flock that must be moved, | through the scope: three turners forming a moving flank beside her |
| 205 | beat09m19.png | kept, | through the scope: the flock tightening around her like migrating geese |
| 206 | beat09m20.png | carried, | through the scope: a subtle course-correction rippling through the herd |
| 207 | beat09m21.png | and not lost. | through the scope: the whole formation working as one body |
| 208 | beat09m22.png | You lower the binoculars | medium: the binoculars lowering, slow and trembling |
| 209 | beat09m23.png | and your hands are shaking. | close-up: white-knuckled fingers shaking on rubber armor |
| 210 | beat10m01.png | The river is rising. | wide: the river valley — swollen brown water, dam-break debris strung high |
| 211 | beat10m02.png | The upstream dam failed in the spring, | close-up: corkboard memo — DAM BREACH SPRING — DO NOT FORD THIS CROSSING |
| 212 | beat10m03.png | everyone knows it, | close-up: the same memo, tape corners curling, coffee ring at the corner |
| 213 | beat10m04.png | Base reminds everyone every week. | medium: the radio on the desk mid-announcement, flashback tint, static |
| 214 | beat10m05.png | The crossing the herd is making for | wide: the crossing ahead — brown swollen water, running high and hard |
| 215 | beat10m06.png | is a quarter mile of open water between this bank | wide: both banks divided by a quarter mile of open water |
| 216 | beat10m07.png | and the far hills. | wide: the far hills — a green hump on the far horizon |
| 217 | beat10m08.png | At the pace they move, | wide: the herd small on the near bank, the river enormous |
| 218 | beat10m09.png | they will reach it tomorrow. | close-up: debris racing the current — branches, a door, foam |
| 219 | beat10m10.png | And the calf cannot swim. | close-up: figure's fist tightening on the jacket strap |
| 220 | beat10m11.png | And the herd does not know what swimming is, | close-up: white water exploding over a submerged boulder |
| 221 | beat10m12.png | or what drowning is, | wide: black-brown current swirling, nothing animate in it |
| 222 | beat10m13.png | or what the word tomorrow means. | close-up: the ledger margin — TOMORROW circled hard in pencil |
| 223 | beat10m14.png | You have a dart gun. | close-up: the dart gun hanging on the hip — unfired, taped |
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
