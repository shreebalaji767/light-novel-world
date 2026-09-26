import hashlib
import random
import secrets
from typing import Dict, List


CHAPTER_COUNT = 600


GENRES = [
    "Dark Fantasy",
    "High Fantasy",
    "Isekai",
    "Romance",
    "Romantic Fantasy",
    "Mystery",
    "Psychological Thriller",
    "Horror",
    "Science Fiction",
    "Cyberpunk",
    "Post-Apocalyptic",
    "Wuxia",
    "Xianxia",
    "Slice of Life",
    "Comedy",
    "Historical Fantasy",
    "Mecha",
    "Time Travel",
    "Supernatural",
    "Steampunk",
    "Military Fantasy",
    "Urban Fantasy",
    "LitRPG",
    "Space Opera",
]


FIRST_NAMES = [
    "Aren", "Kael", "Ren", "Lucian", "Elias", "Noah", "Riven",
    "Akira", "Kaito", "Haruto", "Yuki", "Sora", "Aster", "Leon",
    "Mira", "Elena", "Liora", "Seraphine", "Aya", "Neria",
    "Rhea", "Iris", "Selene", "Aria", "Nadia", "Vera",
    "Cassian", "Dorian", "Rowan", "Silas", "Theo", "Julian",
]


LAST_NAMES = [
    "Vale", "Ashford", "Evernight", "Ravencrest", "Silver",
    "Blackwood", "Stormborn", "Veyr", "Arclight", "Winter",
    "Moonfall", "Dusk", "Starling", "Nightveil", "Draven",
    "Solmere", "Aurel", "Graves", "Eldrin", "Voss",
]


PLACES = [
    "Aurelia",
    "The Ashen Kingdom",
    "Veloria",
    "Eclipse City",
    "The Silver Dominion",
    "Nareth",
    "The Endless Frontier",
    "Valenreach",
    "The Hollow Empire",
    "Elysian",
    "The Obsidian Coast",
    "Caelora",
    "The Crimson Marches",
    "New Avalon",
    "The Last Meridian",
    "Lunaris",
    "The Iron Republic",
    "The Forgotten Continent",
    "The Glass Desert",
    "The Celestial Isles",
]


FACTIONS = [
    "The Silver Court",
    "The Black Order",
    "The Astral Academy",
    "The Crimson Guild",
    "The Night Assembly",
    "The Dawn Legion",
    "The Seven Houses",
    "The Hollow Church",
    "The Royal Institute",
    "The Wandering Clan",
    "The Iron Directorate",
    "The Moon Society",
    "The Phoenix Alliance",
    "The Silent Council",
    "The Meridian Company",
]


POWERS = [
    "Shadow Weaving",
    "Astral Fire",
    "Soul Resonance",
    "Time Fracture",
    "Void Calling",
    "Blood Oath",
    "Spirit Binding",
    "Starforged Aura",
    "Memory Craft",
    "Dream Walking",
    "Lightning Scripture",
    "Mirror Arts",
    "Gravity Manipulation",
    "Frost Dominion",
    "Ember Sight",
    "Reality Threading",
    "Moonlight Swordsmanship",
    "Echo Summoning",
]


OBJECTS = [
    "a broken silver sword",
    "a black pocket watch",
    "a sealed letter",
    "an ancient crown",
    "a crystal key",
    "a nameless journal",
    "a forbidden map",
    "a glass pendant",
    "a mechanical bird",
    "a ruined mask",
    "a star-shaped coin",
    "a blood-red gemstone",
    "a forgotten photograph",
    "a strange compass",
    "a sealed weapon",
    "a fragment of meteorite",
]


CONFLICTS = [
    "a kingdom preparing for war",
    "a forgotten prophecy returning",
    "a mysterious organization manipulating events",
    "an ancient power awakening",
    "a city disappearing one district at a time",
    "a plague affecting memories",
    "a succession crisis",
    "a dimensional breach",
    "a rebellion spreading across the continent",
    "a series of impossible murders",
    "a machine predicting the future",
    "a god whose name has been erased",
    "a civilization returning from beneath the earth",
    "a war between different versions of reality",
]


