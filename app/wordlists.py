# These words should be written as the stem to make it easier to match all variants.
# In other words, the suffix should be intentionally left out.

feminine_coded_words = [
    'feminine', 'beauty', 'floral', 'beautiful', 'moisturizers',
       'trust', 'different', 'match', 'soybean', 'summer', 'incredible',
       'delicate', 'soft', 'rose', 'powder', 'jasmine', 'shaving',
       'conditions', 'needed', 'magazines', 'feels', 'p', 'starts',
       'conditioners', 'three', 'favorite', 'moisture', 'additional',
       'discomfort', 'days', 'capsules', 'among', 'controls', 'tested',
       'brand', 'organic', 'soothing', 'activity', 'fun', 'botanical',
       'alcoholuses', 'everyday', 'lady', 'flower'
]

masculine_coded_words = [
    'spice', 'old', 'guard', 'masculine', 'defense', 'endurance',
       'phoenix', 'axe', 'energized', 'machine', 'climb', 'moisturizer',
       'zone', 'tough', 'put', 'rush', 'freedom', 'apollo', 'sports',
       'armpit', 'answer', 'wash', 'adventure', 'enduring', 'precision',
       'system', 'bodyspray', 'sport', 'magic', 'places', 'energizing',
       'neck', 'hint', 'anywhere', 'legendary', 'wood', 'transparent',
       'stronger', 'resistant', 'irresistible', 'fiji', '17', 'game',
       'cannot', 'got', 'blast', 'high', 'cologne', 'seal', 'chest',
       'conditioner', 'lime', 'cl', 'fully', 'freshest', 'caught'
]

hyphenated_coded_words = [
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
