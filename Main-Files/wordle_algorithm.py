
from cgitb import reset
from configparser import NoSectionError
from tkinter import *
import csv
from dataclasses import replace

possibleAnswers = ["cigar", "rebut", "sissy", "humph", "awake", "blush", "focal", "evade", "naval", "serve", "heath", "dwarf", "model", "karma", "stink", "grade", "quiet", "bench", "abate", "feign", "major", "death", "fresh", "crust", "stool", "colon", "abase", "marry", "react", "batty", "pride", "floss", "helix", "croak", "staff", "paper", "unfed", "whelp", "trawl", "outdo", "adobe", "crazy", "sower", "repay", "digit", "crate", "cluck", "spike", "mimic", "pound", "maxim", "linen", "unmet", "flesh", "booby", "forth", "first", "stand", "belly", "ivory", "seedy", "print", "yearn", "drain", "bribe", "stout", "panel", "crass", "flume", "offal", "agree", "error", "swirl", "argue", "bleed", "delta", "flick", "totem", "wooer", "front", "shrub", "parry", "biome", "lapel", "start", "greet", "goner", "golem", "lusty", "loopy", "round", "audit", "lying", "gamma", "labor", "islet", "civic", "forge", "corny", "moult", "basic", "salad", "agate", "spicy", "spray", "essay", "fjord", "spend", "kebab", "guild", "aback", "motor", "alone", "hatch", "hyper", "thumb", "dowry", "ought", "belch", "dutch", "pilot", "tweed", "comet", "jaunt", "enema", "steed", "abyss", "growl", "fling", "dozen", "boozy", "erode", "world", "gouge", "click", "briar", "great", "altar", "pulpy", "blurt", "coast", "duchy", "groin", "fixer", "group", "rogue", "badly", "smart", "pithy", "gaudy", "chill", "heron", "vodka", "finer", "surer", "radio", "rouge", "perch", "retch", "wrote", "clock", "tilde", "store", "prove", "bring", "solve", "cheat", "grime", "exult", "usher", "epoch", "triad", "break", "rhino", "viral", "conic", "masse", "sonic", "vital", "trace", "using", "peach", "champ", "baton", "brake", "pluck", "craze", "gripe", "weary", "picky", "acute", "ferry", "aside", "tapir", "troll", "unify", "rebus", "boost", "truss", "siege", "tiger", "banal", "slump", "crank", "gorge", "query", "drink", "favor", "abbey", "tangy", "panic", "solar", "shire", "proxy", "point", "robot", "prick", "wince", "crimp", "knoll", "sugar", "whack", "mount", "perky", "could", "wrung", "light", "those", "moist", "shard", "pleat", "aloft", "skill", "elder", "frame", "humor", "pause", "ulcer", "ultra", "robin", "cynic", "aroma", "caulk", "shake", "dodge", "swill", "tacit", "other", "thorn", "trove", "bloke", "vivid", "spill", "chant", "choke", "rupee", "nasty", "mourn", "ahead", "brine", "cloth", "hoard", "sweet", "month", "lapse", "watch", "today", "focus", "smelt", "tease", "cater", "movie", "saute", "allow", "renew", "their", "slosh", "purge", "chest", "depot", "epoxy", "nymph", "found", "shall", "stove", "lowly", "snout", "trope", "fewer", "shawl", "natal", "comma", "foray", "scare", "stair", "black", "squad", "royal", "chunk", "mince", "shame", "cheek", "ample", "flair", "foyer", "cargo", "oxide", "plant", "olive", "inert", "askew", "heist", "shown", "zesty", "trash", "larva", "forgo", "story", "hairy", "train", "homer", "badge", "midst", "canny", "fetus", "butch", "farce", "slung", "tipsy", "metal", "yield", "delve", "being", "scour", "glass", "gamer", "scrap", "money", "hinge", "album", "vouch", "asset", "tiara", "crept", "bayou", "atoll", "manor", "creak", "showy", "phase", "froth", "depth", "gloom", "flood", "trait", "girth", "piety", "goose", "float", "donor", "atone", "primo", "apron", "blown", "cacao", "loser", "input", "gloat", "awful", "brink", "smite", "beady", "rusty", "retro", "droll", "gawky", "hutch", "pinto", "egret", "lilac", "sever", "field", "fluff", "flack", "agape", "voice", "stead", "stalk", "berth", "madam", "night", "bland", "liver", "wedge", "augur", "roomy", "wacky", "flock", "angry", "trite", "aphid", "tryst", "midge", "power", "elope", "cinch", "motto", "stomp", "upset", "bluff", "cramp", "quart", "coyly", "youth", "rhyme", "buggy", "alien", "smear", "unfit", "patty", "cling", "glean", "label", "hunky", "khaki", "poker", "gruel", "twice", "twang", "shrug", "treat", "waste", "merit", "woven", "needy", "clown", "widow", "irony", "ruder", "gauze", "chief", "onset", "prize", "fungi", "charm", "gully", "inter", "whoop", "taunt", "leery", "class", "theme", "lofty", "tibia", "booze", "alpha", "thyme", "doubt", "parer", "chute", "stick", "trice", "alike", "recap", "saint", "glory", "grate", "admit", "brisk", "soggy", "usurp", "scald", "scorn", "leave", "twine", "sting", "bough", "marsh", "sloth", "dandy", "vigor", "howdy", "enjoy", "valid", "ionic", "equal", "floor", "catch", "spade", "stein", "exist", "quirk", "denim", "grove", "spiel", "mummy", "fault", "foggy", "flout", "carry", "sneak", "libel", "waltz", "aptly", "piney", "inept", "aloud", "photo", "dream", "stale", "unite", "snarl", "baker", "there", "glyph", "pooch", "hippy", "spell", "folly", "louse", "gulch", "vault", "godly", "threw", "fleet", "grave", "inane", "shock", "crave", "spite", "valve", "skimp", "claim", "rainy", "musty", "pique", "daddy", "quasi", "arise", "aging", "valet", "opium", "avert", "stuck", "recut", "mulch", "genre", "plume", "rifle", "count", "incur", "total", "wrest", "mocha", "deter", "study", "lover", "safer", "rivet", "funny", "smoke", "mound", "undue", "sedan", "pagan", "swine", "guile", "gusty", "equip", "tough", "canoe", "chaos", "covet", "human", "udder", "lunch", "blast", "stray", "manga", "melee", "lefty", "quick", "paste", "given", "octet", "risen", "groan", "leaky", "grind", "carve", "loose", "sadly", "spilt", "apple", "slack", "honey", "final", "sheen", "eerie", "minty", "slick", "derby", "wharf", "spelt", "coach", "erupt", "singe", "price", "spawn", "fairy", "jiffy", "filmy", "stack", "chose", "sleep", "ardor", "nanny", "niece", "woozy", "handy", "grace", "ditto", "stank", "cream", "usual", "diode", "valor", "angle", "ninja", "muddy", "chase", "reply", "prone", "spoil", "heart", "shade", "diner", "arson", "onion", "sleet", "dowel", "couch", "palsy", "bowel", "smile", "evoke", "creek", "lance", "eagle", "idiot", "siren", "built", "embed", "award", "dross", "annul", "goody", "frown", "patio", "laden", "humid", "elite", "lymph", "edify", "might", "reset", "visit", "gusto", "purse", "vapor", "crock", "write", "sunny", "loath", "chaff", "slide", "queer", "venom", "stamp", "sorry", "still", "acorn", "aping", "pushy", "tamer", "hater", "mania", "awoke", "brawn", "swift", "exile", "birch", "lucky", "freer", "risky", "ghost", "plier", "lunar", "winch", "snare", "nurse", "house", "borax", "nicer", "lurch", "exalt", "about", "savvy", "toxin", "tunic", "pried", "inlay", "chump", "lanky", "cress", "eater", "elude", "cycle", "kitty", "boule", "moron", "tenet", "place", "lobby", "plush", "vigil", "index", "blink", "clung", "qualm", "croup", "clink", "juicy", "stage", "decay", "nerve", "flier", "shaft", "crook", "clean", "china", "ridge", "vowel", "gnome", "snuck", "icing", "spiny", "rigor", "snail", "flown", "rabid", "prose", "thank", "poppy", "budge", "fiber", "moldy", "dowdy", "kneel", "track", "caddy", "quell", "dumpy", "paler", "swore", "rebar", "scuba", "splat", "flyer", "horny", "mason", "doing", "ozone", "amply", "molar", "ovary", "beset", "queue", "cliff", "magic", "truce", "sport", "fritz", "edict", "twirl", "verse", "llama", "eaten", "range", "whisk", "hovel", "rehab", "macaw", "sigma", "spout", "verve", "sushi", "dying", "fetid", "brain", "buddy", "thump", "scion", "candy", "chord", "basin", "march", "crowd", "arbor", "gayly", "musky", "stain", "dally", "bless", "bravo", "stung", "title", "ruler", "kiosk", "blond", "ennui", "layer", "fluid", "tatty", "score", "cutie", "zebra", "barge", "matey", "bluer", "aider", "shook", "river", "privy", "betel", "frisk", "bongo", "begun", "azure", "weave", "genie", "sound", "glove", "braid", "scope", "wryly", "rover", "assay", "ocean", "bloom", "irate", "later", "woken", "silky", "wreck", "dwelt", "slate", "smack", "solid", "amaze", "hazel", "wrist", "jolly", "globe", "flint", "rouse", "civil", "vista", "relax", "cover", "alive", "beech", "jetty", "bliss", "vocal", "often", "dolly", "eight", "joker", "since", "event", "ensue", "shunt", "diver", "poser", "worst", "sweep", "alley", "creed", "anime", "leafy", "bosom", "dunce", "stare", "pudgy", "waive", "choir", "stood", "spoke", "outgo", "delay", "bilge", "ideal", "clasp", "seize", "hotly", "laugh", "sieve", "block", "meant", "grape", "noose", "hardy", "shied", "drawl", "daisy", "putty", "strut", "burnt", "tulip", "crick", "idyll", "vixen", "furor", "geeky", "cough", "naive", "shoal", "stork", "bathe", "aunty", "check", "prime", "brass", "outer", "furry", "razor", "elect", "evict", "imply", "demur", "quota", "haven", "cavil", "swear", "crump", "dough", "gavel", "wagon", "salon", "nudge", "harem", "pitch", "sworn", "pupil", "excel", "stony", "cabin", "unzip", "queen", "trout", "polyp", "earth", "storm", "until", "taper", "enter", "child", "adopt", "minor", "fatty", "husky", "brave", "filet", "slime", "glint", "tread", "steal", "regal", "guest", "every", "murky", "share", "spore", "hoist", "buxom", "inner", "otter", "dimly", "level", "sumac", "donut", "stilt", "arena", "sheet", "scrub", "fancy", "slimy", "pearl", "silly", "porch", "dingo", "sepia", "amble", "shady", "bread", "friar", "reign", "dairy", "quill", "cross", "brood", "tuber", "shear", "posit", "blank", "villa", "shank", "piggy", "freak", "which", "among", "fecal", "shell", "would", "algae", "large", "rabbi", "agony", "amuse", "bushy", "copse", "swoon", "knife", "pouch", "ascot", "plane", "crown", "urban", "snide", "relay", "abide", "viola", "rajah", "straw", "dilly", "crash", "amass", "third", "trick", "tutor", "woody", "blurb", "grief", "disco", "where", "sassy", "beach", "sauna", "comic", "clued", "creep", "caste", "graze", "snuff", "frock", "gonad", "drunk", "prong", "lurid", "steel", "halve", "buyer", "vinyl", "utile", "smell", "adage", "worry", "tasty", "local", "trade", "finch", "ashen", "modal", "gaunt", "clove", "enact", "adorn", "roast", "speck", "sheik", "missy", "grunt", "snoop", "party", "touch", "mafia", "emcee", "array", "south", "vapid", "jelly", "skulk", "angst", "tubal", "lower", "crest", "sweat", "cyber", "adore", "tardy", "swami", "notch", "groom", "roach", "hitch", "young", "align", "ready", "frond", "strap", "puree", "realm", "venue", "swarm", "offer", "seven", "dryer", "diary", "dryly", "drank", "acrid", "heady", "theta", "junto", "pixie", "quoth", "bonus", "shalt", "penne", "amend", "datum", "build", "piano", "shelf", "lodge", "suing", "rearm", "coral", "ramen", "worth", "psalm", "infer", "overt",
                   "mayor", "ovoid", "glide", "usage", "poise", "randy", "chuck", "prank", "fishy", "tooth", "ether", "drove", "idler", "swath", "stint", "while", "begat", "apply", "slang", "tarot", "radar", "credo", "aware", "canon", "shift", "timer", "bylaw", "serum", "three", "steak", "iliac", "shirk", "blunt", "puppy", "penal", "joist", "bunny", "shape", "beget", "wheel", "adept", "stunt", "stole", "topaz", "chore", "fluke", "afoot", "bloat", "bully", "dense", "caper", "sneer", "boxer", "jumbo", "lunge", "space", "avail", "short", "slurp", "loyal", "flirt", "pizza", "conch", "tempo", "droop", "plate", "bible", "plunk", "afoul", "savoy", "steep", "agile", "stake", "dwell", "knave", "beard", "arose", "motif", "smash", "broil", "glare", "shove", "baggy", "mammy", "swamp", "along", "rugby", "wager", "quack", "squat", "snaky", "debit", "mange", "skate", "ninth", "joust", "tramp", "spurn", "medal", "micro", "rebel", "flank", "learn", "nadir", "maple", "comfy", "remit", "gruff", "ester", "least", "mogul", "fetch", "cause", "oaken", "aglow", "meaty", "gaffe", "shyly", "racer", "prowl", "thief", "stern", "poesy", "rocky", "tweet", "waist", "spire", "grope", "havoc", "patsy", "truly", "forty", "deity", "uncle", "swish", "giver", "preen", "bevel", "lemur", "draft", "slope", "annoy", "lingo", "bleak", "ditty", "curly", "cedar", "dirge", "grown", "horde", "drool", "shuck", "crypt", "cumin", "stock", "gravy", "locus", "wider", "breed", "quite", "chafe", "cache", "blimp", "deign", "fiend", "logic", "cheap", "elide", "rigid", "false", "renal", "pence", "rowdy", "shoot", "blaze", "envoy", "posse", "brief", "never", "abort", "mouse", "mucky", "sulky", "fiery", "media", "trunk", "yeast", "clear", "skunk", "scalp", "bitty", "cider", "koala", "duvet", "segue", "creme", "super", "grill", "after", "owner", "ember", "reach", "nobly", "empty", "speed", "gipsy", "recur", "smock", "dread", "merge", "burst", "kappa", "amity", "shaky", "hover", "carol", "snort", "synod", "faint", "haunt", "flour", "chair", "detox", "shrew", "tense", "plied", "quark", "burly", "novel", "waxen", "stoic", "jerky", "blitz", "beefy", "lyric", "hussy", "towel", "quilt", "below", "bingo", "wispy", "brash", "scone", "toast", "easel", "saucy", "value", "spice", "honor", "route", "sharp", "bawdy", "radii", "skull", "phony", "issue", "lager", "swell", "urine", "gassy", "trial", "flora", "upper", "latch", "wight", "brick", "retry", "holly", "decal", "grass", "shack", "dogma", "mover", "defer", "sober", "optic", "crier", "vying", "nomad", "flute", "hippo", "shark", "drier", "obese", "bugle", "tawny", "chalk", "feast", "ruddy", "pedal", "scarf", "cruel", "bleat", "tidal", "slush", "semen", "windy", "dusty", "sally", "igloo", "nerdy", "jewel", "shone", "whale", "hymen", "abuse", "fugue", "elbow", "crumb", "pansy", "welsh", "syrup", "terse", "suave", "gamut", "swung", "drake", "freed", "afire", "shirt", "grout", "oddly", "tithe", "plaid", "dummy", "broom", "blind", "torch", "enemy", "again", "tying", "pesky", "alter", "gazer", "noble", "ethos", "bride", "extol", "decor", "hobby", "beast", "idiom", "utter", "these", "sixth", "alarm", "erase", "elegy", "spunk", "piper", "scaly", "scold", "hefty", "chick", "sooty", "canal", "whiny", "slash", "quake", "joint", "swept", "prude", "heavy", "wield", "femme", "lasso", "maize", "shale", "screw", "spree", "smoky", "whiff", "scent", "glade", "spent", "prism", "stoke", "riper", "orbit", "cocoa", "guilt", "humus", "shush", "table", "smirk", "wrong", "noisy", "alert", "shiny", "elate", "resin", "whole", "hunch", "pixel", "polar", "hotel", "sword", "cleat", "mango", "rumba", "puffy", "filly", "billy", "leash", "clout", "dance", "ovate", "facet", "chili", "paint", "liner", "curio", "salty", "audio", "snake", "fable", "cloak", "navel", "spurt", "pesto", "balmy", "flash", "unwed", "early", "churn", "weedy", "stump", "lease", "witty", "wimpy", "spoof", "saner", "blend", "salsa", "thick", "warty", "manic", "blare", "squib", "spoon", "probe", "crepe", "knack", "force", "debut", "order", "haste", "teeth", "agent", "widen", "icily", "slice", "ingot", "clash", "juror", "blood", "abode", "throw", "unity", "pivot", "slept", "troop", "spare", "sewer", "parse", "morph", "cacti", "tacky", "spool", "demon", "moody", "annex", "begin", "fuzzy", "patch", "water", "lumpy", "admin", "omega", "limit", "tabby", "macho", "aisle", "skiff", "basis", "plank", "verge", "botch", "crawl", "lousy", "slain", "cubic", "raise", "wrack", "guide", "foist", "cameo", "under", "actor", "revue", "fraud", "harpy", "scoop", "climb", "refer", "olden", "clerk", "debar", "tally", "ethic", "cairn", "tulle", "ghoul", "hilly", "crude", "apart", "scale", "older", "plain", "sperm", "briny", "abbot", "rerun", "quest", "crisp", "bound", "befit", "drawn", "suite", "itchy", "cheer", "bagel", "guess", "broad", "axiom", "chard", "caput", "leant", "harsh", "curse", "proud", "swing", "opine", "taste", "lupus", "gumbo", "miner", "green", "chasm", "lipid", "topic", "armor", "brush", "crane", "mural", "abled", "habit", "bossy", "maker", "dusky", "dizzy", "lithe", "brook", "jazzy", "fifty", "sense", "giant", "surly", "legal", "fatal", "flunk", "began", "prune", "small", "slant", "scoff", "torus", "ninny", "covey", "viper", "taken", "moral", "vogue", "owing", "token", "entry", "booth", "voter", "chide", "elfin", "ebony", "neigh", "minim", "melon", "kneed", "decoy", "voila", "ankle", "arrow", "mushy", "tribe", "cease", "eager", "birth", "graph", "odder", "terra", "weird", "tried", "clack", "color", "rough", "weigh", "uncut", "ladle", "strip", "craft", "minus", "dicey", "titan", "lucid", "vicar", "dress", "ditch", "gypsy", "pasta", "taffy", "flame", "swoop", "aloof", "sight", "broke", "teary", "chart", "sixty", "wordy", "sheer", "leper", "nosey", "bulge", "savor", "clamp", "funky", "foamy", "toxic", "brand", "plumb", "dingy", "butte", "drill", "tripe", "bicep", "tenor", "krill", "worse", "drama", "hyena", "think", "ratio", "cobra", "basil", "scrum", "bused", "phone", "court", "camel", "proof", "heard", "angel", "petal", "pouty", "throb", "maybe", "fetal", "sprig", "spine", "shout", "cadet", "macro", "dodgy", "satyr", "rarer", "binge", "trend", "nutty", "leapt", "amiss", "split", "myrrh", "width", "sonar", "tower", "baron", "fever", "waver", "spark", "belie", "sloop", "expel", "smote", "baler", "above", "north", "wafer", "scant", "frill", "awash", "snack", "scowl", "frail", "drift", "limbo", "fence", "motel", "ounce", "wreak", "revel", "talon", "prior", "knelt", "cello", "flake", "debug", "anode", "crime", "salve", "scout", "imbue", "pinky", "stave", "vague", "chock", "fight", "video", "stone", "teach", "cleft", "frost", "prawn", "booty", "twist", "apnea", "stiff", "plaza", "ledge", "tweak", "board", "grant", "medic", "bacon", "cable", "brawl", "slunk", "raspy", "forum", "drone", "women", "mucus", "boast", "toddy", "coven", "tumor", "truer", "wrath", "stall", "steam", "axial", "purer", "daily", "trail", "niche", "mealy", "juice", "nylon", "plump", "merry", "flail", "papal", "wheat", "berry", "cower", "erect", "brute", "leggy", "snipe", "sinew", "skier", "penny", "jumpy", "rally", "umbra", "scary", "modem", "gross", "avian", "greed", "satin", "tonic", "parka", "sniff", "livid", "stark", "trump", "giddy", "reuse", "taboo", "avoid", "quote", "devil", "liken", "gloss", "gayer", "beret", "noise", "gland", "dealt", "sling", "rumor", "opera", "thigh", "tonga", "flare", "wound", "white", "bulky", "etude", "horse", "circa", "paddy", "inbox", "fizzy", "grain", "exert", "surge", "gleam", "belle", "salvo", "crush", "fruit", "sappy", "taker", "tract", "ovine", "spiky", "frank", "reedy", "filth", "spasm", "heave", "mambo", "right", "clank", "trust", "lumen", "borne", "spook", "sauce", "amber", "lathe", "carat", "corer", "dirty", "slyly", "affix", "alloy", "taint", "sheep", "kinky", "wooly", "mauve", "flung", "yacht", "fried", "quail", "brunt", "grimy", "curvy", "cagey", "rinse", "deuce", "state", "grasp", "milky", "bison", "graft", "sandy", "baste", "flask", "hedge", "girly", "swash", "boney", "coupe", "endow", "abhor", "welch", "blade", "tight", "geese", "miser", "mirth", "cloud", "cabal", "leech", "close", "tenth", "pecan", "droit", "grail", "clone", "guise", "ralph", "tango", "biddy", "smith", "mower", "payee", "serif", "drape", "fifth", "spank", "glaze", "allot", "truck", "kayak", "virus", "testy", "tepee", "fully", "zonal", "metro", "curry", "grand", "banjo", "axion", "bezel", "occur", "chain", "nasal", "gooey", "filer", "brace", "allay", "pubic", "raven", "plead", "gnash", "flaky", "munch", "dully", "eking", "thing", "slink", "hurry", "theft", "shorn", "pygmy", "ranch", "wring", "lemon", "shore", "mamma", "froze", "newer", "style", "moose", "antic", "drown", "vegan", "chess", "guppy", "union", "lever", "lorry", "image", "cabby", "druid", "exact", "truth", "dopey", "spear", "cried", "chime", "crony", "stunk", "timid", "batch", "gauge", "rotor", "crack", "curve", "latte", "witch", "bunch", "repel", "anvil", "soapy", "meter", "broth", "madly", "dried", "scene", "known", "magma", "roost", "woman", "thong", "punch", "pasty", "downy", "knead", "whirl", "rapid", "clang", "anger", "drive", "goofy", "email", "music", "stuff", "bleep", "rider", "mecca", "folio", "setup", "verso", "quash", "fauna", "gummy", "happy", "newly", "fussy", "relic", "guava", "ratty", "fudge", "femur", "chirp", "forte", "alibi", "whine", "petty", "golly", "plait", "fleck", "felon", "gourd", "brown", "thrum", "ficus", "stash", "decry", "wiser", "junta", "visor", "daunt", "scree", "impel", "await", "press", "whose", "turbo", "stoop", "speak", "mangy", "eying", "inlet", "crone", "pulse", "mossy", "staid", "hence", "pinch", "teddy", "sully", "snore", "ripen", "snowy", "attic", "going", "leach", "mouth", "hound", "clump", "tonal", "bigot", "peril", "piece", "blame", "haute", "spied", "undid", "intro", "basal", "shine", "gecko", "rodeo", "guard", "steer", "loamy", "scamp", "scram", "manly", "hello", "vaunt", "organ", "feral", "knock", "extra", "condo", "adapt", "willy", "polka", "rayon", "skirt", "faith", "torso", "match", "mercy", "tepid", "sleek", "riser", "twixt", "peace", "flush", "catty", "login", "eject", "roger", "rival", "untie", "refit", "aorta", "adult", "judge", "rower", "artsy", "rural", "shave", "bobby", "eclat", "fella", "gaily", "harry", "hasty", "hydro", "liege", "octal", "ombre", "payer", "sooth", "unset", "unlit", "vomit", "fanny"]

