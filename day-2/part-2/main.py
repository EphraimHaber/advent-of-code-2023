from math import prod
from game_utils import load_game_data

if __name__ == '__main__':
    data = load_game_data()
    power_sum = 0
    for key in data:
        rounds = data[key]
        lookup = {'red': 0, 'green': 0, 'blue': 0}
        for game_round in rounds:
            for color in game_round:
                if game_round[color] > lookup[color]:
                    lookup[color] = game_round[color]
        power_sum += prod(lookup.values())

    print(power_sum)

