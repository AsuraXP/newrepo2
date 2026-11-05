#!/usr/bin/env python3
"""Build visuals.csv (STATE 3) from the approved script.

Micro-beat splitting: every verb / subject / camera shift is its own row.
Frame count is an OUTPUT of the split, never a budget. visual_prompt carries
scene content + [STYLE_BLOCK]/[NEG_BLOCK] placeholders; the verbatim locked
style/character block is injected at STATE 4 after anchor approval.

Invariant enforced here: concatenating every moment_text (whitespace-normalized)
must equal the script narration word-for-word, so Kaggle word-level TTS
timestamps map 1:1 onto rows.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# MASTER ANCHOR LOCK — winner B (cinematic), user-selected 2026-11-05.
# These blocks are copied VERBATIM into every visual_prompt. Never rephrase.
STYLE = ("Cinematic storytime style: dramatic atmospheric lighting, deep desaturated blues "
         "with a warm amber accent, heavy film grain, bold expressive shading, moody depth, "
         "hand-drawn 2D illustration with slightly wobbly ink contours. Match ONLY the rendering "
         "style, palette, grain and line weight of the reference image; do not copy its scene or "
         "composition. Recurring protagonist, when present: a stick-figure human with a large "
         "round white head, messy spiky dark-brown hair, a minimal expressive face with two dot "
         "eyes, simple brows and a small mouth, thin black stick limbs, and a simple ragged brown "
         "hide tunic.")
NEG = ("No text, no letters, no numbers, no watermark, no signature, no extra limbs, "
       "no melted faces, no photorealism, no 3D render.")

# Each slide = one sentence / tight visual idea; moments = its micro-beats.
# (moment_text, scene_content)
SLIDES = [
 [
  ("You are standing on a beach in East Africa.", "Wide establishing: a lone round-headed stick figure stands small on an empty prehistoric beach, calm ocean, soft dawn light, untouched shore."),
  ("Sixty thousand years ago.", "Same beach, primeval and untouched: no modern objects anywhere, ancient dunes and wild vegetation, deep-time atmosphere."),
  ("Behind you is the only home your species has ever known.", "Camera behind the figure looking back over the shoulder toward the African interior: savanna and acacia trees inland."),
  ("Ahead of you is the entire planet.", "Camera behind the figure looking out: vast open ocean and an enormous empty horizon, tiny figure, huge world."),
 ],
 [
  ("Your descendants will walk from this beach", "The figure begins walking along the shoreline, small against the beach, first footprints trailing behind."),
  ("to the last tip of South America.", "Far destination vision: a cold wind-scoured southern headland under grey light, the end of the land."),
  ("The end of the world.", "Dramatic cliff at land's end, vast empty sea beyond, lone tiny figure at the edge."),
  ("More than forty thousand kilometers.", "Immense-distance visual: a tiny figure and a long winding path stretching across stylized continents to the horizon."),
 ],
 [
  ("Here is the strange part.", "The figure pauses mid-step and turns to face the camera, curious tilted-head pose."),
  ("If you walked that route without stopping,", "The figure walks determinedly along an endless straight path, steady stride."),
  ("twenty kilometers a day, every day,", "Rhythmic walking under a sun arcing overhead, repeated stride marks, day-cycle feel."),
  ("it would take about two thousand days.", "A very long line of footprints stretching to the horizon, no numbers or text anywhere."),
  ("Less than six years of walking.", "The figure strides through rapidly shifting season colors along the path, time-lapse feel."),
 ],
 [
  ("But your family will take fifty thousand years to do it.", "Generational relay: an aging figure passes the stride to a child figure, repeating silhouettes fading into the deep distance."),
 ],
 [
  ("Two thousand days of walking.", "Close on a trail of footprints marching forward across sand."),
  ("Fifty thousand years of time.", "Deep-time night: a tiny figure under an enormous wheeling starfield, immense scale."),
  ("How does that work?", "The figure shrugs with open palms, looking at the camera, questioning pose."),
 ],
 [
  ("That is the story of the greatest journey ever made.", "Epic ultra-wide: a tiny figure on a huge landscape with a faint path curving to the horizon."),
  ("And you are going to walk it.", "Close on the figure's stick feet taking one deliberate step forward."),
 ],
 [
  ("First, look down at your legs.", "First-person POV looking down at one's own thin black stick legs and feet on the ground."),
  ("You are not the fastest animal on the savanna.", "Savanna scene: the figure stands still while a blurred fast animal streaks past."),
  ("A kudu can leave you behind in seconds.", "A kudu antelope sprinting away in a burst of dust, figure left small behind."),
  ("But you have a trick no antelope has.", "The figure taps the side of its round head, confident knowing pose."),
  ("You can cool down while moving.", "The figure jogs steadily, small sweat droplets flying off the skin."),
  ("Sweat.", "Extreme close-up: a single sweat droplet rolling down skin, heat shimmer."),
  ("Your whole body is a radiator.", "The figure jogging with gentle heat-wave lines radiating off the whole body."),
  ("A galloping animal has to stop and pant.", "An antelope stopped in the shade, head low, panting, tongue out, overheated."),
  ("You just keep jogging.", "The figure jogs past the panting animal, steady and unhurried."),
 ],
 [
  ("Your feet have arches that work like springs.", "Close-up of a stick foot with the arch highlighted as a coiled spring, simple diagram feel."),
  ("Your Achilles tendon stores energy and gives it back.", "Close-up of the ankle/Achilles drawn as a springy energy coil compressing and releasing."),
  ("A tiny ligament in your neck keeps your head steady while you run.", "Side view of the figure running, head perfectly level, a small highlighted ligament line at the neck."),
  ("Chimps do not have it.", "A chimp silhouette running with its head bobbing, contrasted and slightly comedic."),
  ("You do.", "The figure runs with a perfectly steady head, confident, level gaze."),
 ],
 [
  ("In the Kalahari, hunters still prove this works.", "Kalahari desert: a small group of stick-figure hunters under a blazing white sun."),
  ("They chase a kudu in the midday heat,", "Hunters jogging after a kudu across hot open desert, intense overhead sun."),
  ("forty degrees Celsius,", "Heat-shimmer close on the desert floor and a fierce white sun, no text or numbers."),
  ("for two to five hours.", "The sun crawling across the sky over a long chase, elongated shadows."),
  ("Up to thirty five kilometers.", "A long winding trail across the desert dotted with tiny pursuit marks."),
  ("The animal sprints, stops, sprints, stops.", "Sequential kudu poses: sprint, stop, sprint, stop across the frame, staccato rhythm."),
  ("The hunter just keeps coming.", "A lone hunter jogging steadily toward the resting animal, relentless."),
  ("Eventually the kudu cannot run anymore.", "The exhausted kudu lying down in the sand, spent, no wound or blood."),
  ("The hunter walks up to it.", "The hunter calmly walks up to the lying kudu, respectful, no gore."),
 ],
 [
  ("You are not built for speed.", "The figure stands beside a motion-blurred sprinting animal, calm contrast."),
  ("You are built for forever.", "The figure walks toward an endless horizon, long shadow, infinite path."),
 ],
 [
  ("But here is the secret of the long walk.", "The figure leans toward the camera, one hand raised as if sharing a secret."),
  ("You never actually go on a journey.", "The figure relaxes at a small camp, sitting by a fire, not traveling."),
 ],
 [
  ("You live in a band of a few dozen people.", "A camp of roughly two dozen stick figures of varied sizes, shelters, a fire, communal life."),
  ("Every day you walk out from camp to find food.", "Figures leaving camp in the morning with simple tools, fanning out to forage."),
  ("Modern hunter gatherers like the Hadza walk about eight to fourteen kilometers a day.", "Hadza-like foragers walking across savanna, digging sticks and bundles, everyday rhythm."),
  ("Then you come home.", "A figure returns to camp at dusk, warm firelight, welcoming group."),
 ],
 [
  ("Every few weeks, camp moves.", "Camp being packed: shelters folded, bundles lifted, figures preparing to leave."),
  ("Eight, ten, twelve kilometers.", "A short path between an old camp spot and a new one, modest distance."),
  ("Maybe twenty five.", "A longer path across open land to a farther new camp spot."),
  ("You pick up everything you own,", "The figure lifts a single small bundle of belongings onto its back."),
  ("which is not much,", "Close on the small bundle: a few simple possessions, deliberately sparse."),
  ("and you walk half a day.", "The figure walks with the bundle under a half-arc sun, half-day journey."),
 ],
 [
  ("That is it.", "Simple quiet camp scene, the figure gives a small shrug."),
  ("That is the migration.", "Ultra-wide: the tiny camp in a vast empty landscape, the whole 'migration'."),
 ],
 [
  ("You are not crossing a continent.", "The figure at camp, NOT marching, calm domestic scene."),
  ("You are just moving camp.", "The camp relocating a short distance, figures carrying bundles."),
  ("Again.", "The same camp-move repeated, a beat of routine."),
  ("And again.", "The camp-move repeated once more, rhythmic."),
  ("For a lifetime.", "The figure aging through repeated camp moves, child to elder silhouettes."),
  ("Do the math,", "The figure pauses, counting on simple stick fingers, calculating pose."),
  ("and your band drifts less than one kilometer per year.", "A vast stylized map where the camp marker barely shifts, tiny drift arrow, no text."),
  ("A distance you could cover in ten minutes.", "The figure casually walks a very short distance, quick and easy."),
  ("That is how fast your family conquers the Earth.", "A tiny camp against an enormous stylized Earth/continent, gentle irony."),
 ],
 [
  ("You will never see the destination.", "The figure gazes at an empty horizon, no destination in sight."),
  ("Your grandchildren will never see it.", "An elder figure and a small child figure look at the same empty horizon."),
  ("Nobody in your family even knows there is a destination.", "The family group content at camp, unaware, warm everyday scene."),
  ("There is only the next waterhole.", "A waterhole ahead on the plain, animals gathered, the next goal."),
  ("The next valley.", "A green valley opening ahead between hills."),
  ("The next season.", "The landscape shifting season colors, cyclical time."),
 ],
 [
  ("So how do you know where to go?", "The figure stands at a fork in the land, looking around, deciding."),
 ],
 [
  ("You read the land like a book.", "The figure studies the landscape, landmarks glowing faintly like readable signs."),
  ("The sun rises one way and sets the other.", "A sun arcing from one horizon to the other over the plain, east-west feel."),
  ("The stars turn around fixed points.", "Night sky with stars wheeling around a fixed pole point, long-exposure feel."),
  ("Rivers always lead somewhere.", "A river winding toward the horizon, the figure following it."),
  ("Mountains stay put.", "Steadfast mountains on the horizon, the figure small below."),
  ("Coastlines are highways.", "A long coastline curving like a road, the figure walking its edge."),
  ("Walk the beach and the food comes to you.", "The figure strolls a beach abundant with easy food, relaxed."),
  ("Shellfish, fish, seals.", "Close on shellfish, a fish, and a seal resting on the shore, simple flat shapes."),
 ],
 [
  ("And when there are no landmarks, you use memory.", "Featureless desert, the figure touches its head, recalling."),
  ("In Australia, your descendants will build maps out of songs.", "Australian red desert, a figure singing, faint musical notes drifting out."),
  ("Songlines.", "A glowing song-path line weaving across the land, connecting landmarks."),
  ("Each verse names a landmark in order.", "A sequence of landmarks linked by a glowing line, ordered waypoints."),
  ("This rock, then that waterhole, then the ridge.", "Three waypoints in sequence: a rock, a waterhole, a ridge, connected in order."),
  ("Sing the song in the right order,", "The figure sings and the path lights up verse by verse ahead."),
  ("and you can cross hundreds of kilometers of desert you have never seen.", "The figure crosses a vast desert confidently along the glowing song-path."),
  ("The song is the map.", "The glowing song-path overlaid on the land like a map, musical notes as waypoints."),
  ("The map is the song.", "Reverse: the map-lines resolve into flowing musical notation across the land."),
  ("Some of these routes run for thousands of kilometers.", "An extremely long glowing song-path spanning a whole continent."),
 ],
 [
  ("No paper.", "The figure holds out empty open hands, no map, no paper."),
  ("No GPS.", "The figure's empty hands, no device, no technology anywhere."),
  ("Just a melody that tells you where the water is.", "A gentle melody-line of notes leading the figure to a hidden waterhole."),
 ],
 [
  ("Then, about sixty five thousand years ago, your family reaches the edge of Asia.", "The family group arrives at a lush Asian coastline, the sea ahead."),
  ("And there is a problem.", "The figure stops and notices the vast ocean, concerned pose."),
  ("A big one.", "The camera pulls wide to reveal the enormous daunting ocean."),
 ],
 [
  ("Australia is out there.", "Ocean horizon with the faintest hint of distant land, mysterious."),
  ("You cannot see it.", "Empty ocean horizon, no land visible, the figure squinting."),
  ("But something is.", "A subtle sign on the horizon, the figure alert."),
  ("Maybe birds.", "Birds flying purposefully toward the distant horizon."),
  ("Maybe a cloud that never moves, the kind that sits over land.", "A single stationary cloud hovering over far unseen land, a navigational clue."),
  ("And between you and it, open ocean.", "Vast open ocean between the figure and the far shore."),
  ("Fifty to ninety kilometers of it.", "A wide ocean gap emphasized, tiny figure at the near shore."),
  ("No land bridge.", "Deep water with no connection between the two lands, clear separation."),
  ("Ever.", "The same deep-water separation, emphatic and permanent."),
  ("Even at the lowest sea levels, Australia was never connected.", "A simple cross-section: even at low sea level a deep-water gap remains between lands."),
 ],
 [
  ("So somebody builds a raft.", "A figure lashing together a simple bamboo raft on the shore."),
  ("Bamboo, maybe.", "Close on bamboo poles being bound with cordage."),
  ("And a group of people, enough to start a population, gets on it", "A group of figures carefully boarding the raft, families, enough to found a population."),
  ("and paddles out of sight of land.", "The raft paddles into open sea, the home shore shrinking behind."),
 ],
 [
  ("Think about that.", "The figure looks at the camera, awed, hand on chest."),
  ("The first ocean voyage in human history was not a drift accident.", "The raft paddled deliberately, purposeful strokes, not drifting."),
  ("It was a plan.", "A figure points decisively toward the horizon, determined leadership."),
  ("By sixty five to fifty thousand years ago, people are living in Australia.", "A thriving camp on Australian land, figures at home, fire and shelters."),
  ("The oldest sites, like Madjedbebe, hold stone tools older than the first human sites in Europe.", "A rock shelter with carefully placed stone tools and ochre, ancient and revered."),
 ],
 [
  ("Your family crossed the sea before anyone invented the wheel.", "The raft on the open sea, emphatically no wheel or cart anywhere, pre-wheel era."),
 ],
 [
  ("Now turn north.", "The figure turns to face north, camera panning toward cold lands."),
  ("The ice age is coming.", "Ice sheets advancing on the horizon, palette shifting cold blue."),
 ],
 [
  ("Water locks up into glaciers.", "Water freezing into a massive glacier, ice crystals forming."),
  ("The oceans drop.", "Sea level visibly dropping, exposed shoreline, the figure watching."),
  ("One hundred twenty meters.", "A dramatic sea-level drop shown as a tall exposed band of former seabed, no text."),
  ("That is a forty story building of missing sea.", "A tall building-height silhouette beside the dropped sea level for scale, no text."),
 ],
 [
  ("And where the Bering Strait should be, between Siberia and Alaska, the seafloor stands up and becomes dry land.", "The seafloor rising up out of the water into a broad land bridge between two continents."),
  ("Beringia.", "A vast revealed grassland where ocean used to be, wide and alive."),
 ],
 [
  ("It is not a bridge.", "A narrow rope-bridge image crossed out with a simple X, correcting the misconception."),
  ("That is the wrong picture.", "The crossed-out narrow-bridge idea, the figure shaking its head."),
  ("At its widest it is sixteen hundred kilometers north to south.", "An enormous landmass shown north-to-south, immense width, tiny figures for scale."),
  ("A country.", "The landmass framed as a whole country, borders implied by scale, no text."),
  ("Grassland, rivers, mammoths, horses.", "Beringia alive: grassland, a river, mammoths and horses grazing."),
  ("People live there for thousands of years", "A settled camp on Beringia, generations living normal lives."),
  ("without ever knowing an ocean is underneath their home.", "A gentle cutaway: the camp on land with a hidden ocean layer beneath, unaware figures."),
 ],
 [
  ("Around twenty thousand years ago, some of your family is standing in America.", "The family group standing on new American land, looking around."),
  ("They did not cross anything.", "No bridge or crossing shown, just open land, the figures simply present."),
  ("They just walked east, following the food, the way they always do.", "The family walking east after grazing animals, ordinary movement."),
 ],
 [
  ("Behind them, two ice sheets the size of continents block the way south.", "Two colossal ice sheets towering behind the figures, blocking the inland way south."),
  ("But the coast is open.", "An open ice-free coastline stretching south, inviting."),
  ("Kelp forests, fish, shellfish, sea mammals.", "Underwater kelp forest with fish, shellfish and a sea mammal, abundant food."),
  ("A highway of food running down the Pacific shore.", "A coastline drawn as a food-rich highway running south, plenty along the shore."),
  ("Some people hug the coast in boats.", "Small boats hugging the coast, figures paddling south along the shore."),
  ("Others wait for a corridor to open between the ice.", "Figures waiting at the edge of a narrowing gap between two ice sheets."),
 ],
 [
  ("And then something changes.", "A shift in the scene, the figure sensing change, anticipatory."),
  ("The drift becomes a sprint.", "The figure breaks into a run, dynamic forward lean."),
 ],
 [
  ("Twenty three thousand years ago, kids are leaving footprints in the mud of White Sands, New Mexico.", "Children's footprints pressed into lakeshore mud at White Sands, small bare feet."),
  ("Teenagers, running and playing beside a lake.", "Teen figures running and playing beside an ancient lake, joyful."),
  ("We can still see their steps today.", "The same footprints fossilized and preserved in pale sediment, still visible."),
 ],
 [
  ("Fourteen thousand years ago, your family is in Panama.", "The family in lush tropical Panama, dense green, humid light."),
  ("And then they pour south.", "A stream of figures flowing south across the land, momentum."),
  ("Through rainforest,", "Dense rainforest, figures threading between huge trees and vines."),
  ("over the Andes,", "High Andes mountains, figures climbing a cold pass, breath visible."),
  ("down the spine of two continents.", "A high continental spine of mountains, figures descending southward."),
 ],
 [
  ("By about eleven thousand years ago, they reach Tierra del Fuego.", "The family arrives at the southern tip, wind-blown, end of the land."),
  ("The last tip.", "The final headland, land running out into sea."),
  ("Cold, wind scoured, staring at Antarctica across the sea.", "Cold wind-scoured shore, the figures staring across the sea toward distant Antarctica."),
  ("There is no more land.", "Empty sea ahead, no further land, the end."),
  ("The walk is over.", "The figure stops and stands still at land's end, journey complete, quiet."),
 ],
 [
  ("From the ice to the tip, two whole continents crossed in just a few thousand years.", "Two continents with a fast bright path sweeping from north to the southern tip."),
  ("Compared to the fifty thousand year crawl out of Africa, this is a sprint.", "Contrast: a slow crawl path out of Africa versus a fast sprint path down the Americas."),
  ("When the land is empty and rich, your family does not crawl.", "Rich empty land full of game, the figures upright and ready."),
  ("It runs.", "The figure running fast across open land, dynamic."),
 ],
 [
  ("Today, one man is trying to walk the whole route alone.", "A modern lone walker with a small pack on a long road, present day."),
  ("Paul Salopek.", "A portrait of the modern walker, simple friendly stick-figure face, travel gear."),
  ("He left Ethiopia in twenty thirteen.", "The walker setting out from an Ethiopian landscape, beginning the long road."),
  ("Forty two thousand kilometers, following your family's path to Tierra del Fuego.", "A long route line on a stylized world map from Africa to the southern tip, no text."),
  ("He is a professional walker, and he has been at it for over a decade.", "The walker mid-journey, seasons passing around him, steady pace."),
  ("He is still not done.", "The walker still on the long road, the destination far ahead."),
 ],
 [
  ("One lifetime is not enough.", "A single human lifetime shown as a short path segment against the huge route."),
  ("It never was.", "The same short segment against the immense route, emphatic."),
  ("That is the point.", "The figure looks at the camera, meaningful pause."),
 ],
 [
  ("So the next time you walk to the store and your legs complain,", "A modern figure walks to a small store, mildly tired, everyday scene."),
  ("remember what they are.", "The figure looks down at its own legs, reflective."),
  ("They are the machine that carried your family out of Africa,", "The legs echo ancient walkers striding out of a savanna, ghosted overlay."),
  ("across the ocean,", "Echo of the raft crossing the open ocean, ghosted overlay."),
  ("through the ice age,", "Echo of figures crossing the ice-age land, ghosted overlay."),
  ("and down to the end of the world.", "Echo of the family at Tierra del Fuego, ghosted overlay."),
 ],
 [
  ("Two thousand days of walking.", "A trail of footprints marching forward, callback."),
  ("Fifty thousand years of patience.", "Deep-time starfield over a tiny patient figure, callback."),
  ("Two thousand generations of just moving camp.", "Many generations of camp-move silhouettes receding into the distance."),
 ],
 [
  ("You did not conquer the planet with speed.", "The figure walks steadily, NOT running, calm power."),
  ("You conquered it with the next step.", "Close on one foot taking the next step, decisive."),
 ],
 [
  ("And you are still taking it.", "The figure walks forward into a hopeful horizon, ancient and modern blended, one ongoing step."),
 ],
]

def norm_words(s):
    return re.findall(r"\S+", s)

def main():
    # Build rows
    rows = []
    for slide_idx, moments in enumerate(SLIDES, start=1):
        for m_idx, (mtext, scene) in enumerate(moments, start=1):
            rows.append({
                "slide_id": slide_idx,
                "moment": m_idx,
                "moment_text": mtext,
                "visual_prompt": f"Wide 16:9 cinematic frame. {scene} {STYLE} {NEG}",
            })

    # Verify concatenation equals narration word-for-word
    script = (ROOT / "script.md").read_text()
    body = script.split("---")[1]
    narr = norm_words(body)
    spine = norm_words(" ".join(r["moment_text"] for r in rows))
    if narr != spine:
        # locate first divergence
        for i, (a, b) in enumerate(zip(narr, spine)):
            if a != b:
                print(f"MISMATCH at word {i}: script={a!r} spine={b!r}")
                print("script ctx:", " ".join(narr[max(0,i-6):i+6]))
                print("spine  ctx:", " ".join(spine[max(0,i-6):i+6]))
                break
        print(f"len script={len(narr)} spine={len(spine)}")
        sys.exit(1)

    out = ROOT / "visuals.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slide_id","moment","moment_text","visual_prompt"])
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    batches = (n + 7) // 8
    print(f"PASS: spine matches narration word-for-word ({len(narr)} words).")
    print(f"rows N={n}; slides={len(SLIDES)}; projected batches (8/turn)={batches}")
    print(f"wrote {out}")

if __name__ == "__main__":
    main()
