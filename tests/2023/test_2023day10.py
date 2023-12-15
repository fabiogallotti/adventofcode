from src.year2023.day10.functions import part_1

EXAMPLE_1 = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    ".....",
]

EXAMPLE_2 = [
    "-L|F7",
    "7S-7|",
    "L|7||",
    "-L-J|",
    "L|-JF",
]

EXAMPLE_3 = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ...",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 4
    assert part_1(EXAMPLE_2) == 4
    assert part_1(EXAMPLE_3) == 8


# EXAMPLE_4 = [
#     "...........",
#     ".S-------7.",
#     ".|F-----7|.",
#     ".||.....||.",
#     ".||.....||.",
#     ".|L-7.F-J|.",
#     ".|..|.|..|.",
#     ".L--J.L--J.",
#     "...........",
# ]


# def test_part_2():
#     assert part_2(EXAMPLE_4) == 4
