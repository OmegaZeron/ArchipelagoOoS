from worlds.tloz_oos.data.Items import ITEMS_DATA
from worlds.tloz_oos.data.Locations import LOCATIONS_DATA

# TODO change keys to asm memory locations
know_it_all_birds = {
    1: "Know-It-All Bird #1",
    2: "Know-It-All Bird #2",
    3: "Know-It-All Bird #3",
    4: "Know-It-All Bird #4",
    5: "Know-It-All Bird #5",
    6: "Know-It-All Bird #6",
    7: "Know-It-All Bird #7",
    8: "Know-It-All Bird #8",
    9: "Know-It-All Bird #9",
    10: "Know-It-All Bird #10"
}
owl_statues = {
    11: "Dodongo Owl",
    12: "Spiked Beetles Owl",
    13: "Trampoline Owl",
    14: "Omuai Owl",
    15: "Greater Distance Owl",
    16: "Gohma Owl",
    17: "Armos Owl",
    18: "Poe Curse Owl",
    19: "Shining Blue Owl",
    20: "Silent Watch Owl",
    21: "Frypolar Owl",
    22: "Magical Ice Owl"
}
hint_locations = know_it_all_birds | owl_statues

# know_it_all_reversemap = {name: id for id, name in know_it_all_birds.items()}
# owl_statue_reversemap = {name: id for id, name in owl_statues.items()}
hint_location_reversemap = {name: id for id, name in hint_locations.items()}

hint_table = {
    'item': {
        key: {
            'foggy_hints': val.get('foggy_hints'),
            'clear_hint': val.get('clear_hint')
        } for key, val in ITEMS_DATA.items()
    },
    'location': {
        key: {
            'foggy_hints': val.get('foggy_hints'),
            'clear_hint': val.get('clear_hint'),
            'region': val.get('region'),
            'essence': val.get('essence', False)
        } for key, val in LOCATIONS_DATA.items()
    }
}

hint_types = ["barren", "woth", "item"]

def get_hint(item, rand, clearHint = False):
    if item in hint_table:
        data = hint_table[item]
        if clearHint or not data["foggy_hints"]:
            return data["clear_hint"]
        else:
            return rand.choice(data["foggy_hints"])
             

def get_barren_hint(world, checked_locations: dict[int, set]):
    regions = list(filter(lambda area:
        area not in checked_locations[world.player],
        world.barren_regions))
    
    if not regions:
        return None
    
    region_weights = [world.barren_regions[region]['weight'] for region in regions]
    if not any(region_weights):
        return None
    
    region = world.hint_rng.choices(regions, weights=region_weights)[0]
    checked_locations[world.player].add(region)

    return f"plundering {region} is a foolish choice."


def get_woth_hint(world, checked_locations: dict[int, set]):
    regions = list(filter(lambda location:
        location['name'] not in checked_locations[location['player']],
        world.woth_regions
    ))
    if not regions:
        return None
    
    region = world.hint_rng.choice(regions)
    checked_locations[region['player']].add(region['name'])
    world.woth_regions.remove(region)
    
    return f"{region['name']} is on the way of the hero"


def get_item_hint(world, checked_locations: dict[int, set]):
    locations = list(filter(lambda location:
        location not in checked_locations[world.player] and
        location.name in list(LOCATIONS_DATA.keys()) and
        location.name not in world.excluded_hint_locs(),
        world.multiworld.get_filled_locations(world.player)
    ))
    location = world.hint_rng.choice(locations)
    if not location:
        return False
    loc_data = world.multiworld.get_location(location.name, world.player)
    checked_locations[world.player].add(location)
    if world.options.clear_hints:
        item_text = ITEMS_DATA[loc_data.item.name]['clear_hint']
        loc_text = LOCATIONS_DATA[location.name]['clear_hint']
    else:
        item_text = world.hint_rng.choice(ITEMS_DATA[loc_data.item.name]['foggy_hints'])
        if not item_text:
            item_text = ITEMS_DATA[loc_data.item.name]['clear_hint']
        loc_text = world.hint_rng.choice(LOCATIONS_DATA[location.name]['foggy_hints'])
        if not loc_text:
            loc_text = LOCATIONS_DATA[location.name]['clear_hint']
    return f"{loc_text} {item_text}"


hint_funcs = {
    "barren": get_barren_hint,
    "woth": get_woth_hint,
    "item": get_item_hint
}

def add_hint(world, hint_locs, text):
    hint_loc = world.hint_rng.choice(hint_locs)
    if hint_loc in know_it_all_birds:
        hint_text = f"Did you know? {text.capitalize()}"
    elif hint_loc in owl_statues:
        hint_text = f"They say that {text}"
    else:
        print("Whoops")
        return False

def generate_hints(world):
    world.barren_dungeon = 0
    world.woth_dungeon = 0

    hint_counts = {}
    checked_locations = {player: set() for player in world.multiworld.get_all_ids()}
    
    unplaced_hint_locations = [id for id in hint_locations.keys()]
    world.hint_rng.shuffle(unplaced_hint_locations)

    weights = [
        int(world.options.hint_weight_barren.value),
        int(world.options.hint_weight_woth.value),
        int(world.options.hint_weight_item.value)
    ]
    # print(weights)
    all_hints = [] # TEST VARIABLE

    while unplaced_hint_locations:
        try:
            weighted_hint_prob = []
            for w1_type, w1_prob in zip(hint_types, weights):
                p = w1_prob
                if p != 0: # If the base prob is 0, then it's 0
                    for w2_type, w2_prob in zip(hint_types, weights):
                        if w2_prob != 0: # If the other prob is 0, then it has no effect
                            # Raising this term to a power greater than 1 will decrease variance
                            # Conversely, a power less than 1 will increase variance
                            p = p * (((hint_counts.get(w2_type, 0) / w2_prob) + 1) / ((hint_counts.get(w1_type, 0) / w1_prob) + 1))
                weighted_hint_prob.append(p)

            hint_type = world.hint_rng.choices(hint_types, weights=weighted_hint_prob)[0]
        except IndexError:
            raise Exception("Not enough hints remaining to fill locations")
        except ValueError:
            raise Exception("Not enough hints remaining to fill locations")
        
        hint = hint_funcs[hint_type](world, checked_locations)

        if hint == None:
            weights[hint_types.index(hint_type)] = 0
        else:
            # success = add_hint(hint)
            # TEMP
            unplaced_hint_locations.pop()
            all_hints.append(hint)
    print(all_hints)
            