# ============================================================
# AUTO-GENERATED NOVEL DESCRIPTIONS
# ============================================================

def make_description_rng(seed: str, name: str) -> random.Random:
    return stable_rng(f"{seed}:description:{name}")


def choose_description(
    rng: random.Random,
    options: List[str],
) -> str:
    return pick(rng, options)


def make_world_description(
    seed: str,
    world: Dict,
    protagonist: str,
    conflict: str,
    faction: str,
    power: str,
    genre: str,
) -> str:

    rng = make_description_rng(seed, "world")

    location_names = world.get(
        "important_locations",
        [],
    )

    location_text = (
        ", ".join(location_names[:3])
        if location_names
        else world["name"]
    )

    openings = [
        (
            f"{world['name']} is {world['type']} existing during "
            f"{world['era']}. From {location_text}, the world feels "
            f"larger than any single kingdom, city, or faction, with "
            f"different regions carrying their own histories, beliefs, "
            f"and dangers."
        ),
        (
            f"At first glance, {world['name']} appears to be a world "
            f"defined by {genre.lower()}, but its deeper identity lies "
            f"in the histories hidden beneath its surface. Its people "
            f"live across places such as {location_text}, while old "
            f"events continue to influence the present."
        ),
        (
            f"The story begins in {world['name']}, {world['type']} "
            f"where the present exists under the shadow of {world['era']}. "
            f"The distance between ordinary life and forgotten history "
            f"is smaller than most people realize."
        ),
    ]

    middle = [
        (
            f"The unresolved problem surrounding {conflict} has begun "
            f"to disturb that balance. Organizations such as {faction} "
            f"hold influence over events, while forces such as "
            f"{power} introduce possibilities that ordinary people "
            f"cannot easily explain."
        ),
        (
            f"Although {conflict} appears to be the immediate danger, "
            f"the deeper problem is the gap between what the people of "
            f"{world['name']} believe about their history and what "
            f"actually happened. {faction} is one of the powers caught "
            f"inside that contradiction."
        ),
        (
            f"Every region contains pieces of a larger story. The "
            f"conflict involving {conflict} gradually pulls "
            f"{protagonist} away from ordinary concerns and toward "
            f"places where the influence of {faction} and the secrets "
            f"behind {power} become impossible to ignore."
        ),
    ]

    endings = [
        (
            f"For {protagonist}, the world therefore becomes more than "
            f"a setting. Every journey reveals another piece of its "
            f"history, and every discovery makes it harder to separate "
            f"the past from the danger approaching the present."
        ),
        (
            f"What begins as a journey through {world['name']} slowly "
            f"becomes an investigation into why its history was allowed "
            f"to remain incomplete."
        ),
        (
            f"The farther {protagonist} travels, the less reliable the "
            f"simple version of the world's history becomes."
        ),
    ]

    return " ".join([
        choose_description(rng, openings),
        choose_description(rng, middle),
        choose_description(rng, endings),
    ])


def make_story_description(
    seed: str,
    title: str,
    protagonist: str,
    conflict: str,
    world: str,
    faction: str,
    power: str,
    central_mystery: str,
    tone: str,
) -> str:

    rng = make_description_rng(seed, "story")

    openings = [
        (
            f"{title} follows {protagonist}, whose life becomes "
            f"entangled with {conflict} before they understand how "
            f"large the consequences will become."
        ),
        (
            f"The journey begins with {protagonist} facing a problem "
            f"that appears local and manageable. That illusion breaks "
            f"when {conflict} reveals connections reaching across "
            f"{world}."
        ),
        (
            f"{protagonist} never intended to become part of the "
            f"events surrounding {conflict}. Circumstances gradually "
            f"force them into a journey that reaches far beyond their "
            f"original goal."
        ),
    ]

    developments = [
        (
            f"As the journey continues, the influence of {faction} "
            f"becomes increasingly difficult to ignore. Alliances "
            f"change, relationships are tested, and the rules behind "
            f"{power} become more important."
        ),
        (
            f"The path ahead is shaped not only by enemies but also "
            f"by allies whose own goals do not always match "
            f"{protagonist}'s. Every discovery creates another choice, "
            f"and every choice changes what comes next."
        ),
        (
            f"What begins as a personal struggle gradually expands "
            f"into something much larger. Friends, rivals, factions, "
            f"and hidden enemies become connected through the same "
            f"unanswered questions."
        ),
    ]

    mystery_lines = [
        (
            f"At the center of everything is one question: "
            f"{central_mystery}"
        ),
        (
            f"Behind the visible conflict lies a mystery that keeps "
            f"changing shape: {central_mystery}"
        ),
        (
            f"The deeper {protagonist} goes, the more important one "
            f"question becomes: {central_mystery}"
        ),
    ]

    tone_lines = [
        (
            f"The journey carries a {tone} atmosphere, allowing quiet "
            f"character moments and major discoveries to exist beside "
            f"the larger conflict."
        ),
        (
            f"Its {tone} tone gives the journey room to move between "
            f"personal moments, dangerous encounters, discoveries, "
            f"and consequences."
        ),
        (
            f"The story's {tone} atmosphere changes as the characters "
            f"move deeper into the unknown."
        ),
    ]

    return " ".join([
        choose_description(rng, openings),
        choose_description(rng, developments),
        choose_description(rng, mystery_lines),
        choose_description(rng, tone_lines),
    ])


