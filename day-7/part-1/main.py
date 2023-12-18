"""
Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind: AAAAA
Four of a kind: AA8AA
Full house: 23332
Three of a kind: TTT98
Two pair: 23432
One pair: A23A4
High card, where all cards' labels are distinct: 23456
"""

# from poker_inner_comparators
from pprint import pprint
from functools import cmp_to_key
from poker_utils import (is_hand_five_of_kind,
                         is_hand_four_of_kind,
                         is_hand_full_house,
                         is_hand_three_of_kind,
                         is_hand_two_pair,
                         is_hand_pair,
                         is_hand_high_card
                         )
from poker_catagory_comparators import (is_five_of_kind_comparator,
                                        is_four_of_kind_comparator,
                                        is_full_house_comparator,
                                        is_hand_three_of_kind_comparator,
                                        is_hand_two_pair_comparator,
                                        is_hand_pair_comparator
                                        )
from poker_inner_comparators import (five_of_kind_comparator,
                                     four_of_kind_comparator,
                                     full_house_comparator,
                                     three_of_kind_comparator,
                                     two_pairs_comparator,
                                     pair_comparator,
                                     high_card_comparator
                                     )

if __name__ == '__main__':
    with open('example.txt') as file:
        lines = file.read().split('\n')
        print(lines)

        category_ranges = {
            'fives': {'start': 0, 'end': -1, 'func': is_hand_five_of_kind, 'comp': five_of_kind_comparator, 'res': []},
            'fours': {'start': 0, 'end': -1, 'func': is_hand_four_of_kind, 'comp': four_of_kind_comparator, 'res': []},
            'full_houses': {'start': 0, 'end': -1, 'func': is_hand_full_house, 'comp': full_house_comparator, 'res': []},
            'threes': {'start': 0, 'end': -1, 'func': is_hand_three_of_kind, 'comp': three_of_kind_comparator, 'res': []},
            'two_pairs': {'start': 0, 'end': -1, 'func': is_hand_two_pair, 'comp': two_pairs_comparator, 'res': []},
            'pairs': {'start': 0, 'end': -1, 'func': is_hand_pair, 'comp': pair_comparator, 'res': []},
            'high_card': {'start': 0, 'end': -1, 'func': is_hand_high_card, 'comp': high_card_comparator, 'res': []},
        }
        category_keys = list(category_ranges.keys())
        for key in category_ranges:
            category_ranges[key]['n'] = 0
        print(category_keys)

        lines.sort(key=cmp_to_key(is_hand_pair_comparator))
        lines.sort(key=cmp_to_key(is_hand_two_pair_comparator))
        lines.sort(key=cmp_to_key(is_hand_three_of_kind_comparator))
        lines.sort(key=cmp_to_key(is_full_house_comparator))
        lines.sort(key=cmp_to_key(is_four_of_kind_comparator))
        lines.sort(key=cmp_to_key(is_five_of_kind_comparator))
        # pprint(lines)
        # exit()
        category_keys_index = 0
        for i, line in enumerate(lines):
            hand = line.split(' ')[0]
            # print(i, hand)
            if not category_ranges[category_keys[category_keys_index]]['func'](hand):
                category_ranges[category_keys[category_keys_index]]['end'] = i
                category_keys_index += 1
                if category_keys_index == len(category_keys):
                    break
                category_ranges[category_keys[category_keys_index]]['start'] = i
            category_ranges[category_keys[category_keys_index]]['n'] += 1
        if category_ranges['high_card']['start'] != 0:
            category_ranges['high_card']['end'] = len(lines)
        for key in category_ranges:
            # print(key, category_ranges[key])
            # print(key, category_ranges[key]['start'], category_ranges[key]['end'])
            category_ranges[key]['res'].extend(lines[category_ranges[key]['start']:category_ranges[key]['end']])
        sorted_hands = []
        for key in category_ranges:
            print(key, category_ranges[key])
        for key in category_ranges:
            if len(category_ranges[key]['res']) == 0 or category_ranges[key]['n'] == 0:
                continue
            print(key, category_ranges[key]['res'])
            category_ranges[key]['res'].sort(key=cmp_to_key(category_ranges[key]['comp']))
            sorted_hands.extend(category_ranges[key]['res'])
        res = 0
        # sorted_hands.reverse()
        for i, bet in enumerate(sorted_hands):
            # print(i+1, int(bet.split(' ')[1]))
            res += (i+1) * int(bet.split(' ')[1])
        print(res)
        print(len(sorted_hands))
        # pprint(sorted_hands)

