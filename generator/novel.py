from __future__ import annotations

import hashlib
import random
import re
import secrets
from functools import lru_cache
from typing import Dict, List


# ============================================================
# CONFIGURATION
# ============================================================

AUTHOR = "blssnvj21"

CHAPTER_COUNT = 600
CHAPTER_WORD_COUNT = 800

ARC_COUNT = 15
CHAPTERS_PER_ARC = CHAPTER_COUNT // ARC_COUNT


# ============================================================
# GENRES
# ============================================================

GENRES = [
    # Fantasy
    "Fantasy",
    "High Fantasy",
    "Epic Fantasy",
    "Dark Fantasy",
    "Low Fantasy",
    "Urban Fantasy",
    "Romantic Fantasy",
    "Historical Fantasy",
    "Mythological Fantasy",
    "Fairy-Tale Fantasy",
    "Grimdark Fantasy",
    "Sword and Sorcery",
    "Heroic Fantasy",
    "Magical Realism",
    "Portal Fantasy",
    "Isekai",
    "Reverse Isekai",
    "Reincarnation Fantasy",
    "Regression Fantasy",
    "Villainess Fantasy",
    "Royal Fantasy",
    "Kingdom Building",
    "Political Fantasy",
    "Academy Fantasy",
    "Magic Academy",
    "Monster Fantasy",
    "Beast Taming Fantasy",
    "Dungeon Fantasy",
    "Tower Fantasy",
    "Survival Fantasy",
    "Travel Fantasy",
    "Adventure Fantasy",
    "Cozy Fantasy",
    "Military Fantasy",
    "Gaslamp Fantasy",
    "Steampunk Fantasy",
    "Comic Fantasy",
    "Parody Fantasy",

    # Eastern Fantasy / Cultivation
    "Xianxia",
    "Xuanhuan",
    "Wuxia",
    "Qihuan",
    "Xianhuan",
    "Cultivation",
    "Immortal Cultivation",
    "Demonic Cultivation",
    "Murim",
    "Martial Arts",
    "Eastern Fantasy",
    "Chinese Historical Fantasy",
    "Chinese Mythological Fantasy",
    "Korean Fantasy",
    "Japanese Fantasy",

    # Science Fiction
    "Science Fiction",
    "Hard Science Fiction",
    "Soft Science Fiction",
    "Space Opera",
    "Military Science Fiction",
    "Cyberpunk",
    "Post-Cyberpunk",
    "Solarpunk",
    "Steampunk",
    "Dieselpunk",
    "Biopunk",
    "Clockpunk",
    "Nanopunk",
    "Mecha",
    "Space Fantasy",
    "Galactic Empire",
    "Alien Invasion",
    "First Contact",
    "Time Travel",
    "Time Loop",
    "Parallel Worlds",
    "Alternate History",
    "Dystopian",
    "Utopian",
    "Post-Apocalyptic",
    "Apocalyptic",
    "Climate Fiction",
    "Artificial Intelligence",
    "Virtual Reality",
    "Simulation Fiction",
    "Space Survival",
    "AI Fiction",
    "Space Western",

    # Action / Adventure
    "Action",
    "Adventure",
    "Action Adventure",
    "Military",
    "War",
    "Battle Fantasy",
    "Monster Hunting",
    "Treasure Hunting",
    "Exploration",
    "Expedition",
    "Survival",
    "Quest",
    "Revenge",
    "Conspiracy",
    "Espionage",
    "Heist",
    "Pirate Adventure",
    "Road Adventure",
    "Tournament",
    "Travel",
    "Road Story",

    # Romance
    "Romance",
    "Romantic Comedy",
    "Slow-Burn Romance",
    "School Romance",
    "College Romance",
    "Fantasy Romance",
    "Historical Romance",
    "Royal Romance",
    "Political Romance",
    "Tragic Romance",
    "Forbidden Romance",
    "First Love",
    "Second Chance Romance",
    "Enemies to Lovers",
    "Friends to Lovers",
    "Fake Relationship",
    "Marriage of Convenience",
    "Harem",
    "Reverse Harem",
    "Love Triangle",
    "Poly Romance",
    "Boys Love",
    "Girls Love",
    "Yuri",
    "Shoujo Romance",
    "Josei Romance",

    # Comedy / Parody
    "Comedy",
    "Dark Comedy",
    "Situational Comedy",
    "Slapstick Comedy",
    "Absurdist Comedy",
    "Deadpan Comedy",
    "Satirical Comedy",
    "Parody",
    "Genre Parody",
    "Fantasy Parody",
    "Isekai Parody",
    "Cultivation Parody",
    "System Parody",
    "Academy Parody",
    "Superhero Parody",
    "Villain Parody",
    "Hero Parody",
    "Reverse Isekai Comedy",
    "Self-Aware Comedy",
    "Meta Comedy",
    "Chaotic Comedy",
    "Fourth-Wall Comedy",
    "Absurd Comedy",

    # Slice of Life
    "Slice of Life",
    "School Life",
    "High School",
    "College Life",
    "Workplace",
    "Family Drama",
    "Healing",
    "Iyashikei",
    "Daily Life",
    "Small Town",
    "Countryside Life",
    "Restaurant Life",
    "Cafe Life",
    "Travel Slice of Life",
    "Found Family",

    # Mystery / Thriller
    "Mystery",
    "Detective",
    "Crime",
    "Crime Thriller",
    "Psychological Thriller",
    "Political Thriller",
    "Conspiracy Thriller",
    "Techno Thriller",
    "Legal Thriller",
    "Espionage Thriller",
    "Suspense",
    "Whodunit",
    "Locked Room Mystery",
    "Supernatural Mystery",
    "Historical Mystery",
    "Occult Mystery",
    "Urban Mystery",
    "Noir",
    "Hardboiled Mystery",
    "Survival Thriller",

    # Horror
    "Horror",
    "Psychological Horror",
    "Cosmic Horror",
    "Body Horror",
    "Gothic Horror",
    "Supernatural Horror",
    "Occult Horror",
    "Monster Horror",
    "Survival Horror",
    "Slasher",
    "Paranormal Horror",
    "Folk Horror",
    "Dark Horror",
    "Apocalyptic Horror",
    "Existential Horror",

    # Supernatural
    "Supernatural",
    "Paranormal",
    "Occult",
    "Ghost Story",
    "Demon Fantasy",
    "Angel Fantasy",
    "Vampire",
    "Werewolf",
    "Spirit World",
    "Psychic Powers",
    "Urban Supernatural",
    "Supernatural Romance",

    # Psychological
    "Psychological",
    "Psychological Drama",
    "Psychological Mystery",
    "Psychological Fantasy",
    "Mind Games",
    "Identity Mystery",
    "Memory Mystery",
    "Unreliable Narrator",
    "Character Study",
    "Existential Fiction",

    # Drama
    "Drama",
    "Character Drama",
    "Political Drama",
    "Historical Drama",
    "Romantic Drama",
    "Tragedy",
    "Melodrama",
    "Coming of Age",
    "Redemption",
    "Betrayal Drama",
    "Revenge Drama",

    # Game / System
    "LitRPG",
    "GameLit",
    "System",
    "Leveling System",
    "Dungeon Core",
    "Dungeon Master",
    "Tower Climbing",
    "Infinite Tower",
    "Virtual Reality Game",
    "Death Game",
    "Battle Royale",
    "RPG Fantasy",
    "Strategy Game",
    "Management System",
    "Skill Tree",
    "Status Window",
    "Quest System",

    # Academy
    "Academy",
    "Military Academy",
    "Martial Arts Academy",
    "Monster Academy",
    "Hero Academy",
    "Villain Academy",
    "Supernatural Academy",
    "Elite School",
    "School Battle",
    "School Mystery",
    "School Comedy",

    # Character / Trope
    "Villainess",
    "Otome Game",
    "Otome Isekai",
    "Villain Protagonist",
    "Antihero",
    "Anti-Villain",
    "Overpowered Protagonist",
    "Weak-to-Strong",
    "Hidden Power",
    "Secret Identity",
    "Reincarnated Protagonist",
    "Regression",
    "Time Rewind",
    "Second Life",
    "Body Swap",
    "Gender Bender",
    "Possession",
    "Summoning",
    "Chosen One",
    "Nobody to Hero",
    "Rise to Power",
    "Kingdom Builder",
    "Merchant Protagonist",
    "Crafting",
    "Cooking Fantasy",
    "Healing Fantasy",
    "Farming Fantasy",
    "Monster Protagonist",
    "Non-Human Protagonist",

    # Historical
    "Historical Fiction",
    "Historical Adventure",
    "Historical War",
    "Samurai Fiction",
    "Ninja Fiction",
    "Pirate Fiction",
    "Medieval Fiction",
    "Ancient Civilization",
    "Royal Court Drama",
    "Period Drama",

    # Sports
    "Sports",
    "Football",
    "Soccer",
    "Basketball",
    "Baseball",
    "Boxing",
    "Martial Arts Sports",
    "Tennis",
    "Racing",
    "Motorsports",
    "Esports",
    "Competitive Gaming",

    # Technology / Mecha
    "Military Mecha",
    "Robot War",
    "Battle Mecha",
    "Android",
    "Cyborg",
    "Space Military",
    "Future War",
    "Tech Fantasy",

    # Social / Political
    "Political Intrigue",
    "Court Intrigue",
    "Royal Politics",
    "Kingdom Politics",
    "Faction Conflict",
    "Revolution",
    "Civil War",
    "Empire Building",
    "Diplomacy",
    "Economic Fiction",
    "Merchant Drama",
    "Social Commentary",

    # Experimental / Meta
    "Meta Fiction",
    "Self-Aware Fiction",
    "Narrative Experiment",
    "Nonlinear Fiction",
    "Multiple Protagonists",
    "Anthology Fantasy",
    "Time-Fragmented Story",
    "Dream Fiction",
    "Surreal Fiction",
]


# ============================================================
# SECONDARY GENRES
# ============================================================

PARODY_GENRES = {
    "Parody", "Genre Parody", "Fantasy Parody", "Isekai Parody",
    "Cultivation Parody", "System Parody", "Academy Parody",
    "Superhero Parody", "Villain Parody", "Hero Parody",
    "Self-Aware Comedy", "Meta Comedy", "Chaotic Comedy",
    "Absurd Comedy", "Fourth-Wall Comedy",
}

