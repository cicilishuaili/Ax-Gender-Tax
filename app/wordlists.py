# These words should be written as the stem to make it easier to match all variants.
# In other words, the suffix should be intentionally left out.

feminine_coded_words = [
    'feminine', 'beauty', 'floral', 'moisturizers', 'beautiful',
       'trust', 'different', 'match', 'soybean', 'summer', 'incredible',
       'delicate', 'rose', 'soft', 'powder', 'jasmine', 'shaving',
       'conditions', 'magazines', 'needed', 'feels', 'starts',
       'three', 'conditioners', 'favorite', 'moisture', 'additional',
       'discomfort', 'days', 'capsules', 'among', 'controls', 'tested',
       'brand', 'organic', 'soothing', 'fun', 'botanical', 'activity',
       'everyday', 'lady', 'flower', 'unstoppable', 'liquid', 'coverage',
       'create', 'compact', 'toxins', 'type', 'enough',
       'microcrystalline', 'protecting', 'stress', 'smooth', 'shake',
       'gluten', 'anyone', 'little', 'breeze', 'making', 'area',
       'hypoallergenic', 'bring', 'better', 'next', 'pink', 'sold',
       'immediately', 'ricinoleate', 'antioxidant', 'carry', 'heavenly',
       'inviting', 'absorbs', 'light', 'matter', 'extracts',
       'description', 'wide', 'splash', 'cruelty', 'purse', 'essentials',
       'aubrey', 'organics', 'ultra', 'wax', 'gentle', 'suave',
       'certified', 'express', 'calendula', 'soften', 'less', 'tender',
       'intended', 'absorb', 'lavender', 'elegant', 'enjoy', 'products',
       'remove', 'aloe', 'bottle', 'contain', 'lovely', 'gently', 'treat',
       'fda', 'delicately', 'synthetic', 'showering', 'sensitive',
       'designer', 'sensual', 'imposters', 'allowing', 'irritated',
       'benefits', 'infused', 'leaf', 'vera', 'roll', 'mineral',
       'essential', 'inspired', 'tried', 'dermatologically', 'work',
       'causing', 'scented', 'held', 'environmentally', 'breast', 'pg',
       'continuous', 'pineapple', 'ease', 'disclaimer', 'statements',
       'cure', 'purified', 'clinical', 'evaluated', 'diagnose', 'visibly',
       'salts', 'en', 'luxurious', 'deodorizing', 'soothes', 'exotic',
       'chemicals', 'prescription', 'prevent', 'fire', 'shower', 'bright',
       'full', 'friends', 'strong', 'neutralize', 'require', 'gardens',
       'seeking', 'arnica', 'alternative', 'watery', 'breathing', 'areas',
       'research', 'color', 'freshening'
]

masculine_coded_words = [
    'spice', 'old', 'guard', 'masculine', 'defense', 'endurance',
       'phoenix', 'axe', 'energized', 'machine', 'climb', 'moisturizer',
       'zone', 'tough', 'put', 'rush', 'freedom', 'apollo', 'sports',
       'armpit', 'answer', 'wash', 'enduring', 'system', 'precision',
       'adventure', 'bodyspray', 'sport', 'magic', 'places', 'energizing',
       'anywhere', 'neck', 'legendary', 'hint', 'wood', 'fiji',
       'irresistible', 'resistant', 'transparent', 'stronger', 'game',
       'got', 'cannot', 'blast', 'high', 'chest', 'cologne', 'seal',
       'lime', 'conditioner', 'fully', 'caught', 'guy', 'freshest',
       'effect', 'transforms', 'song', 'comfort', 'experience', 'arctic',
       'reveal', 'anytime', 'mennen', 'pretty', 'revolutionary', 'whole',
       'taking', 'containing', 'irritant', 'unilever', 'complex', 'chill',
       'spicy', 'rugged', 'come', 'subtle', 'stands', 'seduce', 'warning',
       'dryness', 'blocking', 'focused', 'onto', 'towards', 'brut',
       'together', 'ladies', 'specifically', 'brings', 'sophisticated',
       'anarchy', 'woods', 'slowly', 'sleeves', 'rosemary', 'team',
       'push', 'demands', 'whisper', 'visible', 'excessive', 'bar', 'top',
       'refresh', 'condition', 'tree', 'continue', 'total', 'moments',
       'imagine', 'arm', 'mint', 'open', 'stains', 'ahead', 'bergamot',
       'dark', 'collection', 'base', 'dynamic', 'reborn', 'combusts',
       'refined', 'perspirants', 'enticing', 'herban', 'bird', 'elements',
       'ashes', 'named', 'many', 'promote', 'cowboy', 'definitely',
       'maranta', 'adidas', 'deep', 'expose', 'highest', 'vary',
       'smoking', 'red', 'smell', 'gets', 'line', 'trimax', 'glide',
       'visit', 'shield', 'rich', 'covered', 'range', 'world', 'essence',
       'power', 'fresher', 'information', 'selection', 'mythical',
       'woody', 'casual', 'vetiver', 'woodsy', 'working', 'embrace',
       'toll', 'grow', 'routine', 'centers', 'part', 'oxygen', 'company',
       'practically', 'concern', 'end', 'deliver', 'field', 'soap',
       'situations', 'eco', 'masculinity', 'cedar', 'musky', 'wait',
       'good', 'blue', 'accept', 'ocean', 'applicator', 'realize',
       'includes', 'cool', 'stain', 'turn', 'complete', 'blocks', 'case',
       'ensure', 'powerful', 'performance', 'hot', 'plants',
       'crafted', 'endorsed', 'compromise', 'shine', 'capric', 'simply',
       'style', 'house', 'like', 'musk', 'ever', 'green', 'could',
       'providing', 'stink', 'protective', 'breakthrough', 'geranium',
       'aromas', 'released'
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
