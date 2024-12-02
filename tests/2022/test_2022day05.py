from year2022.day05.functions import part_1, part_2

INPUT = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_part_1():
    assert part_1(INPUT) == "CMZ"


def test_part_2():
    assert part_2(INPUT) == "MCD"