PARODY_LINES = [
    "A narrator somewhere quietly questioned why this situation was following the exact rules of a light novel.",
    "The protagonist considered making a dramatic speech, then remembered they had not prepared one.",
    "A suspiciously convenient coincidence arrived exactly on schedule and was immediately treated with distrust.",
    "The situation had become so dramatic that even the background music seemed to be looking for an exit.",
    "Someone mentioned destiny. Everyone stared at them until they stopped.",
    "The universe appeared to have a very specific sense of humor, and unfortunately the protagonist was the joke.",
]

SECONDARY_GENRES = [
    "Adventure",
    "Action",
    "Romance",
    "Comedy",
    "Parody",
    "Satire",
    "Drama",
    "Mystery",
    "Thriller",
    "Horror",
    "Psychological",
    "Slice of Life",
    "Coming of Age",
    "School Life",
    "Academy",
    "Supernatural",
    "Fantasy",
    "Science Fiction",
    "Historical",
    "Political Intrigue",
    "Survival",
    "Exploration",
    "War",
    "Revenge",
    "Tragedy",
    "Healing",
    "Found Family",
    "Cultivation",
    "Martial Arts",
    "Isekai",
    "Reincarnation",
    "Regression",
    "System",
    "LitRPG",
    "Dungeon",
    "Kingdom Building",
    "Villainess",
    "Harem",
    "Reverse Harem",
]


# ============================================================
# TONES
# ============================================================

TONES = [
    "lighthearted",
    "comedic",
    "chaotic",
    "wholesome",
    "heartwarming",
    "dramatic",
    "melancholic",
    "mysterious",
    "dark",
    "grim",
    "hopeful",
    "romantic",
    "epic",
    "cinematic",
    "fast-paced",
    "slow-burn",
    "psychological",
    "intense",
    "satirical",
    "absurd",
    "serious",
    "adventurous",
    "bittersweet",
    "philosophical",
]


# ============================================================
# WORLD NAMES
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
    "Hanamori",
    "Kurohana",
    "Seiran",
    "Akatsuki",
    "Yukishiro",
    "Hoshizora",
    "Gyeonghwa",
    "Mujin",
    "Haeryeong",
    "Baekcheon",
    "Cheonhwa",
    "Jinhwa",
    "Xianyu",
    "Yunhai",
    "Longwei",
    "Qinglan",
    "Tianluo",
    "Jadefall",
    "Hongyuan",
]


# ============================================================
# FACTIONS
# ============================================================

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
    "The Laughing Swordsmen",
    "The Bureau of Extremely Serious Problems",
    "The Heavenly Pavilion",
    "The Jade Sect",
    "The Celestial Court",
    "The Blood Moon Sect",
    "The Northern Murim Alliance",
    "The Black Lotus Society",
    "The Imperial Academy",
    "The Royal Mage Association",
    "The Adventurer's Guild",
    "The Seven Dragon Clans",
]


# ============================================================
# POWER SYSTEMS
# ============================================================

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
    "Mana Circulation",
    "Sword Intent",
    "Qi Manipulation",
    "Demonic Energy",
    "Heavenly Energy",
    "Spirit Contract",
    "Divine Authority",
    "System Interface",
    "Skill Synthesis",
    "Soul Rank",
    "Monster Evolution",
    "Bloodline Awakening",
    "Concept Manipulation",
    "Reality Editing",
]


# ============================================================
# OBJECTS
# ============================================================

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
    "a mysterious smartphone",
    "a strange game cartridge",
    "a jade pendant",
    "an ancient cultivation manual",
    "a talking sword",
    "a cursed doll",
    "a ridiculous-looking crown",
]


# ============================================================
# CONFLICTS
# ============================================================

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
    "a kingdom secretly controlled by another power",
    "a dungeon appearing in the middle of a city",
    "a mysterious system choosing random people",
    "the destruction of the protagonist's homeland",
    "an immortal returning after centuries",
    "a tournament hiding a much larger conspiracy",
    "a demon king who claims to be retired",
    "a hero who desperately wants to become a villain",
]


# ============================================================
# CHAPTER TITLES
# ============================================================

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
    "The Problem With",
    "The Absolutely Terrible Idea of",
    "The Unexpected Visit From",
    "The Day Everything Went",
    "The Quest That Should Have Been Simple",
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
    "Completely Wrong",
    "Ridiculous",
    "Impossible",
    "Unexpected",
]


# ============================================================
# ARC SYSTEM
# ============================================================

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
# FICTIONAL NAME SYSTEM
# ============================================================

JAPANESE_FIRST_NAMES = [
    "Akira", "Ren", "Haruto", "Sora", "Yuki",
    "Hikaru", "Kaito", "Riku", "Aoi", "Itsuki",
    "Shin", "Takumi", "Rei", "Koharu", "Mio",
    "Yuna", "Rin", "Kaede", "Hana", "Ayame",
    "Natsuki", "Kiyomi", "Masato", "Kazuki", "Ryo",
    "Tsubasa", "Asuka", "Sayaka", "Mei", "Nozomi",
]

JAPANESE_LAST_NAMES = [
    "Kurosawa", "Aoyama", "Takahashi", "Mizuno",
    "Kobayashi", "Fujimoto", "Shirakawa", "Kisaragi",
    "Amamiya", "Hoshino", "Kanzaki", "Moriyama",
    "Tsukishiro", "Sakuraba", "Kurokawa", "Hayashida",
    "Minamoto", "Shinomiya", "Yamashiro", "Akizuki",
]

KOREAN_FIRST_NAMES = [
    "Seo-jun", "Ji-ho", "Min-jun", "Hyun-woo",
    "Do-yun", "Ji-hoon", "Ha-jun", "Si-woo",
    "Joon-ho", "Tae-hyun", "Min-seo", "Seo-yeon",
    "Ji-eun", "Ha-eun", "Yu-na", "Soo-ah",
    "Ye-jin", "Eun-chae", "Da-hyun", "Hye-jin",
]

KOREAN_LAST_NAMES = [
    "Kim", "Lee", "Park", "Choi", "Jung",
    "Kang", "Yoon", "Han", "Shin", "Kwon",
    "Seo", "Hwang", "Lim", "Jang", "Moon",
    "Baek", "Song", "Ryu", "Jeon", "Hong",
]

CHINESE_FIRST_NAMES = [
    "Wei", "Chen", "Jun", "Hao", "Lei",
    "Ming", "Tian", "Jian", "Yun", "Feng",
    "Xiao", "Lin", "Jing", "Mei", "Lan",
    "Qing", "Yue", "Shan", "Rui", "Xuan",
]

CHINESE_LAST_NAMES = [
    "Li", "Wang", "Zhang", "Liu", "Chen",
    "Yang", "Huang", "Zhao", "Wu", "Zhou",
    "Xu", "Sun", "Ma", "Zhu", "Hu",
    "Guo", "He", "Gao", "Lin", "Luo",
]

WESTERN_FIRST_NAMES = [
    "Aren", "Kael", "Liora", "Seren", "Mira",
    "Elias", "Riven", "Neria", "Darian", "Elara",
    "Lucian", "Vera", "Arian", "Selene", "Kieran",
    "Lyra", "Orin", "Nolan", "Ayla", "Cassian",
]

WESTERN_LAST_NAMES = [
    "Valen", "Ardent", "Nox", "Raven", "Eld",
    "Veyr", "Aster", "Cael", "Morrow", "Thorne",
    "Ashen", "Vale", "Serin", "Dawn", "Wren",
    "Ever", "Drake", "Lorne", "Voss", "Meridian",
]


# ============================================================
# CHARACTER SYSTEM
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
    "Merchant",
    "Teacher",
    "Adventurer",
    "Detective",
    "Cultivator",
    "Swordsman",
    "Healer",
    "Comedian",
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
    "terrible at making normal decisions",
    "always hungry",
    "dramatically overconfident",
    "serious until someone makes a terrible joke",
    "lazy but strangely talented",
    "kind despite a frightening reputation",
    "competitive about absolutely everything",
    "convinced they are the main character",
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
    "Can copy temporary abilities",
    "Can evolve after surviving dangerous battles",
    "Can see hidden status information",
    "Can step between reflected surfaces",
    "Can speak with monsters",
    "Can temporarily freeze time",
    "Can convert damage into energy",
    "Can turn extremely bad luck into unexpected advantages",
]


# ============================================================
# DESIGN SYSTEM
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
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(185,140,255,.20), transparent 35%), "
            "linear-gradient(135deg,#09090d,#151020)"
        ),
    },
    {
        "name": "Ember",
        "accent": "#ff8a5b",
        "accent2": "#d84d2b",
        "surface": "#100a08",
        "surface2": "#1b100d",
        "text": "#fff6f0",
        "muted": "#c4aaa0",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(255,138,91,.22), transparent 35%), "
            "linear-gradient(135deg,#100a08,#24120c)"
        ),
    },
    {
        "name": "Azure",
        "accent": "#5db7ff",
        "accent2": "#277bd4",
        "surface": "#071019",
        "surface2": "#0e1b28",
        "text": "#f1f8ff",
        "muted": "#a4b8ca",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(93,183,255,.22), transparent 35%), "
            "linear-gradient(135deg,#071019,#0c1c2b)"
        ),
    },
    {
        "name": "Verdant",
        "accent": "#66d9a0",
        "accent2": "#299e69",
        "surface": "#07110c",
        "surface2": "#0d1c14",
        "text": "#f0fff6",
        "muted": "#a4bcae",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(102,217,160,.20), transparent 35%), "
            "linear-gradient(135deg,#07110c,#102219)"
        ),
    },
    {
        "name": "Crimson",
        "accent": "#ff667c",
        "accent2": "#c52f4a",
        "surface": "#12080b",
        "surface2": "#1f0d12",
        "text": "#fff2f4",
        "muted": "#c9a5aa",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(255,102,124,.22), transparent 35%), "
            "linear-gradient(135deg,#12080b,#240d14)"
        ),
    },
    {
        "name": "Golden",
        "accent": "#e7c56b",
        "accent2": "#ae8224",
        "surface": "#110f08",
        "surface2": "#1d190d",
        "text": "#fffbed",
        "muted": "#c1b99e",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(231,197,107,.20), transparent 35%), "
            "linear-gradient(135deg,#110f08,#211c0c)"
        ),
    },
    {
        "name": "Rose",
        "accent": "#f49ac2",
        "accent2": "#c65b8e",
        "surface": "#120a10",
        "surface2": "#20121b",
        "text": "#fff4fa",
        "muted": "#c5a8b7",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(244,154,194,.22), transparent 35%), "
            "linear-gradient(135deg,#120a10,#25131e)"
        ),
    },
    {
        "name": "Void",
        "accent": "#8aa4ff",
        "accent2": "#526bd3",
        "surface": "#06070c",
        "surface2": "#0d0f18",
        "text": "#f2f4ff",
        "muted": "#9ea5bd",
        "hero": (
            "radial-gradient(circle at 70% 20%, "
            "rgba(138,164,255,.18), transparent 35%), "
            "linear-gradient(135deg,#06070c,#101329)"
        ),
    },
]


