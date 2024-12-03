from year2024.day03.functions import part_1, part_2

EXAMPLE_1 = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]

EXAMPLE_2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


def test_part_1():
    assert part_1(EXAMPLE_1) == 161


def test_part_2():
    assert part_2(EXAMPLE_2) == 48
