from year2024.day06.functions import part_1, part_2

EXAMPLE_1 = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 41


def test_part_2():
    assert part_2(EXAMPLE_1) == 6
