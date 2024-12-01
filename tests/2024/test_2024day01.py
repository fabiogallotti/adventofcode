from src.year2024.day01.functions import part_1, part_2

EXAMPLE_1 = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 11


def test_part_2():
    assert part_2(EXAMPLE_1) == 31
