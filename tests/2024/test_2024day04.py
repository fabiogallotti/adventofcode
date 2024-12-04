from year2024.day04.functions import part_1, part_2

EXAMPLE_1 = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 18


def test_part_2():
    assert part_2(EXAMPLE_1) == 9