def make_people_description(
    seed: str,
    protagonist: Dict,
    characters: List[Dict],
    antagonists: List[Dict],
) -> str:

    rng = make_description_rng(seed, "people")

    supporting = [
        character
        for character in characters
        if character["name"] != protagonist["name"]
    ]

    names = [
        character["name"]
        for character in supporting[:4]
    ]

    antagonist_names = [
        antagonist["name"]
        for antagonist in antagonists[:3]
    ]

    supporting_text = (
        ", ".join(names)
        if names
        else "the people encountered along the journey"
    )

    antagonist_text = (
        ", ".join(antagonist_names)
        if antagonist_names
        else "hidden enemies"
    )

    openings = [
        (
            f"At the center of the story is {protagonist['name']}, "
            f"a character whose {protagonist['trait']} nature shapes "
            f"many of the decisions that follow."
        ),
        (
            f"{protagonist['name']} begins the journey with "
            f"{protagonist['trait']} qualities, but the people they "
            f"meet gradually challenge the assumptions they began with."
        ),
        (
            f"The people surrounding {protagonist['name']} are as "
            f"important to the journey as the world itself. Trust "
            f"must be earned, relationships must survive pressure, "
            f"and nobody remains unchanged forever."
        ),
    ]

    relationship_lines = [
        (
            f"Among the important companions are {supporting_text}. "
            f"Each brings a different personality, ability, and reason "
            f"for remaining involved in the journey."
        ),
        (
            f"The journey brings {protagonist['name']} together with "
            f"{supporting_text}, creating friendships, disagreements, "
            f"rivalries, and unexpected forms of loyalty."
        ),
        (
            f"Some of the strongest relationships develop through "
            f"disagreement. Characters such as {supporting_text} do "
            f"not always see the same solution, but their differences "
            f"shape the direction of the story."
        ),
    ]

    enemy_lines = [
        (
            f"Opposing them are figures such as {antagonist_text}, "
            f"whose goals are connected to conflicts larger than any "
            f"single confrontation."
        ),
        (
            f"Beyond the immediate group, {antagonist_text} represent "
            f"different kinds of opposition, from personal rivalry to "
            f"plans that threaten the wider world."
        ),
    ]

    return " ".join([
        choose_description(rng, openings),
        choose_description(rng, relationship_lines),
        choose_description(rng, enemy_lines),
    ])


def make_power_description(
    seed: str,
    power: Dict,
    protagonist: str,
) -> str:

    rng = make_description_rng(seed, "power")

    mechanism = power["mechanism"]
    costs = power.get("costs", [])
    levels = power.get("levels", [])

    primary_cost = (
        costs[0]
        if costs
        else "physical and mental exhaustion"
    )

    level_text = (
        ", ".join(levels[:5])
        if levels
        else "gradual stages of mastery"
    )

    openings = [
        (
            f"{power['name']} is not simply a weapon but a system "
            f"that determines what its users can attempt and what "
            f"they must sacrifice to succeed."
        ),
        (
            f"The power at the heart of the story is {power['name']}, "
            f"a system whose rules become increasingly important as "
            f"{protagonist} grows."
        ),
        (
            f"For {protagonist}, learning {power['name']} is a process "
            f"of discovering limits as much as discovering strength."
        ),
    ]

    mechanism_lines = [
        (
            f"It works because {mechanism}. Progress therefore "
            f"depends on understanding the system rather than simply "
            f"possessing greater raw strength."
        ),
        (
            f"Its users must learn how to work with a system in which "
            f"{mechanism}. The difference between a beginner and a "
            f"master comes from control, knowledge, and experience."
        ),
        (
            f"The underlying principle is that {mechanism}. This "
            f"makes knowledge and technique just as important as "
            f"natural talent."
        ),
    ]

    cost_lines = [
        (
            f"Every meaningful use carries a price, beginning with "
            f"{primary_cost}. Stronger techniques demand greater "
            f"control and can create consequences that cannot simply "
            f"be undone."
        ),
        (
            f"The system deliberately has limits. Even when "
            f"{protagonist} becomes stronger, using the power can cause "
            f"{primary_cost}, preventing it from becoming an effortless "
            f"answer to every problem."
        ),
        (
            f"Power does not come without consequence. One of the "
            f"earliest dangers is {primary_cost}, while more advanced "
            f"abilities introduce risks that become important later."
        ),
    ]

    progression_lines = [
        (
            f"The known progression includes stages such as "
            f"{level_text}, although the deeper limits of the system "
            f"remain uncertain."
        ),
        (
            f"Growth follows stages including {level_text}. Each stage "
            f"represents a change in understanding as well as an "
            f"increase in ability."
        ),
    ]

    return " ".join([
        choose_description(rng, openings),
        choose_description(rng, mechanism_lines),
        choose_description(rng, cost_lines),
        choose_description(rng, progression_lines),
    ])


