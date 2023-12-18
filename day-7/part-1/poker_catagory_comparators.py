from poker_utils import (is_hand_five_of_kind,
                         is_hand_four_of_kind,
                         is_hand_full_house,
                         is_hand_three_of_kind,
                         is_hand_two_pair,
                         is_hand_pair
                         )


def is_five_of_kind_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if is_hand_five_of_kind(hand1) == is_hand_five_of_kind(hand2):
        return 0
    if is_hand_five_of_kind(hand1):
        return 1
    return -1


def is_four_of_kind_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if is_hand_four_of_kind(hand1) == is_hand_four_of_kind(hand2):
        return 0
    if is_hand_four_of_kind(hand1):
        return 1
    return -1


def is_full_house_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if is_hand_full_house(hand1) == is_hand_full_house(hand2):
        return 0
    if is_hand_full_house(hand1):
        return 1
    return -1


def is_hand_three_of_kind_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if is_hand_three_of_kind(hand1) == is_hand_three_of_kind(hand2):
        return 0
    if is_hand_three_of_kind(hand1):
        return 1
    return -1


def is_hand_two_pair_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if is_hand_two_pair(hand1) == is_hand_two_pair(hand2):
        return 0
    if is_hand_two_pair(hand1):
        return 1
    return -1


def is_hand_pair_comparator(hand1: str, hand2: str) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if is_hand_pair(hand1) == is_hand_pair(hand2):
        return 0
    if is_hand_pair(hand1):
        return 1
    return -1