# ============================================================
# TITLE SYSTEM
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
    "The Completely Normal",
    "My Very Strange",
    "I Accidentally Became",
    "The Extremely Unfortunate",
    "Why Am I",
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
    "Ridiculous",
    "Unemployed",
    "Overpowered",
    "Accidental",
    "Lazy",
    "Terrible",
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
    "Hero",
    "Villain",
    "Adventurer",
    "Mage",
    "Swordsman",
    "Dungeon",
    "System",
]


# ============================================================
# RANDOM HELPERS
# ============================================================

def stable_rng(value: str) -> random.Random:
    digest = hashlib.sha256(
        value.encode("utf-8")
    ).digest()

    integer = int.from_bytes(
        digest[:16],
        "big",
    )

    return random.Random(integer)


def make_seed(
    genre: str | None = None,
    parody: bool = False,
) -> str:
    if genre in GENRES or parody:
        if genre not in GENRES:
            genre = GENRES[secrets.randbelow(len(GENRES))]
        index = GENRES.index(genre)
        return (
            f"ff{index:04x}"
            f"{'01' if parody else '00'}"
            f"{secrets.token_hex(28)}"
        )
    return f"fe{secrets.token_hex(31)}"


def decode_seed_options(
    seed: str,
) -> tuple[str | None, bool]:
    if not isinstance(seed, str) or len(seed) != 64:
        return None, False

    if seed.startswith("ff"):
        try:
            index = int(seed[2:6], 16)
            if 0 <= index < len(GENRES):
                return (
                    GENRES[index],
                    seed[6:8] == "01",
                )
        except ValueError:
            pass

    return None, False


def pick(
    rng: random.Random,
    items: list,
):
    return items[
        rng.randrange(
            len(items)
        )
    ]


def pick_unique(
    rng: random.Random,
    items: list,
    used: set,
):
    available = [
        item
        for item in items
        if item not in used
    ]

    if not available:
        return pick(rng, items)

    value = pick(
        rng,
        available,
    )

    used.add(value)

    return value


# ============================================================
# NAME GENERATION
# ============================================================

def make_name(
    rng: random.Random,
    style: str | None = None,
) -> str:

    if style is None:
        style = pick(
            rng,
            [
                "western",
                "japanese",
                "korean",
                "chinese",
            ],
        )

    if style == "japanese":
        return (
            f"{pick(rng, JAPANESE_LAST_NAMES)} "
            f"{pick(rng, JAPANESE_FIRST_NAMES)}"
        )

    if style == "korean":
        return (
            f"{pick(rng, KOREAN_LAST_NAMES)} "
            f"{pick(rng, KOREAN_FIRST_NAMES)}"
        )

    if style == "chinese":
        return (
            f"{pick(rng, CHINESE_LAST_NAMES)} "
            f"{pick(rng, CHINESE_FIRST_NAMES)}"
        )

    return (
        f"{pick(rng, WESTERN_FIRST_NAMES)} "
        f"{pick(rng, WESTERN_LAST_NAMES)}"
    )


def make_unique_name(
    rng: random.Random,
    used_names: set,
    style: str | None = None,
) -> str:

    for _ in range(100):
        name = make_name(
            rng,
            style,
        )

        if name not in used_names:
            used_names.add(name)
            return name

    suffix = rng.randrange(
        1000,
        9999,
    )

    name = (
        f"{make_name(rng, style)} "
        f"{suffix}"
    )

    used_names.add(name)

    return name


# ============================================================
# TITLE GENERATION
# ============================================================

def make_title(
    rng: random.Random,
) -> str:

    prefix = pick(
        rng,
        TITLE_PREFIXES,
    )

    adjective = pick(
        rng,
        TITLE_WORDS,
    )

    noun = pick(
        rng,
        TITLE_NOUNS,
    )

    patterns = [
        f"{prefix} {adjective} {noun}",
        f"{adjective} {noun}",
        f"{prefix} {noun} of {adjective}",
        f"{prefix} {adjective} {noun}",
        f"{adjective} {noun}: A Completely Unnecessary Adventure",
    ]

    return pick(
        rng,
        patterns,
    )


# ============================================================
# CHARACTER GENERATION
# ============================================================

def make_characters(
    rng: random.Random,
    protagonist: str,
) -> List[Dict]:

    used_names = {
        protagonist
    }

    characters = []

    protagonist_trait = pick(
        rng,
        CHARACTER_TRAITS,
    )

    protagonist_ability = pick(
        rng,
        ABILITIES,
    )

    characters.append(
        {
            "name": protagonist,
            "role": "Protagonist",
            "origin_style": "mixed",
            "trait": protagonist_trait,
            "ability": protagonist_ability,
            "description": (
                f"{protagonist} is the central figure of the story, "
                f"defined by being {protagonist_trait}. Their journey "
                f"begins with circumstances that seem personal, but "
                f"the decisions they make gradually connect them to "
                f"events far larger than themselves."
            ),
        }
    )

    roles = [
        role
        for role in CHARACTER_ROLES
        if role != "Protagonist"
    ]

    styles = [
        "japanese",
        "korean",
        "chinese",
        "western",
    ]

    for index, role in enumerate(
        roles[:9]
    ):

        style = styles[
            index % len(styles)
        ]

        name = make_unique_name(
            rng,
            used_names,
            style,
        )

        trait = pick(
            rng,
            CHARACTER_TRAITS,
        )

        ability = pick(
            rng,
            ABILITIES,
        )

        characters.append(
            {
                "name": name,
                "role": role,
                "origin_style": style,
                "trait": trait,
                "ability": ability,
                "description": (
                    f"{name} serves as the story's "
                    f"{role.lower()}. Their {trait} personality "
                    f"and ability to {ability.lower()} make them "
                    f"more than a supporting figure; their choices "
                    f"can change the direction of the journey."
                ),
            }
        )

    return characters


# ============================================================
# WORLD BLUEPRINT
# ============================================================

def make_world_blueprint(
    seed: str,
    world: str,
    genre: str,
    faction: str,
) -> Dict:

    rng = stable_rng(
        f"{seed}:world"
    )

    world_types = [
        "a continent ruled by ancient kingdoms",
        "a modern city hiding a supernatural society",
        "a vast magical empire",
        "a world connected by mysterious gates",
        "a post-apocalyptic civilization",
        "a cultivation world divided into sects",
        "a futuristic interstellar civilization",
        "a world where humans and monsters coexist",
        "an academy-centered magical society",
        "a world built around enormous floating cities",
    ]

    eras = [
        "an age of forgotten magic",
        "the beginning of a technological revolution",
        "a fragile post-war era",
        "the final years of an ancient dynasty",
        "a period of political instability",
        "an era when supernatural phenomena have returned",
        "a new age following the collapse of an old civilization",
    ]

    location_pool = [
        place
        for place in PLACES
        if place != world
    ]

    important_locations = [
        world
    ]

    while len(important_locations) < 7:
        location = pick(
            rng,
            location_pool,
        )

        if location not in important_locations:
            important_locations.append(
                location
            )

    geography = [
        f"the central region surrounding {world}",
        f"the northern territories beyond {world}",
        "the western frontier",
        "the eastern kingdoms",
        "the southern coast",
        "the hidden region beyond the old boundary",
    ]

    rules = [
        f"The influence of {faction} affects political and social life.",
        "Ancient knowledge cannot be safely used without consequences.",
        "Major powers are limited by personal cost, knowledge, or resources.",
        "The world contains truths that contradict commonly accepted history.",
        "Important locations have histories that become relevant later.",
    ]

    return {
        "name": world,
        "type": pick(
            rng,
            world_types,
        ),
        "genre_context": genre,
        "era": pick(
            rng,
            eras,
        ),
        "geography": geography,
        "important_locations": important_locations,
        "world_rules": rules,
        "society": (
            f"Different communities in {world} have developed "
            f"different beliefs about power, history, authority, "
            f"and the unexplained events affecting their lives."
        ),
        "history": (
            f"The official history of {world} leaves several major "
            f"events unexplained. Those missing pieces gradually "
            f"become central to the main story."
        ),
    }


# ============================================================
# POWER BLUEPRINT
# ============================================================

def make_power_blueprint(
    seed: str,
    power: str,
) -> Dict:

    rng = stable_rng(
        f"{seed}:power"
    )

    mechanisms = [
        "energy is controlled through mental focus",
        "power is awakened through emotional resonance",
        "abilities are activated through ancient symbols",
        "users develop abilities through training and experience",
        "power is connected to the user's soul",
        "abilities evolve after major personal breakthroughs",
        "users exchange resources for temporary supernatural effects",
        "power responds to contracts with supernatural entities",
    ]

    costs = [
        "physical exhaustion",
        "loss of concentration",
        "memory damage",
        "temporary weakness",
        "emotional instability",
        "limited resources",
        "risk of losing control",
        "permanent consequences when abilities are overused",
    ]

    levels = [
        "Awakening",
        "Novice",
        "Initiate",
        "Adept",
        "Expert",
        "Master",
        "Transcendent",
        "Mythic",
        "Legendary",
    ]

    rare = [
        "an ability that ignores normal limitations",
        "a forbidden form of the power",
        "a lost technique",
        "an ability connected to ancient history",
        "a technique believed to be impossible",
    ]

    selected_costs = []

    while len(selected_costs) < 3:
        value = pick(
            rng,
            costs,
        )

        if value not in selected_costs:
            selected_costs.append(
                value
            )

    selected_rare = []

    while len(selected_rare) < 3:
        value = pick(
            rng,
            rare,
        )

        if value not in selected_rare:
            selected_rare.append(
                value
            )

    return {
        "name": power,
        "mechanism": pick(
            rng,
            mechanisms,
        ),
        "costs": selected_costs,
        "levels": levels,
        "limitations": [
            "power cannot solve every problem",
            "strong abilities require preparation or sacrifice",
            "knowledge of the system is incomplete",
            "stronger enemies can exploit weaknesses",
        ],
        "rare_abilities": selected_rare,
        "progression": (
            "The protagonist's understanding of the power system "
            "develops gradually rather than becoming complete at "
            "the beginning of the story."
        ),
    }


