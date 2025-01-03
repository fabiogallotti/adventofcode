from year2023.day10.functions import part_1, part_2

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


EXAMPLE_4 = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
]

EXAMPLE_5 = [
    ".F----7F7F7F7F-7....",
    ".|F--7||||||||FJ....",
    ".||.FJ||||||||L7....",
    "FJL7L7LJLJ||LJ.L-7..",
    "L--J.L7...LJS7F-7L7.",
    "....F-J..F7FJ|L7L7L7",
    "....L7.F7||L7|.L7L7|",
    ".....|FJLJ|FJ|F7|.LJ",
    "....FJL-7.||.||||...",
    "....L---J.LJ.LJLJ...",
]


EXAMPLE_6 = [
    "FF7FSF7F7F7F7F7F---7",
    "L|LJ||||||||||||F--J",
    "FL-7LJLJ||||||LJL-77",
    "F--JF--7||LJLJ7F7FJ-",
    "L---JF-JLJ.||-FJLJJ7",
    "|F|F-JF---7F7-L7L|7|",
    "|FFJF7L7F-JF7|JL---7",
    "7-L-JL7||F7|L7F-7F7|",
    "L.L7LFJ|||||FJL7||LJ",
    "L7JLJL-JLJLJL--JLJ.L",
]


def test_part_2():
    assert part_2(EXAMPLE_4) == 4
    assert part_2(EXAMPLE_5) == 8
    assert part_2(EXAMPLE_6) == 10
