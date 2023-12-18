from poker_utils import (is_hand_five_of_kind,
                         is_hand_four_of_kind,
                         is_hand_full_house,
                         is_hand_three_of_kind,
                         is_hand_two_pair,
                         is_hand_pair,
                         is_hand_high_card
                         )


class TestFiveOfKind:
    def test_negative(self):
        x = "KTJJT"
        assert not is_hand_five_of_kind(x)

    def test_positive(self):
        x = "AAAAA"
        assert is_hand_five_of_kind(x)


class TestFourOfKind:
    def test_positive(self):
        x = "AAAA1"
        assert is_hand_four_of_kind(x)

    def test_negative(self):
        x = "AAAKK"
        assert not is_hand_four_of_kind(x)

    def test_five_of_kind(self):
        x = "AAAAA"
        assert not is_hand_four_of_kind(x)


class TestFullHouse:
    def test_positive(self):
        x = "AAAKK"
        assert is_hand_full_house(x)

    def test_negative(self):
        x = "A5556"
        assert not is_hand_full_house(x)


class TestThreeOfKind:
    def test_positive(self):
        x = "AAA56"
        assert is_hand_three_of_kind(x)

    def test_negative(self):
        x = "A6789"
        assert not is_hand_three_of_kind(x)

    def test_negative_another(self):
        x = "A6689"
        assert not is_hand_three_of_kind(x)

    def test_negative_when_4(self):
        x = "AAAAK"
        assert not is_hand_three_of_kind(x)

    def test_negative_when_5(self):
        x = "AAAAA"
        assert not is_hand_three_of_kind(x)


class TestTwoPair:
    def test_positive(self):
        x = "AAQQ3"
        assert is_hand_two_pair(x)

    def test_negative(self):
        x = "AA789"
        assert not is_hand_two_pair(x)

    def test_negative_another(self):
        x = "KKKQQ"
        assert not is_hand_two_pair(x)


class TestPair:
    def test_positive(self):
        x = "AA123"
        assert is_hand_pair(x)

    def test_negative(self):
        x = "56789"
        assert not is_hand_pair(x)

    def test_negative_on_hand_of_five(self):
        x = "TTTTT"
        assert not is_hand_pair(x)

    def test_negative_on_hand_of_four(self):
        x = "TTTTK"
        assert not is_hand_pair(x)

    def test_negative_on_hand_of_three(self):
        x = "TTKTQ"
        assert not is_hand_pair(x)


class TestHighCard:
    def test_positive(self):
        x = "A4769"
        assert is_hand_high_card(x)

    def test_negative(self):
        x = "A4T6T3"
        assert not is_hand_high_card(x)