# ============================================================
# ANTAGONISTS
# ============================================================

def make_antagonists(
    seed: str,
    used_names: set,
) -> List[Dict]:

    rng = stable_rng(
        f"{seed}:antagonists"
    )

    roles = [
        "Primary Antagonist",
        "Secondary Antagonist",
        "Political Antagonist",
        "Personal Rival",
        "Hidden Antagonist",
    ]

    motivations = [
        "believes that the world must be forcibly changed",
        "is pursuing knowledge forbidden by every major faction",
        "has a personal connection to the protagonist's past",
        "appears helpful while pursuing a hidden objective",
        "believes their actions are necessary to prevent a greater disaster",
        "treats the conflict as an intellectual game",
        "wants to restore an ancient order",
    ]

    antagonists = []

    styles = [
        "western",
        "japanese",
        "korean",
        "chinese",
    ]

    for index, role in enumerate(
        roles
    ):

        name = make_unique_name(
            rng,
            used_names,
            styles[
                index % len(styles)
            ],
        )

        motivation = pick(
            rng,
            motivations,
        )

        antagonists.append(
            {
                "name": name,
                "role": role,
                "motivation": motivation,
                "description": (
                    f"{name} is a {role.lower()} who {motivation}. "
                    f"Their actions influence the long-term direction "
                    f"of the story, even when they are not physically "
                    f"present."
                ),
            }
        )

    return antagonists


# ============================================================
# AUTO DESCRIPTION ENGINE
# ============================================================

def description_rng(
    seed: str,
    section: str,
) -> random.Random:

    return stable_rng(
        f"{seed}:description:{section}"
    )


def make_world_description(
    seed: str,
    world: Dict,
    protagonist: str,
    conflict: str,
    faction: str,
    power: str,
    genre: str,
) -> str:

    rng = description_rng(
        seed,
        "world",
    )

    locations = world[
        "important_locations"
    ]

    location_text = ", ".join(
        locations[:3]
    )

    openings = [
        (
            f"{world['name']} is {world['type']} existing during "
            f"{world['era']}. Its regions stretch from {location_text} "
            f"into territories whose histories are still only partly "
            f"understood. Although the world appears to have settled "
            f"into familiar patterns of society and power, those "
            f"patterns are built on a history that contains several "
            f"missing pieces."
        ),
        (
            f"The story opens in {world['name']}, {world['type']} "
            f"where the present is shaped by {world['era']}. Places "
            f"such as {location_text} are connected by trade, conflict, "
            f"old alliances, and stories that have survived for "
            f"generations. Beneath those ordinary connections lies "
            f"a history that has never been completely explained."
        ),
        (
            f"Life in {world['name']} has been shaped by centuries "
            f"of changing kingdoms, beliefs, and discoveries. It is "
            f"{world['type']} during {world['era']}, and locations "
            f"such as {location_text} show how different its regions "
            f"can be. Yet the differences between them hide a common "
            f"history that will gradually become important to "
            f"{protagonist}."
        ),
    ]

    conflict_lines = [
        (
            f"The unresolved danger surrounding {conflict} is beginning "
            f"to disturb that balance. {faction} is one of the powers "
            f"whose decisions can influence what happens next, while "
            f"{power} introduces forces capable of changing the balance "
            f"between ordinary people and those who possess greater "
            f"abilities."
        ),
        (
            f"What initially looks like an isolated problem involving "
            f"{conflict} gradually reaches beyond one location. "
            f"{faction} becomes entangled in the developing situation, "
            f"and the existence of {power} means that knowledge itself "
            f"can become a source of power."
        ),
        (
            f"The conflict surrounding {conflict} creates pressure "
            f"across the world. Factions such as {faction} have their "
            f"own reasons for becoming involved, while the secrets "
            f"behind {power} suggest that the current crisis may have "
            f"begun long before anyone noticed it."
        ),
    ]

    endings = [
        (
            f"For {protagonist}, travelling through this world slowly "
            f"changes what the setting means. Places that first seem "
            f"unrelated begin to connect, old stories acquire new "
            f"meanings, and the difference between the world's accepted "
            f"history and its actual history becomes increasingly "
            f"difficult to ignore."
        ),
        (
            f"The deeper {protagonist} travels into {world['name']}, "
            f"the more the world reveals itself as something larger "
            f"than its surface. Every discovery creates another reason "
            f"to question what people believe they already know."
        ),
        (
            f"What begins as a journey through a {genre.lower()} world "
            f"eventually becomes an exploration of its people, history, "
            f"power structures, and forgotten truths."
        ),
    ]

    return " ".join([
        pick(rng, openings),
        pick(rng, conflict_lines),
        pick(rng, endings),
    ])


def make_story_description(
    seed: str,
    title: str,
    protagonist: str,
    conflict: str,
    world: str,
    faction: str,
    power: str,
    mystery: str,
    tone: str,
) -> str:

    rng = description_rng(
        seed,
        "story",
    )

    openings = [
        (
            f"{title} follows {protagonist}, whose life becomes "
            f"entangled with {conflict} before they understand how "
            f"large its consequences will become. What begins as a "
            f"personal problem gradually draws them into events "
            f"affecting people across {world}."
        ),
        (
            f"{protagonist} never intended to become involved in "
            f"{conflict}. The first steps of the journey seem small, "
            f"but each discovery reveals another connection between "
            f"their circumstances and the larger history of {world}."
        ),
        (
            f"The journey begins when {protagonist} encounters the "
            f"consequences of {conflict}. At first there appears to be "
            f"a simple explanation. The farther the story moves, "
            f"however, the more that explanation begins to fall apart."
        ),
    ]

    development = [
        (
            f"As the journey continues, {faction} becomes increasingly "
            f"important. Alliances shift, relationships are tested, "
            f"and the rules surrounding {power} become impossible "
            f"to ignore."
        ),
        (
            f"The people surrounding {protagonist} do not always want "
            f"the same things. Some become allies, some become rivals, "
            f"and some hide goals that only become visible much later. "
            f"At the same time, {power} develops from an unusual ability "
            f"into a central part of the larger conflict."
        ),
        (
            f"Every new stage introduces another problem. The journey "
            f"moves through relationships, discoveries, confrontations, "
            f"mistakes, victories, and consequences rather than following "
            f"a simple path from weakness to strength."
        ),
    ]

    mystery_lines = [
        (
            f"Behind all of this is a question that refuses to disappear: "
            f"{mystery}"
        ),
        (
            f"Eventually the visible conflict leads back to a deeper "
            f"question: {mystery}"
        ),
        (
            f"The further {protagonist} goes, the more important one "
            f"question becomes: {mystery}"
        ),
    ]

    endings = [
        (
            f"The story carries a {tone} atmosphere, allowing personal "
            f"moments and character relationships to exist alongside "
            f"the larger mysteries and conflicts."
        ),
        (
            f"Its {tone} tone allows the journey to move between "
            f"quiet discoveries, emotional choices, dangerous encounters, "
            f"and larger turning points."
        ),
        (
            f"The {tone} atmosphere changes naturally as the characters "
            f"move from ordinary uncertainty toward increasingly serious "
            f"discoveries."
        ),
    ]

    return " ".join([
        pick(rng, openings),
        pick(rng, development),
        pick(rng, mystery_lines),
        pick(rng, endings),
    ])


def make_people_description(
    seed: str,
    protagonist: Dict,
    characters: List[Dict],
    antagonists: List[Dict],
) -> str:

    rng = description_rng(
        seed,
        "people",
    )

    supporting = [
        character
        for character in characters
        if character["name"]
        != protagonist["name"]
    ]

    support_names = [
        character["name"]
        for character in supporting[:4]
    ]

    enemy_names = [
        antagonist["name"]
        for antagonist in antagonists[:3]
    ]

    support_text = (
        ", ".join(support_names)
        if support_names
        else "the people encountered during the journey"
    )

    enemy_text = (
        ", ".join(enemy_names)
        if enemy_names
        else "the hidden enemies"
    )

    openings = [
        (
            f"At the center of the story is {protagonist['name']}, "
            f"whose {protagonist['trait']} personality influences "
            f"how they respond when the world begins changing around "
            f"them. Their ability, {protagonist['ability'].lower()}, "
            f"gives them an unusual starting point, but it does not "
            f"remove the uncertainty surrounding their journey."
        ),
        (
            f"{protagonist['name']} begins the story as someone who is "
            f"{protagonist['trait']}. That quality becomes both an "
            f"advantage and a weakness as they encounter people whose "
            f"goals do not always match their own."
        ),
        (
            f"The story's characters are built around different "
            f"personalities, abilities, fears, and ambitions. "
            f"{protagonist['name']} stands at the center of those "
            f"relationships, but the journey repeatedly proves that "
            f"no single character controls what happens next."
        ),
    ]

    relationships = [
        (
            f"Among the people who become important are "
            f"{support_text}. Their relationships with "
            f"{protagonist['name']} develop through cooperation, "
            f"disagreement, trust, rivalry, and shared experiences."
        ),
        (
            f"The journey brings {protagonist['name']} together with "
            f"{support_text}. Some relationships become friendships, "
            f"others become rivalries, and some remain uncertain even "
            f"after the characters begin depending on one another."
        ),
        (
            f"Characters such as {support_text} are not simply present "
            f"to assist the protagonist. Their own decisions, mistakes, "
            f"and ambitions can change the direction of the story."
        ),
    ]

    enemies = [
        (
            f"Opposing them are figures including {enemy_text}. Their "
            f"motivations differ, which means the conflict is not built "
            f"around a single kind of enemy."
        ),
        (
            f"Beyond the central group are people such as {enemy_text}, "
            f"whose goals create different forms of pressure, from "
            f"personal rivalry to larger threats."
        ),
    ]

    return " ".join([
        pick(rng, openings),
        pick(rng, relationships),
        pick(rng, enemies),
    ])


