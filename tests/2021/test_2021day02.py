from src.year2021.day02.functions import part_1, part_2

DATA = [
    ["forward", "5"],
    ["down", "5"],
    ["forward", "8"],
    ["up", "3"],
    ["down", "8"],
    ["forward", "2"],
]


def test_single():
    assert part_1(DATA) == 150


def test_three():
    assert part_2(DATA) == 900
