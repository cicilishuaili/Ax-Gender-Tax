# These words are written as the stem to make it easier to match all variants.
# In other words, the suffix is intentionally left out.

feminine_coded_words = [
    "agree",
    "affectionate",
    "child",
    "cheer",
    "collab",
    "commit",
    "communal",
    "compassion",
    "connect",
    "considerate",
    "cooperat",
    "co-operat",
    "depend",
    "emotiona",
    "empath",
    "feel",
    "flatterable",
    "gentle",
    "honest",
    "interpersonal",
    "interdependen",
    "interpersona",
    "inter-personal",
    "inter-dependen",
    "inter-persona",
    "kind",
    "kinship",
    "loyal",
    "modesty",
    "nag",
    "nurtur",
    "pleasant",
    "polite",
    "quiet",
    "respon",
    "sensitiv",
    "submissive",
    "support",
    "sympath",
    "tender",
    "together",
    "trust",
    "understand",
    "warm",
    "whin",
    "enthusias",
    "inclusive",
    "yield",
    "shar"
]

masculine_coded_words = [
    "active",
    "adventurous",
    "aggress",
    "ambitio",
    "analy",
    "assert",
    "athlet",
    "autonom",
    "battle",
    "boast",
    "challeng",
    "champion",
    "compet",
    "confident",
    "courag",
    "decid",
    "decision",
    "decisive",
    "defend",
    "determin",
    "domina",
    "dominant",
    "driven",
    "fearless",
    "fight",
    "force",
    "greedy",
    "head-strong",
    "headstrong",
    "hierarch",
    "hostil",
    "impulsive",
    "independen",
    "individual",
    "intellect",
    "lead",
    "logic",
    "objective",
    "opinion",
    "outspoken",
    "persist",
    "principle",
    "reckless",
    "self-confiden",
    "self-relian",
    "self-sufficien",
    "selfconfiden",
    "selfrelian",
    "selfsufficien",
    "stubborn",
    "superior",
    "unreasonab"
]

hyphenated_coded_words = [
    "co-operat",
    "inter-personal",
    "inter-dependen",
    "inter-persona",
    "self-confiden",
    "self-relian",
    "self-sufficien"
]

possible_codings = (
    "strongly feminine-coded",
    "feminine-coded",
    "neutral",
    "masculine-coded",
    "strongly masculine-coded"
)

explanations = {
    "feminine-coded": ("This description uses more words that "
                        "are skewed feminine than words that are "
                        "skewed masculine."),
    "masculine-coded": ("This description uses more words that "
                        "skew masculine than words that are "
                        "skew feminine."),
    "strongly feminine-coded": ("This description uses more words that "
                        "are skewed feminine than words that are "
                        "skewed as masculine."),
    "strongly masculine-coded": ("This job ad uses more words that "
                        "are skewed masculine than words that"
                        "skew feminine."),
    "empty": ("This description doesn't use any words "
              "that are skewed masculine or feminine."),
    "neutral": ("This description uses an equal number "
              "of words that are skewed masculine and feminine.")
}
