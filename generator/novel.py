from __future__ import annotations

import hashlib
import secrets
import random
import re
from typing import Dict, List


# ============================================================
# CONFIGURATION
# ============================================================

CHAPTER_COUNT = 600


# ============================================================
# GENRES
# ============================================================

GENRES = [
    "Dark Fantasy",
    "Epic Fantasy",
    "High Fantasy",
    "Urban Fantasy",
    "Romantic Fantasy",
    "Mystery",
    "Supernatural Mystery",
    "Science Fiction",
    "Cyberpunk",
    "Space Opera",
    "Post-Apocalyptic",
    "Steampunk",
    "Magical Academy",
    "Martial Arts",
    "Cultivation",
    "Adventure",
    "Thriller",
    "Psychological Fantasy",
    "Time Travel",
    "Historical Fantasy",
    "Mythological Fantasy",
    "Monster Fantasy",
    "Portal Fantasy",
    "Action Fantasy",
]


SECONDARY_GENRES = [
    "Adventure",
    "Mystery",
    "Romance",
    "Drama",
    "Action",
    "Thriller",
    "Supernatural",
    "Political Intrigue",
    "Coming of Age",
    "Exploration",
    "Survival",
    "Comedy",
    "Tragedy",
]


# ============================================================
# WORLDS / PLACES
# ============================================================

PLACES = [
    "Asterion",
    "Velmora",
    "Eldoria",
    "Noxhaven",
    "Caelith",
    "Veyra",
    "Lunareth",
    "Arkenfall",
    "Serathis",
    "Elarion",
    "Valthera",
    "Nocteris",
    "Mystral",
    "Ravenreach",
    "Solmere",
    "Dravora",
    "Aurelia",
    "Kharadon",
    "Evershade",
    "Thalorien",
    "Zeraphine",
    "Mordane",
    "Ilyria",
    "Ashvale",
    "Orinth",
    "Velaris",
    "Nythera",
    "Cindral",
    "Eryndor",
    "Marovelle",
]


FACTIONS = [
    "The Obsidian Covenant",
    "The Silver Assembly",
    "The Crimson Order",
    "The Astral Court",
    "The Veiled Kingdom",
    "The Dawn Guard",
    "The Hollow Circle",
    "The Seven Houses",
    "The Eternal Archive",
    "The Black Meridian",
    "The Moonlit Council",
    "The Iron Dominion",
    "The Starbound Guild",
    "The Silent Church",
    "The Golden Consortium",
    "The Ashen Brotherhood",
    "The Azure Legion",
    "The Nameless Court",
]


POWERS = [
    "Astral Resonance",
    "Void Calling",
    "Soul Weaving",
    "Flame Scripture",
    "Shadow Binding",
    "Chrono Sight",
    "Spirit Echo",
    "Blood Sigil",
    "Dream Walking",
    "Starfire",
    "Gravity Thread",
    "Memory Forge",
    "Thunder Veil",
    "Moonlight Communion",
    "Rune Shaping",
    "Ether Manipulation",
    "Life Thread",
    "Mirror Step",
    "World Sense",
    "Ember Heart",
]


OBJECTS = [
    "a broken silver compass",
    "a black glass key",
    "an ancient pocket watch",
    "a sealed letter",
    "a crystal shard",
    "a rusted ceremonial blade",
    "a strange wooden box",
    "a forgotten diary",
    "a ring bearing an unknown crest",
    "a cracked mirror",
    "a blue stone",
    "a mechanical bird",
    "an old map",
    "a golden coin",
    "a sealed scroll",
    "a black feather",
    "a clockwork pendant",
    "a translucent mask",
    "a small metal sphere",
    "a book without a title",
]


CONFLICTS = [
    "the disappearance of an entire district",
    "a war that was never officially declared",
    "a mysterious succession crisis",
    "the return of an ancient enemy",
    "a series of unexplained murders",
    "a forbidden experiment",
    "the collapse of the old magical order",
    "the awakening of something beneath the capital",
    "a prophecy that contradicts history",
    "the disappearance of several powerful warriors",
    "a secret conflict between rival factions",
    "a forgotten disaster returning to the world",
]


CHAPTER_VERBS = [
    "The Door That",
    "The Night When",
    "The Secret Beneath",
    "The Stranger Who",
    "The Promise That",
    "The Shadow That",
    "The Truth Behind",
    "The Day We",
    "The Memory of",
    "The Path Toward",
    "The Voice From",
    "The Last Light of",
    "The Return of",
    "The Name That",
    "The Silence Before",
]


