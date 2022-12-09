from src.year2022.day09.functions import part_1, part_2

INPUT1 = [
    ["R", "4"],
    ["U", "4"],
    ["L", "3"],
    ["D", "1"],
    ["R", "4"],
    ["D", "1"],
    ["L", "5"],
    ["R", "2"],
]

INPUT2 = [
    ["R", "5"],
    ["U", "8"],
    ["L", "8"],
    ["D", "3"],
    ["R", "17"],
    ["D", "10"],
    ["L", "25"],
    ["U", "20"],
]


def test_part_1():
    assert part_1(INPUT1) == 13


def test_part_2():
    assert part_2(INPUT2) == 36
