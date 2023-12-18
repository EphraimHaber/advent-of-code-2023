from functools import cmp_to_key

from poker_utils import (is_hand_five_of_kind,
                         is_hand_four_of_kind,
                         is_hand_full_house,
                         is_hand_three_of_kind,
                         is_hand_two_pair,
                         is_hand_pair,
                         is_hand_high_card,
                         CARDS_SCORE
                         )


from poker_inner_comparators import (five_of_kind_comparator,
                                     four_of_kind_comparator,
                                     three_of_kind_comparator, full_house_comparator, two_pairs_comparator, pair_comparator, high_card_comparator)


HAND_TYPES = [is_hand_five_of_kind,
              is_hand_four_of_kind,
              is_hand_full_house,
              is_hand_three_of_kind,
              is_hand_two_pair,
              is_hand_pair,
              is_hand_high_card
              ]

HAND_TYPES.reverse()


def get_hand_type(hand: str):
    assert len(hand) == 5
    for i, func in enumerate(HAND_TYPES):
        if func(hand):
            return i
    raise ValueError('Hand Type Mismatch')


def card_comparator(hand1, hand2) -> int:
    hand1 = hand1.split(' ')[0]
    hand2 = hand2.split(' ')[0]
    if get_hand_type(hand1) > get_hand_type(hand2):
        return 1
    if get_hand_type(hand1) < get_hand_type(hand2):
        return -1
    if get_hand_type(hand1) == get_hand_type(hand2):
        if is_hand_five_of_kind(hand1):
            assert is_hand_five_of_kind(hand1) and is_hand_five_of_kind(hand2)
            return five_of_kind_comparator(hand1, hand2)
        if is_hand_four_of_kind(hand1):
            assert is_hand_four_of_kind(hand1) and is_hand_four_of_kind(hand2)
            return four_of_kind_comparator(hand1, hand2)
        if is_hand_full_house(hand1):
            assert is_hand_full_house(hand1) and is_hand_full_house(hand2)
            return full_house_comparator(hand1, hand2)
        if is_hand_three_of_kind(hand1):
            assert is_hand_three_of_kind(hand1) and is_hand_three_of_kind(hand2)
            return three_of_kind_comparator(hand1, hand2)
        if is_hand_two_pair(hand1):
            assert is_hand_two_pair(hand1) and is_hand_two_pair(hand2)
            return two_pairs_comparator(hand1, hand2)
        if is_hand_pair(hand1):
            assert is_hand_pair(hand1) and is_hand_pair(hand2)
            return pair_comparator(hand1, hand2)
        if is_hand_high_card(hand1):
            return high_card_comparator(hand1, hand2)
    raise ValueError('not good')


# hands = ['22222', 'JJJJJ', 'AAAAA', 'QQQQQ', 'QQQQ2', 'QQQQJ', 'QQQQJ', 'QQ3QQ', 'AAAQQ', 'AAAKK', 'JJJ22', '222JJ']
# hands = ['QQQQ2', 'QQQQJ', 'QQQQJ', 'QQ3QQ', 'AAAQQ', 'AAAKK', 'JJJ22', '222JJ', 'AAKK2', 'KKAA2', 'QQJJ5', 'JJQQ5', 'JJ338', 'JJ339', '22234', '22345', '22567']
# hands = ['AA223', 'AA227', 'AA225']
# hands = ['22345', '22567', '22ATJ']
# hands.sort(key=cmp_to_key(card_comparator))
# hands.reverse()
# print(hands)
