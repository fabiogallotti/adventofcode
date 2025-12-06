from year2025.day06.functions import part_1, part_2

EXAMPLE_1 = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 4277556


def test_part_2():
    assert part_2(EXAMPLE_1) == 3263827
