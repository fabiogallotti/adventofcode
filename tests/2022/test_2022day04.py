from year2022.day04.functions import part_1, part_2

INPUT = [
    [["2", "4"], ["6", "8"]],
    [["2", "3"], ["4", "5"]],
    [["5", "7"], ["7", "9"]],
    [["2", "8"], ["3", "7"]],
    [["6", "6"], ["4", "6"]],
    [["2", "6"], ["4", "8"]],
]


def test_part_1():
    assert part_1(INPUT) == 2


def test_part_2():
    assert part_2(INPUT) == 4
