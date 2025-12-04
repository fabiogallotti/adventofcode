from year2025.day03.functions import part_1, part_2

EXAMPLE_1 = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 357


def test_part_2():
    assert part_2(EXAMPLE_1) == 3121910778619
