from colors import COLORS


def load_game_data():
    games_data = {}
    with open('puzzle.txt', 'r') as file:
        games = file.read().split('\n')
        for game in games:
            game_id = game.split(':')[0].replace('Game ', '')
            games_data[game_id] = game.split(':')[1]
        for game_id, game_data in games_data.items():
            games_data[game_id] = [game_res.strip().split(', ') for game_res in game_data.split(';')]
            temp = []
            for game_round in games_data[game_id]:
                temp2 = {'red': 0, 'green': 0, 'blue': 0}
                for toss in game_round:
                    for color in COLORS:
                        if color in toss:
                            toss = toss.replace(f' {color}', '')
                            temp2[color] = int(toss)
                temp.append(temp2)
            games_data[game_id] = temp
        return games_data