filtPosAns = possibleAnswers

dotJoin = '\n'

filename = 'Main-Files/weighted_records.csv'

fields = []
rows = []


fl = 0
flWeight = 1
ll = 2
llWeight = 3
cl = 4
clWeight = 5

incorrectPos = []


with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

inputedAns = 'salet'
inputedOut = ''

knownLetPos = '-----'
letInWord = []
letNotInWord = []

noSecChar = []
noSecCharPos = []

topPicks = []


def removeWord(word):
    global filtPosAns
    filtPosAns = [sub.replace(word, '-', 1) for sub in filtPosAns]


def getProbability(posAns):
    global topPicks
    global knownLetPos
    global letInWord
    global letNotInWord
    global rows
    global fl
    global flWeight
    global ll
    global llWeight
    global cl
    global clWeight

    ansWeights = []
    ansAndWeights = []

    simpleRows = []

    notAllowed = ['\'', '[', ']']

    for row in rows:
        for row1 in row:
            simpleRow = ''
            for x in row1:
                if x not in notAllowed:
                    simpleRow = simpleRow + x

            simpleRows.append(simpleRow)

    for word in posAns:

        wordFl = word[0:1]
        wordLl = word[4:5]
        wordCls = []
        for x in range(len(word)):
            if len(word[x: x+2]) == 2:
                wordCls.append(word[x: x+2])

        wordWeight = 0.0
        for line in simpleRows:
            if line[0:1] == wordFl:
                wordWeight += float(line[3: 9])
            if line[11: 12] == wordLl:
                wordWeight += float(line[14: 20])
            for x in range(len(word)):
                if len(word[x: x+2]) == 2:
                    if line[22: 24] == word[x: x+2]:
                        wordWeight += float(line[26: 32])

        tempWordLets = []
        for char in word:
            if char in tempWordLets:
                wordWeight = wordWeight * 0.25
            else:
                tempWordLets.append(char)

        wordWeight = round(wordWeight, 8)
        ansWeights.append(wordWeight)
        ansAndWeights.append(f'{word} - {wordWeight}')
        ansWeights.sort(reverse=True)

    topPicks = []
    if len(posAns) >= 5:
        for i in range(5):
            for word in posAns:
                if f'{word} - {ansWeights[i]}' in ansAndWeights:
                    topPicks.append(f'{word}: {ansWeights[i]}')
    elif len(posAns) <= 4:
        for i in range(len(posAns)):
            for word in posAns:
                if f'{word} - {ansWeights[i]}' in ansAndWeights:
                    topPicks.append(f'{word}: {ansWeights[i]}')

    if len(topPicks) > 3:
        while len(topPicks) > 3:
            topPicks.pop(len(topPicks)-1)
    return topPicks[0][0: 5]