def make_mystery_description(
    seed: str,
    world: str,
    protagonist: str,
    conflict: str,
    mystery: str,
    factions: List[Dict],
) -> str:

    rng = make_description_rng(seed, "mystery")

    faction_names = [
        faction["name"]
        for faction in factions[:3]
    ]

    faction_text = (
        ", ".join(faction_names)
        if faction_names
        else "the major factions"
    )

    openings = [
        (
            f"Nothing in {world} is quite as simple as it first "
            f"appears. Records disagree, important people know more "
            f"than they admit, and old events continue to leave traces."
        ),
        (
            f"The mystery surrounding {world} develops slowly. "
            f"Fragments of information appear in different places, "
            f"often contradicting what the characters previously "
            f"believed."
        ),
        (
            f"Long before {protagonist} became involved, something "
            f"already happened beneath the visible history of "
            f"{world}. The evidence is scattered across people, "
            f"places, and forgotten records."
        ),
    ]

    central_lines = [
        (
            f"The central question is: {mystery}"
        ),
        (
            f"At the heart of the mystery is a question that refuses "
            f"to disappear: {mystery}"
        ),
        (
            f"Every major revelation eventually leads back to the "
            f"same unanswered question: {mystery}"
        ),
    ]

    faction_lines = [
        (
            f"Organizations such as {faction_text} possess pieces of "
            f"the truth, but none of them necessarily understand the "
            f"whole picture."
        ),
        (
            f"The major factions each hold different fragments of the "
            f"answer, making alliances and betrayals increasingly "
            f"important as {conflict} develops."
        ),
    ]

    return " ".join([
        choose_description(rng, openings),
        choose_description(rng, central_lines),
        choose_description(rng, faction_lines),
    ])


def make_journey_description(
    seed: str,
    protagonist: str,
    world: str,
    arcs: List[Dict],
) -> str:

    rng = make_description_rng(seed, "journey")

    first_arc = arcs[0]
    middle_arc = arcs[len(arcs) // 2]
    final_arc = arcs[-1]

    options = [
        (
            f"{protagonist}'s journey begins with {first_arc['title']}, "
            f"where incomplete information gives way to discovery. "
            f"As the story reaches {middle_arc['title']}, the scale "
            f"of the conflict changes and earlier assumptions begin "
            f"to collapse. By the time the journey reaches "
            f"{final_arc['title']}, the choices made along the way "
            f"have consequences for the future of {world}."
        ),
        (
            f"The journey is designed to grow rather than simply move "
            f"forward. The early stages focus on discovery through "
            f"{first_arc['title']}; later events widen the conflict "
            f"through {middle_arc['title']}; and the final movement "
            f"brings the accumulated mysteries toward "
            f"{final_arc['title']}."
        ),
        (
            f"Across six hundred chapters, {protagonist} moves from "
            f"the uncertainty of {first_arc['title']} toward the "
            f"larger consequences introduced by {middle_arc['title']}, "
            f"before reaching the final confrontation represented by "
            f"{final_arc['title']}. The journey changes both the "
            f"character and the world around them."
        ),
    ]

    return choose_description(rng, options)


def make_auto_descriptions(
    seed: str,
    blueprint_data: Dict,
) -> Dict:

    world = blueprint_data["world"]
    power = blueprint_data["power_system"]
    protagonist = blueprint_data["protagonist"]
    characters = blueprint_data["characters"]
    antagonists = blueprint_data["antagonists"]
    factions = blueprint_data["factions"]

    title = blueprint_data["title"]
    genre = blueprint_data["genre"]
    conflict = blueprint_data["main_conflict"]
    central_mystery = blueprint_data["central_mystery"]

    world_description = make_world_description(
        seed=seed,
        world=world,
        protagonist=protagonist["name"],
        conflict=conflict,
        faction=factions[0]["name"],
        power=power["name"],
        genre=genre,
    )

    story_description = make_story_description(
        seed=seed,
        title=title,
        protagonist=protagonist["name"],
        conflict=conflict,
        world=world["name"],
        faction=factions[0]["name"],
        power=power["name"],
        central_mystery=central_mystery,
        tone=blueprint_data["tone"],
    )

    people_description = make_people_description(
        seed=seed,
        protagonist=protagonist,
        characters=characters,
        antagonists=antagonists,
    )

    power_description = make_power_description(
        seed=seed,
        power=power,
        protagonist=protagonist["name"],
    )

    mystery_description = make_mystery_description(
        seed=seed,
        world=world["name"],
        protagonist=protagonist["name"],
        conflict=conflict,
        mystery=central_mystery,
        factions=factions,
    )

    journey_description = make_journey_description(
        seed=seed,
        protagonist=protagonist["name"],
        world=world["name"],
        arcs=blueprint_data["arcs"],
    )

    return {
        "world": world_description,
        "story": story_description,
        "people": people_description,
        "power": power_description,
        "mystery": mystery_description,
        "journey": journey_description,
    }
