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
from functools import cmp_to_key
from poker_utils import CARDS, CARDS_SCORE


def get_n_of_kind(n: int, hand: str) -> str:
    counts = Counter(hand)
    for record in counts.most_common():
        if record[1] == n:
            return record[0]
    return ''


def get_full_house_major_minor(hand: str) -> tuple[str, str]:
    major, minor = get_two_top_common(hand)
    return major, minor


def get_top_common(hand: str) -> str:
    counts = Counter(hand)
    return counts.most_common()[0][0]


def card_comparator(card1, card2):
    if CARDS_SCORE[card1] > CARDS_SCORE[card2]:
        return 1
    if CARDS_SCORE[card1] == CARDS_SCORE[card2]:
        return 0
    return -1


def order_cards_high_to_low(hand: str) -> list[str]:
    cards_list = [c for c in hand]
    cards_list.sort(key=cmp_to_key(card_comparator), reverse=True)
    return cards_list


def get_highest_card(hand: str) -> str:
    res = hand[0]
    for i in range(1, len(hand)):
        if CARDS_SCORE[hand[i]] > CARDS_SCORE[res]:
            res = hand[i]
    return res


def get_two_top_common(hand: str) -> tuple[str, str]:
    counts = Counter(hand)
    first_place = counts.most_common()[0][0]
    second_place = counts.most_common()[1][0]
    return first_place, second_place


def five_of_kind_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1_card_index = CARDS.index(hand1[0])
    hand2_card_index = CARDS.index(hand2[0])
    if hand1_card_index == hand2_card_index:
        return 0
    if hand1_card_index > hand2_card_index:
        return 1
    return -1


def four_of_kind_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1_card_index = CARDS.index(get_n_of_kind(4, hand1))
    hand2_card_index = CARDS.index(get_n_of_kind(4, hand2))
    if hand1_card_index == hand2_card_index:
        return 0
    if hand1_card_index > hand2_card_index:
        return 1
    return -1


def full_house_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1_major, hand1_minor = get_full_house_major_minor(hand1)
    hand2_major, hand2_minor = get_full_house_major_minor(hand2)
    if CARDS_SCORE[hand1_major] > CARDS_SCORE[hand2_major]:
        return 1
    if CARDS_SCORE[hand1_major] == CARDS_SCORE[hand2_major]:
        if CARDS_SCORE[hand1_minor] > CARDS_SCORE[hand2_minor]:
            return 1
        if CARDS_SCORE[hand1_minor] == CARDS_SCORE[hand2_minor]:
            return 0
        return -1
    return -1


def three_of_kind_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1_card_index = CARDS.index(get_n_of_kind(3, hand1))
    hand2_card_index = CARDS.index(get_n_of_kind(3, hand2))
    if hand1_card_index == hand2_card_index:
        return 0
    if hand1_card_index > hand2_card_index:
        return 1
    return -1


def two_pairs_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1_pair_card_1, hand1_pair_card_2 = get_two_top_common(hand1)
    hand2_pair_card_1, hand2_pair_card_2 = get_two_top_common(hand2)

    if CARDS_SCORE[hand1_pair_card_1] < CARDS_SCORE[hand1_pair_card_2]:
        hand1_pair_card_1, hand1_pair_card_2 = hand1_pair_card_2, hand1_pair_card_1
    if CARDS_SCORE[hand2_pair_card_1] < CARDS_SCORE[hand2_pair_card_2]:
        hand2_pair_card_1, hand2_pair_card_2 = hand2_pair_card_2, hand2_pair_card_1

    if CARDS_SCORE[hand1_pair_card_1] > CARDS_SCORE[hand2_pair_card_1]:
        return 1
    if CARDS_SCORE[hand1_pair_card_1] == CARDS_SCORE[hand2_pair_card_1]:
        if CARDS_SCORE[hand1_pair_card_2] > CARDS_SCORE[hand2_pair_card_1]:
            return 1
        if CARDS_SCORE[hand1_pair_card_2] == CARDS_SCORE[hand2_pair_card_1]:
            return 0
        return -1
    return -1


def pair_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1_card = get_top_common(hand1)
    hand2_card = get_top_common(hand2)
    if CARDS_SCORE[hand1_card] > CARDS_SCORE[hand2_card]:
        return 1
    if CARDS_SCORE[hand1_card] == CARDS_SCORE[hand2_card]:
        return 0
    return -1


def high_card_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    hand1 = order_cards_high_to_low(hand1)
    hand2 = order_cards_high_to_low(hand2)

    decision = 0
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        if CARDS_SCORE[hand1[i]] > CARDS_SCORE[hand1[i]]:
            decision = 1
            break
        else:
            decision = -1
            break
    return decision


# hands = ['5J476', 'AJ986']
# hands.sort(key=cmp_to_key(high_card_comparator))
# print(hands)
# print(high_card_comparator('A2345', '2345A'))


# hands = ['22222', 'JJJJJ', 'AAAAA', 'QQQQQ']
# hands.sort(key=cmp_to_key(five_of_kind_comparator))
# print(hands)

# full_houses = ["AA222", "TTTAA", "33AAA", "QQQAA", "TTT22", "22233"]
# full_houses.sort(key=cmp_to_key(full_house_comparator))
# print(full_houses)
# print(CARDS.index('3'))