CHAPTER_VERBS = [
    "Awakening",
    "Arrival",
    "Encounter",
    "Discovery",
    "Whispers",
    "Revelation",
    "Confrontation",
    "Crossing",
    "Inheritance",
    "Betrayal",
    "Return",
    "Descent",
    "Ascension",
    "Fracture",
    "Echo",
    "Promise",
    "Secret",
    "Trial",
    "Oath",
    "Storm",
    "Silence",
    "Memory",
    "Exile",
    "Choice",
    "Aftermath",
]


CHAPTER_NOUNS = [
    "of the Forgotten Gate",
    "of the Silver Moon",
    "of the Last Promise",
    "of the Broken Crown",
    "of the Nameless City",
    "of the Hidden Truth",
    "of the Crimson Sky",
    "of the Endless Road",
    "of the Silent Tower",
    "of the Black Star",
    "of the Lost Kingdom",
    "of the First Flame",
    "of the Empty Throne",
    "of the Ancient Song",
    "of the Final Door",
    "of the Shattered World",
    "of the Wandering Soul",
    "of the Unwritten Future",
]


ARC_NAMES = [
    "The Beginning",
    "The Hidden Village",
    "The First Trial",
    "The Silver Road",
    "The City of Masks",
    "The Broken Kingdom",
    "The Crimson War",
    "The Forgotten Archive",
    "The Night Sea",
    "The Astral Tower",
    "The Seven Crowns",
    "The World Beneath",
    "The Last Frontier",
    "The Time Labyrinth",
    "The Hollow Throne",
    "The Celestial War",
    "The Final Meridian",
]


DESIGN_PRESETS = [
    {
        "mode": "midnight",
        "accent": "#8b5cf6",
        "accent2": "#ec4899",
        "surface": "#11111a",
        "surface2": "#191923",
        "text": "#f8fafc",
        "muted": "#a1a1aa",
    },
    {
        "mode": "emerald",
        "accent": "#10b981",
        "accent2": "#06b6d4",
        "surface": "#081411",
        "surface2": "#0e211b",
        "text": "#ecfdf5",
        "muted": "#9ca3af",
    },
    {
        "mode": "crimson",
        "accent": "#f43f5e",
        "accent2": "#f97316",
        "surface": "#16090d",
        "surface2": "#241016",
        "text": "#fff1f2",
        "muted": "#a8a29e",
    },
    {
        "mode": "ocean",
        "accent": "#38bdf8",
        "accent2": "#6366f1",
        "surface": "#07121c",
        "surface2": "#0d1d2a",
        "text": "#f0f9ff",
        "muted": "#94a3b8",
    },
    {
        "mode": "gold",
        "accent": "#f59e0b",
        "accent2": "#eab308",
        "surface": "#171106",
        "surface2": "#241a09",
        "text": "#fffbeb",
        "muted": "#a8a29e",
    },
]


def stable_rng(seed: str) -> random.Random:
    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    number = int.from_bytes(digest[:16], "big")
    return random.Random(number)


def make_seed() -> str:
    return secrets.token_hex(32)


def pick(rng: random.Random, values):
    return values[rng.randrange(len(values))]


def make_name(rng: random.Random) -> str:
    return f"{pick(rng, FIRST_NAMES)} {pick(rng, LAST_NAMES)}"


def make_title(rng: random.Random, genre: str) -> str:
    templates = [
        "{place}: The {noun}",
        "The {adjective} {noun}",
        "{name} and the {noun}",
        "The {noun} of {place}",
        "When {noun} Awoke",
        "The Last {noun}",
        "Beyond the {noun}",
        "A {adjective} Chronicle",
    ]

    adjectives = [
        "Forgotten",
        "Silent",
        "Crimson",
        "Eternal",
        "Broken",
        "Nameless",
        "Hidden",
        "Fallen",
        "Immortal",
        "Wandering",
        "Unwritten",
        "Infinite",
        "Forsaken",
        "Celestial",
        "Hollow",
    ]

    nouns = [
        "Moon",
        "Throne",
        "Kingdom",
        "Star",
        "Sword",
        "Gate",
        "Empire",
        "Prophecy",
        "Tower",
        "Dream",
        "Memory",
        "World",
        "Heir",
        "Hero",
        "Shadow",
        "Chronicle",
        "Oracle",
        "Flame",
        "Sea",
        "Hour",
    ]

    template = pick(rng, templates)

    return template.format(
        place=pick(rng, PLACES),
        noun=pick(rng, nouns),
        name=make_name(rng),
        adjective=pick(rng, adjectives),
    )


