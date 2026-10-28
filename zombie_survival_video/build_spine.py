#!/usr/bin/env python3
"""Builds zombie_survival_video/visuals.csv.

The style prefix is a single constant so all 89 prompts carry a byte-identical
style block. Frame count is an OUTPUT: one row per visual moment in script.md.
Run from the repo root:  python3 zombie_survival_video/build_spine.py
"""
import csv
import os

STYLE = (
    "Flat 2D cartoon illustration in hand-drawn stick-figure animation style: "
    "solid black outlines of uniform weight with a slightly wobbly hand-drawn edge, "
    "flat muted fills, no gradients, no texture, no shading, no cast shadows, no highlights. "
    "Characters are simple stick figures with a round white head, two small black dot eyes, "
    "a thin straight mouth line, and single-stroke black limbs with rounded ends. "
    "Clean empty background planes, minimal detail, wide 16:9 composition with generous "
    "negative space. Full-bleed: the artwork fills the entire frame edge to edge, no border, "
    "no frame line, no vignette."
)

PALETTE = (
    "Palette strictly limited to #010101, #f8f3dc, #e5d3ba, #75503b, #6b767f, #473425, "
    "#f0c667, #1e2d50. Absolutely no text, no lettering, no readable writing, no signage, "
    "no watermark, no signature."
)

SURV = (
    "the survivor — a male stick figure, round white head, two black dot eyes, thin straight "
    "mouth, six short black hair strokes on top of the head, single-stroke black limbs with "
    "rounded ends, flat charcoal-grey hooded jacket worn open over a black torso stroke, flat "
    "olive-brown trousers on the leg strokes, dark boots, one shoulder-strap line across the chest"
)
ASH = (
    "Ash — a small stick-figure dog, round white head, two black dot eyes, single-stroke black "
    "legs and tail with rounded ends, two flat brown #473425 floppy ear shapes, one flat brown "
    "#473425 patch on the back of the body, thin straight mouth line, half the survivor's height "
    "at the shoulder"
)