def make_power_description(
    seed: str,
    power: Dict,
    protagonist: str,
) -> str:

    rng = description_rng(
        seed,
        "power",
    )

    costs = power[
        "costs"
    ]

    levels = power[
        "levels"
    ]

    primary_cost = costs[0]

    level_text = ", ".join(
        levels[:5]
    )

    openings = [
        (
            f"{power['name']} is more than a collection of special "
            f"abilities. It is a system with rules, limitations, "
            f"techniques, and consequences that determine what its "
            f"users can accomplish."
        ),
        (
            f"The extraordinary force at the heart of the story is "
            f"{power['name']}. For {protagonist}, understanding it "
            f"becomes a gradual process of discovering both strength "
            f"and limitation."
        ),
        (
            f"{protagonist}'s relationship with {power['name']} develops "
            f"slowly. The system rewards understanding and control rather "
            f"than simply giving its users unlimited strength."
        ),
    ]

    mechanisms = [
        (
            f"The system works because {power['mechanism']}. This makes "
            f"knowledge and technique important, since possessing "
            f"potential does not automatically mean knowing how to use it."
        ),
        (
            f"Its underlying principle is that {power['mechanism']}. "
            f"Users therefore have to learn how the system behaves "
            f"before they can safely attempt more advanced techniques."
        ),
        (
            f"At its foundation, {power['mechanism']}. The result is "
            f"a system in which experience, control, and understanding "
            f"matter alongside natural talent."
        ),
    ]

    costs_text = [
        (
            f"Every meaningful use carries a price. One of the earliest "
            f"costs is {primary_cost}, while stronger techniques can "
            f"introduce consequences that cannot simply be reversed."
        ),
        (
            f"The system is deliberately limited. Using it can cause "
            f"{primary_cost}, and pushing beyond safe limits becomes "
            f"dangerous even for characters who understand it well."
        ),
        (
            f"Strength always has a consequence. The most immediate "
            f"danger is {primary_cost}, while later stages reveal "
            f"greater risks hidden inside the system."
        ),
    ]

    progression = [
        (
            f"Known stages include {level_text}. Each stage represents "
            f"more than an increase in strength; it also reflects a "
            f"deeper understanding of what the system can and cannot do."
        ),
        (
            f"Progression moves through stages such as {level_text}. "
            f"The higher stages remain difficult to reach because the "
            f"characters must overcome both external threats and the "
            f"limitations of their own understanding."
        ),
    ]

    return " ".join([
        pick(rng, openings),
        pick(rng, mechanisms),
        pick(rng, costs_text),
        pick(rng, progression),
    ])


def make_mystery_description(
    seed: str,
    world: str,
    protagonist: str,
    conflict: str,
    mystery: str,
    factions: List[Dict],
) -> str:

    rng = description_rng(
        seed,
        "mystery",
    )

    faction_names = [
        faction["name"]
        for faction in factions
    ]

    faction_text = ", ".join(
        faction_names[:3]
    )

    openings = [
        (
            f"Nothing in {world} is quite as simple as it first appears. "
            f"Records disagree, important people know more than they "
            f"admit, and old events continue to leave traces in the "
            f"present."
        ),
        (
            f"The mystery surrounding {world} develops through fragments "
            f"rather than a single discovery. Information appears in "
            f"places, memories, documents, and conversations, often "
            f"forcing the characters to reconsider what they believed."
        ),
        (
            f"Long before {protagonist} became involved, something had "
            f"already been hidden beneath the visible history of "
            f"{world}. The evidence is scattered, and different people "
            f"have preserved different versions of what happened."
        ),
    ]

    central = [
        (
            f"At the heart of the mystery is one question: {mystery}"
        ),
        (
            f"Everything eventually leads back to the same unanswered "
            f"question: {mystery}"
        ),
        (
            f"The deeper mystery can be reduced to a question that "
            f"becomes harder to ignore: {mystery}"
        ),
    ]

    factions_text = [
        (
            f"Organizations such as {faction_text} possess different "
            f"pieces of the truth, but none necessarily understands "
            f"the entire picture."
        ),
        (
            f"The major factions each hold fragments of the answer. "
            f"That makes alliances, betrayals, and competing versions "
            f"of history increasingly important as {conflict} develops."
        ),
        (
            f"The factions do not agree about what the past means. "
            f"Some want to preserve it, some want to exploit it, and "
            f"others would rather see the truth disappear."
        ),
    ]

    return " ".join([
        pick(rng, openings),
        pick(rng, central),
        pick(rng, factions_text),
    ])


def make_journey_description(
    seed: str,
    protagonist: str,
    world: str,
    arcs: List[Dict],
) -> str:

    rng = description_rng(
        seed,
        "journey",
    )

    first_arc = arcs[0]
    middle_arc = arcs[
        len(arcs) // 2
    ]
    final_arc = arcs[-1]

    options = [
        (
            f"{protagonist}'s journey begins with {first_arc['title']}, "
            f"where incomplete information gives way to discovery. "
            f"As the story reaches {middle_arc['title']}, the scale "
            f"of the conflict changes and earlier assumptions begin "
            f"to collapse. By the time the journey reaches "
            f"{final_arc['title']}, choices made much earlier have "
            f"consequences for the future of {world}."
        ),
        (
            f"The six-hundred-chapter journey is designed to grow in "
            f"scale. The early movement through {first_arc['title']} "
            f"focuses on discovery, the middle stages surrounding "
            f"{middle_arc['title']} widen the conflict, and the final "
            f"movement through {final_arc['title']} brings accumulated "
            f"mysteries and consequences toward their largest turning "
            f"point."
        ),
        (
            f"The journey does not remain the same from beginning to "
            f"end. {first_arc['title']} establishes the initial mystery, "
            f"{middle_arc['title']} changes the meaning of what came "
            f"before, and {final_arc['title']} forces the characters "
            f"to confront the consequences of everything they have "
            f"learned."
        ),
    ]

    return pick(
        rng,
        options,
    )


def make_auto_descriptions(
    seed: str,
    title: str,
    genre: str,
    tone: str,
    world: Dict,
    power: Dict,
    protagonist: Dict,
    characters: List[Dict],
    antagonists: List[Dict],
    factions: List[Dict],
    conflict: str,
    mystery: str,
    arcs: List[Dict],
) -> Dict:

    return {
        "world": make_world_description(
            seed=seed,
            world=world,
            protagonist=protagonist["name"],
            conflict=conflict,
            faction=factions[0]["name"],
            power=power["name"],
            genre=genre,
        ),

        "story": make_story_description(
            seed=seed,
            title=title,
            protagonist=protagonist["name"],
            conflict=conflict,
            world=world["name"],
            faction=factions[0]["name"],
            power=power["name"],
            mystery=mystery,
            tone=tone,
        ),

        "people": make_people_description(
            seed=seed,
            protagonist=protagonist,
            characters=characters,
            antagonists=antagonists,
        ),

        "power": make_power_description(
            seed=seed,
            power=power,
            protagonist=protagonist["name"],
        ),

        "mystery": make_mystery_description(
            seed=seed,
            world=world["name"],
            protagonist=protagonist["name"],
            conflict=conflict,
            mystery=mystery,
            factions=factions,
        ),

        "journey": make_journey_description(
            seed=seed,
            protagonist=protagonist["name"],
            world=world["name"],
            arcs=arcs,
        ),
    }


# ============================================================
# ARC GENERATION
# ============================================================

def make_arcs(
    seed: str,
    characters: List[Dict],
    antagonists: List[Dict],
    world: Dict,
    power: Dict,
) -> List[Dict]:

    arcs = []

    character_names = [
        character["name"]
        for character in characters
    ]

    for index in range(
        ARC_COUNT
    ):

        rng = stable_rng(
            f"{seed}:arc:{index + 1}"
        )

        start = (
            index
            * CHAPTERS_PER_ARC
            + 1
        )

        end = (
            CHAPTER_COUNT
            if index == ARC_COUNT - 1
            else (
                index + 1
            )
            * CHAPTERS_PER_ARC
        )

        shuffled = list(
            character_names
        )

        rng.shuffle(
            shuffled
        )

        involved = shuffled[
            :min(
                4,
                len(shuffled),
            )
        ]

        antagonist = pick(
            rng,
            antagonists,
        )

        theme = pick(
            rng,
            ARC_THEMES,
        )

        locations = list(
            world[
                "important_locations"
            ]
        )

        rng.shuffle(
            locations
        )

        selected_locations = locations[
            :min(
                3,
                len(locations),
            )
        ]

        arcs.append(
            {
                "number": index + 1,
                "title": ARC_NAMES[index],
                "start": start,
                "end": end,
                "theme": theme,

                "objective": (
                    f"The characters must survive the events of "
                    f"this stage while discovering another part "
                    f"of the mystery surrounding {world['name']}."
                ),

                "central_conflict": (
                    f"The conflict between the protagonists and "
                    f"{antagonist['name']} becomes increasingly "
                    f"important during this stage."
                ),

                "locations": selected_locations,

                "characters_involved": involved,

                "antagonist_activity": (
                    f"{antagonist['name']} advances a plan connected "
                    f"to the larger conflict while avoiding a complete "
                    f"revelation of their intentions."
                ),

                "power_progression": (
                    f"The characters gain a deeper understanding "
                    f"of {power['name']} and discover another "
                    f"limitation or possibility."
                ),

                "major_revelation": (
                    f"A new piece of the history of {world['name']} "
                    f"becomes known and changes the meaning of "
                    f"earlier discoveries."
                ),

                "beginning_state": (
                    "The characters enter this arc with incomplete "
                    "information and unresolved questions."
                ),

                "ending_state": (
                    "The characters leave this arc changed, with "
                    "new knowledge and a new problem to solve."
                ),
            }
        )

    return arcs


# ============================================================
# CHAPTER ROADMAP
# ============================================================

