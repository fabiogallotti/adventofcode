from src.year2022.day02.functions import part_1, part_2

STRATEGY = [
    ["A", "Y"],
    ["B", "X"],
    ["C", "Z"],
]


def test_part_1():
    assert part_1(STRATEGY) == 15


def test_part_2():
    assert part_2(STRATEGY) == 12