def filterPossibleGuesses(knownPos, correctLet, incorrectSub, notIn, noSec, noSecPos):
    global filtPosAns
    filtPosAns = list(filter(('-').__ne__, filtPosAns))
    index = 0
    for char in knownPos:
        if char != '-':
            # checking every word

            for word in filtPosAns:
                # checking the specified words index of the known letter
                if word[index: index+1] != char:
                    removeWord(word)

        index += 1

    for word in filtPosAns:
        # checking for characters that ARE in the word
        index1 = 0
        for x in correctLet:
            if x not in word or x in word and word[incorrectSub[index1]: incorrectSub[index1]+1] == x:

                removeWord(word)

            index1 += 1
        # checking for douplicate characters
        word1 = ''
        for x in noSec:
            for char in word:
                if char == x and char in word1:
                    removeWord(word)
                    break
                else:
                    word1 = word1 + char

        # checking for characters that ARENT in the word

        for x in notIn:
            if x in word:
                removeWord(word)

    filtPosAns = list(filter(('-').__ne__, filtPosAns))
    return filtPosAns


def resetProg():
    global colorIndex
    global dispLetterList
    global colorsList
    global inputedAns
    global knownLetPos
    global letInWord
    global letNotInWord
    global incorrectPos
    global noSecChar
    global noSecCharPos
    global filtPosAns

    filtPosAns = possibleAnswers

    colorIndex = 0
    dispLetterList = ['s', 'a', 'l', 'e', 't']
    colorsList = ['#202020', '#202020', '#202020', '#202020', '#202020']

    inputedAns = 'salet'
    knownLetPos = '-----'
    letInWord = []
    letNotInWord = []
    incorrectPos = []
    noSecChar = []
    noSecCharPos = []


