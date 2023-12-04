from colors import COLORS
from game_utils import load_game_data, is_valid_game


def main():
    res_games_data = load_game_data()
    for key in res_games_data:
        rounds = res_games_data[key]
        lookup = {'red': 0, 'green': 0, 'blue': 0}
        for game_round in rounds:
            for color in COLORS:
                lookup[color] = max(lookup[color], game_round[color])
        if not is_valid_game(lookup):
            res_games_data[key] = ''
    legal_games = {k: v for k, v in res_games_data.items() if v != ''}
    print(sum([int(pk) for pk in legal_games.keys()]))


if __name__ == '__main__':
    main()
