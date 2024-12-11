from year2015.day01.exercises import part_1, part_2

EXAMPLE_1 = ["(())"]
EXAMPLE_2 = ["()()"]
EXAMPLE_3 = ["((("]
EXAMPLE_4 = ["(()(()("]
EXAMPLE_5 = ["))((((("]
EXAMPLE_6 = ["())"]
EXAMPLE_7 = ["))("]
EXAMPLE_8 = [")))"]
EXAMPLE_9 = [")())())"]


def test_part_1():
    assert part_1(EXAMPLE_1) == 0
    assert part_1(EXAMPLE_2) == 0
    assert part_1(EXAMPLE_3) == 3
    assert part_1(EXAMPLE_4) == 3
    assert part_1(EXAMPLE_5) == 3
    assert part_1(EXAMPLE_6) == -1
    assert part_1(EXAMPLE_7) == -1
    assert part_1(EXAMPLE_8) == -3
    assert part_1(EXAMPLE_9) == -3


EXAMPLE_10 = [")"]
EXAMPLE_11 = ["()())"]


def test_part_2():
    assert part_2(EXAMPLE_10) == 1
    assert part_2(EXAMPLE_11) == 5