CHAPTER_NOUNS = [
    "Forgotten",
    "Opened",
    "Returned",
    "Disappeared",
    "Awakened",
    "Changed",
    "Remembered",
    "Burned",
    "Waited",
    "Called",
    "Broke",
    "Answered",
    "Watched",
    "Moved",
    "Whispered",
]


ARC_THEMES = [
    "awakening",
    "discovery",
    "rising conflict",
    "hidden history",
    "betrayal",
    "war",
    "transformation",
    "lost memories",
    "political upheaval",
    "the unknown",
    "confrontation",
    "revelation",
    "collapse",
    "rebirth",
    "final reckoning",
]


ARC_NAMES = [
    "The First Awakening",
    "Echoes of the Forgotten",
    "The Hidden Road",
    "Whispers in the Dark",
    "The Broken Crown",
    "The City Beyond the Mist",
    "The Crimson Turning",
    "The War Beneath the World",
    "The House of Unspoken Names",
    "The Starless Night",
    "The Last Boundary",
    "The Eternal Door",
    "The Ashen Kingdom",
    "The Final Convergence",
    "The Beginning of the End",
]


# ============================================================
# NAME PARTS
# ============================================================

FIRST_NAMES = [
    "Aren",
    "Kael",
    "Liora",
    "Seren",
    "Mira",
    "Elias",
    "Riven",
    "Neria",
    "Darian",
    "Elara",
    "Lucian",
    "Vera",
    "Arian",
    "Selene",
    "Kieran",
    "Lyra",
    "Orin",
    "Nolan",
    "Ayla",
    "Cassian",
    "Rhea",
    "Eryn",
    "Soren",
    "Maren",
    "Iris",
    "Theo",
    "Nadia",
    "Varen",
    "Aria",
    "Ren",
]


LAST_NAMES = [
    "Valen",
    "Ardent",
    "Nox",
    "Raven",
    "Eld",
    "Veyr",
    "Aster",
    "Cael",
    "Morrow",
    "Thorne",
    "Ashen",
    "Vale",
    "Serin",
    "Dawn",
    "Wren",
    "Ever",
    "Drake",
    "Lorne",
    "Voss",
    "Meridian",
]


# ============================================================
# DESIGN SYSTEMS
# ============================================================

DESIGN_PRESETS = [
    {
        "name": "Obsidian",
        "accent": "#b98cff",
        "accent2": "#6f4bd8",
        "surface": "#09090d",
        "surface2": "#12121a",
        "text": "#f5f3ff",
        "muted": "#a9a5b8",
        "hero": "radial-gradient(circle at 70% 20%, rgba(185,140,255,.20), transparent 35%), linear-gradient(135deg,#09090d,#151020)",
    },
    {
        "name": "Ember",
        "accent": "#ff8a5b",
        "accent2": "#d84d2b",
        "surface": "#100a08",
        "surface2": "#1b100d",
        "text": "#fff6f0",
        "muted": "#c4aaa0",
        "hero": "radial-gradient(circle at 70% 20%, rgba(255,138,91,.22), transparent 35%), linear-gradient(135deg,#100a08,#24120c)",
    },
    {
        "name": "Azure",
        "accent": "#5db7ff",
        "accent2": "#277bd4",
        "surface": "#071019",
        "surface2": "#0e1b28",
        "text": "#f1f8ff",
        "muted": "#a4b8ca",
        "hero": "radial-gradient(circle at 70% 20%, rgba(93,183,255,.22), transparent 35%), linear-gradient(135deg,#071019,#0c1c2b)",
    },
    {
        "name": "Verdant",
        "accent": "#66d9a0",
        "accent2": "#299e69",
        "surface": "#07110c",
        "surface2": "#0d1c14",
        "text": "#f0fff6",
        "muted": "#a4bcae",
        "hero": "radial-gradient(circle at 70% 20%, rgba(102,217,160,.20), transparent 35%), linear-gradient(135deg,#07110c,#102219)",
    },
    {
        "name": "Crimson",
        "accent": "#ff667c",
        "accent2": "#c52f4a",
        "surface": "#12080b",
        "surface2": "#1f0d12",
        "text": "#fff2f4",
        "muted": "#c9a5aa",
        "hero": "radial-gradient(circle at 70% 20%, rgba(255,102,124,.22), transparent 35%), linear-gradient(135deg,#12080b,#240d14)",
    },
    {
        "name": "Golden",
        "accent": "#e7c56b",
        "accent2": "#ae8224",
        "surface": "#110f08",
        "surface2": "#1d190d",
        "text": "#fffbed",
        "muted": "#c1b99e",
        "hero": "radial-gradient(circle at 70% 20%, rgba(231,197,107,.20), transparent 35%), linear-gradient(135deg,#110f08,#211c0c)",
    },
    {
        "name": "Rose",
        "accent": "#f49ac2",
        "accent2": "#c65b8e",
        "surface": "#120a10",
        "surface2": "#20121b",
        "text": "#fff4fa",
        "muted": "#c5a8b7",
        "hero": "radial-gradient(circle at 70% 20%, rgba(244,154,194,.22), transparent 35%), linear-gradient(135deg,#120a10,#25131e)",
    },
    {
        "name": "Void",
        "accent": "#8aa4ff",
        "accent2": "#526bd3",
        "surface": "#06070c",
        "surface2": "#0d0f18",
        "text": "#f2f4ff",
        "muted": "#9ea5bd",
        "hero": "radial-gradient(circle at 70% 20%, rgba(138,164,255,.18), transparent 35%), linear-gradient(135deg,#06070c,#101329)",
    },
]


