from year2024.day08.functions import part_1, part_2

EXAMPLE_1 = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 14


def test_part_2():
    assert part_2(EXAMPLE_1) == 34
