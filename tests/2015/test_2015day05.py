from year2015.day05.exercises import part_1, part_2

EXAMPLE_1 = ["ugknbfddgicrmopn"]
EXAMPLE_2 = ["aaa"]
EXAMPLE_3 = ["jchzalrnumimnmhp"]
EXAMPLE_4 = ["haegwjzuvuyypxyu"]
EXAMPLE_5 = ["dvszwmarrgswjxmb"]


def test_part_1():
    assert part_1(EXAMPLE_1) == 1
    assert part_1(EXAMPLE_2) == 1
    assert part_1(EXAMPLE_3) == 0
    assert part_1(EXAMPLE_4) == 0
    assert part_1(EXAMPLE_5) == 0


EXAMPLE_6 = ["qjhvhtzxzqqjkmpb"]
EXAMPLE_7 = ["xxyxx"]
EXAMPLE_8 = ["uurcxstgmygtbstg"]
EXAMPLE_9 = ["ieodomkazucvgmuy"]


def test_part_2():
    assert part_2(EXAMPLE_6) == 1
    assert part_2(EXAMPLE_7) == 1
    assert part_2(EXAMPLE_8) == 0
    assert part_2(EXAMPLE_9) == 0
