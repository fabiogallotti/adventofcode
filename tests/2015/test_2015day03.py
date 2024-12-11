from year2015.day03.exercises import part_1, part_2

EXAMPLE_1 = [">"]
EXAMPLE_2 = ["^>v<"]
EXAMPLE_3 = ["^v^v^v^v^v"]


def test_part_1():
    assert part_1(EXAMPLE_1) == 2
    assert part_1(EXAMPLE_2) == 4
    assert part_1(EXAMPLE_3) == 2


EXAMPLE_4 = ["^v"]


def test_part_2():
    assert part_2(EXAMPLE_4) == 3
    assert part_2(EXAMPLE_2) == 3
    assert part_2(EXAMPLE_3) == 11