def getNextGuess(ans, out):

    global inputedAns
    global knownLetPos
    global letInWord
    global letNotInWord
    global incorrectPos
    global noSecChar
    global noSecCharPos
    if out == 'END' or out == 'end' or out == 'ggggg':
        resetProg()
        return

    global rows

    posList = []

    for i in knownLetPos:
        posList.append(i)

    sub = 0
    for char in out:
        if char == 'g':
            posList[sub] = ans[sub: sub+1]
        else:
            posList[sub] = '-'

        if char == 'y':
            letInWord.append(ans[sub: sub+1])
            incorrectPos.append(sub)
        elif char == 'b':
            if ans[sub: sub+1] in letInWord:
                noSecChar.append(ans[sub: sub+1])
                noSecCharPos.append(sub)
            else:
                letNotInWord.append(ans[sub: sub+1])
        sub += 1
    knownLetPos = ''
    for i in range(len(posList)):
        knownLetPos = knownLetPos + posList[i]

    print(
        f'Known letter possitions: {knownLetPos}')

    filtPosAns = filterPossibleGuesses(
        knownLetPos, letInWord, incorrectPos, letNotInWord, noSecChar, noSecCharPos)
    inputedAns = getProbability(filtPosAns)


colorIndex = 0
dispLetterList = ['s', 'a', 'l', 'e', 't']
colorsList = ['#202020', '#202020', '#202020', '#202020', '#202020']

