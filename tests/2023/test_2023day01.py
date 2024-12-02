from year2023.day01.functions import part_1, part_2

EXAMPLE_1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 142


EXAMPLE_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def test_part_2():
    assert part_2(EXAMPLE_2) == 281
