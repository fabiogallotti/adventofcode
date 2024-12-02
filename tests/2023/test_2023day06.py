from year2023.day06.functions import part_1, part_2

EXAMPLE = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def test_part_1():
    assert part_1(EXAMPLE) == 288


def test_part_2():
    assert part_2(EXAMPLE) == 71503
