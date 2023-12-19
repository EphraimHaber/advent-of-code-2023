import re
from primefac import primefac
from math import prod

def walk_pattern():
    global steps_counter
    global locations
    for direction in walking_pattern:
        for i, location in enumerate(locations):
            locations[i] = nodes_tree[location][direction]
        steps_counter += 1


with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = [line for line in lines if line != '']
    walking_pattern = lines[0]
    nodes = lines[1:]
    for node in nodes:
        x = re.findall(r'[0-9A-Z]{3}', node)
    nodes_tree = {re.findall(r'[0-9A-Z]{3}', node)[0]: {
        'L': re.findall(r'[0-9A-Z]{3}', node)[1],
        'R': re.findall(r'[0-9A-Z]{3}', node)[2]
    } for node in nodes}
    locations = [key for key in list(nodes_tree.keys()) if key.endswith('A')]
    print(len(locations))
    best_steps = []

    temp_locations = [loc for loc in locations]
    for i in range(len(locations)):
        steps_counter = 0
        locations = [temp_locations[i]]
        print(locations)
        while True:
            walk_pattern()
            if all(loc.endswith('Z') for loc in locations):
                best_steps.append(steps_counter)
                print(best_steps)
                break
    print(best_steps)
    t = [list(primefac(step)) for step in best_steps]
    t = [element for sublist in t for element in sublist]
    unique_best_steps_factors = list(set(t))
    print(unique_best_steps_factors)
    res = prod(unique_best_steps_factors)
    print(res)
    '''
    21883 -> 79 * 277
    13019 -> 47 * 277
    11911 -> 43 * 277
    16897 -> 61 * 277
    19667 -> 71 * 277
    18559 -> 67 * 277
    '''

