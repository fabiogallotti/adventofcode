from src.year2022.day12.functions import part_1, part_2

INPUT = [
    ["S", "a", "b", "q", "p", "o", "n", "m"],
    ["a", "b", "c", "r", "y", "x", "x", "l"],
    ["a", "c", "c", "s", "z", "E", "x", "k"],
    ["a", "c", "c", "t", "u", "v", "w", "j"],
    ["a", "b", "d", "e", "f", "g", "h", "i"],
]


def test_part_1():
    assert part_1(INPUT) == 31


def test_part_2():
    assert part_2(INPUT) == 29
