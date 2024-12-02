from year2022.day01.functions import part_1, part_2

CALORIES = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


def test_part_1():
    assert part_1(CALORIES) == 24000


def test_part_2():
    assert part_2(CALORIES) == 45000
