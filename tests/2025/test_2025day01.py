from year2025.day01.functions import part_1, part_2

EXAMPLE_1 = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 3


def test_part_2():
    assert part_2(EXAMPLE_1) == 6