def make_chapter_roadmap(
    seed: str,
    arcs: List[Dict],
    characters: List[Dict],
    world: Dict,
    power: Dict,
    antagonists: List[Dict],
) -> List[Dict]:

    roadmap = []

    used_titles = set()

    character_names = [
        character["name"]
        for character in characters
    ]

    for chapter_number in range(
        1,
        CHAPTER_COUNT + 1,
    ):

        rng = stable_rng(
            f"{seed}:roadmap:{chapter_number}"
        )

        arc = get_arc(
            arcs,
            chapter_number,
        )

        relative = (
            chapter_number
            - arc["start"]
        )

        arc_length = (
            arc["end"]
            - arc["start"]
            + 1
        )

        ratio = (
            relative
            / max(
                1,
                arc_length - 1,
            )
        )

        if ratio < 0.20:
            phase = "opening"
        elif ratio < 0.50:
            phase = "development"
        elif ratio < 0.75:
            phase = "turning point"
        elif ratio < 0.93:
            phase = "climax"
        else:
            phase = "aftermath"

        title = (
            f"{pick(rng, CHAPTER_VERBS)} "
            f"{pick(rng, CHAPTER_NOUNS)}"
        )

        attempts = 0

        while (
            title in used_titles
            and attempts < 50
        ):
            title = (
                f"{pick(rng, CHAPTER_VERBS)} "
                f"{pick(rng, CHAPTER_NOUNS)}"
            )

            attempts += 1

        if title in used_titles:
            title = (
                f"{title} "
                f"— Chapter {chapter_number:03d}"
            )

        used_titles.add(
            title
        )

        shuffled_characters = list(
            character_names
        )

        rng.shuffle(
            shuffled_characters
        )

        focus = shuffled_characters[
            :min(
                3,
                len(
                    character_names
                ),
            )
        ]

        antagonist = pick(
            rng,
            antagonists,
        )

        location = pick(
            rng,
            world[
                "important_locations"
            ],
        )

        if phase == "opening":
            purpose = (
                f"Introduce or develop the central problem "
                f"of the {arc['title']} arc."
            )

        elif phase == "development":
            purpose = (
                "Build character relationships, mysteries, "
                "and consequences."
            )

        elif phase == "turning point":
            purpose = (
                "Change the direction of the story through "
                "a discovery, betrayal, victory, or defeat."
            )

        elif phase == "climax":
            purpose = (
                "Resolve a major conflict while creating "
                "the conditions for the next stage."
            )

        else:
            purpose = (
                "Show the consequences of the arc and "
                "prepare the next major storyline."
            )

        events = [
            (
                f"The characters investigate a problem connected "
                f"to {arc['theme']}."
            ),
            (
                f"{focus[0]} makes a decision that changes "
                f"the immediate situation."
            ),
            (
                f"{antagonist['name']} or their influence "
                f"creates another complication."
            ),
        ]

        if phase in {
            "turning point",
            "climax",
        }:
            events.append(
                (
                    f"The rules of {power['name']} become "
                    f"more important to the conflict."
                )
            )

        roadmap.append(
            {
                "number": chapter_number,
                "title": title,
                "arc_number": arc["number"],
                "arc_title": arc["title"],
                "phase": phase,
                "purpose": purpose,
                "location": location,
                "characters": focus,
                "events": events,

                "character_development": (
                    f"The characters involved must confront "
                    f"a personal consequence related to "
                    f"the events of this chapter."
                ),

                "world_development": (
                    f"The reader learns another detail about "
                    f"{world['name']}."
                ),

                "power_development": (
                    f"The chapter develops understanding of "
                    f"{power['name']} without making it an "
                    f"unlimited solution."
                ),

                "revelation": (
                    "A clue connected to the deeper mystery "
                    "is revealed."
                ),

                "state_before": (
                    f"The characters begin Chapter "
                    f"{chapter_number:03d} with unresolved "
                    f"problems from the preceding events."
                ),

                "state_after": (
                    "The situation changes enough to create "
                    "a reason to continue into the next chapter."
                ),

                "cliffhanger": (
                    "A new question, threat, discovery, or "
                    "unexpected consequence appears."
                ),

                "emotional_beat": pick(
                    rng,
                    [
                        "uncertainty",
                        "curiosity",
                        "hope",
                        "tension",
                        "fear",
                        "determination",
                        "surprise",
                        "anger",
                        "relief",
                        "wonder",
                        "sadness",
                        "excitement",
                    ],
                ),
            }
        )

    return roadmap


# ============================================================
# DESIGN
# ============================================================

def make_design(
    rng: random.Random,
) -> Dict:

    preset = dict(
        pick(
            rng,
            DESIGN_PRESETS,
        )
    )

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
# ARC LOOKUP
# ============================================================

def get_arc(
    arcs: List[Dict],
    chapter_number: int,
) -> Dict:

    for arc in arcs:
        if (
            arc["start"]
            <= chapter_number
            <= arc["end"]
        ):
            return arc

    return arcs[-1]


# ============================================================
# NOVEL BLUEPRINT
# ============================================================

@lru_cache(maxsize=64)
def generate_blueprint(
    seed: str,
    genre_override: str | None = None,
    parody_override: bool = False,
) -> Dict:

    core_rng = stable_rng(
        f"{seed}:core"
    )

    encoded_genre, encoded_parody = decode_seed_options(seed)
    genre = genre_override or encoded_genre or pick(core_rng, GENRES)
    parody_mode = bool(parody_override or encoded_parody)

    secondary_genre = pick(
        core_rng,
        SECONDARY_GENRES,
    )

    tone = pick(
        core_rng,
        TONES,
    )

    world_name = pick(
        core_rng,
        PLACES,
    )

    faction = pick(
        core_rng,
        FACTIONS,
    )

    power_name = pick(
        core_rng,
        POWERS,
    )

    conflict = pick(
        core_rng,
        CONFLICTS,
    )

    protagonist_style = pick(
        core_rng,
        [
            "japanese",
            "korean",
            "chinese",
            "western",
        ],
    )

    used_names = set()

    protagonist = make_unique_name(
        core_rng,
        used_names,
        protagonist_style,
    )

    title = make_title(
        core_rng
    )

    world = make_world_blueprint(
        seed,
        world_name,
        genre,
        faction,
    )

    power = make_power_blueprint(
        seed,
        power_name,
    )

    characters = make_characters(
        stable_rng(
            f"{seed}:characters"
        ),
        protagonist,
    )

    antagonists = make_antagonists(
        seed,
        used_names,
    )

    secondary_faction_rng = stable_rng(
        f"{seed}:faction:secondary"
    )

    secondary_faction = pick(
        secondary_faction_rng,
        [
            name
            for name in FACTIONS
            if name != faction
        ],
    )

    factions = [
        {
            "name": faction,
            "role": "major faction",
            "description": (
                f"{faction} is one of the major organizations "
                f"whose decisions influence the events surrounding "
                f"{conflict}."
            ),
        },
        {
            "name": secondary_faction,
            "role": "secondary faction",
            "description": (
                f"{secondary_faction} operates independently of "
                f"{faction}, creating another source of alliances, "
                f"competition, and uncertainty."
            ),
        },
    ]

    arcs = make_arcs(
        seed,
        characters,
        antagonists,
        world,
        power,
    )

    central_mystery_rng = stable_rng(
        f"{seed}:mystery"
    )

    mysteries = [
        (
            f"Why does the history of {world_name} contradict "
            f"the records preserved by the major factions?"
        ),
        (
            f"Why does {power_name} appear to know something "
            f"about events that happened before {protagonist} "
            f"was born?"
        ),
        (
            f"Who originally created the hidden system behind "
            f"{conflict}?"
        ),
        (
            f"Why is {faction} connected to events that officially "
            f"never happened?"
        ),
    ]

    central_mystery = pick(
        central_mystery_rng,
        mysteries,
    )

    roadmap = make_chapter_roadmap(
        seed,
        arcs,
        characters,
        world,
        power,
        antagonists,
    )

    theme_rng = stable_rng(
        f"{seed}:themes"
    )

    theme_pool_one = [
        "identity",
        "friendship",
        "freedom",
        "ambition",
        "trust",
        "sacrifice",
        "redemption",
        "power",
        "responsibility",
        "family",
        "survival",
        "truth",
        "love",
        "belonging",
        "second chances",
    ]

    theme_pool_two = [
        "the cost of power",
        "the meaning of heroism",
        "the difference between truth and history",
        "the consequences of choices",
        "the absurdity of fate",
        "the value of ordinary life",
        "the danger of unchecked ambition",
    ]

    first_theme = pick(
        theme_rng,
        theme_pool_one,
    )

    second_theme = pick(
        theme_rng,
        theme_pool_two,
    )

    themes = [
        first_theme,
        second_theme,
    ]

    synopsis = (
        f"{title} is a long-form {genre.lower()} light novel "
        f"with elements of {secondary_genre.lower()} and a "
        f"{tone} tone. The story follows {protagonist}, whose "
        f"life becomes connected to {conflict} within "
        f"{world_name}. As the influence of {faction} grows and "
        f"the mysteries surrounding {power_name} deepen, what "
        f"begins as a personal journey gradually expands into "
        f"a conflict capable of changing the future of the world."
    )

    comedy_genres = {
        "Comedy",
        "Parody",
        "Romantic Comedy",
        "Fantasy Parody",
        "Isekai Parody",
        "Cultivation Parody",
        "System Parody",
        "Academy Parody",
        "Superhero Parody",
        "Villain Parody",
        "Hero Parody",
        "Self-Aware Comedy",
        "Meta Comedy",
        "Chaotic Comedy",
        "Absurd Comedy",
        "Fourth-Wall Comedy",
    }

    if (
        parody_mode
        or genre in comedy_genres
        or secondary_genre in comedy_genres
        or tone in {
            "comedic",
            "absurd",
            "satirical",
            "chaotic",
        }
    ):
        synopsis += (
            " The journey also embraces comedic situations, "
            "absurd misunderstandings, exaggerated reactions, "
            "unexpected failures, genre jokes, and occasional "
            "parody of familiar light-novel conventions."
        )

    protagonist_character = next(
        character
        for character in characters
        if character["name"] == protagonist
    )

    auto_descriptions = make_auto_descriptions(
        seed=seed,
        title=title,
        genre=genre,
        tone=tone,
        world=world,
        power=power,
        protagonist=protagonist_character,
        characters=characters,
        antagonists=antagonists,
        factions=factions,
        conflict=conflict,
        mystery=central_mystery,
        arcs=arcs,
    )

    protagonist_description = (
        f"{protagonist} is the central character whose "
        f"{protagonist_character['trait']} nature shapes the "
        f"early direction of the story. Their initial ability is "
        f"{protagonist_character['ability'].lower()}, but their "
        f"greatest challenge is learning what to do when the "
        f"answers they find create even more questions."
    )

    return {
        # ----------------------------------------------------
        # AUTHOR
        # ----------------------------------------------------

        "author": AUTHOR,

        # ----------------------------------------------------
        # BASIC INFORMATION
        # ----------------------------------------------------

        "title": title,
        "genre": genre,
        "secondary_genre": secondary_genre,
        "tone": tone,
        "parody_mode": parody_mode,
        "themes": themes,
        "synopsis": synopsis,

        # ----------------------------------------------------
        # AUTO-GENERATED LONG-FORM DESCRIPTIONS
        # ----------------------------------------------------

        "descriptions": {
            "world": auto_descriptions["world"],
            "story": auto_descriptions["story"],
            "people": auto_descriptions["people"],
            "power": auto_descriptions["power"],
            "mystery": auto_descriptions["mystery"],
            "journey": auto_descriptions["journey"],
        },

        # ----------------------------------------------------
        # WORLD
        # ----------------------------------------------------

        "world": {
            **world,
            "description": auto_descriptions["world"],
        },

        # ----------------------------------------------------
        # POWER SYSTEM
        # ----------------------------------------------------

        "power_system": {
            **power,
            "description": auto_descriptions["power"],
        },

        # ----------------------------------------------------
        # PROTAGONIST
        # ----------------------------------------------------

        "protagonist": {
            "name": protagonist,
            "style": protagonist_style,
            "trait": protagonist_character[
                "trait"
            ],
            "ability": protagonist_character[
                "ability"
            ],
            "description": protagonist_description,
            "goal": (
                "Discover the truth behind the events "
                "that changed their life."
            ),
            "fear": (
                "Losing the people who become important "
                "during the journey."
            ),
            "strengths": [
                "adaptability",
                "determination",
                "curiosity",
                "ability to form relationships",
            ],
            "weaknesses": [
                "incomplete knowledge",
                "limited experience",
                "emotional decisions",
                "difficulty understanding their own power",
            ],
        },

        # ----------------------------------------------------
        # CHARACTERS
        # ----------------------------------------------------

        "characters": characters,

        # ----------------------------------------------------
        # ANTAGONISTS
        # ----------------------------------------------------

        "antagonists": antagonists,

        # ----------------------------------------------------
        # FACTIONS
        # ----------------------------------------------------

        "factions": factions,

        # ----------------------------------------------------
        # CONFLICT
        # ----------------------------------------------------

        "main_conflict": conflict,

        "main_conflict_description": (
            auto_descriptions["story"]
        ),

        # ----------------------------------------------------
        # MYSTERY
        # ----------------------------------------------------

        "central_mystery": central_mystery,

        "central_mystery_description": (
            auto_descriptions["mystery"]
        ),

        # ----------------------------------------------------
        # STORY RULES
        # ----------------------------------------------------

        "story_rules": [
            "Actions have consequences.",
            "Power has limitations and costs.",
            "Characters can change their beliefs.",
            "Important mysteries are resolved gradually.",
            "Major revelations should connect to earlier clues.",
            "Relationships can change because of choices.",
            "Characters can fail.",
            "Characters can learn from failure.",
            "Important events should influence later chapters.",
            "Comedy can interrupt serious situations without "
            "automatically erasing their consequences.",
            "Parody elements can reference genre conventions "
            "without requiring existing copyrighted characters.",
        ],

        # ----------------------------------------------------
        # LONG-FORM STORY SECTIONS
        # ----------------------------------------------------

        "story_description": (
            auto_descriptions["story"]
        ),

        "people_description": (
            auto_descriptions["people"]
        ),

        "journey_description": (
            auto_descriptions["journey"]
        ),

        # ----------------------------------------------------
        # ARCS
        # ----------------------------------------------------

        "arcs": arcs,

        # ----------------------------------------------------
        # 600-CHAPTER ROADMAP
        # ----------------------------------------------------

        "chapter_roadmap": roadmap,

        # ----------------------------------------------------
        # COUNTS
        # ----------------------------------------------------

        "chapter_count": CHAPTER_COUNT,
        "chapter_word_count": CHAPTER_WORD_COUNT,
    }


