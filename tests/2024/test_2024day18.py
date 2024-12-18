from year2024.day18.functions import part_1, part_2

EXAMPLE_1 = [
    "5,4",
    "4,2",
    "4,5",
    "3,0",
    "2,1",
    "6,3",
    "2,4",
    "1,5",
    "0,6",
    "3,3",
    "2,6",
    "5,1",
    "1,2",
    "5,5",
    "2,5",
    "6,5",
    "1,4",
    "0,4",
    "6,4",
    "1,1",
    "6,1",
    "1,0",
    "0,5",
    "1,6",
    "2,0",
]


def test_part_1():
    assert part_1(EXAMPLE_1, max_x=7, max_y=7, fallen=12) == 22


def test_part_2():
    assert part_2(EXAMPLE_1, max_x=7, max_y=7) == "6,1"
