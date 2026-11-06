#!/usr/bin/env python3
"""Spine builder + validator for word-reactive frames.

The spine is `visuals.csv`: one row per spoken micro-beat. Each `moment_text`
MUST be a verbatim, unique, in-order substring of the narration, because Kaggle
matches those words against edge-tts WordBoundary timestamps to set cut points.
Nothing here sets a duration. Durations are measured.

Usage:
    python tools/spine.py build --repo .     # write visuals.csv from BEATS
    python tools/spine.py check --repo .     # validate an existing visuals.csv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

PROJECT = "broken_leg_video"

# (slide_id, moment_text verbatim from the narration, visual_prompt)
# Slide ids are scene blocks, not acts. Moment numbers are assigned per slide.
BEATS: list[tuple[int, str, str]] = [
    # --- 01 hillside, the snap -------------------------------------------------
    (1, "You are three hours from camp,", "Extreme wide static shot, a bare ridge line under a low ochre sun, a single line of five small figures crossing a stone slope, the nearest one to camera."),
    (1, "on a slope of loose stone,", "Low angle close shot of loose scree, a boot sole skidding sideways, dust puffing out from under the heel."),
    (1, "and the sun is already dropping behind the ridge.", "Wide backlit shot, the group reduced to long shadows, the sun half-eaten by the ridge, sky the colour of weak tea."),
    (1, "The rock under your foot rolls.", "Insert shot, a flat round stone turning over on its edge, a thin ribbon of dust, the toe of a hide boot just above it."),
    (1, "You hear the crack before you feel it.", "Tight static close-up on the protagonist's round white face, dot eyes flung wide, two small ink burst marks beside one ear."),
    (1, "A wet snap, close, like a green branch breaking under a boot.", "Insert shot on dark ground, a thin green branch snapped clean in two, pale wood showing at the break, no other objects."),
    (1, "Then your leg folds the wrong way", "Medium static shot, the protagonist collapsing mid-stride, one lower leg bent at a wrong angle, drawn as flat shapes, no gore."),
    (1, "and you are on your side,", "Ground-level shot, the protagonist lying on one side in the dust, cheek against the stones, arms folded near the chest."),
    (1, "and every bird on the hillside goes quiet.", "Wide empty sky above the ridge, not one bird, dry grass standing perfectly still, unnaturally calm."),

    # --- 02 nobody runs --------------------------------------------------------
    (2, "Nobody runs to you.", "Very wide flat shot, five figures standing on the slope at a distance, the fallen protagonist small in the foreground, miles of stone between them."),
    (2, "That is the first thing you notice.", "Over-the-shoulder shot from where the protagonist lies, four standing figures framed between two rocks, all facing camera, motionless."),
    (2, "Four people stop, and none of them move.", "Static tableau, four band members in a row on the slope, arms slack, weight on both feet, absolutely still, dust settling around them."),
    (2, "They are not being cruel.", "Close-up on one band member's face, flat neutral expression, tired eyes, no anger, no pity, just calculation."),
    (2, "They are doing arithmetic.", "Medium shot of a band member looking from the fallen protagonist to the distant horizon and back, eyes tracking the distance, hands loose at their sides."),

    # --- 03 the cost of a working pair of legs ---------------------------------
    (3, "A human on two working legs can walk all day", "Side-on wide shot, two figures walking steadily across a plain with long strides, one carrying a bundle, the horizon flat and endless."),
    (3, "and still carry something home.", "Medium shot, a band member walking toward camera with a wrapped joint of meat balanced across one shoulder, unhurried."),
    (3, "Take that away", "Close shot of the protagonist's useless leg lying flat in the dust, drawn as a simple shape, no wound, no blood, just wrong."),
    (3, "and you are not an injured person out here.", "Wide shot of the protagonist alone on the ground, the rest of the band small and far away on the ridge line, the space between them enormous."),
    (3, "You are a weight,", "Insert shot, a hide sling being hauled up off the ground with a body-shaped bundle in it, the hide stretched taut, two hands gripping."),
    (3, "measured in water, meat, warmth, and danger.", "Flat overhead still life on bare earth: a leaking water skin, a strip of dried meat, a burning brand, and a single animal eye in shadow, spaced evenly."),
    (3, "And the band is small.", "Wide static shot of a small cave camp at dusk, a handful of figures around a low fire, hides and racks, the cave mouth swallowing the light."),
    (3, "Twelve people, maybe fifteen,", "Medium wide shot, the whole band gathered and visible at once, twelve or so figures of different heights, the fire at the centre."),
    (3, "of whom four are children.", "Low shot of four small figures running past the fire, bare feet, oversized hides, the adults' legs behind them."),
    (3, "There is no surplus to draw on.", "Insert shot of a drying rack almost empty, two thin strips of meat hanging, the frame otherwise bare."),
    (3, "Every mouthful given to you", "Close shot of two hands passing a small piece of food from one palm to another, firelight between the fingers."),
    (3, "was carried by somebody else's legs.", "Wide shot, a hunter walking back from a long way off, small against the plain, a heavy load on their back, the camp tiny in the distance."),

    # --- 04 what keeping you alive means ---------------------------------------
    (4, "Keeping you alive means someone hauls water to you.", "Medium shot, a band member climbing a steep slope with a full water skin across their shoulders, water darkening the hide where it leaks."),
    (4, "Someone shares meat they earned.", "Close shot, a hand tearing a strip of meat in half and holding one half out to another hand, firelit, unceremonious."),
    (4, "Someone keeps a fire going through a cold night,", "Night shot inside the cave, one figure crouched at the fire feeding it twigs, snow blowing past the cave mouth behind them."),
    (4, "and someone stays awake to watch the dark,", "Night shot, a band member sitting with their back to the fire facing out into the black, a spear across their knees, alert."),
    (4, "because a body that cannot run", "Medium shot, the protagonist's leg stretched out uselessly beside the fire, the rest of the band standing around it, none of them sitting."),
    (4, "is a body that smells like an ending.", "Wide night shot, two pairs of predator eyes at the edge of the firelight, low to the ground, shapes barely readable in the dark."),

    # --- 05 the camp cannot wait -----------------------------------------------
    (5, "And the camp cannot simply wait.", "Medium shot of a camp being half-dismantled, hides rolled, racks taken down, figures glancing at the horizon while they work."),
    (5, "The animals move.", "Wide shot of a herd crossing a far plain in a long line, dust hanging over them, the camp tiny in the foreground."),
    (5, "The water sours.", "Insert shot of a still brown pool, a skin of scum across the surface, a dead leaf floating in the middle."),
    (5, "The season turns", "Wide shot of a snow line crawling down a ridge, grey sky above, the last of the grass bending under the wind."),
    (5, "whether or not your leg has healed.", "Close shot of the protagonist's leg wrapped in a hide bandage beside a low fire, the bone underneath shown as a faint line, unhealed."),

    # --- 06 the question -------------------------------------------------------
    (6, "So the question on that hillside is not a kind one.", "Ground-level wide shot, four band members standing over the fallen protagonist as dark silhouettes, the sky bright behind them, faces unreadable."),
    (6, "It is exact.", "Hard static close-up on a single face, mouth flat, eyes level, no expression at all, firelit ochre on one cheek."),
    (6, "Do these four people spend the next three months carrying you,", "Imagined wide shot, four figures carrying a hide stretcher across a plain, snow and green and snow again painted as bands behind them."),
    (6, "or do they spend one afternoon saying goodbye?", "Imagined static shot, a shallow scrape in the earth with a single flat stone beside it, no body visible, the band standing far off with their backs turned."),

    # --- 07 animals ------------------------------------------------------------
    (7, "Most animals never have to answer that.", "Wide shot, a limping deer falling behind a moving herd on a plain, the herd already small in the distance."),
    (7, "Injured animals are left behind.", "Wide shot, a limping wolf trailing a pack across snow, the pack's tracks ahead, the gap widening."),
    (7, "It is not malice.", "Static close-up of an animal's face, blank and calm, no snarl, no threat, simply unbothered."),
    (7, "It is arithmetic.", "Very wide shot, the herd gone over the ridge, one small shape standing alone in the middle of an empty plain."),

    # --- 08 but you are not most animals ---------------------------------------
    (8, "But you are not most animals.", "Wide shot, the four figures on the ridge turning back toward camera at the same moment, silhouetted against the low sun."),
    (8, "And fifty thousand years later, we know what your kind chose,", "Hard cut to a modern museum drawer sliding open, a single long bone on grey foam, cold white light."),
    (8, "because bone keeps a diary.", "Macro shot of the bone surface with one healed seam picked out in ochre, everything else cool grey, the seam like a written line."),

    # --- 09 bone ---------------------------------------------------------------
    (9, "Bone is not scaffolding.", "Flat diagram-style shot of a long bone as a simple cut shape on cream paper, no machinery, no labels, just the form."),
    (9, "It is living tissue that rebuilds itself,", "Cutaway of the same bone, its inside drawn as soft porous texture with tiny dots moving through it, alive rather than solid."),
    (9, "and it leaves a record of every repair.", "Close shot of a bone shaft with three faint healed seams picked out in ochre, each one a different age."),
    (9, "Break a leg and the body floods the gap with blood,", "Diagram shot, a clean break in a bone, the gap filled with a warm red wash, contained and simple, no splatter."),
    (9, "then builds a soft bridge of cartilage across it,", "Same framing, the gap now spanned by a pale blue-grey bridge, soft edged, translucent."),
    (9, "then hardens that bridge into new bone.", "Same framing, the bridge turned ochre and solid, the seam visible but closed, edges still lumpy."),
    (9, "Weeks pass.", "Wide static shot of a cave floor, a bar of sunlight crawling across the dust from one rock to another, shadows long."),
    (9, "Months pass.", "Wide static shot of the same ridge, snow retreating upslope, green showing through, the light warmer."),
    (9, "The new bone slowly remodels itself", "Macro shot of the bone surface, the lumpy seam smoothing grain by grain, ochre fading into ordinary bone."),
    (9, "into something that almost matches the old shape.", "Full bone shot, straight and whole, one faint line left where the break was, almost invisible."),
    (9, "If you die in the first days, the bone shows nothing.", "Cold static shot, a clean break with sharp square edges, no swelling, background drained of warmth."),
    (9, "A clean break with no healing at all.", "Extreme close-up of the same break, edges sharp as flint flakes, nothing growing across the gap."),
    (9, "If you live for a while, the edges round off and swell.", "Close-up, the break's edges rounded and puffed out, a soft collar around the gap, healing underway."),
    (9, "If you live for months, the fracture line closes and the limb knits.", "Close-up, the seam closed and smooth, the bone continuous again, one ochre line the only evidence."),
    (9, "Which means a healed fracture is not a medical record.", "Bone lying on a plain museum table, evenly lit, nothing dramatic, just an object."),
    (9, "It is a witness statement.", "Same bone under a single spotlight, a faint ink halo around it, the healed line catching the light."),
    (9, "Someone survived long enough to heal,", "Warm cave shot, a figure lying on a hide being tended, a damp cloth pressed to the forehead, fire low."),
    (9, "and out here, surviving long enough means someone else was involved.", "Close shot of four hands near a fire, one passing water toward a body just out of frame, faces in shadow."),

    # --- 10 discovery ----------------------------------------------------------
    (10, "In 1957, in a cave in the mountains of northern Iraq,", "Wide exterior shot of a cave mouth in a dry mountain range, a small field camp with canvas tents and crates below it, mid-century tools."),
    (10, "excavators pulled a skeleton out of the dirt", "Medium shot of a shallow trench, brushes and a trowel, a skeleton partly revealed in the soil, drawn cleanly, no gore."),
    (10, "that reads like that statement.", "Overhead shot of the skeleton laid out in the trench, its outline traced with a thin ink line like a page of handwriting."),

    # --- 11 Shanidar 1 ---------------------------------------------------------
    (11, "He is called Shanidar 1.", "Close profile shot of a fossil skull on a workbench, ochre lamplight from one side, dust in the air."),
    (11, "He lived between fifty and seventy thousand years ago,", "Wide imagined shot of the same cave full of life, fire at the mouth, an ice-age plain beyond, figures wrapped in hides."),
    (11, "and he was somewhere between forty and fifty when he died,", "Medium shot of an older Neanderthal man seated near the fire, grey streaked through his hair, a hide across his shoulders."),
    (11, "which for a Neanderthal was old.", "Close shot of the same face, deeply lined, patient, the firelight picking out the worn cheekbones."),
    (11, "He is the most famous damaged person in prehistory,", "Wide museum shot, a lit case holding a skeleton reconstruction, three modern visitor silhouettes standing in front of it."),
    (11, "and every one of his injuries had healed before he died.", "Diagram shot of the whole skeleton with six small ochre dots marking healed places, evenly lit, no labels."),

    # --- 12 the injuries -------------------------------------------------------
    (12, "A crushing blow had broken his left eye socket", "Close shot of the skull's left eye socket, flattened and misshapen on one side, clean bone, no blood, no wound."),
    (12, "and flattened that side of his face.", "Two static profile shots of the same skull side by side, one side rounded, the other pressed flat, identical lighting."),
    (12, "His right forearm and hand were gone,", "Medium shot of an arm ending in a smooth rounded stump below the elbow, hide sleeve folded back, drawn plainly."),
    (12, "the bone closed and smoothed over,", "Macro shot of the rounded bone end, surface worn smooth, no sharp edges, pale against dark cloth."),
    (12, "and we cannot tell whether that was surgery, an accident, or something he was born with.", "Still life: the smoothed bone end on linen, a flint flake beside it, a round river stone opposite, three possible stories, no answer."),
    (12, "Bony growths had sealed his right ear canal,", "Cutaway diagram of an ear canal choked by bony growths, drawn as simple interlocking shapes on cream paper."),
    (12, "so he was deaf on that side at least.", "Medium shot of the older man with one hand cupped behind his ear, the other side of his head blank of any sound marks."),
    (12, "His spine had stiffened into a single column.", "Diagram shot of a spine with its joints fused into one straight rod, ochre highlights along the fused section."),
    (12, "His front teeth were worn down to the roots.", "Close shot of a lower jaw, the front teeth ground flat to the gumline, dark roots showing, clinical and calm."),

    # --- 13 the foot -----------------------------------------------------------
    (13, "And his right foot carries a healed fracture", "Close diagram of foot bones, one long bone with a visible healed lump halfway along, ochre ring around it."),
    (13, "in a bone that bears your weight when you walk.", "Side shot of a bare foot mid-step, weight landing on the outside edge, a small ochre glow where the bone takes the load."),

    # --- 14 he lived -----------------------------------------------------------
    (14, "None of that killed him.", "Static wide shot of the complete skeleton laid out evenly on a table, orderly, unremarkable, no drama."),
    (14, "He lived for years afterwards,", "Wide shot of the cave mouth through four seasons at once, snow, green, dry, snow, each band a flat stripe of colour."),
    (14, "probably a decade or more,", "Medium shot of the older man seated in the same spot, hair now fully grey, the fire rebuilt beside him."),
    (14, "and he most likely died in a rockfall in the cave,", "Wide shot inside the cave, a scatter of fallen boulders and dust hanging in a shaft of light, the fire gone out."),
    (14, "not of his wounds.", "Close shot of the healed bones in shadow, the old seams plain and closed, nothing recent on them."),

    # --- 15 backwards arithmetic -----------------------------------------------
    (15, "So follow the arithmetic backwards.", "Flat overhead still life again, water skin, meat, brand and animal eye, lit from the opposite side, shadows pointing the other way."),
    (15, "A man who could not hear well,", "Close shot of the older man's head turned sharply, one ear toward the fire, the other side dead to the room."),
    (15, "could not see well,", "Extreme close-up of one eye squinting, the iris flat and pale, the other eye out of focus behind it."),
    (15, "could not hunt,", "Wide shot, three hunters walking out of camp with spears, the older man seated by the fire, watching them go."),
    (15, "could not run,", "Wide shot, the band running across open ground, the older man left standing small in the foreground, leaning on a stick."),
    (15, "and could not walk without pain", "Medium shot of the older man limping, one hand on a stick, jaw set, the bad foot barely touching the ground."),
    (15, "did not feed himself for ten years on a mountain in the ice age.", "Very wide shot of a cold mountain, the camp a few dots of fire, one figure handing food to another outside the shelter."),

    # --- 16 somebody -----------------------------------------------------------
    (16, "Somebody carried the water.", "Medium shot, a band member climbing toward camera with a water skin on their back, sweat dark on the hide, breath visible."),
    (16, "Somebody chewed or mashed his food,", "Close shot of hands mashing soft food in a shallow stone bowl with a rounded pebble, patient and repetitive."),
    (16, "because his teeth were gone.", "Close shot of the worn jaw beside the bowl of mash, the comparison plain, no commentary."),
    (16, "Somebody kept him warm", "Medium shot of a hide blanket being drawn over the older man's shoulders from behind, hands tucking it in at the neck."),
    (16, "and moved him when the camp moved.", "Wide shot, two band members walking on either side of the older man, his arms over their shoulders, the camp behind them half-packed."),
    (16, "Somebody decided, again and again,", "Medium shot of faces around the fire, one band member looking directly at the older man, considering him."),
    (16, "that he was worth the cost.", "Wide shot of the whole group walking at a slow pace across a plain, the older man in the middle, no one ahead of him."),

    # --- 17 the stretcher ------------------------------------------------------
    (17, "And notice what carrying a person actually requires.", "Wide shot, four band members standing around two long poles and a hide spread on the ground, working out how to build it."),
    (17, "Two poles.", "Flat overhead shot, two stripped birch poles laid parallel on bare earth, ends freshly cut, simple and exact."),
    (17, "A hide stretched between them.", "Close shot, a hide being lashed to the poles with twisted cord, four hands pulling it tight, the surface drum-flat."),
    (17, "Four people who can walk in step,", "Side-on wide shot, four figures carrying the loaded stretcher, strides matched, heads level, moving as one shape."),
    (17, "at the speed of the slowest,", "Wide shot of the same procession from behind, short careful steps, the rear carrier adjusting constantly to keep pace."),
    (17, "over ground that does not forgive a stumble.", "Close shot of a carrier's foot sliding on loose scree, the stretcher tilting a few degrees, the other three bracing."),

    # --- 18 no artifact --------------------------------------------------------
    (18, "No stretcher survives from the ice age.", "Still shot of bare ground, a faint rectangular impression in the dust where poles and a hide once lay, nothing else there."),
    (18, "Wood rots, hide rots, rope rots.", "Still life on earth: a pole crumbling at one end, a hide fraying to fibres, a coil of cord coming apart, all three in decay."),
    (18, "The oldest ones we have are thousands of years too late to help us.", "Museum shot of a later wooden litter in a glass case, clean and intact, cold light, a barrier rope in front."),
    (18, "So the invention that may have mattered more than any stone tool", "Flat still life, a finely worked hand axe in the foreground and two rough stretcher poles behind it, both given equal weight."),
    (18, "left no object behind at all.", "Extreme wide shot of empty dust and stone, the impression gone, wind moving the surface."),
    (18, "It left only the arithmetic of who got carried.", "Wide shot of the four carrying the stretcher across a plain at dusk, the group reduced to one dark shape and four pairs of legs."),

    # --- 19 La Chapelle --------------------------------------------------------
    (19, "There is a second skeleton worth knowing about.", "Overhead shot of a second museum drawer sliding open, an older skull resting on foam, cooler light than the first."),
    (19, "In France,", "Wide exterior shot of a limestone cave mouth in a green river valley, warm daylight, swallows in the air."),
    (19, "an old Neanderthal man had lost most of his teeth years before he died,", "Close shot of a jaw with most of the teeth missing, the bone healed smooth over the empty sockets."),
    (19, "and his spine and hip were so arthritic that walking would have been painful every day.", "Medium shot of an old man walking with a stick, shoulders hunched, one hand pressed to his hip, face tight."),
    (19, "He could not chew hard food.", "Flat overhead shot, a tough root and a strip of dried meat on one side, a bowl of soft mash on the other, clearly divided."),
    (19, "Somebody was preparing it for him for years,", "Close shot of hands mashing food in the same bowl, the background changing colour through the seasons behind them."),
    (19, "long enough for the arthritis to get worse.", "Medium shot of the same man, more stooped than before, both hands on the stick now, the fire lower."),

    # --- 20 unsettling ---------------------------------------------------------
    (20, "That is the part that unsettles people.", "Wide shot of a single modern visitor standing in front of a lit museum case, small and still, their reflection faint in the glass."),
    (20, "Not that ancient humans were strong.", "Static museum diorama, a muscular hunter in a heroic spear pose, painted backdrop, everything arranged to impress."),
    (20, "That they were slow.", "Wide shot of four figures carrying a stretcher at a crawl across an open plain, no urgency at all, the horizon empty."),
    (20, "That they stopped for each other.", "Wide shot, the whole band halted on a slope, every one of them waiting, the slowest member still catching up."),

    # --- 21 the honest turn ----------------------------------------------------
    (21, "But here is where the science gets honest,", "Close shot of a bone on a lab bench under a white lamp, calipers and a notebook beside it, the room otherwise dark."),
    (21, "because the story I just told you is the version everyone likes,", "Warm golden shot of the cave, everyone gathered kindly around the fire, the light soft and flattering, almost too perfect."),
    (21, "and it is not the only reading.", "The same cave shot in cold blue-grey light, the same people, the same fire, nothing warm in it at all."),

    # --- 22 care vs tolerance --------------------------------------------------
    (22, "Survival proves support.", "Close shot, one hand holding food out to another, the offering clear and practical."),
    (22, "It does not prove love.", "Same hands, same food, flat even light, no glow, no warmth in the colour."),
    (22, "A group can tolerate a member without feeling anything about him.", "Medium shot of four figures around a fire, the older man among them, nobody looking at him, nobody moved away either."),
    (22, "He may have been someone's brother.", "Close shot of two similar faces side by side, the same jaw, the same brow, unmistakably related."),
    (22, "He may have carried knowledge worth more than his appetite,", "Medium shot of the older man pointing across the valley, three younger figures following his arm with their eyes."),
    (22, "where the good stone was,", "Wide shot of a flint outcrop in a chalk bank, fresh flakes on the ground, a hand resting on the seam."),
    (22, "when the river rose,", "Wide shot of a flooded river running brown and fast, driftwood piling against a rock, the far bank unreachable."),
    (22, "which cave stayed dry.", "Wide shot of a dry cave mouth during heavy rain, water sheeting past the entrance while the inside stays pale and dry."),
    (22, "He may have watched children while the hunters were gone.", "Medium shot of the older man seated with three children around him, one asleep against his bad arm, the fire low."),

    # --- 23 unresolved ---------------------------------------------------------
    (23, "Researchers call this the difference between care and tolerance,", "Close shot of two hands side by side, one holding food out, one resting flat, nothing to say which is which."),
    (23, "and it is genuinely unresolved.", "Static shot of the bone alone on the bench, no label, no tag, no answer attached to it."),
    (23, "Sceptics point out that Neanderthals took enormous injuries at close range,", "Wide shot of a hunter face to face with a large animal in a thicket, both very close, neither backing away."),
    (23, "that small bands help each other as a matter of habit,", "Medium shot of routine camp work, food passed without looking, hides shared, no ceremony in it."),
    (23, "and that a healed bone cannot tell you what anyone felt.", "Extreme close-up of the healed seam, flat and closed, entirely silent about everything except survival."),

    # --- 24 harder critique ----------------------------------------------------
    (24, "There is a harder critique too.", "Shot from behind a modern researcher's shoulders, the bone on the bench and a wall of casts beyond, cool light."),
    (24, "Some archaeologists argue that we are too quick to assume a disabled person was a burden", "Imagined shot of four figures carrying the older man, his weight visibly pulling their shoulders down, drawn as a burden."),
    (24, "who was generously maintained.", "The same imagined shot in flat pale colour, faded at the edges, clearly a drawing of an idea rather than a memory."),
    (24, "Maybe he was not carried.", "Static shot of the two poles and the hide lying unused on the ground, nobody near them."),
    (24, "Maybe he walked.", "Medium shot of the older man walking slowly on his own, stick in hand, keeping his own pace, nobody helping."),
    (24, "Maybe the group simply moved at the pace of its slowest member,", "Wide shot of the band walking with the older man in the middle of the group, no gap in front of him, no hurry."),
    (24, "and nobody experienced that as sacrifice at all.", "Medium shot of ordinary walking, someone chewing, someone talking, the older man among them, nothing heroic happening."),
    (24, "That argument is not nitpicking.", "Close shot of the bone under the lamp again, harder light, the healed line undeniable."),
    (24, "It changes the story from charity to ordinary life.", "Warm camp shot, cooking, mending, children, the older man asleep by the fire, everyone busy and unbothered."),

    # --- 25 Tilley -------------------------------------------------------------
    (25, "Lorna Tilley built a method for navigating this,", "Flat overhead shot of a modern desk: a notebook, a pencil, a photograph of a long bone, a mug, morning light."),
    (25, "called the bioarchaeology of care.", "Still life of four flat stones laid in a row on cream paper, spaced evenly, each a step."),
    (25, "It forces a researcher to answer four questions in order.", "Close shot of a hand touching the first of the four stones, the other three waiting in line behind it."),
    (25, "What exactly was wrong with this person.", "Close shot of a bone with four small ochre marks on it, each one circled lightly in pencil."),
    (25, "What could they no longer do.", "Medium shot of a figure trying to lift a heavy hide roll and failing, the roll dropping back to the ground."),
    (25, "What would it have taken to keep them alive in that specific place.", "Wide shot of a cave interior laid out as a checklist of objects: water, firewood, meat, hides, all in a row against the wall."),
    (25, "And what does that tell us about the people around them.", "Medium shot of faces around a fire, close together, half of them looking at the person just out of frame."),

    # --- 26 jobs ---------------------------------------------------------------
    (26, "Applied properly, it turns a sad skeleton into a list of physical jobs.", "Flat shot of a bone beside a row of simple tools, a waterskin, a bowl, a fire drill, a hide, evenly spaced."),
    (26, "Carry water.", "Medium shot, a band member hauling a water skin up a slope, hands gripping the strap, back bent."),
    (26, "Reposition a body so sores do not form.", "Close shot of two hands rolling a lying figure gently onto their side, a folded hide pushed underneath."),
    (26, "Keep a fire.", "Close shot of a hand feeding a small flame with dry grass, sparks going up, the cave wall glowing."),
    (26, "Move a person who cannot walk.", "Medium shot, two band members carrying a third between them, arms over shoulders, feet dragging lightly."),
    (26, "Share food that took a whole day to get.", "Medium shot, a hunter holding out a joint of meat to the older man, both hands steady, no ceremony."),

    # --- 27 Spikins ------------------------------------------------------------
    (27, "Penny Spikins and her colleagues went further", "Wide shot of a lab wall covered in casts of long bones, a researcher's silhouette walking along it, no text anywhere."),
    (27, "and looked at more than thirty individuals with injuries that healed instead of killing them.", "Overhead shot of more than thirty bone casts laid out in careful rows on a long table, ochre dots on the healed ones."),
    (27, "Their conclusion was not that Neanderthals were gentle.", "Medium shot of a hard-faced hunter cleaning a spear, scarred hands, no softness in the frame at all."),
    (27, "It was that healthcare was one of their survival strategies,", "Wide shot of practical care in camp, water carried, fire fed, a leg splinted with two sticks and cord, unsentimental work."),
    (27, "sitting alongside hunting together, sharing food, and raising children.", "Wide camp shot in three clear zones: hunters leaving with spears, food being divided at the fire, children playing between them."),

    # --- 28 midwives -----------------------------------------------------------
    (28, "They even argue that without help,", "Medium shot of a woman in labour supported upright by two others, hands gripping forearms, firelight, no gore."),
    (28, "Neanderthal mothers and newborns would have died often enough to threaten the group.", "Wide shot of a small group standing close around a shelter, an infant wrapped against a chest, everyone leaning in."),
    (28, "Which means the first midwives may be older than our species.", "Close shot of two hands holding a newborn wrapped in hide, warm firelight, the faces of the helpers just out of frame."),

    # --- 29 return -------------------------------------------------------------
    (29, "So come back to the hillside.", "Wide static shot of the opening ridge, same framing as the first shot, but the light gone blue and the stones colder."),
    (29, "The sun is down now.", "Wide shot of the sky after sunset, deep navy overhead, one thin ochre band left on the horizon behind the ridge."),
    (29, "Someone has made a decision,", "Medium shot, the four band members looking at each other, then two of them nodding, the decision made without words."),
    (29, "and you feel two people lift you badly,", "Close shot, two sets of hands hooked under the protagonist's arms, lifting unevenly, the body sagging between them."),
    (29, "and a third take your weight on their shoulder,", "Close shot of a shoulder pushed under an arm, a hand gripping a wrist, hides bunching at the contact."),
    (29, "and the fourth walk ahead to choose the ground.", "Wide shot, one figure walking ahead of the group, testing stones with a foot, pointing the way down the slope."),

    # --- 30 not rescued --------------------------------------------------------
    (30, "You are not being rescued.", "Very wide shot, five small figures on a dark slope, no fire, no lights, no help anywhere on the horizon."),
    (30, "There is no rescue out here.", "Wide shot of an empty plain at night, cold stars, not one light in any direction."),
    (30, "You are being carried at a speed that costs everyone else something,", "Close shot of the carriers' faces, jaws tight, breath visible, the stretcher poles bending slightly."),
    (30, "and you will hear about it for the rest of your life,", "Medium shot around the fire, one band member gesturing toward the protagonist, the others watching, no anger, just accounting."),
    (30, "and the whole point is that you still have one.", "Close shot of the protagonist's face by firelight, eyes open, alive, the outline soft and warm."),

    # --- 31 the cost -----------------------------------------------------------
    (31, "Someone will hunt less.", "Shot of the drying rack with fewer strips of meat than before, the empty spaces obvious."),
    (31, "Someone will carry less.", "Medium shot, a hunter walking with a small bundle instead of a full load, shoulders free, expression flat."),
    (31, "For months this group will be slower, hungrier, and easier to kill,", "Wide shot, the group moving slowly across open ground, two pairs of predator eyes watching from the treeline behind them."),
    (31, "and they will do it anyway,", "Wide shot, the group choosing the longer, gentler path around a slope, the stretcher level, nobody running."),
    (31, "and you will know the exact size of what it cost them.", "Close shot of the protagonist's face turned toward the carriers, watching them strain, understanding it precisely."),

    # --- 32 close --------------------------------------------------------------
    (32, "And fifty thousand years later, a bone in a drawer", "Hard cut to a modern museum drawer, white light, the bone on grey foam, the drawer half open."),
    (32, "carries one healed line", "Macro shot of the healed line running across the bone shaft, ochre against pale grey."),
    (32, "where your leg knit back together.", "Extreme close-up, the seam closed and continuous, the two halves of the bone made one again."),
    (32, "Someone reads it and knows you were not alone.", "Close shot of a modern hand resting flat on the bone, warm skin against cold fossil, a gentle hold."),
    (32, "That is the strange thing about us.", "Wide shot of a museum hall, tall cases on both sides, three visitor silhouettes small in the middle."),
    (32, "Every other animal on that hillside was faster, sharper, stronger.", "Wide shot, three predators moving fast across the slope, teeth and claws drawn as clean simple shapes, no gore."),
    (32, "We are the ones who slowed down.", "Very wide dawn shot, the group carrying the stretcher at a crawl along the ridge, silhouetted against a pale sky."),
    (32, "And the first invention was not fire, or the spear, or the wheel.", "Flat overhead still life on bare earth: a fire drill, a spear, a wooden wheel-disc, evenly spaced, nothing else."),
    (32, "It was the stretcher.", "Wide shot of two poles and a hide lying in the dust at sunrise, ochre light across it, the band standing just beyond, waiting to lift."),
]


def narration_text(repo: Path) -> str:
    p = repo / "narration" / "narration.md"
    raw = p.read_text(encoding="utf-8")
    m = re.search(r"<!-- TTS:START -->(.*?)<!-- TTS:END -->", raw, re.S)
    if not m:
        sys.exit("FATAL: no TTS markers in narration/narration.md")
    return re.sub(r"\s+", " ", m.group(1)).strip()


def build(repo: Path) -> int:
    out = repo / PROJECT / "visuals.csv"
    counts: dict[int, int] = {}
    rows = []
    for slide, text, prompt in BEATS:
        counts[slide] = counts.get(slide, 0) + 1
        rows.append([slide, counts[slide], text, prompt])
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["slide_id", "moment", "moment_text", "visual_prompt"])
        w.writerows(rows)
    print(f"wrote {out} with {len(rows)} rows across {len(counts)} slides")
    return check(repo)


def check(repo: Path) -> int:
    csv_path = repo / PROJECT / "visuals.csv"
    narrative = narration_text(repo)
    total_words = len(narrative.split())

    with csv_path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    problems: list[str] = []
    cursor = 0
    covered: set[int] = set()
    prev_slide, prev_moment = 0, 0
    spans: list[tuple[int, int]] = []

    for i, r in enumerate(rows, start=1):
        slide, moment = int(r["slide_id"]), int(r["moment"])
        text = re.sub(r"\s+", " ", r["moment_text"]).strip()
        if not text:
            problems.append(f"row {i}: empty moment_text")
            continue

        hits = [m.start() for m in re.finditer(re.escape(text), narrative)]
        if not hits:
            problems.append(f"row {i} [{slide:02d}m{moment:02d}]: NOT IN NARRATION -> {text!r}")
            continue
        if len(hits) > 1:
            problems.append(f"row {i} [{slide:02d}m{moment:02d}]: AMBIGUOUS x{len(hits)} -> {text!r}")
            continue
        if not r["visual_prompt"].strip():
            problems.append(f"row {i}: empty visual_prompt")
        if (slide, moment) <= (prev_slide, prev_moment):
            problems.append(f"row {i}: out of order {slide:02d}m{moment:02d} after {prev_slide:02d}m{prev_moment:02d}")
        if hits[0] < cursor:
            problems.append(f"row {i} [{slide:02d}m{moment:02d}]: OVERLAP with previous beat")
        cursor = hits[0] + len(text)
        prev_slide, prev_moment = slide, moment
        spans.append((hits[0], hits[0] + len(text)))

        for w_i in range(hits[0], hits[0] + len(text)):
            covered.add(w_i)

    # word-char coverage: how much of the narration is spoken inside some beat
    covered_chars = len(covered)
    coverage = covered_chars / len(narrative) * 100

    # gaps: characters between end of one beat and start of the next
    gaps = []
    end = 0
    for start, stop in spans:
        if start > end:
            gaps.append(narrative[end:start].strip())
        end = max(end, stop)
    if end < len(narrative):
        gaps.append(narrative[end:].strip())

    slides = len({int(r["slide_id"]) for r in rows})
    print(f"rows={len(rows)}  slides={slides}  narration_words={total_words}  chars_covered={coverage:.1f}%")
    print(f"avg words per beat = {total_words / len(rows):.1f}")
    word_gaps = [g for g in gaps if re.search(r"[A-Za-z0-9]", g)]
    print(f"gaps: {len(gaps)} total, {len(word_gaps)} containing words (punctuation-only elsewhere)")
    for g in word_gaps[:20]:
        print("   gap ->", repr(g))
    if problems:
        print(f"FAIL: {len(problems)} problem(s)")
        for p in problems:
            print("  -", p)
        return 1
    print("PASS: every beat is verbatim, unique, in order, non-overlapping")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "check"])
    ap.add_argument("--repo", default=".")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    return build(repo) if a.cmd == "build" else check(repo)


if __name__ == "__main__":
    raise SystemExit(main())
