from BaseClasses import ItemClassification

ITEMS_DATA = {
    #   "No Item": {
    #   'classification': ItemClassification.filler,
    #   "",
    #    'id': 0x00,
    #    'subid': 0x00
    #    },
    "Progressive Shield": {
        'classification': ItemClassification.progression,
        'id': 0x01,
        'foggy_hints': ['a board', 'scrap wood'],
        'clear_hint': 'a Shield'
    },
    "Bombs (10)": {
        'classification': ItemClassification.progression,
        'id': 0x03,
        'foggy_hints': ['some explosives'],
        'clear_hint': 'ten Bombs'
    },
    "Progressive Sword": {
        'classification': ItemClassification.progression,
        'id': 0x05,
        'foggy_hints': ['an ouch stick'],
        'clear_hint': 'a Sword'
    },
    "Progressive Boomerang": {
        'classification': ItemClassification.progression,
        'id': 0x06,
        'foggy_hints': ['a returning weapon', 'a stun stick'],
        'clear_hint': 'a Boomerang'
    },
    "Rod of Seasons (Spring)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x02,
        'foggy_hints': ['a way to call flowers', 'a way to cause flooding', "a green fairy's reward"],
        'clear_hint': 'the Rod of Spring'
    },
    "Rod of Seasons (Summer)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x03,
        'foggy_hints': ['a way to call vines', 'a way to dry lakes', "a red fairy's reward"],
        'clear_hint': 'the Rod of Summer'
    },
    "Rod of Seasons (Autumn)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x04,
        'foggy_hints': ['a way to clear mushrooms', 'a way to walk on pits', "an orange fairy's reward"],
        'clear_hint': 'the Rod of Autumn'
    },
    "Rod of Seasons (Winter)": {
        'classification': ItemClassification.progression,
        'id': 0x07,
        'subid': 0x05,
        'foggy_hints': ['a way to create snow', 'the way to become Santa', "a blue fairy's reward"],
        'clear_hint': 'the Rod of Winter'
    },
    "Magnetic Gloves": {
        'classification': ItemClassification.progression,
        'id': 0x08,
        'foggy_hints': ['the pole puller'],
        'clear_hint': 'the Magnetic Gloves'
    },
    "Biggoron's Sword": {
        'classification': ItemClassification.progression,
        'id': 0x0c,
        'foggy_hints': ['a big ouch stick'],
        'clear_hint': "Biggoron's Sword"
    },
    # "Bombchus (10)": {
    #     'classification': ItemClassification.progression,
    #     'id': 0x0d,
    #     'foggy_hints': ['a living explosive'],
    #     'clear_hint': 'ten Bombchus'
    # },
    "Ricky's Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e,
        'subid': 0x00,
        'foggy_hints': ['a friendly kangaroo', 'a friendly boxer', 'a friendly hopper'],
        'clear_hint': "Ricky's Flute"
    },
    "Dimitri's Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e,
        'subid': 0x01,
        'foggy_hints': ['a friendly lizard', 'a red fish', 'a waterfall a-fish-ionado'],
        'clear_hint': "Dimitri's Flute"
    },
    "Moosh's Flute": {
        'classification': ItemClassification.progression,
        'id': 0x0e,
        'subid': 0x02,
        'foggy_hints': ['a friendly bear', 'a hungry bear', 'a friendly pit leaper', 'a hydrophobic friend'],
        'clear_hint': "Moosh's Flute"
    },
    "Progressive Slingshot": {
        'classification': ItemClassification.progression,
        'id': 0x13,
        'foggy_hints': ["a child's weapon", 'a ranged weapon'],
        'clear_hint': "a Slingshot"
    },
    "Shovel": {
        'classification': ItemClassification.progression,
        'id': 0x15,
        'foggy_hints': ['snow removal', 'a treasure finder'],
        'clear_hint': 'a Shovel'
    },
    "Power Bracelet": {
        'classification': ItemClassification.progression,
        'id': 0x16,
        'foggy_hints': ['a croissant', 'strength'],
        'clear_hint': 'the Power Bracelet'
    },
    "Progressive Feather": {
        'classification': ItemClassification.progression,
        'id': 0x17,
        'foggy_hints': [],
        'clear_hint': 'a Feather'
    },
    "Seed Satchel": {
        'classification': ItemClassification.progression,
        'id': 0x19,
        'foggy_hints': ['a versatile bag'],
        'clear_hint': 'a Seed Satchel'
    },
    "Fool's Ore": {
        'classification': ItemClassification.progression,
        'id': 0x1e,
        'foggy_hints': ['the best weapon', 'a rock'],
        'clear_hint': "the Fool's Ore"
    },
    "Ember Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x20,
        'foggy_hints': ['a spicy snack'],
        'clear_hint': 'Ember Seeds'
    },
    "Scent Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x21,
        'foggy_hints': ['an enticing seed'],
        'clear_hint': 'Scent Seeds'
    },
    "Pegasus Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x22,
        'foggy_hints': ['a noble steed', 'replacement boots'],
        'clear_hint': 'Pegasus Seeds'
    },
    "Gale Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x23,
        'foggy_hints': ['a flight method', 'the Song of Soaring'],
        'clear_hint': 'Gale Seeds'
    },
    "Mystery Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x24,
        'foggy_hints': ["an owl's voice"],
        'clear_hint': 'Mystery Seeds'
    },
    "Rupees (1)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x00,
        'foggy_hints': ['a penny', 'a green gem'],
        'clear_hint': 'a Rupee'
    },
    "Rupees (5)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x01,
        'foggy_hints': ['a nickel'],
        'clear_hint': 'five Rupees'
    },
    "Rupees (10)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x02,
        'foggy_hints': ['a dime'],
        'clear_hint': 'ten Rupees'
    },
    "Rupees (20)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x03,
        'foggy_hints': [],
        'clear_hint': 'twenty Rupees'
    },
    "Rupees (30)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x04,
        'foggy_hints': [],
        'clear_hint': 'thirty Rupees'
    },
    "Rupees (50)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x05,
        'foggy_hints': ['two quarters'],
        'clear_hint': 'fifty Rupees'
    },
    "Rupees (100)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x06,
        'foggy_hints': ['a dollar', 'a big blue gem'],
        'clear_hint': 'one hundred Rupees'
    },
    "Rupees (200)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x08,
        'foggy_hints': ['two dollars', 'a big red gem'],
        'clear_hint': 'two hundred Rupees'
    },
    "Ore Chunks (10)": {
        'classification': ItemClassification.filler,
        'id': 0x37,
        'subid': 0x02,
        'foggy_hints': [],
        'clear_hint': 'ten Ore Chunks'
    },
    "Ore Chunks (25)": {
        'classification': ItemClassification.filler,
        'id': 0x37,
        'subid': 0x01,
        'foggy_hints': [],
        'clear_hint': 'twenty five Ore Chunks'
    },
    "Ore Chunks (50)": {
        'classification': ItemClassification.filler,
        'id': 0x37,
        'subid': 0x00,
        'foggy_hints': [],
        'clear_hint': 'fifty Ore Chunks'
    },
    "Heart Container": {
        'classification': ItemClassification.useful,
        'id': 0x2a,
        'foggy_hints': ['a boss reward'],
        'clear_hint': 'a Heart Container'
    },
    "Piece of Heart": {
        'classification': ItemClassification.filler,
        'id': 0x2b,
        'subid': 0x01,
        'foggy_hints': ['four of a kind'],
        'clear_hint': 'a Piece of Heart'
    },
    "Rare Peach Stone": {
        'classification': ItemClassification.filler,
        'id': 0x2b,
        'subid': 0x02,
        'foggy_hints': ['a rare fruit'],
        'clear_hint': 'a Rare Peach Stone'
    },
    "Flippers": {
        'classification': ItemClassification.progression,
        'id': 0x2e,
        'foggy_hints': [],
        'clear_hint': 'the Flippers'
    },
    "Potion": {
        'classification': ItemClassification.filler,
        'id': 0x2f,
        'foggy_hints': [],
        'clear_hint': 'a Potion'
    },

    "Small Key (Hero's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D0 Small Key'
    },
    "Small Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D1 Small Key'
    },
    "Small Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D2 Small Key'
    },
    "Small Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D3 Small Key'
    },
    "Small Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D4 Small Key'
    },
    "Small Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D5 Small Key'
    },
    "Small Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x06,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D6 Small Key'
    },
    "Small Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x07,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D7 Small Key'
    },
    "Small Key (Sword & Shield Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x08,
        'foggy_hints': ['a lockpick'],
        'clear_hint': 'a D8 Small Key'
    },
    "Master Key (Hero's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x80,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D0 Master Key'
    },
    "Master Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x81,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D1 Master Key'
    },
    "Master Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x82,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D2 Master Key'
    },
    "Master Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x83,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D3 Master Key'
    },
    "Master Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x84,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D4 Master Key'
    },
    "Master Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x85,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D2=5 Master Key'
    },
    "Master Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x86,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D6 Master Key'
    },
    "Master Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x87,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D7 Master Key'
    },
    "Master Key (Sword & Shield Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x88,
        'foggy_hints': ['a great lockpick'],
        'clear_hint': 'the D8 Master Key'
    },
    "Boss Key (Gnarled Root Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x00,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D1 Boss Key'
    },
    "Boss Key (Snake's Remains)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x01,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D2 Boss Key'
    },
    "Boss Key (Poison Moth's Lair)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x02,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D3 Boss Key'
    },
    "Boss Key (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x03,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D4 Boss Key'
    },
    "Boss Key (Unicorn's Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x04,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D5 Boss Key'
    },
    "Boss Key (Ancient Ruins)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x05,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D6 Boss Key'
    },
    "Boss Key (Explorer's Crypt)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x06,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D7 Boss Key'
    },
    "Boss Key (Sword & Shield Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x07,
        'foggy_hints': ['a big lockpick'],
        'clear_hint': 'the D8 Boss Key'
    },
    # "Compass (Hero's Cave)": {
    #     'classification': ItemClassification.useful,
    #     'id': 0x32,
    #     'subid': 0x00,
    #     'foggy_hints': [],
    #     'clear_hint': "you shouldn't see this"
    # },
    "Compass (Gnarled Root Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x01,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D1 Compass'
    },
    "Compass (Snake's Remains)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x02,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D2 Compass'
    },
    "Compass (Poison Moth's Lair)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x03,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D3 Compass'
    },
    "Compass (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x04,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D4 Compass'
    },
    "Compass (Unicorn's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x05,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D5 Compass'
    },
    "Compass (Ancient Ruins)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x06,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D6 Compass'
    },
    "Compass (Explorer's Crypt)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x07,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D7 Compass'
    },
    "Compass (Sword & Shield Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x08,
        'foggy_hints': ['a tracking tool'],
        'clear_hint': 'the D8 Compass'
    },
    # "Dungeon Map (Hero's Cave)": {
    #     'classification': ItemClassification.useful,
    #     'id': 0x33,
    #     'subid': 0x00,
    #     'foggy_hints': [],
    #     'clear_hint': "you shouldn't see this"
    # },
    "Dungeon Map (Gnarled Root Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x01,
        'foggy_hints': [],
        'clear_hint': 'the D1 Map'
    },
    "Dungeon Map (Snake's Remains)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x02,
        'foggy_hints': [],
        'clear_hint': 'the D2 Map'
    },
    "Dungeon Map (Poison Moth's Lair)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x03,
        'foggy_hints': [],
        'clear_hint': 'the D3 Map'
    },
    "Dungeon Map (Dancing Dragon Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x04,
        'foggy_hints': [],
        'clear_hint': 'the D4 Map'
    },
    "Dungeon Map (Unicorn's Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x05,
        'foggy_hints': [],
        'clear_hint': 'the D5 Map'
    },
    "Dungeon Map (Ancient Ruins)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x06,
        'foggy_hints': [],
        'clear_hint': 'the D6 Map'
    },
    "Dungeon Map (Explorer's Crypt)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x07,
        'foggy_hints': [],
        'clear_hint': 'the D7 Map'
    },
    "Dungeon Map (Sword & Shield Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x08,
        'foggy_hints': [],
        'clear_hint': 'the D8 Map'
    },

    "Gasha Seed": {
        'classification': ItemClassification.filler,
        'id': 0x34,
        'subid': 0x01,
        'foggy_hints': ["a botanist's product"],
        'clear_hint': 'a Gasha Seed'
    },

    "Cuccodex": {
        'classification': ItemClassification.progression,
        'id': 0x55,
        'foggy_hints': ['a chicken compendium'],
        'clear_hint': 'the Cuccodex'
    },
    "Lon Lon Egg": {
        'classification': ItemClassification.progression,
        'id': 0x56,
        'foggy_hints': ['a beauty aid'],
        'clear_hint': 'the Lon Lon Egg'
    },
    "Ghastly Doll": {
        'classification': ItemClassification.progression,
        'id': 0x57,
        'foggy_hints': ['a chilling puppet'],
        'clear_hint': 'the Ghastly Doll'
    },
    "Iron Pot": {
        'classification': ItemClassification.progression,
        'id': 0x35,
        'foggy_hints': ['a cooking container'],
        'clear_hint': 'an Iron Pot'
    },
    "Lava Soup": {
        'classification': ItemClassification.progression,
        'id': 0x38,
        'foggy_hints': ["a Goron's cold medicine"],
        'clear_hint': 'some Lava Soup'
    },
    "Goron Vase": {
        'classification': ItemClassification.progression,
        'id': 0x39,
        'foggy_hints': ["a collector's item"],
        'clear_hint': 'the Goron Vase'
    },
    "Fish": {
        'classification': ItemClassification.progression,
        'id': 0x3a,
        'foggy_hints': [],
        'clear_hint': 'a Fish'
    },
    "Megaphone": {
        'classification': ItemClassification.progression,
        'id': 0x3b,
        'foggy_hints': ['a voice amplifier'],
        'clear_hint': 'a megaphone'
    },
    "Mushroom": {
        'classification': ItemClassification.progression,
        'id': 0x3c,
        'foggy_hints': [],
        'clear_hint': 'a Mushroom'
    },
    "Wooden Bird": {
        'classification': ItemClassification.progression,
        'id': 0x3d,
        'foggy_hints': [],
        'clear_hint': 'a Wooden Bird'
    },
    "Engine Grease": {
        'classification': ItemClassification.progression,
        'id': 0x3e,
        'foggy_hints': [],
        'clear_hint': 'some Engine Grease'
    },
    "Phonograph": {
        'classification': ItemClassification.progression,
        'id': 0x3f,
        'foggy_hints': ['a record player'],
        'clear_hint': 'a Phonograph'
    },

    "Gnarled Key": {
        'classification': ItemClassification.progression,
        'id': 0x42,
        'foggy_hints': ['a wooden key'],
        'clear_hint': 'the Gnarled Key'
    },
    "Floodgate Key": {
        'classification': ItemClassification.progression,
        'id': 0x43,
        'foggy_hints': ['a way to release the dam'],
        'clear_hint': 'the Floodgate Key'
    },
    "Dragon Key": {
        'classification': ItemClassification.progression,
        'id': 0x44,
        'foggy_hints': [],
        'clear_hint': 'the Dragon Key'
    },
    "Star Ore": {
        'classification': ItemClassification.progression,
        'id': 0x45,
        'foggy_hints': [],
        'clear_hint': 'the Star Ore'
    },
    "Ribbon": {
        'classification': ItemClassification.progression,
        'id': 0x46,
        'foggy_hints': ['a beautiful gift'],
        'clear_hint': 'a Ribbon'
    },
    "Spring Banana": {
        'classification': ItemClassification.progression,
        'id': 0x47,
        'foggy_hints': ['a yellow fruit', 'some bear food'],
        'clear_hint': 'Spring Bananas'
    },
    #   "ricky's gloves": {
    #       'classification': ItemClassification.progression,
    #       'pretty_name': "Ricky's Gloves",
    #       'id': 0x48
    #   },
    "Rusty Bell": {
        'classification': ItemClassification.progression,
        'id': 0x4a,
        'foggy_hints': ['an item of great value'],
        'clear_hint': 'the Rusty Bell'
    },
    "Pirate's Bell": {
        'classification': ItemClassification.progression,
        'id': 0x25,
        'foggy_hints': ['an heirloom', "a pirate's treasure"]
    },
    "Treasure Map": {
        'classification': ItemClassification.useful,
        'id': 0x4b,
        'foggy_hints': [],
        'clear_hint': 'the Treasure Map'
    },
    "Round Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4c,
        'foggy_hints': [],
        'clear_hint': 'the Round Jewel'
    },
    "Pyramid Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4d,
        'foggy_hints': [],
        'clear_hint': 'the Pyramid Jewel'
    },
    "Square Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4e,
        'foggy_hints': [],
        'clear_hint': 'the Square Jewel'
    },
    "X-Shaped Jewel": {
        'classification': ItemClassification.progression,
        'id': 0x4f,
        'foggy_hints': [],
        'clear_hint': 'the X-Shaped Jewel'
    },
    "Red Ore": {
        'classification': ItemClassification.progression,
        'id': 0x50,
        'foggy_hints': [],
        'clear_hint': 'the Red Ore'
    },
    "Blue Ore": {
        'classification': ItemClassification.progression,
        'id': 0x51,
        'foggy_hints': [],
        'clear_hint': 'the Blue Ore'
    },
    "Hard Ore": {
        'classification': ItemClassification.progression,
        'id': 0x52,
        'foggy_hints': [],
        'clear_hint': 'the Hard Ore'
    },
    "Member's Card": {
        'classification': ItemClassification.progression,
        'id': 0x53,
        'foggy_hints': [],
        'clear_hint': "the Member's Card"
    },
    "Master's Plaque": {
        'classification': ItemClassification.progression,
        'id': 0x54,
        'foggy_hints': [],
        'clear_hint': "the Master's Plaque"
    },
    #   "Bomb Upgrade": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x61
    #    },
    #   "Satchel Upgrade": {
    #   'classification': ItemClassification.progression,
    #   "",
    #        'id': 0x62)

    "Friendship Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x04,
        'ring': 'useless',
        'foggy_hints': ['a useless ring', "Vasu's gift"],
        'clear_hint': 'the Friendship Ring'
    },
    "Power Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x05,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a damage upgrade'],
        'clear_hint': 'the Power Ring L-1'
    },
    "Power Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x06,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a damage upgrade'],
        'clear_hint': 'the Power Ring L-2'
    },
    "Power Ring L-3": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x07,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a damage upgrade'],
        'clear_hint': 'the Power Ring L-3'
    },
    "Armor Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x08,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a defense upgrade'],
        'clear_hint': 'the Armor Ring L-1'
    },
    "Armor Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x09,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a defense upgrade'],
        'clear_hint': 'the Armor Ring L-2'
    },
    "Armor Ring L-3": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0a,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a defense upgrade'],
        'clear_hint': 'the Armor Ring L-3'
    },
    "Red Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0b,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a damage upgrade'],
        'clear_hint': 'the Red Ring'
    },
    "Blue Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0c,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a defense upgrade'],
        'clear_hint': 'the Blue Ring'
    },
    "Green Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0d,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a damage upgrade', 'a defense upgrade'],
        'clear_hint': 'the Green Ring'
    },
    "Cursed Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0e,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the Cursed Ring'
    },
    "Expert's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0f,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': "the Expert's Ring"
    },
    "Blast Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x10,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Blast Ring'
    },
    "Rang Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x11,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Rang Ring L-1'
    },
    "GBA Time Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x12,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the GBA Time Ring'
    },
    "Maple's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x13,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': "Maple's Ring"
    },
    "Steadfast Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x14,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Steadfast Ring'
    },
    "Pegasus Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x15,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a speed booster'],
        'clear_hint': 'the Pegasus Ring'
    },
    "Toss Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x16,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Toss Ring'
    },
    "Heart Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x17,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'some health recovery'],
        'clear_hint': 'the Heart Ring L-1'
    },
    "Heart Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x18,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'some health recovery'],
        'clear_hint': 'the Heart Ring L-2'
    },
    "Swimmer's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x19,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': "the Swimmer's Ring"
    },
    "Charge Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1a,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Charge Ring'
    },
    "Light Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1b,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Light Ring L-1'
    },
    "Light Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1c,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Light Ring L-2'
    },
    "Bomber's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1d,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': "the Bomber's Ring"
    },
    "Green Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1e,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Green Luck Ring'
    },
    "Blue Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1f,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Blue Luck Ring'
    },
    "Gold Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x20,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Gold Luck Ring'
    },
    "Red Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x21,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Red Luck Ring'
    },
    "Green Holy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x22,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Green Holy Ring'
    },
    "Blue Holy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x23,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Blue Holy Ring'
    },
    "Red Holy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x24,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Red Holy Ring'
    },
    "Snowshoe Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x25,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'an anti-ice measure'],
        'clear_hint': 'the Snowshow Ring'
    },
    "Roc's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x26,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': "Roc's Ring"
    },
    "Quicksand Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x27,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Quicksand Ring'
    },
    "Red Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x28,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Red Joy Ring'
    },
    "Blue Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x29,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Blue Joy Ring'
    },
    "Gold Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2a,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a resource doubler'],
        'clear_hint': 'the Gold Joy Ring'
    },
    "Green Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2b,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Green Joy Ring'
    },
    "Discovery Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2c,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Discovery Ring'
    },
    "Rang Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2d,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Rang Ring L-2'
    },
    "Octo Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2e,
        'ring': 'useless',
        'foggy_hints': ['a useless ring', 'a transformation ring'],
        'clear_hint': 'the Octo Ring'
    },
    "Moblin Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2f,
        'ring': 'useless',
        'foggy_hints': ['a useless ring', 'a transformation ring'],
        'clear_hint': 'the Moblin Ring'
    },
    "Like Like Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x30,
        'ring': 'useless',
        'foggy_hints': ['a useless ring', 'a transformation ring'],
        'clear_hint': 'the Like Like Ring'
    },
    "Subrosian Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x31,
        'ring': 'useless',
        'foggy_hints': ['a useless ring', 'a transformation ring'],
        'clear_hint': 'the Subrosian Ring'
    },
    "First Gen Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x32,
        'ring': 'useless',
        'foggy_hints': ['a useless ring', 'a transformation ring'],
        'clear_hint': 'the First Gen Ring'
    },
    "Spin Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x33,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Spin Ring'
    },
    "Bombproof Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x34,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Bombproof Ring'
    },
    "Energy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x35,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a spin replacement'],
        'clear_hint': 'the Energy Ring'
    },
    "Dbl. Edge Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x36,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a dangerous damage upgrade'],
        'clear_hint': ''
    },
    "GBA Nature Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x37,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the GBA Nature Ring'
    },
    "Slayer's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x38,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': "the Slayer's Ring"
    },
    "Rupee Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x39,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the Rupee Ring'
    },
    "Victory Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3a,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the Victory Ring'
    },
    "Sign Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3b,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the Sign Ring'
    },
    "100th Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3c,
        'ring': 'useless',
        'foggy_hints': ['a useless ring'],
        'clear_hint': 'the 100th Ring'
    },
    "Whisp Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3d,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Whisp Ring'
    },
    "Gasha Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3e,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'some fertilizer'],
        'clear_hint': 'the Gasha Ring'
    },
    "Peace Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3f,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Peace Ring'
    },
    "Zora Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x40,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Zora Ring'
    },
    "Fist Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x41,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Fist Ring'
    },
    "Whimsical Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x42,
        'ring': 'good',
        'foggy_hints': ['a useful ring', 'a whimsical damage upgrade'],
        'clear_hint': 'the Whimsical Ring'
    },
    "Protection Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x43,
        'ring': 'good',
        'foggy_hints': ['a useful ring'],
        'clear_hint': 'the Protection Ring'
    },

    "Bomb Flower": {
        'classification': ItemClassification.progression,
        'id': 0x49,
        'foggy_hints': ['a single-use explosive'],
        'clear_hint': 'the Bomb Flower'
    },
    "Fertile Soil": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x00,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Fertile Soil',
        'essence': True
    },
    "Gift of Time": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x01,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Gift of Time',
        'essence': True
    },
    "Bright Sun": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x02,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Bright Sun',
        'essence': True
    },
    "Soothing Rain": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x03,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Soothing Rain',
        'essence': True
    },
    "Nurturing Warmth": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x04,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Nurturing Warmth',
        'essence': True
    },
    "Blowing Wind": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x05,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Blowing Wind',
        'essence': True
    },
    "Seed of Life": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x06,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Seed of Life',
        'essence': True
    },
    "Changing Seasons": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x07,
        'foggy_hints': ['a McGuffin'],
        'clear_hint': 'the Changing Seasons',
        'essence': True
    },
    "Maku Seed": {  # Mostly for debug
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x36
    },
}
