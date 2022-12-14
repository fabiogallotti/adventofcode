from src.year2022.day14.functions import part_1, part_2

INPUT = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]


def test_part_1():
    assert part_1(INPUT) == 24


def test_part_2():
    assert part_2(INPUT) == 93