window = Tk()

window.geometry('600x450')
window.title('Wordle Algorithm')
window.config(bg="black")
window.resizable(False, False)


def updateLetters():
    global letterLbl1
    global letterLbl2
    global letterLbl3
    global letterLbl4
    global letterLbl5

    letterLbl1.config(text=dispLetterList[0])
    letterLbl2.config(text=dispLetterList[1])
    letterLbl3.config(text=dispLetterList[2])
    letterLbl4.config(text=dispLetterList[3])
    letterLbl5.config(text=dispLetterList[4])

    letterLbl1.config(bg=colorsList[0])
    letterLbl2.config(bg=colorsList[1])
    letterLbl3.config(bg=colorsList[2])
    letterLbl4.config(bg=colorsList[3])
    letterLbl5.config(bg=colorsList[4])


def setGray():
    global colorIndex
    if colorIndex >= 4:
        startAlgorithmBtn.place(x=243, y=350)
    colorsList[colorIndex] = '#828282'
    updateLetters()
    colorIndex += 1


def setYellow():
    global colorIndex
    if colorIndex >= 4:
        startAlgorithmBtn.place(x=243, y=350)
    colorsList[colorIndex] = 'yellow'
    updateLetters()
    colorIndex += 1


def setGreen():
    global colorIndex
    if colorIndex >= 4:
        startAlgorithmBtn.place(x=243, y=350)
    colorsList[colorIndex] = 'green'
    updateLetters()
    colorIndex += 1