# ============================================================
# RANDOM HELPERS
# ============================================================

def stable_rng(value: str) -> random.Random:
    """
    Creates a deterministic RNG from a string.

    Same seed + same input = same generated data.
    """
    digest = hashlib.sha256(value.encode("utf-8")).digest()
    integer = int.from_bytes(digest[:16], "big")
    return random.Random(integer)


def make_seed() -> str:
    """
    Cryptographically random seed.

    Every request receives a new seed.
    """
    return secrets.token_hex(32)


def pick(rng: random.Random, items: list):
    return items[rng.randrange(len(items))]


def make_name(rng: random.Random) -> str:
    return f"{pick(rng, FIRST_NAMES)} {pick(rng, LAST_NAMES)}"


# ============================================================
# UNIQUE SELECTION
# ============================================================

def pick_unique(
    rng: random.Random,
    items: list,
    used: set,
):
    """
    Pick an item not previously used when possible.
    """
    available = [item for item in items if item not in used]

    if not available:
        return pick(rng, items)

    value = pick(rng, available)
    used.add(value)

    return value


def make_unique_name(
    rng: random.Random,
    used_names: set,
) -> str:
    """
    Generate a name not already used in this novel.
    """
    for _ in range(100):
        name = make_name(rng)

        if name not in used_names:
            used_names.add(name)
            return name

    # Extremely unlikely fallback.
    name = f"{make_name(rng)} {rng.randrange(1000, 9999)}"
    used_names.add(name)

    return name


# ============================================================
# TITLE GENERATION
# ============================================================

TITLE_PREFIXES = [
    "The",
    "A",
    "When",
    "Beyond",
    "Under",
    "After",
    "Before",
    "Through",
    "Inside",
    "The Last",
    "The First",
    "Echoes of",
    "Children of",
    "Kingdom of",
    "Chronicles of",
]


TITLE_WORDS = [
    "Forgotten",
    "Eternal",
    "Crimson",
    "Silent",
    "Broken",
    "Hidden",
    "Fallen",
    "Endless",
    "Distant",
    "Shattered",
    "Celestial",
    "Midnight",
    "Infinite",
    "Vanishing",
    "Hollow",
    "Wandering",
    "Awakened",
    "Lost",
    "Ancient",
    "Burning",
]


TITLE_NOUNS = [
    "Moon",
    "Crown",
    "Kingdom",
    "Star",
    "Throne",
    "World",
    "Gate",
    "Memory",
    "Shadow",
    "Empire",
    "Dream",
    "Tower",
    "Garden",
    "Sea",
    "Sky",
    "Flame",
    "Road",
    "Prophecy",
    "City",
    "Door",
]


def make_title(rng: random.Random) -> str:
    prefix = pick(rng, TITLE_PREFIXES)
    adjective = pick(rng, TITLE_WORDS)
    noun = pick(rng, TITLE_NOUNS)

    patterns = [
        f"{prefix} {adjective} {noun}",
        f"{prefix} {adjective} {noun}",
        f"{adjective} {noun}",
        f"{prefix} {noun} of {adjective}",
    ]

    return pick(rng, patterns)


