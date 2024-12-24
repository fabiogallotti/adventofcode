from year2024.day22.functions import part_1, part_2

EXAMPLE_1 = [
    "1",
    "10",
    "100",
    "2024",
]
EXAMPLE_2 = [
    "1",
    "2",
    "3",
    "2024",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 37327623


def test_part_2():
    assert part_2(EXAMPLE_2) == 23