def newWord():
    print('test')
    newWord = newWordEntry.get()
    if(len(newWord) != 5):
        newWordConfirm.config(text='invalid')
        return
    dispLetterList = []
    for i in newWord:
        dispLetterList.append(i)
    updateLetters()


def startAlgo():
    global inputedAns
    global inputedOut
    global dispLetterList
    global colorsList
    global colorIndex

    inputedOut = ''

    inputedAns = ''.join(dispLetterList)
    for color in colorsList:
        if color == '#828282':
            inputedOut = inputedOut + 'b'
        elif color == 'yellow':
            inputedOut = inputedOut + 'y'
        elif color == 'green':
            inputedOut = inputedOut + 'g'

    getNextGuess(inputedAns, inputedOut)

    dispLetterList = []
    for char in inputedAns:
        dispLetterList.append(char)

    colorsList = ['#202020', '#202020', '#202020', '#202020', '#202020']
    colorIndex = 0

    updateLetters()
    topPicksLbl.config(text='Top Picks:\n'+'\n'.join(topPicks))


newWordConfirm = Button(window,
                        text='Enter',
                        bg='#202020',
                        fg='#cacaca',
                        justify='center',
                        command=newWord)


newWordEntry = Entry(window,
                     font=('Arial', 12, 'bold'),
                     bg='#202020',
                     fg='#cacaca',
                     justify='center')