# ============================================================
# CHARACTERS
# ============================================================

CHARACTER_ROLES = [
    "Protagonist",
    "Guardian",
    "Rival",
    "Scholar",
    "Wanderer",
    "Knight",
    "Mage",
    "Strategist",
    "Heir",
    "Assassin",
    "Explorer",
    "Outsider",
]


CHARACTER_TRAITS = [
    "quiet but observant",
    "recklessly optimistic",
    "calm under pressure",
    "deeply suspicious",
    "curious about forbidden knowledge",
    "protective of their companions",
    "haunted by an unexplained memory",
    "driven by an old promise",
    "unable to trust easily",
    "surprisingly compassionate",
    "ambitious but uncertain",
    "patient and calculating",
]


ABILITIES = [
    "Can sense hidden energy",
    "Can manipulate ancient symbols",
    "Can temporarily alter gravity",
    "Can communicate with spirits",
    "Can perceive possible futures",
    "Can absorb magical attacks",
    "Can create protective barriers",
    "Can manipulate memories",
    "Can move through shadows",
    "Can summon spectral weapons",
    "Can read forgotten languages",
    "Can control elemental energy",
]


def make_characters(
    rng: random.Random,
    protagonist: str,
) -> List[Dict]:
    used_names = {protagonist}
    characters = []

    protagonist_traits = pick(rng, CHARACTER_TRAITS)
    protagonist_ability = pick(rng, ABILITIES)

    characters.append(
        {
            "name": protagonist,
            "role": "Protagonist",
            "trait": protagonist_traits,
            "ability": protagonist_ability,
        }
    )

    roles = [
        role for role in CHARACTER_ROLES
        if role != "Protagonist"
    ]

    for role in roles[:5]:
        characters.append(
            {
                "name": make_unique_name(rng, used_names),
                "role": role,
                "trait": pick(rng, CHARACTER_TRAITS),
                "ability": pick(rng, ABILITIES),
            }
        )

    return characters


# ============================================================
# ARC GENERATION
# ============================================================

def make_arcs(rng: random.Random) -> List[Dict]:
    arcs = []

    chapters_per_arc = CHAPTER_COUNT // 15

    for index in range(15):
        start = index * chapters_per_arc + 1

        if index == 14:
            end = CHAPTER_COUNT
        else:
            end = (index + 1) * chapters_per_arc

        title = ARC_NAMES[index]

        arcs.append(
            {
                "number": index + 1,
                "title": title,
                "start": start,
                "end": end,
                "theme": pick(rng, ARC_THEMES),
            }
        )

    return arcs


def get_arc(
    arcs: List[Dict],
    chapter_number: int,
) -> Dict:
    for arc in arcs:
        if arc["start"] <= chapter_number <= arc["end"]:
            return arc

    return arcs[-1]


# ============================================================
# DESIGN GENERATION
# ============================================================

def make_design(rng: random.Random) -> Dict:
    preset = dict(pick(rng, DESIGN_PRESETS))

    # Add subtle generated variations while preserving readability.
    preset["radius"] = pick(
        rng,
        [
            "14px",
            "18px",
            "22px",
            "26px",
            "30px",
        ],
    )

    preset["shadow"] = pick(
        rng,
        [
            "0 20px 60px rgba(0,0,0,.25)",
            "0 24px 80px rgba(0,0,0,.32)",
            "0 16px 50px rgba(0,0,0,.20)",
        ],
    )

    preset["hero_style"] = pick(
        rng,
        [
            "cinematic",
            "minimal",
            "dramatic",
            "mystical",
            "futuristic",
        ],
    )

    return preset


# ============================================================
# NOVEL GENERATION
# ============================================================

