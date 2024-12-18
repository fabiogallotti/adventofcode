from year2024.day12.functions import part_1, part_2

EXAMPLE_1 = [
    "AAAA",
    "BBCD",
    "BBCC",
    "EEEC",
]

EXAMPLE_2 = [
    "OOOOO",
    "OXOXO",
    "OOOOO",
    "OXOXO",
    "OOOOO",
]

EXAMPLE_3 = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]


EXAMPLE_4 = [
    "EEEEE",
    "EXXXX",
    "EEEEE",
    "EXXXX",
    "EEEEE",
]


EXAMPLE_5 = [
    "AAAAAA",
    "AAABBA",
    "AAABBA",
    "ABBAAA",
    "ABBAAA",
    "AAAAAA",
]


def test_part_1():
    assert part_1(EXAMPLE_1) == 140
    assert part_1(EXAMPLE_2) == 772
    assert part_1(EXAMPLE_3) == 1930


def test_part_2():
    assert part_2(EXAMPLE_1) == 80
    assert part_2(EXAMPLE_2) == 436
    assert part_2(EXAMPLE_3) == 1206
    assert part_2(EXAMPLE_4) == 236
    assert part_2(EXAMPLE_5) == 368