newWordEntry.pack_forget()

wordLblBorder = Frame(window, bg='#cacaca')
enterWordLbl = Label(wordLblBorder,
                     text='Wordle Algorithm',
                     font=('Arial', 24, 'bold'),
                     bg='black',
                     fg='#cacaca',
                     bd=0)
enterWordLbl.pack(padx=2, pady=2)
wordLblBorder.pack(padx=0, pady=5)

letterBorder1 = Frame(window,
                      bg='#5f5f5f',
                      width=2)
letterLbl1 = Label(letterBorder1,
                   text=dispLetterList[0],
                   width=2,
                   bg=colorsList[0],
                   font=('Arial', 50),
                   fg='#cacaca',
                   justify='center')
letterLbl1.pack(padx=2, pady=2)
letterBorder1.place(x=57, y=75)

letterBorder2 = Frame(window,
                      bg='#5f5f5f',
                      width=2)
letterLbl2 = Label(letterBorder2,
                   text=dispLetterList[1],
                   width=2,
                   bg=colorsList[1],
                   font=('Arial', 50),
                   fg='#cacaca',
                   justify='center')
letterLbl2.pack(padx=2, pady=2)
letterBorder2.place(x=157, y=75)

letterBorder3 = Frame(window,
                      bg='#5f5f5f',
                      width=2)
