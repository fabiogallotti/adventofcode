from year2015.day02.exercises import part_1, part_2

EXAMPLE_1 = ["2x3x4"]
EXAMPLE_2 = ["1x1x10"]


def test_part_1():
    assert part_1(EXAMPLE_1) == 58
    assert part_1(EXAMPLE_2) == 43


def test_part_2():
    assert part_2(EXAMPLE_1) == 34
    assert part_2(EXAMPLE_2) == 14
