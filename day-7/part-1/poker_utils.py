from collections import Counter


CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDS_SCORE = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def is_hand_five_of_kind(hand: str) -> bool:
    assert len(hand) == 5
    return hand.count(hand[0]) == 5


def is_hand_four_of_kind(hand: str) -> bool:
    # print(hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4)
    assert len(hand) == 5
    return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4


def is_hand_four_of_kind_v2(hand: str) -> bool:
    return hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4


def is_hand_full_house(hand: str) -> bool:
    unique_cards = "".join(set(hand))
    if len(unique_cards) != 2:
        return False
    return all(hand.count(card) in [2, 3] for card in unique_cards)
    # return hand.count(unique_cards[0]) + hand.count(unique_cards[1]) == 5


def is_hand_three_of_kind(hand: str) -> bool:
    card_counts = Counter(hand)
    temp = [count[1] for count in card_counts.most_common()]
    assert sum(temp) == 5
    return temp[0] == 3 and all(num == 1 for num in temp[1:])


def is_hand_two_pair(hand: str) -> bool:
    card_counts = Counter(hand)
    return card_counts.most_common()[0][1] == 2 and card_counts.most_common()[1][1] == 2 and card_counts.most_common()[2][1] == 1


def is_hand_pair(hand: str) -> bool:
    card_counts = Counter(hand)
    temp = [count[1] for count in card_counts.most_common()]
    assert sum(temp) == 5
    return len(temp) == 4
    # return any(count == 2 for count in card_counts.values())


def is_hand_high_card(hand: str) -> bool:
    card_counts = Counter(hand)
    return all(card_repeats == 1 for card_repeats in list(card_counts.values()))