# ============================================================
# NOVEL GENERATION
# ============================================================

def generate_novel(
    genre: str | None = None,
    parody: bool = False,
) -> Dict:

    seed = make_seed(genre, parody)

    blueprint = generate_blueprint(
        seed,
        genre_override=genre,
        parody_override=parody,
    )

    design = make_design(
        stable_rng(
            f"{seed}:design"
        )
    )

    world = blueprint[
        "world"
    ]

    power = blueprint[
        "power_system"
    ]

    faction = blueprint[
        "factions"
    ][0]["name"]

    descriptions = blueprint[
        "descriptions"
    ]

    return {
        "seed": seed,

        "author": AUTHOR,

        "title": blueprint[
            "title"
        ],

        "genre": blueprint[
            "genre"
        ],

        "secondary_genre": blueprint[
            "secondary_genre"
        ],

        "parody_mode": blueprint[
            "parody_mode"
        ],

        "tone": blueprint[
            "tone"
        ],

        "themes": blueprint[
            "themes"
        ],

        "synopsis": blueprint[
            "synopsis"
        ],

        # -----------------------------------------------
        # Existing simple values
        # -----------------------------------------------

        "world": world[
            "name"
        ],

        "faction": faction,

        "power": power[
            "name"
        ],

        "conflict": blueprint[
            "main_conflict"
        ],

        "protagonist": blueprint[
            "protagonist"
        ]["name"],

        # -----------------------------------------------
        # Automatically generated prose
        # -----------------------------------------------

        "world_description": descriptions[
            "world"
        ],

        "story_description": descriptions[
            "story"
        ],

        "people_description": descriptions[
            "people"
        ],

        "power_description": descriptions[
            "power"
        ],

        "mystery_description": descriptions[
            "mystery"
        ],

        "journey_description": descriptions[
            "journey"
        ],

        "author_description": (
            f"This original light novel was generated "
            f"for Light Novel World and is credited to "
            f"{AUTHOR}."
        ),

        "chapter_count": CHAPTER_COUNT,

        "chapter_word_count": CHAPTER_WORD_COUNT,

        "characters": blueprint[
            "characters"
        ],

        "arcs": blueprint[
            "arcs"
        ],

        "design": design,

        "blueprint": blueprint,
    }


# ============================================================
# WORD UTILITIES
# ============================================================

def clean_words(
    text: str,
) -> List[str]:

    return re.findall(
        r"\S+",
        text,
    )


def word_count(
    paragraphs: List[str],
) -> int:

    return sum(
        len(
            clean_words(
                paragraph
            )
        )
        for paragraph in paragraphs
    )


def trim_to_exact_words(
    paragraphs: List[str],
    target: int,
) -> List[str]:

    total = word_count(
        paragraphs
    )

    if total <= target:
        return paragraphs

    result = []

    remaining = target

    for paragraph in paragraphs:

        if remaining <= 0:
            break

        words = clean_words(
            paragraph
        )

        if len(words) <= remaining:

            result.append(
                paragraph
            )

            remaining -= len(
                words
            )

        else:

            shortened = " ".join(
                words[:remaining]
            )

            if shortened:
                result.append(
                    shortened
                )

            remaining = 0

    return result


def fill_to_exact_words(
    paragraphs: List[str],
    target: int,
    seed: str,
) -> List[str]:

    filler_rng = stable_rng(
        f"{seed}:filler"
    )

    fillers = [
        "The silence lasted longer than expected.",
        "Nobody immediately knew what to say.",
        "The unanswered question remained between them.",
        "Somewhere nearby, something moved.",
        "The night continued without offering an explanation.",
        "For now, the group could only continue forward.",
        "The road ahead remained uncertain.",
        "Another possibility quietly entered the discussion.",
        "No one wanted to admit how serious the situation had become.",
        "The discovery would make more sense later.",
        "For the moment, there was nothing else to do.",
        "The atmosphere changed without anyone announcing why.",
    ]

    while word_count(
        paragraphs
    ) < target:

        remaining = (
            target
            - word_count(
                paragraphs
            )
        )

        candidates = [
            sentence
            for sentence in fillers
            if len(
                clean_words(
                    sentence
                )
            ) <= remaining
        ]

        if not candidates:
            break

        paragraphs.append(
            pick(
                filler_rng,
                candidates,
            )
        )

    return trim_to_exact_words(
        paragraphs,
        target,
    )


# ============================================================
# CHAPTER GENERATION
# ============================================================

