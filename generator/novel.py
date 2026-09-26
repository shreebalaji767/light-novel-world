from __future__ import annotations

import hashlib
import random
import re
import secrets
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

    # East Asian Fantasy / Cultivation
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
    "Romantic Comedy",
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
    "Family Drama",
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

    # School / Academy
    "Academy",
    "Magic Academy",
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
    "School Romance",

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
    "Historical Romance",
    "Historical Mystery",
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
    "Mecha",
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
    "Fourth-Wall Comedy",
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


def make_seed() -> str:
    return secrets.token_hex(32)


def pick(rng: random.Random, items: list):
    return items[rng.randrange(len(items))]


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
            f"{pick(rng, JAPANESE_FIRST_NAMES)} "
            f"{pick(rng, JAPANESE_LAST_NAMES)}"
        )

    if style == "korean":
        return (
            f"{pick(rng, KOREAN_FIRST_NAMES)} "
            f"{pick(rng, KOREAN_LAST_NAMES)}"
        )

    if style == "chinese":
        return (
            f"{pick(rng, CHINESE_FIRST_NAMES)} "
            f"{pick(rng, CHINESE_LAST_NAMES)}"
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
        name = make_name(rng, style)

        if name not in used_names:
            used_names.add(name)
            return name

    suffix = rng.randrange(1000, 9999)
    name = f"{make_name(rng, style)} {suffix}"

    used_names.add(name)

    return name


# ============================================================
# UNIQUE SELECTION
# ============================================================

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

    value = pick(rng, available)

    used.add(value)

    return value


# ============================================================
# TITLE GENERATION
# ============================================================

def make_title(
    rng: random.Random,
) -> str:

    prefix = pick(rng, TITLE_PREFIXES)
    adjective = pick(rng, TITLE_WORDS)
    noun = pick(rng, TITLE_NOUNS)

    patterns = [
        f"{prefix} {adjective} {noun}",
        f"{adjective} {noun}",
        f"{prefix} {noun} of {adjective}",
        f"{prefix} {adjective} {noun}",
        f"{adjective} {noun}: A Completely Unnecessary Adventure",
    ]

    return pick(rng, patterns)


# ============================================================
# CHARACTER GENERATION
# ============================================================

def make_characters(
    rng: random.Random,
    protagonist: str,
) -> List[Dict]:

    used_names = {protagonist}

    characters = []

    characters.append(
        {
            "name": protagonist,
            "role": "Protagonist",
            "origin_style": "mixed",
            "trait": pick(rng, CHARACTER_TRAITS),
            "ability": pick(rng, ABILITIES),
            "description": (
                f"{protagonist} is the central character of "
                f"the story. Their journey begins with a personal "
                f"problem but gradually becomes connected to a "
                f"much larger conflict."
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

    for index, role in enumerate(roles[:9]):

        style = styles[index % len(styles)]

        name = make_unique_name(
            rng,
            used_names,
            style,
        )

        characters.append(
            {
                "name": name,
                "role": role,
                "origin_style": style,
                "trait": pick(rng, CHARACTER_TRAITS),
                "ability": pick(rng, ABILITIES),
                "description": (
                    f"{name} serves as the story's "
                    f"{role.lower()}. Their decisions can "
                    f"change the direction of the journey."
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

    rng = stable_rng(f"{seed}:world")

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

    locations = [
        world,
        pick(rng, PLACES),
        pick(rng, PLACES),
        pick(rng, PLACES),
        pick(rng, PLACES),
        pick(rng, PLACES),
    ]

    unique_locations = []

    for location in locations:
        if location not in unique_locations:
            unique_locations.append(location)

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

    description = (
        f"{world} is a fictional world shaped by {genre.lower()}, "
        f"where ancient history, competing cultures, hidden powers, "
        f"and unresolved mysteries influence everyday life. "
        f"The setting combines familiar places with unexplored "
        f"regions whose histories gradually become important to "
        f"{protagonist_placeholder(world)}."
    )

    return {
        "name": world,
        "type": pick(rng, world_types),
        "genre_context": genre,
        "era": pick(rng, eras),
        "description": description,
        "geography": geography,
        "important_locations": unique_locations,
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


def protagonist_placeholder(world: str) -> str:
    return f"the people living within {world}"


# ============================================================
# WORLD DESCRIPTION
# ============================================================

def make_world_description(
    world: Dict,
    conflict: str,
    faction: str,
    power: str,
) -> str:

    return (
        f"{world['name']} is {world['type']} set during "
        f"{world['era']}. Its regions, cultures, and hidden "
        f"history are shaped by the unresolved conflict surrounding "
        f"{conflict}. The world is also influenced by organizations "
        f"such as {faction}, while {power} represents one of the "
        f"extraordinary forces that can change the balance of power. "
        f"What appears to be ordinary history gradually reveals "
        f"secrets that connect the world's past to the present journey."
    )


# ============================================================
# CONFLICT DESCRIPTION
# ============================================================

def make_conflict_description(
    conflict: str,
    world: str,
    protagonist: str,
    faction: str,
) -> str:

    return (
        f"The central conflict begins with {conflict}. "
        f"What first appears to be an isolated problem in {world} "
        f"gradually reveals connections to older events and hidden "
        f"interests. {protagonist} becomes involved before fully "
        f"understanding what is at stake, while {faction} becomes "
        f"one of the major forces whose decisions can alter the "
        f"course of the story."
    )


# ============================================================
# FACTION DESCRIPTION
# ============================================================

def make_faction_description(
    faction: str,
    world: str,
    conflict: str,
) -> str:

    return (
        f"{faction} is a major organization operating within "
        f"{world}. Its influence extends beyond a single location, "
        f"and its members have their own interests, alliances, "
        f"secrets, and disagreements. As {conflict} develops, "
        f"the faction's true position becomes increasingly important "
        f"to the characters and the larger mystery."
    )


# ============================================================
# POWER DESCRIPTION
# ============================================================

def make_power_description(
    power: Dict,
    protagonist: str,
) -> str:

    return (
        f"{power['name']} is an extraordinary ability system whose "
        f"users rely on {power['mechanism']}. For {protagonist}, "
        f"understanding this power is a gradual process rather than "
        f"an instant transformation. Its use carries meaningful "
        f"costs, including {power['costs'][0]}, and stronger forms "
        f"require greater knowledge, control, and sacrifice. "
        f"The system therefore provides opportunities for growth "
        f"without becoming an unlimited solution to every problem."
    )


# ============================================================
# POWER BLUEPRINT
# ============================================================

def make_power_blueprint(
    seed: str,
    power: str,
) -> Dict:

    rng = stable_rng(f"{seed}:power")

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

    return {
        "name": power,
        "description": (
            f"{power} is the primary extraordinary ability system "
            f"associated with the story. It begins as a limited "
            f"ability and becomes increasingly important as the "
            f"protagonist discovers its deeper rules."
        ),
        "mechanism": pick(rng, mechanisms),
        "costs": [
            pick(rng, costs),
            pick(rng, costs),
            pick(rng, costs),
        ],
        "levels": levels,
        "limitations": [
            "power cannot solve every problem",
            "strong abilities require preparation or sacrifice",
            "knowledge of the system is incomplete",
            "stronger enemies can exploit weaknesses",
        ],
        "rare_abilities": [
            pick(rng, rare),
            pick(rng, rare),
            pick(rng, rare),
        ],
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

    rng = stable_rng(f"{seed}:antagonists")

    roles = [
        "Primary Antagonist",
        "Secondary Antagonist",
        "Political Antagonist",
        "Personal Rival",
        "Hidden Antagonist",
    ]

    descriptions = [
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

    for index, role in enumerate(roles):

        name = make_unique_name(
            rng,
            used_names,
            styles[index % 4],
        )

        antagonists.append(
            {
                "name": name,
                "role": role,
                "motivation": pick(rng, descriptions),
                "description": (
                    f"{name} is a fictional {role.lower()} whose "
                    f"actions influence the long-term direction "
                    f"of the story."
                ),
            }
        )

    return antagonists


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

    for index in range(ARC_COUNT):

        rng = stable_rng(
            f"{seed}:arc:{index + 1}"
        )

        start = (
            index * CHAPTERS_PER_ARC
            + 1
        )

        end = (
            CHAPTER_COUNT
            if index == ARC_COUNT - 1
            else (index + 1) * CHAPTERS_PER_ARC
        )

        character_names = [
            character["name"]
            for character in characters
        ]

        involved = []

        available = list(character_names)

        for _ in range(min(4, len(character_names))):
            if available:
                selected = pick(rng, available)
                involved.append(selected)
                available.remove(selected)

        antagonist = pick(rng, antagonists)

        arcs.append(
            {
                "number": index + 1,
                "title": ARC_NAMES[index],
                "start": start,
                "end": end,
                "theme": pick(rng, ARC_THEMES),
                "objective": (
                    f"The characters must survive the events of "
                    f"this stage while discovering another part "
                    f"of the mystery surrounding {world['name']}."
                ),
                "central_conflict": (
                    f"The conflict between the protagonists and "
                    f"{antagonist['name']} becomes increasingly important."
                ),
                "locations": world["important_locations"][
                    :min(3, len(world["important_locations"]))
                ],
                "characters_involved": involved,
                "antagonist_activity": (
                    f"{antagonist['name']} advances a plan connected "
                    f"to the larger conflict."
                ),
                "power_progression": (
                    f"The characters gain a deeper understanding "
                    f"of {power['name']}."
                ),
                "major_revelation": (
                    f"A new piece of the history of "
                    f"{world['name']} becomes known."
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

        ratio = relative / max(
            1,
            arc_length - 1,
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

        for _ in range(10):
            if title not in used_titles:
                break

            title = (
                f"{pick(rng, CHAPTER_VERBS)} "
                f"{pick(rng, CHAPTER_NOUNS)}"
            )

        if title in used_titles:
            title = f"{title} #{chapter_number}"

        used_titles.add(title)

        shuffled_characters = list(character_names)
        rng.shuffle(shuffled_characters)

        focus = shuffled_characters[
            :min(3, len(character_names))
        ]

        antagonist = pick(rng, antagonists)

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

        if phase in {"turning point", "climax"}:
            events.append(
                (
                    f"The rules of {power['name']} become "
                    f"more important to the conflict."
                )
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

        roadmap.append(
            {
                "number": chapter_number,
                "title": title,
                "arc_number": arc["number"],
                "arc_title": arc["title"],
                "phase": phase,
                "purpose": purpose,
                "location": pick(
                    rng,
                    world["important_locations"],
                ),
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
                    f"The chapter develops the understanding "
                    f"of {power['name']} without making it "
                    f"an unlimited solution."
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
        if arc["start"] <= chapter_number <= arc["end"]:
            return arc

    return arcs[-1]


# ============================================================
# NOVEL BLUEPRINT
# ============================================================

def generate_blueprint(
    seed: str,
) -> Dict:

    core_rng = stable_rng(
        f"{seed}:core"
    )

    genre = pick(core_rng, GENRES)
    secondary_genre = pick(core_rng, SECONDARY_GENRES)
    tone = pick(core_rng, TONES)

    world_name = pick(core_rng, PLACES)
    faction = pick(core_rng, FACTIONS)
    power_name = pick(core_rng, POWERS)
    conflict = pick(core_rng, CONFLICTS)

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

    title = make_title(core_rng)

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
        stable_rng(f"{seed}:characters"),
        protagonist,
    )

    antagonists = make_antagonists(
        seed,
        used_names,
    )

    arcs = make_arcs(
        seed,
        characters,
        antagonists,
        world,
        power,
    )

    roadmap = make_chapter_roadmap(
        seed,
        arcs,
        characters,
        world,
        power,
        antagonists,
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
            f"about events that happened before the protagonist "
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

    themes = [
        pick(
            core_rng,
            [
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
            ],
        ),
        pick(
            core_rng,
            [
                "the cost of power",
                "the meaning of heroism",
                "the difference between truth and history",
                "the consequences of choices",
                "the absurdity of fate",
                "the value of ordinary life",
                "the danger of unchecked ambition",
            ],
        ),
    ]

    synopsis = (
        f"{title} is a long-form {genre.lower()} light novel "
        f"with elements of {secondary_genre.lower()} and a "
        f"{tone} tone. The story follows {protagonist}, who "
        f"becomes involved in {conflict} within {world_name}. "
        f"As the influence of {faction} grows and the mysteries "
        f"surrounding {power_name} deepen, what begins as a "
        f"personal journey gradually expands into a conflict "
        f"that can reshape the entire world."
    )

    if (
        "Comedy" in genre
        or "Parody" in genre
    ):
        synopsis += (
            " Along the way, the story deliberately embraces "
            "comedic situations, absurd misunderstandings, "
            "genre jokes, exaggerated character reactions, "
            "and occasional parody of familiar light-novel "
            "story conventions."
        )

    world_description = make_world_description(
        world,
        conflict,
        faction,
        power_name,
    )

    conflict_description = make_conflict_description(
        conflict,
        world_name,
        protagonist,
        faction,
    )

    faction_description = make_faction_description(
        faction,
        world_name,
        conflict,
    )

    power_description = make_power_description(
        power,
        protagonist,
    )

    return {
        # ----------------------------------------------------
        # AUTHOR
        # ----------------------------------------------------

        "author": AUTHOR,

        # ----------------------------------------------------
        # BASIC NOVEL INFORMATION
        # ----------------------------------------------------

        "title": title,
        "genre": genre,
        "secondary_genre": secondary_genre,
        "tone": tone,
        "themes": themes,
        "synopsis": synopsis,

        # ----------------------------------------------------
        # DESCRIPTIVE HERO INFORMATION
        # ----------------------------------------------------

        "descriptions": {
            "world": world_description,
            "conflict": conflict_description,
            "faction": faction_description,
            "power": power_description,
        },

        # ----------------------------------------------------
        # WORLD
        # ----------------------------------------------------

        "world": world,

        # ----------------------------------------------------
        # POWER SYSTEM
        # ----------------------------------------------------

        "power_system": power,

        # ----------------------------------------------------
        # PROTAGONIST
        # ----------------------------------------------------

        "protagonist": {
            "name": protagonist,
            "style": protagonist_style,
            "description": (
                f"{protagonist} is the central character whose "
                f"personal choices gradually connect to the "
                f"larger conflict."
            ),
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

        "factions": [
            {
                "name": faction,
                "role": "major faction",
                "description": faction_description,
            },
            {
                "name": pick(
                    stable_rng(
                        f"{seed}:faction:secondary"
                    ),
                    FACTIONS,
                ),
                "role": "secondary faction",
                "description": (
                    "A second organization whose interests "
                    "sometimes align with the protagonists "
                    "and sometimes oppose them."
                ),
            },
        ],

        # ----------------------------------------------------
        # CONFLICT
        # ----------------------------------------------------

        "main_conflict": conflict,

        # Human-readable version
        "main_conflict_description": conflict_description,

        # ----------------------------------------------------
        # MYSTERY
        # ----------------------------------------------------

        "central_mystery": central_mystery,

        # ----------------------------------------------------
        # STORY RULES
        # ----------------------------------------------------

        "story_rules": [
            "Actions have consequences.",
            "Power has limitations and costs.",
            "Characters can change their beliefs.",
            "Important mysteries are resolved gradually.",
            "Major revelations should connect to earlier clues.",
            "Comedy can interrupt serious situations without "
            "automatically erasing their consequences.",
            "Parody elements can reference genre conventions "
            "without requiring existing copyrighted characters.",
        ],

        # ----------------------------------------------------
        # ARCS
        # ----------------------------------------------------

        "arcs": arcs,

        # ----------------------------------------------------
        # 600 CHAPTER ROADMAP
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

def generate_novel() -> Dict:

    seed = make_seed()

    blueprint = generate_blueprint(seed)

    design = make_design(
        stable_rng(
            f"{seed}:design"
        )
    )

    world = blueprint["world"]
    power = blueprint["power_system"]
    faction = blueprint["factions"][0]["name"]

    return {
        "seed": seed,

        # AUTHOR — ALWAYS blssnvj21
        "author": AUTHOR,

        "title": blueprint["title"],
        "genre": blueprint["genre"],
        "secondary_genre": blueprint["secondary_genre"],
        "tone": blueprint["tone"],
        "synopsis": blueprint["synopsis"],

        # Existing simple values retained
        "world": world["name"],
        "faction": faction,
        "power": power["name"],
        "conflict": blueprint["main_conflict"],
        "protagonist": blueprint["protagonist"]["name"],

        # NEW DESCRIPTIVE VALUES FOR UI
        "world_description": blueprint[
            "descriptions"
        ]["world"],

        "conflict_description": blueprint[
            "descriptions"
        ]["conflict"],

        "faction_description": blueprint[
            "descriptions"
        ]["faction"],

        "power_description": blueprint[
            "descriptions"
        ]["power"],

        "author_description": (
            f"This original light novel was generated "
            f"for Light Novel World and is credited to "
            f"{AUTHOR}."
        ),

        "chapter_count": CHAPTER_COUNT,
        "chapter_word_count": CHAPTER_WORD_COUNT,

        "characters": blueprint["characters"],
        "arcs": blueprint["arcs"],
        "design": design,
        "blueprint": blueprint,
    }


# ============================================================
# WORD UTILITIES
# ============================================================

def clean_words(text: str) -> List[str]:

    return re.findall(
        r"\S+",
        text,
    )


def word_count(
    paragraphs: List[str],
) -> int:

    return sum(
        len(clean_words(paragraph))
        for paragraph in paragraphs
    )


def trim_to_exact_words(
    paragraphs: List[str],
    target: int,
) -> List[str]:

    total = word_count(paragraphs)

    if total == target:
        return paragraphs

    if total < target:
        return paragraphs

    result = []
    remaining = target

    for paragraph in paragraphs:

        if remaining <= 0:
            break

        words = clean_words(paragraph)

        if len(words) <= remaining:

            result.append(paragraph)
            remaining -= len(words)

        else:

            shortened = " ".join(
                words[:remaining]
            )

            if shortened:
                result.append(shortened)

            remaining = 0

    return result


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

    blueprint = generate_blueprint(seed)

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

    genre = blueprint["genre"]
    secondary_genre = blueprint["secondary_genre"]
    world = blueprint["world"]
    power = blueprint["power_system"]
    faction = blueprint["factions"][0]["name"]

    characters = blueprint["characters"]

    protagonist_character = next(
        (
            character
            for character in characters
            if character["role"] == "Protagonist"
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
        blueprint["antagonists"],
    )

    location = plan["location"]

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
        pick(rng, openings)
    )

    paragraphs.append(
        (
            f"This chapter marks the {plan['phase']} phase "
            f"of the {arc['title']} arc. The immediate purpose "
            f"is to {plan['purpose'].lower()} "
            f"{protagonist} does not yet understand how "
            f"important the events will become."
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

    paragraphs.append(
        plan["events"][0]
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
        plan["events"][1]
    )

    paragraphs.append(
        (
            f"The decision immediately created a new problem. "
            f"{secondary_name} disagreed, arguing that the group "
            f"was missing information that could completely "
            f"change their interpretation of the evidence."
        )
    )

    paragraphs.append(
        plan["events"][2]
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
        plan["character_development"]
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
        pick(rng, power_events)
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
        plan["power_development"]
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
        pick(rng, dialogue_sets)
    )

    # --------------------------------------------------------
    # COMEDY / PARODY
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
    }

    if (
        genre in comedy_genres
        or secondary_genre in comedy_genres
        or blueprint["tone"] in {
            "comedic",
            "absurd",
            "satirical",
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
            pick(rng, comedy_events)
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
        plan["world_development"]
    )

    paragraphs.append(
        plan["revelation"]
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
            f"was not acting randomly. Every movement was connected "
            f"to a larger objective."
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
        plan["state_after"]
    )

    # --------------------------------------------------------
    # NON-REPEATING BRIDGE MATERIAL
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

    for bridge in bridge_paragraphs:
        if word_count(paragraphs) >= 700:
            break

        paragraphs.append(bridge)

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
        pick(rng, cliffhangers)
    )

    paragraphs.append(
        (
            f"{protagonist} stared into the darkness. "
            f"The answer would have to wait until tomorrow."
        )
    )

    # --------------------------------------------------------
    # EXACT WORD TARGET
    # --------------------------------------------------------

    paragraphs = trim_to_exact_words(
        paragraphs,
        CHAPTER_WORD_COUNT,
    )

    current_count = word_count(paragraphs)

    if current_count < CHAPTER_WORD_COUNT:

        filler_sentences = [
            (
                f"The silence around {protagonist} felt "
                f"different now."
            ),
            (
                "Nobody spoke for several seconds."
            ),
            (
                "The unanswered question remained."
            ),
            (
                "Somewhere nearby, something moved."
            ),
            (
                "The night continued without offering an answer."
            ),
        ]

        filler_index = 0

        while word_count(paragraphs) < CHAPTER_WORD_COUNT:

            sentence = filler_sentences[
                filler_index % len(filler_sentences)
            ]

            remaining = (
                CHAPTER_WORD_COUNT
                - word_count(paragraphs)
            )

            sentence_words = clean_words(sentence)

            if len(sentence_words) <= remaining:
                paragraphs.append(sentence)
            else:
                shortened = " ".join(
                    sentence_words[:remaining]
                )

                if shortened:
                    paragraphs.append(shortened)

            filler_index += 1

        paragraphs = trim_to_exact_words(
            paragraphs,
            CHAPTER_WORD_COUNT,
        )

    final_count = word_count(paragraphs)

    # --------------------------------------------------------
    # FINAL CHAPTER OBJECT
    # --------------------------------------------------------

    return {
        "author": AUTHOR,
        "number": chapter_number,
        "title": title,
        "arc": arc,
        "arc_number": arc["number"],
        "phase": plan["phase"],
        "location": location,
        "genre": genre,
        "secondary_genre": secondary_genre,
        "characters": focus_names,
        "antagonist": antagonist["name"],
        "chapter_plan": plan,
        "paragraphs": paragraphs,
        "word_count": final_count,

        # Descriptive information available to the frontend
        "world_description": blueprint[
            "descriptions"
        ]["world"],

        "conflict_description": blueprint[
            "descriptions"
        ]["conflict"],

        "faction_description": blueprint[
            "descriptions"
        ]["faction"],

        "power_description": blueprint[
            "descriptions"
        ]["power"],

        "author_description": (
            f"Original light novel by {AUTHOR}."
        ),
    }
