def generate_chapter(seed: str, chapter_number: int) -> Dict:
    if chapter_number < 1 or chapter_number > CHAPTER_COUNT:
        raise ValueError("Invalid chapter number")

    rng = stable_rng(f"{seed}:chapter:{chapter_number}")
    base_rng = stable_rng(seed)

    # ---------------------------------------------------------
    # RECREATE THE NOVEL'S CORE DATA
    # ---------------------------------------------------------

    genre = pick(base_rng, GENRES)
    world = pick(base_rng, PLACES)
    faction = pick(base_rng, FACTIONS)
    power = pick(base_rng, POWERS)
    protagonist = make_name(base_rng)

    # Recreate deterministic arc structure.
    arc_rng = stable_rng(f"{seed}:arcs")
    arcs = make_arcs(arc_rng)
    arc = get_arc(arcs, chapter_number)

    # ---------------------------------------------------------
    # CHAPTER-SPECIFIC DATA
    # ---------------------------------------------------------

    location = pick(rng, PLACES)
    object_item = pick(rng, OBJECTS)
    conflict = pick(rng, CONFLICTS)

    supporting_character = make_name(rng)
    secondary_character = make_name(rng)
    rival_character = make_name(rng)

    used_names = {
        protagonist,
        supporting_character,
        secondary_character,
        rival_character,
    }

    while secondary_character in used_names:
        secondary_character = make_name(rng)

    used_names.add(secondary_character)

    while rival_character in used_names:
        rival_character = make_name(rng)

    # ---------------------------------------------------------
    # CHAPTER TITLE
    # ---------------------------------------------------------

    title = (
        f"{chapter_number:03d}. "
        f"{pick(rng, CHAPTER_VERBS)} "
        f"{pick(rng, CHAPTER_NOUNS)}"
    )

    # ---------------------------------------------------------
    # CHAPTER DEVELOPMENT MATERIAL
    # ---------------------------------------------------------

    openings = [
        (
            f"The morning arrived quietly over {location}. "
            f"A thin layer of mist covered the streets, and the first light "
            f"of dawn had barely reached the rooftops when {protagonist} "
            f"opened their eyes."
        ),
        (
            f"Rain had continued throughout the night. "
            f"By sunrise, the road outside {location} had become a narrow "
            f"stream of mud and reflected light. {protagonist} stood near "
            f"the window, watching the world slowly awaken."
        ),
        (
            f"{protagonist} woke with the uncomfortable feeling that "
            f"someone had been calling their name. There was nobody in the "
            f"room, yet the sensation remained."
        ),
        (
            f"The journey had reached {location} before sunset, but nobody "
            f"felt relieved. The town looked ordinary from a distance. "
            f"Up close, however, small details suggested that something "
            f"was deeply wrong."
        ),
        (
            f"Nothing appeared unusual at first. People walked through the "
            f"streets, merchants opened their shops, and distant bells "
            f"announced the beginning of another day. Then {protagonist} "
            f"saw the symbol carved into the wall."
        ),
    ]

    discoveries = [
        (
            f"Near an abandoned building, {protagonist} discovered "
            f"{object_item}. It looked insignificant at first, but the "
            f"moment they touched it, the atmosphere around them changed."
        ),
        (
            f"Behind a damaged section of wall, the group discovered "
            f"a narrow passage. The entrance had been deliberately hidden, "
            f"and old marks covered the stone surrounding it."
        ),
        (
            f"A forgotten document contained several references to "
            f"{faction}. Most of the writing had faded, but one sentence "
            f"remained perfectly readable."
        ),
        (
            f"The group found evidence that somebody had arrived before "
            f"them. Footprints crossed the dust, leading directly toward "
            f"a sealed door."
        ),
        (
            f"A strange sound came from beneath the ground. "
            f"When they investigated, they discovered a chamber that "
            f"should not have existed beneath {location}."
        ),
    ]

    developments = [
        (
            f"The discovery connected directly to the larger mystery "
            f"surrounding {world}."
        ),
        (
            f"The evidence suggested that {faction} had been involved "
            f"in the events for much longer than anyone realized."
        ),
        (
            f"The information contradicted everything {protagonist} "
            f"had previously believed about {power}."
        ),
        (
            f"The discovery revealed that the current conflict was only "
            f"one part of a much older struggle."
        ),
        (
            f"The truth appeared to be connected to {conflict}."
        ),
    ]

    complications = [
        (
            "Before they could investigate further, footsteps echoed "
            "through the corridor."
        ),
        (
            "The door behind them suddenly closed."
        ),
        (
            "A warning signal began sounding throughout the settlement."
        ),
        (
            "Someone had apparently been waiting for them."
        ),
        (
            "The object suddenly reacted to the presence of "
            f"{protagonist}."
        ),
        (
            "A distant explosion interrupted the conversation."
        ),
        (
            "The lights disappeared one by one."
        ),
    ]

    emotional_events = [
        (
            f"{protagonist} remembered the reason they had started "
            f"the journey in the first place."
        ),
        (
            f"{supporting_character} finally admitted that they were "
            f"afraid of what would happen next."
        ),
        (
            f"{secondary_character} revealed a secret they had kept "
            f"hidden since the beginning of the journey."
        ),
        (
            f"The argument that followed was not really about the "
            f"discovery. It was about trust."
        ),
        (
            f"For a moment, nobody knew what to say. The silence "
            f"made the danger feel even closer."
        ),
    ]

    action_events = [
        (
            f"The confrontation began before anyone was prepared. "
            f"{protagonist} moved first, using {power} to create an "
            f"opening for the others."
        ),
        (
            f"The attackers moved quickly. {supporting_character} "
            f"blocked the first strike while {protagonist} searched "
            f"for a way to escape."
        ),
        (
            f"The ground shook violently. Something enormous was moving "
            f"beneath the structure."
        ),
        (
            f"{rival_character} appeared without warning and immediately "
            f"challenged {protagonist}."
        ),
        (
            f"The escape became a desperate race through the narrow "
            f"streets of {location}."
        ),
    ]

    power_events = [
        (
            f"{power} awakened more strongly than before."
        ),
        (
            f"The energy surrounding {protagonist} changed color and "
            f"shape, behaving in a way nobody had witnessed before."
        ),
        (
            f"For several seconds, {protagonist} could see fragments "
            f"of possible futures."
        ),
        (
            f"The ability responded to the hidden object rather than "
            f"to {protagonist}'s conscious command."
        ),
        (
            f"The power suddenly became silent, leaving "
            f"{protagonist} more frightened than before."
        ),
    ]

    revelations = [
        (
            f"The final clue revealed that the events surrounding "
            f"{world} had happened before."
        ),
        (
            f"The evidence suggested that someone had deliberately "
            f"created the current conflict."
        ),
        (
            f"{protagonist} discovered that the enemy knew their name."
        ),
        (
            f"The document contained a prediction describing an event "
            f"that had not happened yet."
        ),
        (
            f"The symbol matched the mark that appeared whenever "
            f"{power} was activated."
        ),
        (
            f"The truth was far older than the current generation."
        ),
    ]

    reflections = [
        (
            f"{protagonist} stood alone for several minutes, thinking "
            f"about everything that had happened."
        ),
        (
            f"The others discussed their options, but every choice "
            f"seemed to carry a different kind of danger."
        ),
        (
            f"Nobody wanted to admit how serious the situation had become."
        ),
        (
            f"The journey had started with a single unanswered question. "
            f"Now there were dozens."
        ),
        (
            f"Trust had become more valuable than information, and "
            f"neither was easy to obtain."
        ),
    ]

    transitions = [
        (
            f"By evening, the immediate danger had passed. "
            f"The group prepared to leave {location} before dawn."
        ),
        (
            f"Night fell over {location}. The streets became empty, "
            f"but the feeling of being watched never disappeared."
        ),
        (
            f"The group found temporary shelter and began planning "
            f"their next move."
        ),
        (
            f"After everything that had happened, sleep was difficult."
        ),
    ]

    cliffhangers = [
        (
            f"Just before midnight, somebody whispered "
            f"{protagonist}'s name from outside the room."
        ),
        (
            f"A message appeared on {object_item}: "
            f"**DO NOT TRUST THE PERSON BESIDE YOU.**"
        ),
        (
            f"Far beyond the horizon, a strange light appeared in the sky."
        ),
        (
            f"The sealed door opened by itself."
        ),
        (
            f"A new symbol appeared on {protagonist}'s hand."
        ),
        (
            f"Someone left a letter outside the door. "
            f"It contained tomorrow's date."
        ),
        (
            f"{rival_character}'s voice came from the darkness."
        ),
    ]

    # ---------------------------------------------------------
    # DIALOGUE
    # ---------------------------------------------------------

    dialogue_sets = [
        [
            f'"We should leave," {supporting_character} said.',
            f'"Not yet," {protagonist} replied.',
            f'"You saw what happened. Staying here is dangerous."',
            f'"Then we find out why it happened before we leave."',
        ],
        [
            f'"How long have you known?" {protagonist} asked.',
            f'{supporting_character} looked away.',
            f'"Long enough to know that the truth is worse than the rumor."',
            f'"That is not an answer."',
            f'"It is the only answer I can give you right now."',
        ],
        [
            f'"This changes everything," {secondary_character} whispered.',
            f'"No," {protagonist} said. "It explains everything."',
            f'"Those are not the same thing."',
            f'"I know."',
        ],
        [
            f'"Who sent you?" {protagonist} demanded.',
            f'{rival_character} smiled.',
            f'"You still think someone sent me?"',
            f'"Then why are you here?"',
            f'"Because you finally reached the place I was waiting for."',
        ],
    ]

    # ---------------------------------------------------------
    # BUILD CHAPTER
    # ---------------------------------------------------------

    paragraphs = []

    paragraphs.append(pick(rng, openings))

    paragraphs.append(
        (
            f"Chapter {chapter_number} belonged to the "
            f"**{arc['title']}** arc, a period increasingly shaped by "
            f"{arc['theme']}. The journey had already changed "
            f"{protagonist}, but the events waiting in {location} "
            f"would force another decision."
        )
    )

    paragraphs.append(pick(rng, discoveries))

    paragraphs.append(
        (
            f"For several seconds, nobody moved. "
            f"{supporting_character} examined the discovery while "
            f"{secondary_character} watched the entrance."
        )
    )

    paragraphs.append(pick(rng, developments))

    paragraphs.append(
        (
            f"The implications were difficult to ignore. If the evidence "
            f"was genuine, then the events happening now were connected "
            f"to something that had begun long before {protagonist} "
            f"entered the story."
        )
    )

    paragraphs.append(pick(rng, complications))

    paragraphs.append(
        (
            f"{protagonist} immediately understood that there was no "
            f"longer enough time for careful planning. Whatever was "
            f"approaching would arrive soon."
        )
    )

    for line in pick(rng, dialogue_sets):
        paragraphs.append(line)

    paragraphs.append(
        (
            f"The conversation ended without agreement. "
            f"Everyone understood that the next decision would affect "
            f"more than the people standing in the room."
        )
    )

    paragraphs.append(pick(rng, emotional_events))

    paragraphs.append(
        (
            f"Outside, the wind grew stronger. The sound travelled "
            f"through the streets of {location}, carrying distant voices "
            f"and the metallic sound of something moving through the dark."
        )
    )

    paragraphs.append(pick(rng, action_events))

    paragraphs.append(
        (
            f"{protagonist} barely had enough time to react. "
            f"The situation had changed from an investigation into a "
            f"fight for survival."
        )
    )

    paragraphs.append(pick(rng, power_events))

    paragraphs.append(
        (
            f"The sudden release of power forced everyone nearby to "
            f"retreat. For one impossible moment, the world seemed "
            f"to stop moving."
        )
    )

    paragraphs.append(
        (
            f"{protagonist} could hear their own breathing. "
            f"The strange energy disappeared almost as quickly as "
            f"it had appeared."
        )
    )

    paragraphs.append(pick(rng, revelations))

    paragraphs.append(
        (
            f"The revelation left the group silent. It did not solve "
            f"the mystery. Instead, it revealed that the mystery was "
            f"far larger than they had imagined."
        )
    )

    paragraphs.append(pick(rng, reflections))

    paragraphs.append(
        (
            f"{supporting_character} finally looked toward "
            f"{protagonist}. There was no certainty in their expression, "
            f"only the understanding that the journey had reached another "
            f"turning point."
        )
    )

    paragraphs.append(
        (
            f"The name of {faction} appeared again in their discussion. "
            f"The organization had been present in too many places to "
            f"be coincidence."
        )
    )

    paragraphs.append(
        (
            f"The conflict surrounding {conflict} was becoming impossible "
            f"to separate from their personal journey."
        )
    )

    paragraphs.append(pick(rng, transitions))

    paragraphs.append(
        (
            f"Before leaving, {protagonist} looked back one final time. "
            f"The place seemed ordinary again, almost peaceful. "
            f"But the silence felt artificial."
        )
    )

    paragraphs.append(
        (
            f"Nobody said it aloud, but everyone understood the same thing: "
            f"whatever happened next would not be a simple continuation "
            f"of the journey."
        )
    )

    # ---------------------------------------------------------
    # FILL TO APPROXIMATELY 800 WORDS
    # ---------------------------------------------------------

    bridge_paragraphs = [
        (
            f"The group spent several minutes checking the area again. "
            f"They searched the walls, the floor, and every object that "
            f"might contain another clue. Nothing appeared at first."
        ),
        (
            f"{protagonist} returned to the original discovery. "
            f"The object remained unchanged, yet something about it "
            f"felt different now."
        ),
        (
            f"{secondary_character} suggested that the answer might not "
            f"be hidden inside the object. Perhaps the object itself was "
            f"only a key."
        ),
        (
            f"The suggestion changed the way everyone looked at the room."
        ),
        (
            f"{supporting_character} remembered an old story involving "
            f"{world}. The details had always sounded like a myth, but "
            f"they suddenly appeared strangely relevant."
        ),
        (
            f"The discussion continued quietly. Each person contributed "
            f"what little they knew, and slowly a pattern began to appear."
        ),
        (
            f"The pattern was incomplete, but it was enough to establish "
            f"a possible direction."
        ),
        (
            f"{protagonist} realized that the next destination was no "
            f"longer a matter of choice."
        ),
        (
            f"The road ahead would take them closer to the heart of the "
            f"mystery, whether they were ready or not."
        ),
        (
            f"Another distant sound echoed through {location}. "
            f"Nobody moved until it disappeared."
        ),
        (
            f"When the silence returned, it somehow felt worse than before."
        ),
        (
            f"{rival_character} had disappeared during the confusion. "
            f"Nobody knew when they had left."
        ),
        (
            f"That disappearance created another question that would "
            f"have to wait until later."
        ),
        (
            f"For now, survival remained more important than answers."
        ),
    ]

    target_min_words = 760
    target_max_words = 900

    def count_words():
        return sum(len(paragraph.split()) for paragraph in paragraphs)

    current_words = count_words()

    bridge_index = 0

    while current_words < target_min_words:
        paragraph = bridge_paragraphs[
            (bridge_index + rng.randrange(len(bridge_paragraphs)))
            % len(bridge_paragraphs)
        ]

        paragraphs.insert(
            max(3, len(paragraphs) - 3),
            paragraph,
        )

        current_words = count_words()
        bridge_index += 1

        if bridge_index > 100:
            break

    # ---------------------------------------------------------
    # FINAL ENDING
    # ---------------------------------------------------------

    paragraphs.append(pick(rng, cliffhangers))

    paragraphs.append(
        (
            f"{protagonist} stared into the darkness. "
            f"The answer would have to wait until tomorrow."
        )
    )

    word_count = count_words()

    return {
        "number": chapter_number,
        "title": title,
        "arc": arc,
        "location": location,
        "genre": genre,
        "paragraphs": paragraphs,
        "word_count": word_count,
    }