def make_characters(rng: random.Random) -> List[Dict]:
    used = set()
    characters = []

    roles = [
        "protagonist",
        "deuteragonist",
        "rival",
        "mentor",
        "mysterious ally",
        "antagonist",
    ]

    for role in roles:
        name = make_name(rng)

        while name in used:
            name = make_name(rng)

        used.add(name)

        characters.append({
            "name": name,
            "role": role,
            "age": rng.randint(17, 38),
            "ability": pick(rng, POWERS),
            "trait": pick(rng, [
                "quiet but observant",
                "recklessly optimistic",
                "calm under pressure",
                "deeply curious",
                "sarcastic and clever",
                "haunted by the past",
                "protective of others",
                "ambitious and secretive",
                "kind despite a hard exterior",
                "impossibly patient",
            ]),
        })

    return characters


def make_arcs(rng: random.Random) -> List[Dict]:
    arcs = []

    chapter = 1

    while chapter <= CHAPTER_COUNT:
        length = rng.randint(25, 48)
        end = min(CHAPTER_COUNT, chapter + length - 1)

        arcs.append({
            "number": len(arcs) + 1,
            "title": pick(rng, ARC_NAMES),
            "start": chapter,
            "end": end,
            "theme": pick(rng, [
                "discovery",
                "survival",
                "betrayal",
                "war",
                "romance",
                "identity",
                "revenge",
                "friendship",
                "politics",
                "mystery",
                "transformation",
                "sacrifice",
            ]),
        })

        chapter = end + 1

    return arcs


def get_arc(arcs: List[Dict], chapter_number: int) -> Dict:
    for arc in arcs:
        if arc["start"] <= chapter_number <= arc["end"]:
            return arc

    return arcs[-1]


def generate_novel() -> Dict:
    seed = make_seed()
    rng = stable_rng(seed)

    genre = pick(rng, GENRES)
    secondary_genre = pick(rng, [g for g in GENRES if g != genre])

    protagonist = make_name(rng)
    world = pick(rng, PLACES)
    faction = pick(rng, FACTIONS)
    power = pick(rng, POWERS)
    conflict = pick(rng, CONFLICTS)

    title = make_title(rng, genre)

    characters = make_characters(rng)
    arcs = make_arcs(rng)

    design = pick(rng, DESIGN_PRESETS).copy()

    story_id = hashlib.sha256(
        f"{seed}:{title}:{world}:{protagonist}".encode()
    ).hexdigest()[:16]

    synopsis = (
        f"{protagonist} expected an ordinary life until {pick(rng, OBJECTS)} "
        f"appeared in their possession. The object connects them to {world}, "
        f"a place where {conflict}. Drawn into the affairs of {faction}, "
        f"{protagonist} awakens the ability known as {power}. "
        f"What begins as a single impossible incident slowly becomes a journey "
        f"through war, secrets, relationships, and a truth capable of changing "
        f"the entire world."
    )

    return {
        "id": story_id,
        "seed": seed,
        "title": title,
        "genre": genre,
        "secondary_genre": secondary_genre,
        "chapter_count": CHAPTER_COUNT,
        "protagonist": protagonist,
        "world": world,
        "faction": faction,
        "power": power,
        "conflict": conflict,
        "synopsis": synopsis,
        "characters": characters,
        "arcs": arcs,
        "design": design,
    }