# (slide, moment_text, visual clause)
ROWS = [
    # ---- slide 01: day 412, waking ----
    (1, "Day four hundred and twelve. The city has stopped pretending.",
     "a wide empty street in pre-dawn grey, flat beige #e5d3ba building planes with simple "
     "punch-hole windows on both sides, flat brown #75503b road band across the bottom third, "
     "flat #1e2d50 dark sky strip above, four scattered grey #6b767f car silhouettes with no "
     "wheels, no people anywhere"),
    (1, "You wake first. You always wake first.",
     f"{SURV} sitting up on a bare mattress, eyes open, one hand flat on the mattress beside him, "
     "flat #e5d3ba wall behind, flat #1e2d50 night in a tall window at the left edge"),
    (1, "Not a growl. A question, low in his chest.",
     f"{ASH} standing beside the mattress in close view, head lifted toward the survivor, one "
     "front leg slightly raised, flat #e5d3ba wall behind, flat brown #75503b floorboard plane"),
    (1, "You put your hand flat on his ribs until he stops asking.",
     f"{SURV} kneeling with one flat palm resting on the ribs of {ASH} in the foreground, both "
     "in profile, flat #e5d3ba wall plane behind, pre-dawn grey light"),
    (1, "You sleep on the third floor, because the third floor is quiet.",
     "an exterior of a flat four-storey building at pre-dawn, seen square-on, simple punch-hole "
     "windows in a grid, one window on the third floor lit flat ivory #f8f3dc, flat #1e2d50 sky "
     "above, flat brown #75503b road band below, no people"),
    (1, "Stairs are a filter. Anything that still remembers how to climb gets tired by the second landing.",
     "a bare concrete stairwell interior, flat grey #6b767f steps receding upward in flat "
     "elevation with no vanishing point, plain walls, one small landing window with flat #1e2d50 "
     "behind it, empty, no figures"),
    (1, "You have rules. You keep them in pencil on the wall.",
     f"{SURV} standing in profile beside a bare wall, one arm raised holding a short stub pencil "
     "against flat #e5d3ba plaster, a column of short scratched tally marks already on the wall "
     "beside him, no readable writing"),
    (1, "When the pencil ran out, you scratched them with a nail.",
     "an extreme close view of a single hand holding one thin nail against a flat #e5d3ba wall, "
     "three short scratched lines already cut into the plaster, no readable writing, no text"),
    (1, "You found Ash in a stairwell in November, thin as a broom, sitting on somebody's coat.",
     f"{ASH} sitting small and upright on a flat dark green-brown coat folded on a concrete step, "
     f"a bare stairwell around him, flat grey #6b767f walls, no other figures"),
    (1, "He didn't bark. He waited to see what you would do.",
     f"close view of {ASH} sitting still on a coat on a step, head level, looking straight out "
     "toward the viewer, flat grey #6b767f stairwell behind, no other figures"),
    (1, "That's how you knew he'd survive.",
     f"{SURV} crouched down low at the foot of a step, one hand extended toward {ASH} sitting on "
     "a coat, both small in the lower left third, flat grey #6b767f stairwell walls, generous "
     "empty space"),

    # ---- slide 02: the rules ----
    (2, "Rule one. Never run in the open.",
     f"{SURV} standing still at the mouth of an alleyway, seen from behind, a wide flat brown "
     "#75503b open road stretching away in front of him, flat beige #e5d3ba walls closing in "
     "either side, empty road, no other figures"),
    (2, "Rule two. Never answer a sound that might be a person.",
     f"{SURV} in profile with one hand lifted near his ear, listening, body still, flat beige "
     "#e5d3ba wall plane behind him, a flat brown #75503b doorway shape at the far right edge, "
     "no other figures"),
    (2, "Rule three. Count everything. Cans, candles, days.",
     "a flat shelf holding eleven identical plain cans in a neat row, four stub candles standing "
     "upright, and a column of scratched tally marks on the wall behind, flat #e5d3ba wall, flat "
     "brown #75503b shelf plank, no readable writing, no labels on the cans"),
    (2, "If the count stops making sense, you made a mistake a week ago.",
     f"{SURV} standing in front of a wall covered in long columns of short scratched tally marks, "
     "both hands hanging at his sides, head tipped slightly down, flat #e5d3ba wall filling the "
     "frame behind him, no readable writing"),
    (2, "You're not the last one. You have evidence.",
     f"{SURV} seen from behind, standing on a rooftop ledge at dusk, looking out across a flat "
     "dark city skyline of simple block shapes, one small orange #ff8421 point of light on a "
     "distant tower silhouette, flat #1e2d50 sky"),

    # ---- slide 03: the number ----
    (3, "Every night at eleven, the tower on the east point transmits.",
     "a slender flat grey #6b767f radio tower standing alone on a gravel point above flat water, "
     "square-on flat elevation, one orange #ff8421 lamp housing near the top, flat #1e2d50 night "
     "sky behind it, water flat #1e2d50 and still, no figures"),
    (3, "Not a voice talking. A voice reading.",
     "an extreme close view of a grey #6b767f radio speaker grille with simple horizontal slit "
     "lines, three short curved sound-arc lines drawn beside it, flat #5e5653 wall behind, no "
     "figures, no text"),
    (3, "Names, one at a time, slow. Then a number.",
     "a close view of an open notebook on a plain desk, flat #f8f3dc paper with two ruled columns "
     "drawn as thin black lines and short illegible black marks along them, one short stub pencil "
     "beside it, flat #5e5653 wall, no readable writing, no letters"),
    (3, "Seven hundred and ninety-four.",
     f"{SURV} standing in a bare room in profile, head turned toward a tall window with flat "
     "#1e2d50 night behind it, three short sound-arc lines drawn beside the window pane, flat "
     "#5e5653 wall planes, no readable writing"),
    (3, "That's how many names are left tonight.",
     "a flat #e5d3ba wall with one long column of short scratched tally marks running from the top "
     "of the frame to the bottom, a single short line separated from the rest at the bottom end, "
     "extreme close view, no readable writing"),
    (3, "Last month it was eight hundred and forty-one.",
     f"{SURV} sitting on the floor in profile against a wall, knees up, one arm resting on a knee, "
     "a column of scratched tally marks on the wall above him, flat #5e5653 wall, flat brown "
     "#75503b floor, no readable writing"),
    (3, "Fewer names could mean fewer people.",
     "a wide flat city skyline at night reduced to simple stepped block silhouettes, flat #1e2d50 "
     "sky above, only two small flat ivory #f8f3dc windows lit across the whole skyline, no "
     "figures"),
    (3, "Or it could mean somebody is finding bodies and correcting the list.",
     "an empty flat brown #75503b road surface in close view with one abandoned flat grey "
     "#6b767f shoe lying on its side and nothing else, flat #e5d3ba kerb edge at the top of the "
     "frame, no figures, no gore"),
    (3, "Either way the tower is alive. Either way, east is where the living are.",
     "a slender flat grey #6b767f radio tower on a point, seen from a distance and small, one "
     "orange #ff8421 lamp with two short motion-arc lines showing it mid-rotation, flat #1e2d50 "
     "sky and water, thin flat #e5d3ba gravel band at the base"),

    # ---- slide 04: the decision ----
    (4, "So you decide something stupid. You decide to go.",
     f"{SURV} standing in a doorway with a flat brown #75503b door hanging open beside him, "
     "looking straight out toward the viewer, framed by the door jamb, flat beige #e5d3ba wall "
     "around the opening, flat #1e2d50 sky beyond him"),
    (4, "Four hundred and twelve days is a long time to be careful.",
     "a close view of a flat #e5d3ba wall beside a window, covered edge to edge in dense columns "
     "of short scratched tally marks, no readable writing, no figures, flat #1e2d50 night in the "
     "window pane at the right edge"),
    (4, "Careful is just dying slowly with extra steps.",
     f"{SURV} seen from behind standing on a long flat stair tread, shoulders low, one hand on "
     "the wall, flat grey #6b767f stairwell walls rising above him, no other figures"),

    # ---- slide 05: Calder Street ----
    (5, "The pharmacy on Calder Street is four blocks of open ground.",
     f"{SURV} small in the frame standing at the near end of a wide flat brown #75503b road, a "
     "long row of flat beige #e5d3ba building faces running away on both sides into a flat "
     "horizon, four simple block shapes marking each intersection, no other figures"),
    (5, "Open ground is where people die looking at their feet, so you keep your eyes up.",
     f"low angle view of {SURV} walking toward the viewer on a flat brown #75503b road, head "
     "lifted and eyes forward, flat beige #e5d3ba building planes behind him, flat #e5d3ba "
     "overcast sky band at the top"),
    (5, "Ash keeps his nose down. Between you, you cover the whole world.",
     f"{ASH} walking in profile, head lowered and nose close to a flat brown #75503b road "
     "surface, four short scent-arc lines drawn at the ground, flat #e5d3ba overcast sky band "
     "above, empty road, no other figures"),
    (5, "Third block. A woman in a green coat stands in the middle of the road, facing the water.",
     f"{SURV} and {ASH} stopped small in the left third of the frame, seen from behind, and far "
     "down the flat brown #75503b road a lone stick figure in a flat dark green coat standing "
     "still in the centre of the road, back turned, flat beige #e5d3ba building planes either "
     "side, flat #1e2d50 water band at the far horizon"),
    (5, "She has been facing the water for a long time.",
     "a lone stick figure in a flat dark green coat seen from behind, standing perfectly still in "
     "the centre of a flat brown #75503b road, facing a flat #1e2d50 water band, small in the "
     "frame, generous empty sky above, no face visible, no other figures"),
    (5, "Her coat is clean. That's the part that frightens you.",
     "a close view of the back and shoulder of a flat dark green coat on a still stick figure, "
     "the fabric clean and unmarked against a flat grey-brown grimy wall plane behind, no face, "
     "no gore"),
    (5, "Somebody dressed her.",
     "a close view of two flat dark green coat sleeves and a neat collar line on a still stick "
     "figure seen from behind, the coat hanging straight and ordered, flat #e5d3ba wall behind, "
     "no face visible"),
    (5, "You don't raise the rifle. The rifle makes a sound, and sound is a debt.",
     f"{SURV} in profile with a plain black single-stroke rifle silhouette slung low on his "
     "shoulder, both hands empty and open at his sides, flat beige #e5d3ba wall plane behind, "
     "flat #e5d3ba overcast sky above"),
    (5, "You take the alley instead.",
     f"{SURV} and {ASH} turning away from the viewer into a narrow gap between two flat "
     "#6b767f walls, the flat brown #75503b road behind them, generous empty wall plane above, "
     "no other figures"),

    # ---- slide 06: the alley ----
    (6, "The alley is full. Not a horde. A crowd.",
     "a narrow alley between two tall flat #6b767f wall planes, and standing in it twenty still "
     "stick figures packed shoulder to shoulder, all seen from behind, no faces visible, flat "
     "brown #75503b wet ground under them, flat #1e2d50 sky slot far above"),
    (6, "Twenty of them standing in the wet between two buildings, swaying like a field.",
     "twenty still stick figures packed in a narrow alley, all seen from behind, drawn leaning at "
     "slightly different angles like a field of stalks, single-stroke limbs, flat #6b767f walls "
     "either side, flat brown #75503b wet ground, no faces"),
    (6, "All of them waiting for something they've forgotten.",
     "the same packed crowd of still stick figures from behind, heads level and empty, drawn "
     "motionless, flat #6b767f alley walls, flat #1e2d50 sky slot above, no faces, no detail"),
    (6, "Ash goes rigid under your hand.",
     f"a close view of a single hand pressed flat on the back of {ASH}, the dog's legs stiff and "
     "straight, ears up, head level, flat brown #75503b ground, flat #6b767f alley wall behind"),
    (6, "You are sixteen steps from the mouth of that alley, and every step is a life you're spending.",
     f"{SURV} and {ASH} small and low at the right edge of the frame, seen from behind, the mouth "
     "of a packed alley in the left third, four short scratched step marks drawn on the flat "
     "brown #75503b ground between them, no faces, no readable writing"),
    (6, "Step one. Step four.",
     "an extreme close view of two dark boots mid-stride on a flat brown #75503b ground plane, "
     "three short hop-marks drawn behind them, no figures above the ankle, flat #6b767f wall "
     "grey in the background"),
    (6, "A can rolls out from under a car.",
     "a single plain flat ivory #f8f3dc can lying on its side on a flat brown #75503b road, two "
     "short curved motion-arc lines behind it, the flat grey #6b767f underside of a car "
     "silhouette at the top of the frame, no figures"),
    (6, "Twenty heads turn at once, one crowd inhaling the same idea.",
     "the packed crowd of still stick figures in the alley all turned toward the viewer at once, "
     "round white heads and black dot eyes now facing front in a single row, flat #6b767f walls "
     "either side, flat brown #75503b wet ground"),
    (6, "You run. Not smart, not quiet. Alive.",
     f"{SURV} running hard toward the viewer with {ASH} at his heel, both stretched into long "
     "cartoon action strides, four short speed-lines trailing behind them, flat brown #75503b "
     "road, flat beige #e5d3ba building planes either side"),

    # ---- slide 07: the laundromat ----
    (7, "The laundromat on the corner has a door that sticks.",
     "a shopfront seen square-on from the street, flat beige #e5d3ba wall, a flat #6b767f glass "
     "front with a plain brown #75503b door standing slightly ajar, three small grey drying "
     "machines visible through the glass, no signage, no lettering"),
    (7, "You get it open with your shoulder and your whole weight behind it.",
     f"{SURV} driving his shoulder against a plain brown #75503b door, body angled and one leg "
     "braced back, two short impact burst lines at the door edge, flat #6b767f glass front beside "
     "him, no text"),
    (7, "Inside, thirty dryers, a wall of detergent, and a radio behind the counter, still plugged in.",
     "the interior of a laundromat, two long flat rows of grey #6b767f drying machines with "
     "simple round door circles, a plain shelf of flat ivory #f8f3dc boxes along the top of the "
     "frame with no labels, a small grey radio on a counter at the right, flat #e5d3ba wall, flat "
     "brown #75503b floor, no figures, no lettering"),
    (7, "You never reach the pharmacy.",
     f"{SURV} standing still in the middle of the laundromat, seen from behind, head turned back "
     "toward the glass front and the flat brown #75503b road beyond it, flat grey #6b767f machine "
     "row either side, no other figures"),
    (7, "Iodine and rope, four blocks away, and you're running the other direction.",
     "a flat #6b767f shop window at dusk with three plain unlabelled flat ivory #f8f3dc bottles "
     "and one coil of flat brown #75503b rope visible behind the glass, flat beige #e5d3ba wall, "
     "flat #1e2d50 sky band above, empty street, no figures, no lettering"),
    (7, "You'll want the rope later. The body keeps its own accounts.",
     f"a close view of the slack free end of a flat brown #75503b rope coil hanging from {SURV}'s "
     "belt, his hand not touching it, flat brown #75503b floor behind, no text"),
    (7, "You have one idea. It's a bad one. It's the only one.",
     f"a close view of {SURV}'s face in three-quarter view, flat white head, two black dot eyes "
     "looking slightly aside, thin straight mouth, one short vertical line above the head as a "
     "thought mark, flat #e5d3ba wall behind"),
    (7, "You set the dryers to forty minutes and switch on every machine in the row.",
     "a long row of grey #6b767f drying machines seen square-on, every round door circle turned "
     "to the same angle, one hand at the far right of the frame reaching for the last dial, flat "
     "#e5d3ba wall above the machines, flat brown #75503b floor below"),
    (7, "Then you switch on the radio, loud enough to hurt.",
     "a close view of one grey #6b767f radio on a counter with a single round dial, five short "
     "sound-arc lines bursting from the speaker slits, a hand on the dial, flat #e5d3ba wall "
     "behind, no text"),
    (7, "The drums start. The whole street turns toward the glass.",
     "seen from inside a laundromat through the flat #6b767f glass front, the packed crowd of "
     "still stick figures out on the flat brown #75503b road all turned toward the window, seen "
     "from behind on the street side, hands flat on the glass on the near side of the surface, "
     "flat beige #e5d3ba building planes behind them"),
    (7, "You and Ash go out the back, into the rain, and you don't stop.",
     f"{SURV} and {ASH} running away from the viewer through a plain brown #75503b back doorway "
     "onto a flat #6b767f wet yard, five short slanted rain strokes across the frame, flat "
     "#1e2d50 sky above, no other figures"),

    # ---- slide 08: the bridge ----
    (8, "The east point is a mile of wet road and one long bridge.",
     "a long flat bridge deck seen square-on in flat elevation, flat brown #75503b deck band "
     "running the full width, simple black rail line above it, flat #1e2d50 water filling the "
     "lower third, flat #1e2d50 dusk sky in the upper third, empty, no figures, no perspective "
     "lines"),
    (8, "Halfway across, one comes up out of the dark beside the rail.",
     f"a single still stick figure rising up from behind the black bridge rail at the right of the "
     "frame, one flat ivory #f8f3dc hand on the rail on the viewer's side of it, {SURV} small at "
     f"the left of the frame in profile, flat #1e2d50 water and sky, flat brown #75503b deck"),
    (8, "Not fast. Just close. Close enough to hear the wet in its throat.",
     "a close view of one still stick figure's round white head and two black dot eyes in profile "
     "at the very edge of the frame, three short sound-arc lines at its throat, flat #1e2d50 "
     "water band behind, flat brown #75503b rail line at the bottom"),
    (8, "You put the pry bar against its shoulder and let its own weight do the rest.",
     f"a close action view of one plain black line as a pry bar pressed against a still stick "
     "figure's shoulder, two short impact burst lines at the contact point, flat #1e2d50 water "
     "behind, flat brown #75503b deck below, no gore, no detail"),
    (8, "It goes over quiet, like a coat sliding off a chair.",
     "a single still stick figure tipping backward past the black bridge rail, drawn small and "
     "simply, three short motion-arc lines trailing it, flat #1e2d50 water filling the frame "
     "below, empty dusk sky above, no gore, no splash, no detail"),
    (8, "You don't stop to feel anything about it. There'll be a year for that later, maybe.",
     f"{SURV} standing still in profile on the bridge deck with one hand lowered holding one "
     "plain black line, head down, flat brown #75503b deck, black rail line at his shoulder, "
     "flat #1e2d50 water beyond, no other figures"),
    (8, "On the bridge you can hear them behind you, a sound like a tide that learned to walk.",
     f"{SURV} seen from behind mid-step, and along the flat brown #75503b road behind him a long "
     "low line of twenty small still stick figures walking in a loose row, flat #1e2d50 dusk sky "
     "above, six short sound-arc lines drawn between the crowd and the viewer"),
    (8, "But the tide is going the wrong way now. Toward the music. Toward the drums.",
     "the same long loose row of small still stick figures seen from behind, now turned and "
     "walking away from the bridge toward a flat beige #e5d3ba building block at the far left, "
     "flat #1e2d50 dusk sky, flat brown #75503b road"),
    (8, "You don't look back. Looking back is a hobby for people with time.",
     f"{SURV} and {ASH} walking away from the viewer along a flat brown #75503b bridge deck, "
     "heads facing forward, black rail line either side, flat #1e2d50 water and sky, the "
     "survivor's back flat and still"),

    # ---- slide 09: the tower exterior ----
    (9, "The tower stands in a gravel lot above the marina, red light turning, turning.",
     "a slender flat grey #6b767f radio tower on a flat #e5d3ba gravel point, seen square-on and "
     "tall in the frame, one orange #ff8421 lamp housing near the top with two short motion-arc "
     "lines showing it mid-rotation, flat #1e2d50 night sky behind it"),
    (9, "There are boats down there, six of them, tied and waiting.",
     "a flat #1e2d50 marina water surface with six small flat ivory #f8f3dc boat shapes tied in a "
     "row along a flat brown #75503b dock, each drawn simply with one mast line, flat #1e2d50 "
     "night sky above, no figures"),
    (9, "Nobody has taken a boat. That's either very good news or very bad.",
     "an extreme close view of one flat brown #75503b dock cleat with a single flat ivory "
     "#f8f3dc rope line wrapped twice around it and hanging slack, flat #1e2d50 water below, "
     "empty, no figures, no text"),

    # ---- slide 10: the stairs ----
    (10, "Eleven o'clock comes while you're still climbing the stairs.",
     "a bare flat grey #6b767f metal stair tread spiralling upward in flat elevation with no "
     "vanishing point, a single pair of dark boots on the third tread, a black handrail line, "
     "flat #1e2d50 night in a narrow window slot at the edge, no figures above the ankle"),
    (10, "The voice starts above you, patient as a clock.",
     "a close view of a flat grey #6b767f ceiling-mounted speaker with simple horizontal slits, "
     "five short sound-arc lines spreading downward from it, flat #5e5653 ceiling plane, no "
     "figures, no text"),
    (10, "Angela Ruiz. Michael Osei. Priya Raman.",
     "three small flat ivory #f8f3dc rectangular card shapes floating in a loose column against "
     "a flat #5e5653 wall plane, each card blank apart from one short illegible black mark, no "
     "readable writing, no letters"),

    # ---- slide 11: the transmitter room ----
    (11, "You reach the transmitter room at eleven forty.",
     f"{SURV} standing in the open doorway of a small equipment room, seen from behind, flat grey "
     "#6b767f boxes stacked on a low shelf inside, flat #5e5653 walls, flat brown #75503b floor, "
     "one tall window with flat #1e2d50 night at the right"),
    (11, "The door is open. The machine is reading to an empty room.",
     "the transmitter room empty of people, seen from just outside the open doorway, flat grey "
     "#6b767f equipment boxes on a low shelf, a plain desk with a microphone on a short stand and "
     "a cassette deck, flat #5e5653 walls, flat brown #75503b floor, no figures"),
    (11, "There's a microphone on the desk. Beside it, a cassette case, and a pencil.",
     "a close view of the top of a plain flat #6b767f desk holding one microphone on a short "
     "stand, one flat brown #75503b cassette case lying flat, and one short flat ivory #f8f3dc "
     "pencil, flat #5e5653 wall behind, no text"),
    (11, "The pencil is sharpened. Somebody sharpened it.",
     "an extreme close view of one short flat ivory #f8f3dc pencil lying on a flat #6b767f desk "
     "surface, its black point carved to a sharp tip, three short emphasis lines drawn at the "
     "tip, flat #5e5653 wall, no text"),
    (11, "There's a logbook open on the desk. A column of days. A column of numbers.",
     "a close view of one open notebook lying flat on a plain desk, two columns of short "
     "illegible black marks ruled down the flat #f8f3dc pages, a short pencil lying in the gutter, "
     "flat #5e5653 wall behind, no readable writing, no letters"),
    (11, "The last entry is this morning. In pencil.",
     "an extreme close view of the bottom corner of one open notebook page, a single fresh short "
     "black mark at the end of the column, the pencil tip resting right beside it, flat #f8f3dc "
     "paper, flat #6b767f desk edge, no readable writing"),
    (11, "The tape ends at the end of the list, and the room goes quiet, and a little red light stays on, waiting.",
     "the transmitter room in close view, one small orange #ff8421 record light glowing on the "
     "flat #6b767f desk beside a silent cassette deck, flat #5e5653 walls, everything else still "
     "and empty, no figures, no text"),

    # ---- slide 12: the broadcast ----
    (12, "So you sit down.",
     f"{SURV} seated squarely in a plain flat #6b767f office chair behind the desk in the "
     "transmitter room, both hands flat on the desk surface, the microphone on its short stand "
     "in front of him, flat #5e5653 wall, one tall window with flat #1e2d50 night at the right"),
    (12, "You press the button, and you say your name like it's an address.",
     f"a close view of {SURV}'s hand pressing one round flat orange #ff8421 button on the desk, a "
     "thin black cable line running from the button to the microphone, flat #6b767f desk surface, "
     "flat #5e5653 wall behind"),
    (12, "Then you say his. Ash. Just Ash. It's the only name he's ever needed.",
     f"{SURV} in profile at the desk speaking into the microphone, and {ASH} sitting upright on "
     "the floor beside his chair looking up at him, flat #5e5653 walls, flat brown #75503b floor, "
     "one tall window with flat #1e2d50 night"),
    (12, "Seven hundred and ninety-six.",
     "a close view of one open notebook on a plain desk with a single short fresh black mark added "
     "at the bottom of a long column, the flat #f8f3dc page filling most of the frame, flat "
     "#6b767f desk edge below, no readable writing, no letters"),
    (12, "It's the wrong direction. You know it's the wrong direction.",
     f"{SURV} seen from behind standing at the tall tower window, looking out over flat #1e2d50 "
     "night sky and flat #1e2d50 water, one flat ivory #f8f3dc boat shape far below, flat "
     "#5e5653 wall and window frame, no other figures"),
    (12, "But it's a number, and you're in it, and tonight the count makes sense.",
     f"{SURV} standing small in the centre of the transmitter room with {ASH} at his heel, seen "
     "from behind, the whole flat #5e5653 room around them, one orange #ff8421 light on the desk "
     "the only warm point in the frame, generous empty wall above"),
    (12, "Whoever you are, listening. The door is unlocked.",
     "a plain brown #75503b door standing wide open in a flat #5e5653 wall, seen square-on from "
     "inside the room, flat #1e2d50 night visible through the opening, no figures, no text"),
    (12, "The pencil's sharp. Come east.",
     "an extreme close view of one short flat ivory #f8f3dc pencil lying diagonally on a bare "
     "flat #6b767f desk surface beside a single corridor of empty floor space, flat #5e5653 wall, "
     "no text"),
    (12, "If you're reading the list, you're already on it.",
     "one open notebook on a plain desk seen from directly above, a long column of short "
     "illegible black marks down the flat #f8f3dc page, the last three slightly darker than the "
     "rest, flat #6b767f desk surface around it, no readable writing"),
    (12, "That's all a list is. A door somebody left open.",
     "a wide exterior of the flat grey #6b767f radio tower at night seen from a low distance, one "
     "orange #ff8421 lamp glowing near the top with two short motion-arc lines, flat #1e2d50 sky "
     "and water, a small flat ivory #f8f3dc rectangle of lit window near the base, empty and "
     "still"),
]

STYLE_TAIL = (
    "Composition: flat elevation, camera square to the plane, no vanishing point, generous "
    "negative space. " + PALETTE
)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "visuals.csv")
    counts = {}
    rows = []
    for slide, text, vis in ROWS:
        counts[slide] = counts.get(slide, 0) + 1
        moment = counts[slide]
        rows.append({
            "slide_id": f"{slide:02d}",
            "moment": f"{moment:02d}",
            "moment_text": text,
            "visual_prompt": f"{STYLE} Subject: {vis}. {STYLE_TAIL}",
        })
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["slide_id", "moment", "moment_text", "visual_prompt"])
        w.writeheader()
        w.writerows(rows)

    words = sum(len(r["moment_text"].split()) for r in rows)
    print(f"rows: {len(rows)}")
    print(f"words carried in moment_text: {words}")
    print(f"projected runtime @3.1wps: {words / 3.1:.0f}s")
    print(f"slides: {len(counts)}")
    print("batches at B=8:", -(-len(rows) // 8))
    for s in sorted(counts):
        print(f"  slide {s:02d}: {counts[s]:2d} frames")


if __name__ == "__main__":
    main()
