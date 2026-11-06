# WORKER ASSIGNMENT 2 — The Rewilding

- Branch: `git checkout -b rewilding-worker-2` (from arena/c251d7fe-newrepo2)
- Target CSV: `rewilding_video/visuals.csv` — **Assigned rows 113 to 223** (111 frames to generate)
- Slides covered: 5, 6, 7, 8, 9, 10
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

## ASSIGNED FRAMES — 111 prompts

| # | frame file | moment_text | visual_prompt |
|---|---|---|---|
| 113 | beat05m02.png | You check the camera traps, | medium: figure crouches at the creekbank, checking the trap strap |
| 114 | beat05m03.png | one by one, | close-up: camera strap buckle and mud-caked boot toe |
| 115 | beat05m04.png | spooling the film in the dry little dark of your pack. | close-up: film cartridge spooling into a belt pouch in the dark pack |
| 116 | beat05m05.png | You tell yourself what you always tell yourself. | close-up: figure's eye reflected in the curved camera lens glass |
| 117 | beat05m06.png | You are a clerk. | medium: figure alone with coffee on the porch, thinking |
| 118 | beat05m07.png | A clerk of the wilderness. | close-up: ink-black fingertips on ledger paper — a clerk's hands |
| 119 | beat05m08.png | Clerks do not interfere. | close-up: a rubber stamp coming down — LOGGED |
| 120 | beat05m09.png | At the second camera, | medium: figure at the second camera on a bent oak, going suddenly still |
| 121 | beat05m10.png | you find the thing you feared. | close-up: printed photo strip lying across a lap, red 04:17 in the corner |
| 122 | beat06m01.png | The frame is timestamped 04:17. | close-up: photo corner INFRARED — 04:17 in hot red type |
| 123 | beat06m02.png | Night grain, | close-up: grainy infrared photo, white figures against green-black wash |
| 124 | beat06m03.png | infrared white | close-up: photo zoomed, a band of white backs across the frame |
| 125 | beat06m04.png | and green. | same photo, green flare tint deepening, sprocket grain visible |
| 126 | beat06m05.png | In it, | medium: figure staring at the photo, eyes widening under hat brim |
| 127 | beat06m06.png | the herd crosses the creek bed — | photo close-up: herd frozen mid creek crossing, water flung in stars |
| 128 | beat06m07.png | eleven adults, | photo close-up: eleven adult backs in a hitching tide formation |
| 129 | beat06m08.png | unmistakable even at that distance, | photo close-up: gait detail — heels dragging, toes clawing |
| 130 | beat06m09.png | that hitching, | photo close-up: the wave of motion rippling down the line |
| 131 | beat06m10.png | tidelike gait — | same photo widened — the ripple line crossing the whole frame |
| 132 | beat06m11.png | and behind the last of them, | photo close-up: the farthest back — low, small, and dragging |
| 133 | beat06m12.png | so low to the ground she is nearly a shadow, | photo close-up: near-shadow fold pressed against the dark |
| 134 | beat06m13.png | the adult you logged two days ago. | photo close-up: the long-toed adult recognized from the mud |
| 135 | beat06m14.png | And under her chest, | photo close-up: under her chest, a small bright bundle-shape |
| 136 | beat06m15.png | tucked against her, | photo close-up: the bundle tucked high and held tight to the torso |
| 137 | beat06m16.png | a small bright shape. | macro: the bright knot of the sling, centered in the frame |
| 138 | beat06m17.png | Wrapped in something. | photo close-up: sling knot visible at the figure's back |
| 139 | beat06m18.png | A tarp scrap. | photo close-up: tarp scrap corner — gray-blue weave, sun-bleached |
| 140 | beat06m19.png | A jacket. | photo close-up: flannel check pattern inside the sling |
| 141 | beat06m20.png | A piece of the old world, | photo close-up: jacket sleeve stripe — old-world red plaid, decades old |
| 142 | beat06m21.png | remade into a sling. | photo close-up: loose sling strap dangling, sway frozen mid-frame |
| 143 | beat06m22.png | The calf. | macro: the bundle centered in the photo — THE CALF in harsh contrast |
| 144 | beat06m23.png | You sit down in the leaf mold with the photograph in your hands, | wide: figure seated on the forest floor, photo in both hands, gold leaf-light |
| 145 | beat06m24.png | and for a long time you do not move. | long hold: figure unmoving, ferns swaying, creek light crawling |
| 146 | beat07m01.png | The manual has a page for a turned animal found dead. | close-up: manual page TURNED — DECEASED PROTOCOL — numbered steps one to six |
| 147 | beat07m02.png | It has a page for a new settlement found in the Drift. | close-up: manual page SETTLEMENTS FOUND IN THE DRIFT — shack illustration |
| 148 | beat07m03.png | It does not have a page for this, | close-up: manual page — THIS PAGE INTENTIONALLY BLANK |
| 149 | beat07m04.png | because this has never happened, | close-up: a finger hovering an inch above the blank paper |
| 150 | beat07m05.png | because this cannot happen, | close-up: figure's face going cold and calculating |
| 151 | beat07m06.png | because turners do not have children, | macro: the photo burning in the reflection of one close eye |
| 152 | beat07m07.png | because the world that ended took the children first, | close-up: manual foreword plate — the evacuation-era city at dusk, storybook flat |
| 153 | beat07m08.png | and because — and your mind keeps returning to this, | medium: over-shoulder — figure reading a torn evacuation poster: ROUTE 9 arrow |
| 154 | beat07m09.png | over and over — | close-up: the same blank page again, close in |
| 155 | beat07m10.png | someone had to carry that baby into the deep woods | wide: the deep woods under untouched canopy, a game trail vanishing east |
| 156 | beat07m11.png | and leave it there, | photo close-up: the adult from behind, bundle hugged to the chest |
| 157 | beat07m12.png | or lose it, | photo close-up: same frame held tighter to the face |
| 158 | beat07m13.png | or die, | photo close-up: the herd from behind, spacing like geese in flight |
| 159 | beat07m14.png | and the herd found it, | photo close-up: the bundle centered — the herd gathered around a lost gosling |
| 160 | beat07m15.png | and the herd kept it. | wide: the creek crossing at dusk, abandoned, reeds bowing in wind |
| 161 | beat07m16.png | You zoom the photo until the pixels break. | macro: a jeweler's loupe over the photo resting on a flat palm |
| 162 | beat07m17.png | The adult's head is bowed. | photo close-up: the adult's head bowed against her chest |
| 163 | beat07m18.png | Not browsing. | same photo — hanging lower, grazing silhouette denied |
| 164 | beat07m19.png | Bowed. | same photo — the bow unmistakable, a different posture entirely |
| 165 | beat07m20.png | The posture of something standing guard over warmth. | photo close-up: shoulders rounded protectively — a sentry over warmth |
| 166 | beat07m21.png | You do not radio Base. | medium: figure at the radio desk, hand hovering above the handset |
| 167 | beat07m22.png | You tell yourself it is | close-up: fingers stopped mid-air above the telephone hook |
| 168 | beat07m23.png | because Base would send a team, | close-up: radio dial glow, red, waiting |
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
