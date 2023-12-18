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
from collections import Counter
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

from complete_comparator import card_comparator


if __name__ == '__main__':
    with (open('puzzle.txt') as file):
        lines = file.read().split('\n')
        lines.sort(key=cmp_to_key(card_comparator))
        res = 0
        fives = []
        fours = []
        full_houses = []
        triples = []
        two_pairs = []
        pairs = []
        high_cards = []
        for i, line in enumerate(lines):
            hand = line.split(" ")[0]
            pot = line.split(" ")[1]
            my_line = f'{hand} {pot}'
            print(f'{i+1}: hand: {line.split(" ")[0]} pot: {line.split(" ")[1]}')
            if is_hand_five_of_kind(hand):
                fives.append(my_line)
            elif is_hand_four_of_kind(hand):
                fours.append(my_line)
            elif is_hand_full_house(hand):
                full_houses.append(my_line)
            elif is_hand_three_of_kind(hand):
                triples.append(my_line)
            elif is_hand_two_pair(hand):
                two_pairs.append(my_line)
            elif is_hand_pair(hand):
                pairs.append(my_line)
            elif is_hand_high_card(hand):
                high_cards.append(my_line)
            res += ((i + 1) * int(line.split(" ")[1]))
        print(fives)
        print(fours)
        print(full_houses)
        print(triples)
        print(two_pairs)
        print(pairs)
        print(high_cards)
        print(len(fives) + len(fours) + len(full_houses) + len(triples) + len(two_pairs) + len(pairs) + len(high_cards))
        print(res)
        temp = []
        temp.extend(high_cards)
        temp.extend(pairs)
        temp.extend(two_pairs)
        temp.extend(triples)
        temp.extend(full_houses)
        temp.extend(fours)
        temp.extend(fives)
        my_res = 0
        for i, line in enumerate(temp):
            hand = line.split(" ")[0]
            pot = line.split(" ")[1]
            my_res += i*int(pot) + int(pot)
            print(f'{i+1}: hand: {line.split(" ")[0]} pot: {line.split(" ")[1]}')
        print(my_res)
        assert res == my_res
        exit()





















        # category_ranges = {
        #     'fives': {'start': 0, 'end': -1, 'func': is_hand_five_of_kind, 'comp': five_of_kind_comparator, 'res': []},
        #     'fours': {'start': 0, 'end': -1, 'func': is_hand_four_of_kind, 'comp': four_of_kind_comparator, 'res': []},
        #     'full_houses': {'start': 0, 'end': -1, 'func': is_hand_full_house, 'comp': full_house_comparator, 'res': []},
        #     'threes': {'start': 0, 'end': -1, 'func': is_hand_three_of_kind, 'comp': three_of_kind_comparator, 'res': []},
        #     'two_pairs': {'start': 0, 'end': -1, 'func': is_hand_two_pair, 'comp': two_pairs_comparator, 'res': []},
        #     'pairs': {'start': 0, 'end': -1, 'func': is_hand_pair, 'comp': pair_comparator, 'res': []},
        #     'high_card': {'start': 0, 'end': -1, 'func': is_hand_high_card, 'comp': high_card_comparator, 'res': []},
        # }
        # category_keys = list(category_ranges.keys())
        # for key in category_ranges:
        #     category_ranges[key]['n'] = 0
        #
        # lines.sort(key=cmp_to_key(is_hand_pair_comparator))
        # lines.sort(key=cmp_to_key(is_hand_two_pair_comparator))
        # lines.sort(key=cmp_to_key(is_hand_three_of_kind_comparator))
        # lines.sort(key=cmp_to_key(is_full_house_comparator))
        # lines.sort(key=cmp_to_key(is_four_of_kind_comparator))
        # lines.sort(key=cmp_to_key(is_five_of_kind_comparator))
        # lines.reverse()
        # # pprint(lines)
        # # exit()
        # last_marked = 0
        # for category_key in category_keys:
        #     for i, line in enumerate(lines):
        #         if i < last_marked:
        #             i = last_marked
        #         hand = line.split(' ')[0]
        #         if category_ranges[category_key]['func'](hand):
        #             category_ranges[category_key]['res'].append(line)
        #             last_marked += 1
        #             category_ranges[category_key]['n'] += 1
        # print(last_marked)
        # ranges_print_debug()
        # res_hands = []
        # for key in category_ranges:
        #     print(category_ranges[key]['res'][0])
        #     category_ranges[key]['res'].sort(key=cmp_to_key(category_ranges[key]['comp']))
        #     print(category_ranges[key]['res'][0])
        #     print(key, category_ranges[key]['res'])
        #     # category_ranges[key]['res'].sort(key=cmp_to_key(category_ranges[key]['comp']))
        #     res_hands.extend(category_ranges[key]['res'])
        # # print(res_hands)
        # res = 0
        # res_hands.reverse()
        # print(len(res_hands))
        # dup = [item for item, count in Counter(res_hands).items() if count > 1]
        # assert len(dup) == 0
        # for i, bet in enumerate(res_hands):
        #     res += (i+1) * int(bet.split(' ')[1])
        # print(res)
        """
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
        """