def generate_chapter(
    seed: str,
    chapter_number: int,
) -> Dict:

    if (
        chapter_number < 1
        or chapter_number > CHAPTER_COUNT
    ):
        raise ValueError(
            "Invalid chapter number"
        )

    blueprint = generate_blueprint(
        seed
    )

    rng = stable_rng(
        f"{seed}:chapter:{chapter_number}"
    )

    plan = blueprint[
        "chapter_roadmap"
    ][
        chapter_number - 1
    ]

    protagonist = blueprint[
        "protagonist"
    ]["name"]

    genre = blueprint[
        "genre"
    ]

    secondary_genre = blueprint[
        "secondary_genre"
    ]

    world = blueprint[
        "world"
    ]

    power = blueprint[
        "power_system"
    ]

    faction = blueprint[
        "factions"
    ][0]["name"]

    characters = blueprint[
        "characters"
    ]

    protagonist_character = next(
        (
            character
            for character in characters
            if character["role"]
            == "Protagonist"
        ),
        characters[0],
    )

    character_map = {
        character["name"]: character
        for character in characters
    }

    focus_characters = [
        character_map[name]
        for name in plan["characters"]
        if name in character_map
    ]

    if not focus_characters:
        focus_characters = [
            protagonist_character
        ]

    focus_names = [
        character["name"]
        for character in focus_characters
    ]

    supporting_name = (
        focus_names[1]
        if len(focus_names) > 1
        else protagonist
    )

    secondary_name = (
        focus_names[2]
        if len(focus_names) > 2
        else supporting_name
    )

    antagonist = pick(
        rng,
        blueprint[
            "antagonists"
        ],
    )

    location = plan[
        "location"
    ]

    object_item = pick(
        rng,
        OBJECTS,
    )

    arc = get_arc(
        blueprint["arcs"],
        chapter_number,
    )

    title = (
        f"Chapter {chapter_number:03d}: "
        f"{plan['title']}"
    )

    paragraphs: List[str] = []

    # --------------------------------------------------------
    # OPENING
    # --------------------------------------------------------

    openings = [
        (
            f"The morning over {location} began quietly, "
            f"although {protagonist} had already learned "
            f"that quiet places rarely stayed quiet for long."
        ),
        (
            f"When {protagonist} arrived in {location}, "
            f"the first thing they noticed was the unusual "
            f"silence. Even the people who normally filled "
            f"the streets seemed to be avoiding one another."
        ),
        (
            f"Nothing about {location} looked particularly "
            f"dangerous at first. That was exactly what made "
            f"{protagonist} uncomfortable."
        ),
        (
            f"{protagonist} had expected the next stage of "
            f"the journey to be simple. That expectation "
            f"lasted approximately until the moment they "
            f"entered {location}."
        ),
    ]

    paragraphs.append(
        pick(
            rng,
            openings,
        )
    )

    if blueprint["parody_mode"]:
        paragraphs.append(
            pick(rng, PARODY_LINES)
        )

    paragraphs.append(
        (
            f"The chapter begins during the {plan['phase']} "
            f"stage of the {arc['title']} arc. The immediate "
            f"purpose is to {plan['purpose'].lower()} "
            f"Although the characters cannot yet see the full "
            f"shape of what is happening, the decisions made "
            f"here will influence what comes next."
        )
    )

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    paragraphs.append(
        (
            f"{supporting_name} noticed something unusual "
            f"near {location}. It was {object_item}, apparently "
            f"left behind by someone who had no intention of "
            f"being identified."
        )
    )

    paragraphs.extend(
        plan["events"]
    )

    paragraphs.append(
        (
            f"{protagonist} examined the situation carefully. "
            f"The evidence seemed connected to {world['name']}, "
            f"and several details pointed toward the influence "
            f"of {faction}."
        )
    )

    paragraphs.append(
        (
            f"The discovery forced the group to reconsider "
            f"what they thought they understood. What had "
            f"appeared to be an isolated incident now seemed "
            f"connected to the larger pattern surrounding "
            f"{arc['theme']}."
        )
    )

    paragraphs.append(
        (
            f"The decision immediately created a new problem. "
            f"{secondary_name} disagreed, arguing that the group "
            f"was missing information that could completely "
            f"change their interpretation of the evidence."
        )
    )

    # --------------------------------------------------------
    # CHARACTER DEVELOPMENT
    # --------------------------------------------------------

    paragraphs.append(
        (
            f"{protagonist} understood that the problem was "
            f"becoming personal. The journey had begun with "
            f"questions, but every new answer demanded another "
            f"choice."
        )
    )

    paragraphs.append(
        plan[
            "character_development"
        ]
    )

    # --------------------------------------------------------
    # POWER
    # --------------------------------------------------------

    power_events = [
        (
            f"The presence of {power['name']} became noticeable "
            f"again. {protagonist} could feel the familiar "
            f"pressure building beneath their awareness."
        ),
        (
            f"{protagonist} attempted to use {power['name']}, "
            f"but the ability responded differently than expected."
        ),
        (
            f"For a brief moment, the rules of {power['name']} "
            f"appeared to change."
        ),
    ]

    paragraphs.append(
        pick(
            rng,
            power_events,
        )
    )

    paragraphs.append(
        (
            f"The effect was limited. {protagonist} knew that "
            f"{power['name']} could not simply solve every "
            f"problem, and forcing the ability further could "
            f"have consequences."
        )
    )

    paragraphs.append(
        plan[
            "power_development"
        ]
    )

    # --------------------------------------------------------
    # DIALOGUE
    # --------------------------------------------------------

    dialogue_sets = [
        [
            f'"We need more information," {supporting_name} said.',
            f'"We already have enough," {protagonist} replied.',
            f'"Enough to do what?"',
            f'"Enough to know that waiting is worse."',
        ],
        [
            f'"Do you trust them?" {secondary_name} asked.',
            f'"No," {protagonist} answered.',
            f'"Then why are we listening?"',
            '"Because sometimes the truth comes from people we dislike."',
        ],
        [
            f'"This cannot be coincidence," {supporting_name} said.',
            f'"I know," {protagonist} replied.',
            '"Then what are we supposed to do?"',
            '"Keep going until coincidence becomes impossible."',
        ],
        [
            f'"You are taking this too seriously," {secondary_name} said.',
            '"Something is trying to kill us."',
            '"Exactly. That means we should at least enjoy breakfast first."',
            f'{protagonist} stared at {secondary_name}.',
            '"You are impossible."',
        ],
    ]

    paragraphs.extend(
        pick(
            rng,
            dialogue_sets,
        )
    )

    # --------------------------------------------------------
    # COMEDY
    # --------------------------------------------------------

    comedy_genres = {
        "Comedy",
        "Parody",
        "Romantic Comedy",
        "Fantasy Parody",
        "Isekai Parody",
        "Cultivation Parody",
        "System Parody",
        "Academy Parody",
        "Superhero Parody",
        "Villain Parody",
        "Hero Parody",
        "Self-Aware Comedy",
        "Meta Comedy",
        "Chaotic Comedy",
        "Absurd Comedy",
        "Fourth-Wall Comedy",
    }

    if (
        genre in comedy_genres
        or secondary_genre in comedy_genres
        or blueprint["tone"] in {
            "comedic",
            "absurd",
            "satirical",
            "chaotic",
        }
    ):

        comedy_events = [
            (
                "For approximately five seconds, everyone "
                "agreed on a sensible plan. Then they immediately "
                "started arguing about who was responsible for it."
            ),
            (
                f"{protagonist} considered using {power['name']} "
                "to solve the problem. Then they remembered "
                "that using mysterious supernatural powers "
                "usually created three additional problems."
            ),
            (
                "Nobody mentioned it aloud, but everyone knew "
                "that this was exactly the sort of situation "
                "that would become embarrassing when retold later."
            ),
            (
                f"{secondary_name} offered a brilliant solution. "
                f"It was so brilliant that {protagonist} immediately "
                f"rejected it."
            ),
            (
                "The situation had officially reached the point "
                "where even the universe seemed to be making jokes."
            ),
        ]

        paragraphs.append(
            pick(
                rng,
                comedy_events,
            )
        )

    # --------------------------------------------------------
    # MYSTERY
    # --------------------------------------------------------

    paragraphs.append(
        (
            f"The clues eventually pointed toward a deeper "
            f"question: {blueprint['central_mystery']}"
        )
    )

    paragraphs.append(
        plan[
            "world_development"
        ]
    )

    paragraphs.append(
        plan[
            "revelation"
        ]
    )

    # --------------------------------------------------------
    # ANTAGONIST
    # --------------------------------------------------------

    paragraphs.append(
        (
            f"{antagonist['name']} remained somewhere beyond "
            f"the immediate scene. Their motives were still "
            f"unclear, but the consequences of their actions "
            f"were becoming easier to recognize."
        )
    )

    paragraphs.append(
        (
            f"The group finally understood that {antagonist['name']} "
            f"was not acting randomly. They were pursuing an "
            f"objective connected to the larger conflict, and "
            f"their next move could change the situation again."
        )
    )

    # --------------------------------------------------------
    # REFLECTION
    # --------------------------------------------------------

    paragraphs.append(
        (
            f"Later, when the immediate danger had passed, "
            f"{protagonist} thought about the journey so far. "
            f"The person who had entered {world['name']} at "
            f"the beginning would not have recognized the person "
            f"standing there now."
        )
    )

    paragraphs.append(
        plan[
            "state_after"
        ]
    )

    # --------------------------------------------------------
    # BRIDGE MATERIAL
    # --------------------------------------------------------

    bridge_paragraphs = [
        (
            f"The group continued through {location}, carefully "
            f"avoiding unnecessary attention."
        ),
        (
            f"{supporting_name} kept the strange object nearby, "
            f"although nobody completely understood its purpose."
        ),
        (
            "The conversation returned repeatedly to the same "
            "unanswered questions."
        ),
        (
            f"{protagonist} noticed another detail connected "
            f"to the mystery and quietly memorized it."
        ),
        (
            "The road ahead was uncertain, but turning back "
            "was no longer an attractive option."
        ),
        (
            "For a moment everything seemed ordinary again."
        ),
        (
            "That moment did not last."
        ),
    ]

    bridge_index = 0

    while (
        word_count(paragraphs) < 700
        and bridge_index < len(
            bridge_paragraphs
        )
    ):

        paragraphs.append(
            bridge_paragraphs[
                bridge_index
            ]
        )

        bridge_index += 1

    # --------------------------------------------------------
    # CLIFFHANGER
    # --------------------------------------------------------

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
            "Far beyond the horizon, a strange light appeared."
        ),
        (
            "The sealed door opened by itself."
        ),
        (
            f"A new symbol appeared on {protagonist}'s hand."
        ),
        (
            "Someone left a letter outside the door containing "
            "tomorrow's date."
        ),
        (
            f"{antagonist['name']}'s voice came from the darkness."
        ),
        (
            "The next destination appeared on a map that had "
            "previously been completely blank."
        ),
    ]

    paragraphs.append(
        pick(
            rng,
            cliffhangers,
        )
    )

    paragraphs.append(
        (
            f"{protagonist} stared into the darkness. "
            f"The answer would have to wait until tomorrow."
        )
    )

    # --------------------------------------------------------
    # EXACT WORD COUNT
    # --------------------------------------------------------

    paragraphs = trim_to_exact_words(
        paragraphs,
        CHAPTER_WORD_COUNT,
    )

    if word_count(
        paragraphs
    ) < CHAPTER_WORD_COUNT:

        paragraphs = fill_to_exact_words(
            paragraphs,
            CHAPTER_WORD_COUNT,
            f"{seed}:{chapter_number}",
        )

    final_count = word_count(
        paragraphs
    )

    # --------------------------------------------------------
    # FINAL CHAPTER OBJECT
    # --------------------------------------------------------

    return {
        "author": AUTHOR,

        "number": chapter_number,

        "title": title,

        "arc": arc,

        "arc_number": arc[
            "number"
        ],

        "phase": plan[
            "phase"
        ],

        "location": location,

        "genre": genre,

        "secondary_genre": secondary_genre,

        "characters": focus_names,

        "antagonist": antagonist[
            "name"
        ],

        "chapter_plan": plan,

        "paragraphs": paragraphs,

        "word_count": final_count,

        "world_description": blueprint[
            "descriptions"
        ]["world"],

        "story_description": blueprint[
            "descriptions"
        ]["story"],

        "people_description": blueprint[
            "descriptions"
        ]["people"],

        "power_description": blueprint[
            "descriptions"
        ]["power"],

        "mystery_description": blueprint[
            "descriptions"
        ]["mystery"],

        "journey_description": blueprint[
            "descriptions"
        ]["journey"],

        "author_description": (
            f"Original light novel by {AUTHOR}."
        ),
    }
