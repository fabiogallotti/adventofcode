from year2024.day02.functions import part_1, part_2

EXAMPLE_1 = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 2


def test_part_2():
    assert part_2(EXAMPLE_1) == 4
