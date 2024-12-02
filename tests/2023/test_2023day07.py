from year2023.day07.functions import part_1, part_2

EXAMPLE = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def test_part_1():
    assert part_1(EXAMPLE) == 6440


def test_part_2():
    assert part_2(EXAMPLE) == 5905