def generate_novel() -> Dict:
    """
    Creates a completely new novel on every HTTP request.

    The seed is cryptographically random.
    """
    seed = make_seed()

    rng = stable_rng(seed)

    genre = pick(rng, GENRES)
    secondary_genre = pick(rng, SECONDARY_GENRES)

    world = pick(rng, PLACES)
    faction = pick(rng, FACTIONS)
    power = pick(rng, POWERS)
    conflict = pick(rng, CONFLICTS)

    protagonist = make_unique_name(
        rng,
        set(),
    )

    title = make_title(rng)

    design = make_design(rng)

    characters = make_characters(
        rng,
        protagonist,
    )

    arc_rng = stable_rng(f"{seed}:arcs")
    arcs = make_arcs(arc_rng)

    synopsis_templates = [
        (
            f"In the world of {world}, {protagonist} becomes trapped "
            f"inside a conflict involving {faction}. When the power "
            f"known as {power} begins behaving strangely, an old mystery "
            f"returns and threatens to change everything."
        ),
        (
            f"{protagonist} expected an ordinary journey through {world}. "
            f"Instead, they become connected to {conflict}. As the "
            f"mysterious power of {power} awakens, the boundaries between "
            f"legend and reality begin to disappear."
        ),
        (
            f"Something is changing in {world}. The ancient influence of "
            f"{faction} is returning, and {protagonist} discovers that "
            f"{power} may be connected to a secret buried for generations."
        ),
        (
            f"When {protagonist} discovers evidence connected to "
            f"{conflict}, they are pulled into a journey across {world}. "
            f"Every answer reveals another question, and the people "
            f"closest to them may know more than they admit."
        ),
    ]

    synopsis = pick(rng, synopsis_templates)

    return {
        "seed": seed,
        "title": title,
        "genre": genre,
        "secondary_genre": secondary_genre,
        "world": world,
        "faction": faction,
        "power": power,
        "conflict": conflict,
        "protagonist": protagonist,
        "synopsis": synopsis,
        "chapter_count": CHAPTER_COUNT,
        "characters": characters,
        "arcs": arcs,
        "design": design,
    }


# ============================================================
# CHAPTER CONTENT
# ============================================================

def clean_words(text: str) -> List[str]:
    return re.findall(r"\S+", text)


def word_count(paragraphs: List[str]) -> int:
    return sum(
        len(clean_words(paragraph))
        for paragraph in paragraphs
    )


def trim_to_exact_words(
    paragraphs: List[str],
    target: int,
) -> List[str]:
    """
    Makes the final chapter exactly target words.

    The final paragraph is shortened if necessary.
    """
    total = word_count(paragraphs)

    if total == target:
        return paragraphs

    if total < target:
        return paragraphs

    result = []
    remaining = target

    for paragraph in paragraphs:
        words = clean_words(paragraph)

        if remaining <= 0:
            break

        if len(words) <= remaining:
            result.append(paragraph)
            remaining -= len(words)
        else:
            shortened = " ".join(words[:remaining])

            if shortened:
                result.append(shortened)

            remaining = 0

    return result


