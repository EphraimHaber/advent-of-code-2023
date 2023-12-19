from pprint import pprint
import re


def walk_pattern():
    global steps_counter
    global location
    for direction in walking_pattern:
        location = nodes_tree[location][direction]
        steps_counter += 1


if __name__ == '__main__':
    with open('puzzle.txt', 'r') as f:
        lines = f.read().split('\n')
        lines = [line for line in lines if line != '']
        walking_pattern = lines[0]
        nodes = lines[1:]
        for node in nodes:
            x = re.findall(r'[A-Z]{3}', node)
            print(x)
        nodes_tree = {re.findall(r'[A-Z]{3}', node)[0]: {
            'L': re.findall(r'[A-Z]{3}', node)[1],
            'R': re.findall(r'[A-Z]{3}', node)[2]
        } for node in nodes}
        location = 'AAA'
        is_mid_walk = False
        steps_counter = 0
        while True:
            walk_pattern()
            if location == 'ZZZ':
                break
        print(steps_counter)  # 21883
        print(location)

