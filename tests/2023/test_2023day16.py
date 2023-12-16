from src.year2023.day16.functions import part_1, part_2

EXAMPLE = [
    ".|...\\....",
    "|.-.\\.....",
    ".....|-...",
    "........|.",
    "..........",
    ".........\\",
    "..../.\\\\..",
    ".-.-/..|..",
    ".|....-|.\\",
    "..//.|....",
]


def test_part_1():
    assert part_1(EXAMPLE) == 46


def test_part_2():
    assert part_2(EXAMPLE) == 51
