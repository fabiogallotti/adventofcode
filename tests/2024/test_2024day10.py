from year2024.day10.functions import part_1, part_2

EXAMPLE_1 = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 36


def test_part_2():
    assert part_2(EXAMPLE_1) == 81
