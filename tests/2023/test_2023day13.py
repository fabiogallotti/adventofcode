from year2023.day13.functions import part_1, part_2

EXAMPLE = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]


def test_part_1():
    assert part_1(EXAMPLE) == 405


def test_part_2():
    assert part_2(EXAMPLE) == 400
