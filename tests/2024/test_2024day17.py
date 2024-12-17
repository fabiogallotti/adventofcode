from year2024.day17.functions import part_1, part_2

EXAMPLE_1 = [
    "Register A: 729",
    "Register B: 0",
    "Register C: 0",
    "",
    "Program: 0,1,5,4,3,0",
]

EXAMPLE_2 = [
    "Register A: 2024",
    "Register B: 0",
    "Register C: 0",
    "",
    "Program: 0,3,5,4,3,0",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == "4,6,3,5,6,3,5,2,1,0"


def test_part_2():
    assert part_2(EXAMPLE_2) == 117440
