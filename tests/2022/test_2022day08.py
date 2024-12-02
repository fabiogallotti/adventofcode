from year2022.day08.functions import part_1, part_2

INPUT = [
    ["3", "0", "3", "7", "3"],
    ["2", "5", "5", "1", "2"],
    ["6", "5", "3", "3", "2"],
    ["3", "3", "5", "4", "9"],
    ["3", "5", "3", "9", "0"],
]


def test_part_1():
    assert part_1(INPUT) == 21


def test_part_2():
    assert part_2(INPUT) == 8
