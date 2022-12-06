from src.year2021.day03.functions import part_1, part_2

INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_part_1():
    assert part_1(INPUT) == 198


def test_part_2():
    assert part_2(INPUT) == 230
