from year2025.day05.functions import part_1, part_2

EXAMPLE_1 = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 3


def test_part_2():
    assert part_2(EXAMPLE_1) == 14