def generate_chapter(
    seed: str,
    chapter_number: int,
) -> Dict:

    if chapter_number < 1 or chapter_number > CHAPTER_COUNT:
        raise ValueError("Invalid chapter number")

    rng = stable_rng(
        f"{seed}:chapter:{chapter_number}"
    )

    base_rng = stable_rng(seed)

    # --------------------------------------------------------
    # RECREATE NOVEL CORE
    # --------------------------------------------------------

    genre = pick(base_rng, GENRES)
    secondary_genre = pick(base_rng, SECONDARY_GENRES)

    world = pick(base_rng, PLACES)
    faction = pick(base_rng, FACTIONS)
    power = pick(base_rng, POWERS)
    conflict = pick(base_rng, CONFLICTS)

    protagonist = make_unique_name(
        base_rng,
        set(),
    )

    arc_rng = stable_rng(
        f"{seed}:arcs"
    )

    arcs = make_arcs(arc_rng)

    arc = get_arc(
        arcs,
        chapter_number,
    )

    # --------------------------------------------------------
    # CHAPTER-SPECIFIC VALUES
    # --------------------------------------------------------

    used_places = set()
    used_objects = set()
    used_names = {protagonist}

    location = pick_unique(
        rng,
        PLACES,
        used_places,
    )

    object_item = pick_unique(
        rng,
        OBJECTS,
        used_objects,
    )

    conflict_item = pick(
        rng,
        CONFLICTS,
    )

    supporting_character = make_unique_name(
        rng,
        used_names,
    )

    secondary_character = make_unique_name(
        rng,
        used_names,
    )

    rival_character = make_unique_name(
        rng,
        used_names,
    )

    # --------------------------------------------------------
    # CHAPTER TITLE
    # --------------------------------------------------------

    title = (
        f"Chapter {chapter_number:03d}: "
        f"{pick(rng, CHAPTER_VERBS)} "
        f"{pick(rng, CHAPTER_NOUNS)}"
    )

    # --------------------------------------------------------
    # STORY POOLS
    # --------------------------------------------------------

    openings = [
        (
            f"Morning arrived over {location} beneath a sky that looked "
            f"far too quiet for the events that had taken place during "
            f"the previous night. {protagonist} stood beside the window, "
            f"watching the first travelers move through the distant street."
        ),
        (
            f"Rain covered {location} when {protagonist} finally woke. "
            f"The sound of water against the roof should have been calming, "
            f"but something about the silence between each distant thunder "
            f"was deeply unsettling."
        ),
        (
            f"{protagonist} woke before sunrise with the strange certainty "
            f"that someone had spoken their name. The room was empty. "
            f"Yet the feeling remained, as though an unseen presence "
            f"had followed them into the night."
        ),
        (
            f"The journey had brought them to {location} just before "
            f"darkness. From a distance the settlement appeared ordinary. "
            f"Only after entering its streets did {protagonist} notice "
            f"the abandoned buildings and shuttered windows."
        ),
    ]

    discoveries = [
        (
            f"Near an abandoned structure, {protagonist} discovered "
            f"{object_item}. Dust covered its surface, yet a faint "
            f"warmth remained beneath the material."
        ),
        (
            f"Behind a damaged wall they found a narrow passage. "
            f"The entrance had been carefully concealed, and the stone "
            f"around it carried markings that looked older than the town."
        ),
        (
            f"A forgotten document contained several references to "
            f"{faction}. Most of the writing had faded, but a single "
            f"paragraph remained clear enough to read."
        ),
        (
            f"Footprints crossed the dust near the entrance. They were "
            f"fresh enough to prove that someone had arrived before them, "
            f"yet there was no sign of where that person had gone."
        ),
        (
            f"A low sound emerged from beneath the ground. Following it "
            f"led the group to a chamber that should not have existed "
            f"beneath {location}."
        ),
    ]

    developments = [
        (
            f"The discovery appeared connected to the larger mystery "
            f"surrounding {world}."
        ),
        (
            f"The evidence suggested that {faction} had been involved "
            f"in these events for much longer than anyone realized."
        ),
        (
            f"The information contradicted what {protagonist} believed "
            f"about {power}."
        ),
        (
            f"The discovery revealed that the current conflict was only "
            f"one part of a struggle that had begun generations earlier."
        ),
        (
            f"The evidence seemed directly connected to {conflict_item}."
        ),
    ]

    complications = [
        (
            "Before anyone could investigate further, footsteps echoed "
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
            f"{object_item.capitalize()} suddenly reacted to "
            f"{protagonist}'s presence."
        ),
        (
            "A distant explosion interrupted the conversation."
        ),
        (
            "The lights disappeared one after another."
        ),
    ]

    emotional_events = [
        (
            f"{protagonist} remembered why the journey had begun."
        ),
        (
            f"{supporting_character} finally admitted that they were "
            f"afraid of what would happen next."
        ),
        (
            f"{secondary_character} revealed a secret that had been "
            f"hidden since the beginning of the journey."
        ),
        (
            "The argument that followed was not really about the "
            "discovery. It was about trust."
        ),
        (
            "For several seconds nobody knew what to say. "
            "The silence made the danger feel closer."
        ),
    ]

    action_events = [
        (
            f"The confrontation began before anyone was prepared. "
            f"{protagonist} moved first, using {power} to create "
            f"an opening for the others."
        ),
        (
            f"The attackers moved quickly. {supporting_character} "
            f"blocked the first strike while {protagonist} searched "
            f"for a way through."
        ),
        (
            "The ground shook violently. Something enormous was moving "
            "beneath the structure."
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
            f"The energy surrounding {protagonist} changed shape, "
            f"behaving in a way nobody had witnessed before."
        ),
        (
            f"For several seconds {protagonist} could see fragments "
            f"of possible futures."
        ),
        (
            f"The ability responded to {object_item} rather than "
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
            "The evidence suggested that someone had deliberately "
            "created the current conflict."
        ),
        (
            f"{protagonist} discovered that the enemy knew their name."
        ),
        (
            "The document contained a prediction describing an event "
            "that had not happened yet."
        ),
        (
            f"The symbol matched the mark that appeared whenever "
            f"{power} was activated."
        ),
        (
            "The truth was far older than the current generation."
        ),
    ]

    reflections = [
        (
            f"{protagonist} stood alone for several minutes, thinking "
            f"about everything that had happened."
        ),
        (
            "The others discussed their options, but every choice "
            "seemed to carry a different kind of danger."
        ),
        (
            "Nobody wanted to admit how serious the situation had become."
        ),
        (
            "The journey had started with a single unanswered question. "
            "Now there were dozens."
        ),
        (
            "Trust had become more valuable than information, and "
            "neither was easy to obtain."
        ),
    ]

    transitions = [
        (
            f"By evening the immediate danger had passed. "
            f"The group prepared to leave {location} before dawn."
        ),
        (
            f"Night fell over {location}. The streets became empty, "
            "but the feeling of being watched never disappeared."
        ),
        (
            "The group found temporary shelter and began planning "
            "their next move."
        ),
        (
            "After everything that had happened, sleep was difficult."
        ),
    ]

    cliffhangers = [
        (
            f"Just before midnight, somebody whispered "
            f"{protagonist}'s name from outside the room."
        ),
        (
            f"A message appeared beside {object_item}: "
            f"DO NOT TRUST THE PERSON BESIDE YOU."
        ),
        (
            "Far beyond the horizon, a strange light appeared in the sky."
        ),
        (
            "The sealed door opened by itself."
        ),
        (
            f"A new symbol appeared on {protagonist}'s hand."
        ),
        (
            "Someone left a letter outside the door. "
            "It contained tomorrow's date."
        ),
        (
            f"{rival_character}'s voice came from the darkness."
        ),
    ]

    dialogue_sets = [
        [
            f'"We should leave," {supporting_character} said.',
            f'"Not yet," {protagonist} replied.',
            '"You saw what happened. Staying here is dangerous."',
            '"Then we find out why it happened before we leave."',
        ],
        [
            f'"How long have you known?" {protagonist} asked.',
            f'{supporting_character} looked away.',
            '"Long enough to know that the truth is worse than the rumor."',
            '"That is not an answer."',
            '"It is the only answer I can give you right now."',
        ],
        [
            f'"This changes everything," {secondary_character} whispered.',
            f'"No," {protagonist} said. "It explains everything."',
            '"Those are not the same thing."',
            '"I know."',
        ],
        [
            f'"Who sent you?" {protagonist} demanded.',
            f'{rival_character} smiled.',
            '"You still think someone sent me?"',
            '"Then why are you here?"',
            '"Because you finally reached the place I was waiting for."',
        ],
    ]

    # --------------------------------------------------------
    # BUILD
    # --------------------------------------------------------

    paragraphs = []

    paragraphs.append(
        pick(rng, openings)
    )

    paragraphs.append(
        (
            f"Chapter {chapter_number} belongs to the "
            f"{arc['title']} arc, a period shaped by "
            f"{arc['theme']}. The journey has already changed "
            f"{protagonist}, but the events waiting in {location} "
            f"will force another decision."
        )
    )

    paragraphs.append(
        pick(rng, discoveries)
    )

    paragraphs.append(
        (
            f"For several seconds nobody moved. "
            f"{supporting_character} examined the discovery while "
            f"{secondary_character} watched the entrance."
        )
    )

    paragraphs.append(
        pick(rng, developments)
    )

    paragraphs.append(
        (
            f"The implications were difficult to ignore. If the evidence "
            f"was genuine, then the events happening now were connected "
            f"to something that had begun long before {protagonist} "
            f"entered the story."
        )
    )

    paragraphs.append(
        pick(rng, complications)
    )

    paragraphs.append(
        (
            f"{protagonist} immediately understood that there was no "
            f"longer enough time for careful planning. Whatever was "
            f"approaching would arrive soon."
        )
    )

    dialogue = pick(rng, dialogue_sets)

    paragraphs.extend(dialogue)

    paragraphs.append(
        (
            "The conversation ended without agreement. Everyone "
            "understood that the next decision would affect more "
            "than the people standing in the room."
        )
    )

    paragraphs.append(
        pick(rng, emotional_events)
    )

    paragraphs.append(
        (
            f"Outside, the wind grew stronger. Its sound travelled "
            f"through the streets of {location}, carrying distant voices "
            "and the metallic sound of something moving through the dark."
        )
    )

    paragraphs.append(
        pick(rng, action_events)
    )

    paragraphs.append(
        (
            f"{protagonist} barely had enough time to react. "
            "The situation had changed from an investigation into "
            "a fight for survival."
        )
    )

    paragraphs.append(
        pick(rng, power_events)
    )

    paragraphs.append(
        (
            "The sudden release of power forced everyone nearby to "
            "retreat. For one impossible moment, the world seemed "
            "to stop moving."
        )
    )

    paragraphs.append(
        (
            f"{protagonist} could hear their own breathing. "
            "The strange energy disappeared almost as quickly as "
            "it had appeared."
        )
    )

    paragraphs.append(
        pick(rng, revelations)
    )

    paragraphs.append(
        (
            "The revelation left the group silent. It did not solve "
            "the mystery. Instead, it revealed that the mystery was "
            "far larger than they had imagined."
        )
    )

    paragraphs.append(
        pick(rng, reflections)
    )

    paragraphs.append(
        (
            f"{supporting_character} finally looked toward "
            f"{protagonist}. There was no certainty in their expression, "
            "only the understanding that the journey had reached "
            "another turning point."
        )
    )

    paragraphs.append(
        (
            f"The name of {faction} appeared again in their discussion. "
            "The organization had been present in too many places "
            "to be coincidence."
        )
    )

    paragraphs.append(
        (
            f"The conflict surrounding {conflict_item} was becoming "
            "impossible to separate from their personal journey."
        )
    )

    paragraphs.append(
        pick(rng, transitions)
    )

    paragraphs.append(
        (
            f"Before leaving, {protagonist} looked back one final time. "
            f"The place seemed ordinary again, almost peaceful. "
            "But the silence felt artificial."
        )
    )

    # --------------------------------------------------------
    # UNIQUE BRIDGES
    # --------------------------------------------------------

    bridge_paragraphs = [
        (
            f"The group spent several minutes checking the area again. "
            f"They searched the walls, floor, and nearby objects for "
            f"another clue. Nothing appeared immediately."
        ),
        (
            f"{protagonist} returned to {object_item}. The object remained "
            "unchanged, yet something about it felt different now."
        ),
        (
            f"{secondary_character} suggested that the answer might not "
            "be hidden inside the object. Perhaps the object itself "
            "was only a key."
        ),
        (
            "The suggestion changed the way everyone looked at the room."
        ),
        (
            f"{supporting_character} remembered an old story involving "
            f"{world}. The details had always sounded like a myth, "
            "but they suddenly appeared strangely relevant."
        ),
        (
            "The discussion continued quietly. Each person contributed "
            "what little they knew, and slowly a pattern began to appear."
        ),
        (
            "The pattern was incomplete, but it was enough to establish "
            "a possible direction."
        ),
        (
            f"{protagonist} realized that the next destination was "
            "no longer a matter of choice."
        ),
        (
            "The road ahead would take them closer to the heart of "
            "the mystery, whether they were ready or not."
        ),
        (
            f"Another distant sound echoed through {location}. "
            "Nobody moved until it disappeared."
        ),
        (
            "When the silence returned, it somehow felt worse than before."
        ),
        (
            f"{rival_character} had disappeared during the confusion. "
            "Nobody knew when they had left."
        ),
        (
            "That disappearance created another question that would "
            "have to wait until later."
        ),
        (
            "For now, survival remained more important than answers."
        ),
    ]

    # Shuffle the bridge pool for this chapter.
    shuffled_bridges = list(bridge_paragraphs)
    rng.shuffle(shuffled_bridges)

    bridge_index = 0

    # Aim beyond 800 before exact trimming.
    while word_count(paragraphs) < 810:
        paragraphs.append(
            shuffled_bridges[
                bridge_index % len(shuffled_bridges)
            ]
        )

        bridge_index += 1

        if bridge_index > 100:
            break

    # --------------------------------------------------------
    # ENDING
    # --------------------------------------------------------

    paragraphs.append(
        pick(rng, cliffhangers)
    )

    paragraphs.append(
        (
            f"{protagonist} stared into the darkness. "
            "The answer would have to wait until tomorrow."
        )
    )

    # --------------------------------------------------------
    # EXACTLY 800 WORDS
    # --------------------------------------------------------

    paragraphs = trim_to_exact_words(
        paragraphs,
        800,
    )

    return {
        "number": chapter_number,
        "title": title,
        "arc": arc,
        "location": location,
        "genre": genre,
        "paragraphs": paragraphs,
        "word_count": word_count(paragraphs),
    }