letterLbl3 = Label(letterBorder3,
                   text=dispLetterList[2],
                   width=2,
                   bg=colorsList[2],
                   font=('Arial', 50),
                   fg='#cacaca',
                   justify='center')
letterLbl3.pack(padx=2, pady=2)
letterBorder3.place(x=257, y=75)

letterBorder4 = Frame(window,
                      bg='#5f5f5f',
                      width=2)
letterLbl4 = Label(letterBorder4,
                   text=dispLetterList[3],
                   width=2,
                   bg=colorsList[3],
                   font=('Arial', 50),
                   fg='#cacaca',
                   justify='center')
letterLbl4.pack(padx=2, pady=2)
letterBorder4.place(x=357, y=75)

letterBorder5 = Frame(window,
                      bg='#5f5f5f',
                      width=2)
letterLbl5 = Label(letterBorder5,
                   text=dispLetterList[4],
                   width=2,
                   bg=colorsList[4],
                   font=('Arial', 50),
                   fg='#cacaca',
                   justify='center')
letterLbl5.pack(padx=2, pady=2)
letterBorder5.place(x=457, y=75)

grayBtn = Button(window,
                 font=('Arial', 25),
                 text='Gray',
                 bg='#828282',
                 fg='#cacaca',
                 justify="center",
                 command=setGray)

yellowBtn = Button(window,
                   font=('Arial', 25),
                   text='Yellow',
                   bg='yellow',
                   fg='#cacaca',
                   justify="center",
                   command=setYellow)

greenBtn = Button(window,
                  font=('Arial', 25),
                  text='Green',
                  bg='green',
                  fg='#cacaca',
                  justify="center",
                  command=setGreen)

startAlgorithmBtn = Button(window,
                           font=('Arial', 15),
                           text='Get Guess',
                           bg='#202020',
                           fg='#cacaca',
                           justify='center',
                           command=startAlgo)

topPicksFrame = Frame(window,
                      bg='#5f5f5f',
                      width=2)
topPicksLbl = Label(topPicksFrame,
                    font=('Arial', 12),
                    bg='#000000',
                    fg='#cacaca',
                    justify='left',
                    text='Top Picks:\n'+',    '.join(topPicks))

topPicksFrame.place(x=57, y=350)
topPicksLbl.pack(padx=2, pady=2)

grayBtn.place(x=57, y=250)
yellowBtn.place(x=240, y=250)
greenBtn.place(x=428, y=250)

newWordEntry.place(x=208, y=175)
newWordConfirm.place(x=280, y=210)

window.mainloop()

guessNum = 0
