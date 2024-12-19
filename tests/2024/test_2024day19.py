from year2024.day19.functions import part_1, part_2

EXAMPLE_1 = [
    "r, wr, b, g, bwu, rb, gb, br",
    "",
    "brwrr",
    "bggr",
    "gbbr",
    "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 6


def test_part_2():
    assert part_2(EXAMPLE_1) == 16