def generate_chapter(seed: str, chapter_number: int) -> Dict:
    if chapter_number < 1 or chapter_number > CHAPTER_COUNT:
        raise ValueError("Invalid chapter number")

    rng = stable_rng(f"{seed}:chapter:{chapter_number}")

    base_rng = stable_rng(seed)

    genre = pick(base_rng, GENRES)
    world = pick(base_rng, PLACES)
    faction = pick(base_rng, FACTIONS)
    power = pick(base_rng, POWERS)
    protagonist = make_name(base_rng)

    arc_rng = stable_rng(f"{seed}:arcs")

    # Rebuild the same arc structure deterministically.
    arcs = make_arcs(arc_rng)
    arc = get_arc(arcs, chapter_number)

    title = (
        f"{chapter_number:03d}. "
        f"{pick(rng, CHAPTER_VERBS)} "
        f"{pick(rng, CHAPTER_NOUNS)}"
    )

    location = pick(rng, PLACES)

    supporting_character = make_name(rng)

    developments = [
        f"{protagonist} discovers that the events surrounding {world} "
        f"are connected to a much older conflict.",
        f"The influence of {faction} becomes impossible to ignore.",
        f"A clue concerning {power} changes what {protagonist} believed to be true.",
        f"{supporting_character} arrives with information that could alter the course "
        f"of the journey.",
        f"An apparently insignificant decision creates consequences that will matter "
        f"far beyond this chapter.",
        f"A hidden relationship between two factions is finally exposed.",
        f"The boundaries between allies and enemies become increasingly uncertain.",
    ]

    development = pick(rng, developments)

    complication = pick(rng, [
        "Before the truth can be understood, an unexpected attack interrupts the investigation.",
        "The answer creates a second question that is even more dangerous.",
        "Someone close to the protagonist refuses to explain what they know.",
        "A seemingly harmless object reveals an ability nobody expected.",
        "The group reaches a place that should not exist on any map.",
        "A forgotten memory suddenly becomes relevant.",
        "The protagonist realizes that somebody has been watching them for a long time.",
    ])

    emotional = pick(rng, [
        "For the first time, the protagonist wonders whether moving forward is actually worth the cost.",
        "The silence that follows feels heavier than any argument.",
        "A small moment of trust becomes unexpectedly important.",
        "The protagonist remembers why they started this journey in the first place.",
        "Nobody says what they are truly afraid of, but everyone understands it.",
        "The distance between the characters becomes harder to ignore.",
    ])

    action = pick(rng, [
        "The confrontation is brief but violent.",
        "The escape becomes a desperate race against time.",
        "The two sides collide before either understands the complete situation.",
        "The protagonist is forced to use their ability in a way they have never attempted.",
        "The group survives only because an unexpected ally intervenes.",
        "A carefully prepared plan begins falling apart almost immediately.",
    ])

    revelation = pick(rng, [
        "A name from the past appears in a place where it should never have existed.",
        "The protagonist learns that the original story was incomplete.",
        "The evidence suggests that the enemy may have been following the same mystery.",
        "A sealed record describes an event that has not happened yet.",
        "Someone finally admits that they have known the truth for years.",
        "The object that started everything reacts to the protagonist once again.",
    ])

    paragraphs = [
        (
            f"The road to {location} had become strangely quiet. "
            f"Even the ordinary sounds of the world seemed distant as "
            f"{protagonist} continued forward. Chapter {chapter_number} of the "
            f"journey had begun without ceremony, but something about the air "
            f"felt different."
        ),
        (
            f"Within the current arc, **{arc['title']}**, the central struggle "
            f"had gradually shifted toward {arc['theme']}. "
            f"{development}"
        ),
        (
            f"Nobody had enough time to examine the discovery. "
            f"{complication} The decision that followed would become one of the "
            f"small moments later remembered as a turning point."
        ),
        (
            f"{supporting_character} watched {protagonist} carefully. "
            f"Neither of them spoke immediately. {emotional}"
        ),
        (
            f"Then everything changed. {action} "
            f"The power known as {power} responded in a way that surprised even "
            f"those who had seen it before."
        ),
        (
            f"When the immediate danger finally passed, the characters found "
            f"themselves standing among the remains of what had just happened. "
            f"{revelation}"
        ),
        (
            f"The discovery did not provide an answer. Instead, it opened a "
            f"larger mystery. Somewhere beyond {world}, forces connected to "
            f"{faction} were already moving."
        ),
        (
            f"{protagonist} looked toward the road ahead. There was no guarantee "
            f"that the next step would be the correct one. There was only the "
            f"knowledge that turning back would leave the mystery unresolved."
        ),
        (
            f"As night settled over {location}, the chapter's final clue remained "
            f"hidden in plain sight. Someone had already made the next move."
        ),
    ]

    word_count = sum(len(p.split()) for p in paragraphs)

    return {
        "number": chapter_number,
        "title": title,
        "arc": arc,
        "location": location,
        "genre": genre,
        "paragraphs": paragraphs,
        "word_count": word_count,
    }
