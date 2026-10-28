#!/usr/bin/env python3
"""Builds zombie_survival_video/visuals.csv for script draft 3.

One row = one visual moment. moment_text is an exact contiguous substring of the
script; the rows in order concatenate back to the script body word-for-word.
Frame count is an OUTPUT of that split, never a target.
Run from repo root: python3 zombie_survival_video/build_spine.py
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

COMP = ("Composition: flat elevation, camera square to the plane, no vanishing point, "
        "one focal point, generous negative space. The subject fills the frame as the "
        "background plane itself — never drawn as a framed picture, inset panel, or "
        "rectangle floating on a wall. Any marks on paper are short straight tally "
        "strokes, evenly spaced, never cursive, never joined, never handwriting. ")

SURV = ("the survivor — a male stick figure, round white head, two black dot eyes, thin "
        "straight mouth, six short black hair strokes on top of the head, single-stroke black "
        "limbs with rounded ends, flat charcoal-grey hooded jacket worn open over a black torso "
        "stroke, flat olive-brown trousers on the leg strokes, dark boots, one shoulder-strap "
        "line across the chest")

ASH = ("Ash — a small stick-figure dog, round white head, two black dot eyes, single-stroke "
       "black legs and tail with rounded ends, two flat brown #473425 floppy ear shapes, one "
       "flat brown #473425 patch on the back of the body, thin straight mouth line, half the "
       "survivor's height at the shoulder")

# (slide, moment_text, visual clause)
ROWS = [
    # ================= SLIDE 01 — the cold open =================
    (1, "At eleven every night, the tower on the east point reads out the names of the living.",
     "a slender flat grey #6b767f radio tower standing alone on a flat #e5d3ba gravel point, "
     "seen square-on and tall in the frame, one orange #ff8421 lamp housing near the top with "
     "two short motion-arc lines showing it mid-rotation, flat #1e2d50 night sky behind it, "
     "flat #1e2d50 water band at its base, no figures"),
    (1, "It does not check whether you still are one.",
     "an extreme close view of a grey #6b767f radio speaker grille with simple horizontal slit "
     "lines, four short curved sound-arc lines spreading rightward from it, flat #5e5653 wall "
     "plane behind, no figures, no lettering"),
    (1, "Day four hundred and twelve. Third floor.",
     "an exterior of a flat four-storey building at night seen square-on, simple punch-hole "
     "windows in a grid, one window on the top floor lit flat ivory #f8f3dc, a column of short "
     "scratched tally marks drawn on the flat #e5d3ba wall beside the building, flat #1e2d50 "
     "sky above, flat brown #75503b road band below, no figures"),
    (1, "One dog, one rifle with four rounds in it, and a radio that keeps better hours than you do.",
     f"a close view of a bare flat #6b767f apartment table holding {ASH} sitting upright beside "
     "one plain black single-stroke rifle silhouette lying flat, four small flat ivory #f8f3dc "
     "round shapes in a neat row on the table top, and a small grey radio with one dial at the "
     "right, flat #e5d3ba wall behind"),
    (1, "Names, one at a time, slow. Then a number.",
     "a close view of one open notebook lying flat on a plain desk, flat #f8f3dc paper with two "
     "ruled columns drawn as thin black lines and short illegible black marks down them, one "
     "short stub pencil in the gutter, flat #5e5653 wall behind, no readable writing"),
    (1, "Last month, eight hundred and forty-one.",
     "a close view of a flat #e5d3ba wall covered in one long vertical column of short "
     "scratched tally marks, the column densely packed and running the full height of the "
     "frame, a separate small cluster of scratches off to the right, no readable writing, no "
     "figures"),
    (1, "Tonight, seven hundred and ninety-four.",
     "a close view of the same flat #e5d3ba wall with its long column of scratched tally marks, "
     "now with one fresh short scratch cut at the bottom of the column, three short emphasis "
     "lines drawn at that single mark, no readable writing, no figures"),
    (1, "You listen for your own name.",
     f"{SURV} seated on the floor in profile leaning toward a small grey radio on a low crate, "
     "one hand flat on the floor, head tipped toward the speaker, flat #e5d3ba wall planes, "
     "flat brown #75503b floorboard plane, flat #1e2d50 night in a tall window at the left edge"),
    (1, "You have listened for four hundred and twelve nights. It has never come.",
     f"{SURV} seated on the floor beside a small grey radio, seen from behind, the wall in front "
     "of him packed edge to edge in columns of short scratched tally marks, flat #e5d3ba wall, "
     "flat brown #75503b floor, no readable writing"),
    (1, "Four hundred and twelve nights of not being counted.",
     "a bare flat #e5d3ba wall filling the whole frame, covered top to bottom in columns of "
     "short scratched tally marks, four of them crossed through with a single diagonal line, no "
     "figures, no readable writing"),
    (1, "That is not loneliness. That is an audit.",
     "an extreme close view of one flat ivory #f8f3dc open notebook page with a ruled column and "
     "short illegible black marks, and one single blank empty row at the very bottom of the "
     "column, flat #6b767f desk edge below, no readable writing"),

    # ================= SLIDE 02 — first problem: the stairs =================
    (2, "First problem, the stairs.",
     "a bare concrete stairwell seen straight on, flat grey #6b767f steps receding upward in "
     "flat elevation with no vanishing point, a simple black handrail line, one narrow window "
     "slot with flat #1e2d50 night behind it, empty of figures"),
    (2, "Twelve floors, one staircase, and the door at the bottom opens inward. Inward is good.",
     "a flat #75503b stair door at the bottom of a stairwell, drawn slightly ajar and opening "
     "toward the camera, one small black arrow arc drawn on the floor showing the swing "
     "direction, flat grey #6b767f wall around it, no figures"),
    (2, "Inward means a crowd pushes it shut.",
     "seen from inside a stairwell, the flat #75503b stair door shut tight in a flat grey "
     "#6b767f wall, twenty small still stick figures pressed against the outside seen through "
     "the narrow window slot in the door, all seen from behind, hands flat on the near side of "
     "the glass, no faces visible"),
    (2, "You learn that on day nine, when you stop being able to sleep through the sound of weight on the other side of it.",
     f"{SURV} lying on a bare mattress in a dark stairwell landing, eyes open, seen from above, "
     "a column of short scratched tally marks on the wall beside the mattress with nine marks, "
     "a flat #75503b door in the wall at the right, flat #5e5653 walls, no other figures"),
    (2, "So you build the stairs into a job.",
     f"{SURV} standing small at the bottom of a tall stairwell looking up, both hands on his "
     "hips, flat grey #6b767f steps rising in a long flat run above him, one flat #6b767f "
     "upright piano shape already visible two floors up, no other figures"),
    (2, "The piano from the second floor landing, laid flat across the fourth.",
     "a flat #6b767f upright piano lying on its back across a stair landing, completely blocking "
     "the flat grey #6b767f stairway, its keyboard lid open, a simple black handrail line behind "
     "it, no figures"),
    (2, "Two fridges across the sixth.",
     "two flat ivory #f8f3dc refrigerator shapes lying on their backs side by side, wedged "
     "across a flat grey #6b767f stair landing and blocking it entirely, simple black door "
     "handle lines, flat #5e5653 wall behind, no figures"),
    (2, "Forty-one cans of paint at fourteen kilos each, stacked to the ceiling at the eighth.",
     "a wall of flat #6b767f paint cans with simple round lid circles stacked in a neat pyramid "
     "from floor to ceiling across a stair landing, a few flat #f0c667 and flat brown #75503b "
     "can shapes mixed in, flat grey #6b767f stairs behind, no labels on the cans, no figures"),
    (2, "That is five hundred and seventy-four kilos of paint. It takes eleven days.",
     f"{SURV} standing at the foot of a floor-to-ceiling wall of flat #6b767f paint cans, seen "
     "from behind, one hand raised flat against the bottom can, flat grey #6b767f stairwell "
     "walls, eleven short scratched tally marks drawn on the wall beside him"),
    (2, "It is the most useful thing you have ever done.",
     f"a wide view of a long stairwell entirely filled with barricade: a flat #6b767f piano, two "
     "flat ivory #f8f3dc fridges and a wall of flat #6b767f paint cans stacked in sequence up "
     "the flights, flat grey #6b767f walls, one small window slot of flat #1e2d50 night far "
     "above, no figures"),
    (2, "House rule one. Nobody gets in.",
     "a close view of a flat #e5d3ba wall with one short line of scratched marks drawn large and "
     "deliberate, three short emphasis lines around it, flat brown #75503b floorboard plane "
     "below, nothing else in the frame, no readable writing"),
    (2, "You write the rules on the wall in pencil.",
     f"{SURV} standing in profile beside a bare flat #e5d3ba wall with one arm raised, a short "
     "flat ivory #f8f3dc pencil against the plaster, three columns of short scratched marks "
     "already on the wall beside him, no readable writing"),
    (2, "When the pencil runs out, you use a nail.",
     "an extreme close view of a single hand holding one thin nail against a flat #e5d3ba wall, "
     "a short rounded pencil stub lying on the floor below at the bottom of the frame, two "
     "scratched lines already cut into the plaster, no readable writing"),
    (2, "There are nine rules. Six of them are the same rule.",
     "a flat #e5d3ba wall with nine separate short groups of scratched marks laid out in a grid, "
     "six of the groups drawn identical and three drawn different, no readable writing, no "
     "figures, flat brown #75503b floorboard plane at the bottom"),

    # ================= SLIDE 03 — second problem: the water =================
    (3, "Second problem, the water.",
     "a bare flat #6b767f bathroom wall with one plain tap and a simple pipe line running down "
     "into it, nothing coming out of the spout, flat #e5d3ba tile plane behind, no figures, no "
     "water drawn anywhere"),
    (3, "On day eight the taps cough and stop.",
     "an extreme close view of one flat #6b767f tap over a plain basin, two short broken "
     "pressure-arc lines escaping the spout, a single small flat #6b767f drip shape below it, "
     "flat #e5d3ba tile wall, no figures"),
    (3, "No power, no pumps, no water.",
     "a flat #6b767f rooftop water tank on a flat #e5d3ba roof plane, its simple pipe line "
     "running down and away out of frame, three short crossed-out marks drawn on the tank, flat "
     "#1e2d50 dusk sky behind, empty and still, no figures"),
    (3, "The bathtub on the second floor holds two hundred litres.",
     "a plain flat ivory #f8f3dc bathtub seen square-on from the side, filled to a flat "
     "#6b767f water line, small tick marks drawn up the inside of one end, flat #e5d3ba tile "
     "wall behind, flat brown #75503b floor plane, no figures"),
    (3, "You fill it on day two, before you understood anything, which is the only reason you are still alive.",
     f"{SURV} standing over a full flat ivory #f8f3dc bathtub, seen from behind, one hand "
     "resting on the rim, flat #6b767f water line inside it, two short scratched tally marks on "
     "the tile wall beside him, flat #e5d3ba tile, no other figures"),
    (3, "Two hundred litres is a hundred and fifty days at one litre a day. It is twenty days at ten.",
     "a close view of one flat ivory #f8f3dc measuring jug standing on a flat brown #75503b "
     "board, a single flat #6b767f water level drawn low inside it, two long columns of short "
     "scratched tally marks drawn on the wall left and right of it, no readable writing"),
    (3, "So you learn to be a one-litre man.",
     f"{SURV} sitting on a bare floor holding one small flat ivory #f8f3dc cup in both hands, "
     "head level, flat #e5d3ba wall plane behind him, flat brown #75503b floorboards, nothing "
     "else in the frame"),
    (3, "The dog gets a litre. You get a litre.",
     f"two identical flat ivory #f8f3dc cups standing side by side on a flat brown #75503b "
     "board, each with the same flat #6b767f water level drawn inside, {ASH} sitting to the "
     "right of the second cup looking at it, flat #e5d3ba wall behind"),
    (3, "You do not negotiate with the dog. You are not that far gone yet.",
     f"a close view of {ASH} sitting upright and looking directly at the viewer, head level, "
     "ears up, one flat ivory #f8f3dc cup on the floor in front of him, flat #e5d3ba wall plane "
     "behind, no other figures"),
    (3, "Rain is free. The roof is flat.",
     "a flat #e5d3ba rooftop plane seen square-on with a low parapet wall along the top of the "
     "frame, flat #6b767f sky band above, five short slanted rain strokes across the upper "
     "third, empty and still, no figures"),
    (3, "One bucket, one tarp, thirty-one millimetres of rain in April, which is thirty-one litres, if the bucket is level.",
     "a single flat #6b767f bucket standing on a flat #e5d3ba rooftop, a flat #f0c667 tarp "
     "stretched between two short poles above it and funnelling rain down into the bucket, five "
     "short slanted rain strokes, flat #1e2d50 sky band, no figures"),
    (3, "The bucket is not level.",
     "an extreme close view of one flat #6b767f bucket standing tilted on a flat #e5d3ba roof "
     "plane, water running over one lip in a thin flat #6b767f line, two short motion-arc lines "
     "at the spill, no figures"),
    (3, "You fix the bucket.",
     f"{SURV} crouched low on a flat #e5d3ba rooftop with both hands flat against the base of a "
     "flat #6b767f bucket, a small flat brown #75503b wedge shape pushed under one side, flat "
     "#1e2d50 sky band above, no other figures"),
    (3, "House rule four. Nobody goes on the roof after dark.",
     "a flat #e5d3ba rooftop parapet wall at night, a plain flat brown #75503b roof hatch "
     "standing closed and bolted at the centre, a short group of scratched marks on the parapet, "
     "flat #1e2d50 night sky above, no figures"),

    # ================= SLIDE 04 — third problem: the noise =================
    (4, "Third problem, the noise.",
     "a close view of a small grey #6b767f radio standing on a bare flat brown #75503b board, "
     "three short sound-arc lines rising from it, flat #e5d3ba wall plane behind, nothing else "
     "in the frame, no figures"),
    (4, "The tower reads from eleven to eleven forty. You have to hear it.",
     f"{SURV} seated in profile at a bare table with a small grey radio in front of him, head "
     "tipped toward it, one hand flat on the table top, flat #e5d3ba wall behind, a tall window "
     "with flat #1e2d50 night at the left edge"),
    (4, "To hear it, the radio has to be on, and the radio on is a six-watt speaker in a room with a window in it.",
     "a flat #e5d3ba room seen square-on from outside at night, with one tall window showing a "
     "small grey #6b767f radio silhouette inside and four short sound-arc lines drawn escaping "
     "through the window pane outward, flat #1e2d50 night around the building, no figures"),
    (4, "So you do the arithmetic.",
     f"{SURV} standing at a bare flat #e5d3ba wall with one arm raised, three short columns of "
     "scratched marks running down the plaster beside him, flat brown #75503b floorboard plane, "
     "no readable writing, no other figures"),
    (4, "Forty minutes of sound, once a night, at the back of the flat, behind two doors and a mattress.",
     "a flat #e5d3ba interior seen in one flat elevation looking down a short corridor: one "
     "plain flat brown #75503b door standing open, a second door beyond it standing open, and a "
     "bare mattress leaning flat against the far wall, a small grey radio shape at the end, flat "
     "#5e5653 walls, no figures"),
    (4, "That is the price of knowing whether you still exist.",
     "an extreme close view of one small grey #6b767f radio dial with a single black pointer "
     "line, four short sound-arc lines rising from the speaker slits, a flat ivory #f8f3dc "
     "notebook edge lying beside it on a flat brown #75503b board, no figures"),
    (4, "Most nights it costs nothing.",
     f"{SURV} asleep on a bare mattress in profile, eyes closed, one hand under his head, "
     f"{ASH} curled flat on the floor beside the mattress, a small grey radio on a crate at the "
     "far right with two short quiet sound-arc lines, flat #e5d3ba walls, flat #1e2d50 night in "
     "a tall window"),
    (4, "On the twenty-eighth, it costs the hallway.",
     "a bare flat #5e5653 hallway seen straight down in flat elevation with no vanishing point, "
     "one plain flat brown #75503b door at the far end standing open, twenty small still stick "
     "figures packed in the corridor all seen from behind, no faces visible, flat brown #75503b "
     "floor plane"),
    (4, "Something comes up as far as the eighth floor and leans on the paint for nine hours.",
     "a wall of flat #6b767f paint cans stacked across a flat grey #6b767f stair landing, with "
     "one small still stick figure pressed flat against the near side of the top row, seen from "
     "behind, arms spread on the cans, no face visible, three short sound-arc lines at the cans"),
    (4, "You listen to it lean.",
     f"a close view of {SURV}'s face in profile in the dark, eyes open, head tipped toward a "
     "flat #5e5653 wall, one hand flat on the wall, three short quiet sound-arc lines coming "
     "through it, flat #1e2d50 darkness around, one small orange #ff8421 point of light far off "
     "at the edge"),
    (4, "You do not get your name that night, because the radio was off.",
     "an extreme close view of one small grey #6b767f radio with its single dial turned all the "
     "way down to the left, one short crossed-out mark drawn beside it on the flat brown "
     "#75503b board, flat #5e5653 wall behind, no sound-arc lines anywhere, no figures"),
    (4, "House rule seven. You can miss the list. You cannot miss the door.",
     "a close view of a flat #e5d3ba wall with two short groups of scratched marks: one group "
     "lightly scored and one group cut deeper with three short emphasis lines around it, flat "
     "brown #75503b floorboard plane below, no readable writing, no figures"),

    # ================= SLIDE 05 — fourth problem: the living =================
    (5, "Fourth problem, the living.",
     "a wide flat brown #75503b road surface at dusk seen square-on with one flat grey #6b767f "
     "truck silhouette parked at the far right, flat #e5d3ba building faces behind it, flat "
     "#1e2d50 sky band above, no figures"),
    (5, "Day two hundred and ninety. A truck pulls into the street below.",
     f"seen from a high window, a flat grey #6b767f truck standing on a flat brown #75503b "
     "street below, four short motion-arc lines behind its wheels, {SURV} small in the bottom "
     "corner of the frame seen from behind at a flat #5e5653 window sill, no other figures"),
    (5, "Working engine, which means working fuel, which means somebody out there has a supply and the patience to defend it.",
     "an extreme close view of the flat grey #6b767f nose of a truck with three short exhaust "
     "puff arcs rising from a simple pipe line, a single flat #f0c667 jerry can shape standing "
     "on the flat brown #75503b road beside it, no figures, no lettering"),
    (5, "Three men and a woman spend four hours measuring your building from the road.",
     "four small stick figures standing in a loose row on a flat brown #75503b road, all seen "
     "from behind, looking up at a tall flat #e5d3ba building face, one of them holding a short "
     "black measuring line, flat #1e2d50 dusk sky, no faces visible"),
    (5, "They are not counting exits. They are counting windows.",
     "a tall flat #e5d3ba building face seen square-on with a grid of simple punch-hole windows, "
     "four of them circled lightly with short black arcs, and one plain flat brown #75503b "
     "doorway at the bottom left left uncircled, no figures, no lettering"),
    (5, "You do the arithmetic before they finish.",
     f"{SURV} standing just inside a flat #5e5653 window, seen from behind, one hand flat on the "
     "sill, head turned down toward the street, three short columns of scratched marks on the "
     "wall beside the window, flat #1e2d50 dusk light, no other figures"),
    (5, "If they come in, the stairs come down.",
     "a stairwell landing with a flat #6b767f piano lying across it, three short collapse-arc "
     "lines drawn at its underside, one flat #6b767f paint can tipping off the top of the stack "
     "above with a short motion line, flat grey #6b767f walls, no figures"),
    (5, "If the stairs come down, everything below the eighth floor gets to meet everything above it.",
     "a tall cutaway of a flat grey #6b767f stairwell drawn as simple stacked floor bars, twenty "
     "small still stick figures packed on one floor bar and one single small figure standing "
     "alone on a higher bar, all seen from behind, no faces, flat #1e2d50 dark around them"),
    (5, "So you do not fight them. You leave a note on the windscreen.",
     f"an extreme close view of one flat ivory #f8f3dc folded paper wedged under a flat #6b767f "
     "windscreen wiper, seen square-on, a hand reaching in from the right edge of the frame, "
     "flat grey #6b767f truck body behind, no readable writing on the paper"),
    (5, "Pencil, block capitals. Building is sealed. There is food on the roof. Come up alone.",
     "a close view of one flat ivory #f8f3dc sheet of paper held flat, covered edge to edge in "
     "short heavy illegible black block marks all the same size, a short pencil stub lying "
     "diagonally across the bottom corner, no readable letters, no figures"),
    (5, "Nobody comes up alone.",
     "a flat brown #75503b street at dusk seen square-on, completely empty of figures, one flat "
     "ivory #f8f3dc note shape peeled off and lying flat on the ground, flat #e5d3ba building "
     "faces either side, flat #1e2d50 sky band above"),

    # ================= SLIDE 06 — the number moves =================
    (6, "Then the night the number moves.",
     "an extreme close view of a flat #e5d3ba wall with one long column of scratched tally "
     "marks, a single fresh scratch cut below the last one with three short emphasis lines "
     "around it, flat #1e2d50 night light on the plaster, no figures, no readable writing"),
    (6, "Seven hundred and ninety-five.",
     "a small grey #6b767f radio seen in close view on a bare flat brown #75503b board, four "
     "short sound-arc lines rising from it, the wall behind washed flat #5e5653, nothing else in "
     "the frame, no readable writing, no figures"),
    (6, "You play it back twice to be certain.",
     f"{SURV} lying on his side on a bare mattress in the dark with one hand flat on a small "
     "grey radio beside him, head close to the speaker, eyes open, flat #5e5653 walls, flat "
     "#1e2d50 darkness, no other figures"),
    (6, "Eight forty-one, seven ninety-four, seven ninety-four, seven ninety-four, and tonight, seven ninety-five.",
     "a flat #e5d3ba wall with five separate columns of scratched tally marks in a row, the "
     "first column long, the next three identical and slightly shorter, the last one with a "
     "single fresh mark at its base, no readable writing, no figures"),
    (6, "Somebody at that tower heard a name and wrote it down.",
     "an extreme close view of one hand holding a short flat ivory #f8f3dc pencil against an "
     "open flat ivory #f8f3dc notebook page, one fresh short black mark being drawn at the "
     "bottom of a long ruled column, three short emphasis lines at the pencil tip, no readable "
     "writing"),
    (6, "You are on the list. Four hundred and thirteen days late, and you are on it.",
     f"{SURV} standing square-on in the centre of the frame looking directly out toward the "
     "viewer, both arms hanging at his sides, lit from one side by flat #1e2d50 night, the "
     "columns of scratched marks on the flat #e5d3ba wall behind him, no other figures"),
    (6, "And that is a problem, because a broadcast is not a phone call.",
     "a slender flat grey #6b767f radio tower seen from a distance, twelve long flat #f8f3dc "
     "sound-arc rings radiating outward from its top in every direction across a flat #1e2d50 "
     "night sky, flat #e5d3ba gravel band at the base, no figures"),
    (6, "It goes out in every direction, at once, to anything with a radio and no reason not to walk toward the sound of one.",
     "a wide flat #1e2d50 night city drawn as simple stepped block silhouettes, and along the "
     "flat brown #75503b roads between them forty small still stick figures all facing the same "
     "way, walking toward one small orange #ff8421 point of light on a tower at the far right, "
     "all seen from behind, no faces visible"),

    # ================= SLIDE 07 — the thing nobody tells you =================
    (7, "Here is the thing nobody tells you about the dead.",
     "twenty small still stick figures drawn in a loose row on a flat brown #75503b road, all "
     "seen from behind, all facing the same direction, flat #e5d3ba building faces either side, "
     "flat #e5d3ba overcast sky band above, no faces visible"),
    (7, "They are not hunting you. They are still going where they were going.",
     "twenty small still stick figures walking in a single loose column along a flat brown "
     "#75503b road away from the viewer, simple flat #6b767f shopfront shapes either side, no "
     "faces visible, flat #e5d3ba overcast sky"),
    (7, "Every one of them is on the way to work, or the shops, or home.",
     "a flat #6b767f shopfront shown square-on with a plain flat brown #75503b door and one "
     "simple awning line, twenty small still stick figures standing in a loose queue in front of "
     "it all seen from behind, one of them with a flat #f0c667 bag shape, no faces, no lettering"),
    (7, "You have four hundred and twelve days of evidence and not one of them has ever knocked.",
     "an extreme close view of one plain flat brown #75503b door seen square-on from inside, its "
     "surface completely unmarked and smooth, a single hand flat against the near side of it at "
     "the left edge of the frame, flat #5e5653 wall around the opening, nothing else"),

    # ================= SLIDE 08 — inventory =================
    (8, "Day four hundred and thirteen. Inventory.",
     "a flat #e5d3ba wall with a fresh column of short scratched tally marks drawn cleanly down "
     "it, the top mark cut deeper than the rest with three short emphasis lines, flat brown "
     "#75503b floorboard plane below, no readable writing, no figures"),
    (8, "People, one. Dog, one.",
     f"{SURV} standing in the centre of a bare flat #e5d3ba room with {ASH} sitting at his heel, "
     "seen square-on in flat elevation, generous empty wall on both sides of them, flat brown "
     "#75503b floor plane, nothing else in the room"),
    (8, "Rifle, four rounds. Cans, two hundred and six.",
     "a close view of a bare flat brown #75503b board holding one plain black single-stroke "
     "rifle silhouette lying flat, four small flat ivory #f8f3dc round shapes in a neat row "
     "beside it, and one row of flat #6b767f can shapes receding to the right, flat #5e5653 wall "
     "behind, no lettering"),
    (8, "Names, one.",
     "an extreme close view of one open flat ivory #f8f3dc notebook page with a long ruled "
     "column of short illegible black marks, and one single mark sitting alone under the column "
     "with a short gap above it, flat #6b767f desk edge below, no readable writing"),

    # ================= SLIDE 09 — three knocks =================
    (9, "Then, tonight, at eleven fifty, three knocks on the stair door.",
     "a plain flat brown #75503b stair door seen square-on, completely closed and sealed, three "
     "short flat #f8f3dc impact burst marks drawn on its surface in a row, flat #5e5653 wall "
     "around it, flat #1e2d50 darkness either side, no figures"),
    (9, "A pause.",
     "an extreme close view of the same flat brown #75503b door surface, empty and unmarked, "
     "with one small flat ivory #f8f3dc clock face shape drawn in the top corner and a single "
     "short gap mark between two scratches, flat #5e5653 wall edge at the left, no figures"),
    (9, "Three more.",
     "the flat brown #75503b door seen square-on with six short flat #f8f3dc impact burst marks "
     "in two rows of three, the second row drawn slightly lower and harder, flat #5e5653 wall "
     "around it, no figures, no lettering"),
    (9, "You stand at a door you spent eleven days sealing, with the nail in one hand and the pencil in the other, and you do the only sum that has ever mattered.",
     f"{SURV} standing squarely in front of a sealed flat brown #75503b door, seen from behind, "
     "one thin nail in his left hand and one short flat ivory #f8f3dc pencil in his right, the "
     "wall of flat #6b767f paint cans visible behind him on the landing, flat #5e5653 walls, no "
     "other figures"),
    (9, "If you open it, everything below the eighth floor comes up.",
     "a tall cutaway of a flat grey #6b767f stairwell drawn as simple stacked floor bars, forty "
     "small still stick figures packed on the lower bars all facing upward, seen from behind, "
     "one plain flat brown #75503b door standing open at the top bar, no faces visible"),
    (9, "If you do not, you go back to being a number nobody wrote down.",
     "a flat #e5d3ba wall with one long column of scratched tally marks that simply stops, the "
     "plaster below the last mark completely bare and clean, flat #1e2d50 night light on the "
     "surface, no figures, no readable writing"),
    (9, "House rule one, amended.",
     "an extreme close view of a flat #e5d3ba wall with one short group of scratched marks, and "
     "a single fresh line drawn through it at an angle, a short flat ivory #f8f3dc pencil stub "
     "resting against the plaster below, no readable writing, no figures"),
    (9, "Nobody gets in. Unless they knock.",
     "a plain flat brown #75503b door seen square-on, standing wide open onto flat #1e2d50 "
     "night, three short flat #f8f3dc impact burst marks on the door face, one small orange "
     "#ff8421 point of light visible in the dark beyond it, flat #5e5653 wall around the "
     "opening, no figures"),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "visuals.csv")
    counts, rows = {}, []
    for slide, text, vis in ROWS:
        counts[slide] = counts.get(slide, 0) + 1
        rows.append({
            "slide_id": f"{slide:02d}",
            "moment": f"{counts[slide]:02d}",
            "moment_text": text,
            "visual_prompt": f"{STYLE} Subject: {vis}. {COMP}{PALETTE}",
        })

    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["slide_id", "moment", "moment_text", "visual_prompt"])
        w.writeheader()
        w.writerows(rows)

    # verification: rows in order must rebuild the script body word-for-word
    body = open(os.path.join(here, "script.md"), encoding="utf-8").read().split("---", 1)[1]
    script_words = body.split()
    csv_words = " ".join(r["moment_text"] for r in rows).split()
    ok = script_words == csv_words

    print(f"rows: {len(rows)}")
    print(f"slides: {len(counts)}")
    print(f"script words: {len(script_words)}  |  csv words: {len(csv_words)}")
    print(f"VERBATIM RECONSTRUCTION: {'PASS' if ok else 'FAIL'}")
    print(f"projected runtime @3.1wps: {len(csv_words)/3.1:.0f}s")
    print(f"batches at B=8: {-(-len(rows)//8)}")
    for s in sorted(counts):
        print(f"  slide {s:02d}: {counts[s]:2d} moments")
    if not ok:
        for i, (a, b) in enumerate(zip(script_words, csv_words)):
            if a != b:
                print(f"  first divergence at word {i}: script={a!r} csv={b!r}")
                break
        raise SystemExit(1)


if __name__ == "__main__":
    main()
