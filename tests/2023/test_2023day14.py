from year2023.day14.functions import part_1, part_2

EXAMPLE = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]


def test_part_1():
    assert part_1(EXAMPLE) == 136


def test_part_2():
    assert part_2(EXAMPLE) == 64
