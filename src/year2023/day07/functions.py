from collections import Counter
from pydantic import BaseModel
from enum import Enum


class Type(int, Enum):
    FIVE = 7
    FOUR = 6
    FULL = 5
    THREE = 4
    TWO = 3
    ONE = 2
    HIGH = 1


class CardStrength(int, Enum):
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10


class Hand(BaseModel):
    cards: str
    bid: int


class DecodedHand(BaseModel):
    cards: list[int]
    bid: int
    type_: Type | None = None


def part_1(data):
    hands = [Hand(cards=x.split()[0], bid=x.split()[1]) for x in data]

    decoded_hands = []
    for hand in hands:
        decoded_cards = []
        for card in hand.cards:
            if card in CardStrength.__members__:
                decoded_cards.append(CardStrength[card].value)
            else:
                decoded_cards.append(int(card))
        decoded_hands.append(DecodedHand(cards=decoded_cards, bid=hand.bid))

    sorted_hands = sorted(decoded_hands, key=lambda x: x.cards)
    hand_types = [
        DecodedHand(**hand.model_dump(exclude={"type_"}), type_=get_hand_type(hand=hand))
        for hand in sorted_hands
    ]

    sorted_hand_type = sorted(hand_types, key=lambda hand_type: hand_type.type_.value)

    return sum(hand.bid * (i + 1) for i, hand in enumerate(sorted_hand_type))


def get_hand_type(hand):
    value_counts = Counter(hand.cards)

    jolly = value_counts[0]

    if jolly in [4, 5]:
        return Type.FIVE

    elif jolly == 3:
        second_common = value_counts.most_common(2)[1]
        value_counts[second_common[0]] += jolly
        del value_counts[0]

    elif jolly == 2:
        all_cards = value_counts.most_common()
        if all_cards.index((0, 2)) == 0:
            second_common = value_counts.most_common(2)[1]
            value_counts[second_common[0]] += jolly
            del value_counts[0]
        else:
            first_common = value_counts.most_common(1)[0]
            value_counts[first_common[0]] += jolly
            del value_counts[0]

    elif jolly == 1:
        all_cards = value_counts.most_common()
        if all_cards.index((0, 1)) == 0:
            return Type.ONE

        first_common = value_counts.most_common(1)[0]
        value_counts[first_common[0]] += jolly
        del value_counts[0]

    if 5 in value_counts.values():
        return Type.FIVE
    elif 4 in value_counts.values():
        return Type.FOUR
    elif set(value_counts.values()) == {3, 2}:
        return Type.FULL
    elif 3 in value_counts.values():
        return Type.THREE
    elif list(value_counts.values()).count(2) == 2:
        return Type.TWO
    elif 2 in value_counts.values():
        return Type.ONE
    return Type.HIGH


class CardStrength2(int, Enum):
    A = 14
    K = 13
    Q = 12
    J = 0
    T = 10


def part_2(data):
    hands = [Hand(cards=x.split()[0], bid=x.split()[1]) for x in data]

    decoded_hands = []
    for hand in hands:
        decoded_cards = []
        for card in hand.cards:
            if card in CardStrength2.__members__:
                decoded_cards.append(CardStrength2[card].value)
            else:
                decoded_cards.append(int(card))
        decoded_hands.append(DecodedHand(cards=decoded_cards, bid=hand.bid))

    sorted_hands = sorted(decoded_hands, key=lambda x: x.cards)
    hand_types = [
        DecodedHand(**hand.model_dump(exclude={"type_"}), type_=get_hand_type(hand=hand))
        for hand in sorted_hands
    ]

    sorted_hand_type = sorted(hand_types, key=lambda hand_type: hand_type.type_.value)

    return sum(hand.bid * (i + 1) for i, hand in enumerate(sorted_hand_type))
