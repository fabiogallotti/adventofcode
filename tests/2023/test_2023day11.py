from year2023.day11.functions import part_1, part_2

EXAMPLE = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]


def test_part_1():
    assert part_1(EXAMPLE, expansion=1) == 374


def test_part_2():
    assert part_2(EXAMPLE, expansion=9) == 1030
    assert part_2(EXAMPLE, expansion=99) == 8410
