from src.year2020.day11.functions import solve_problem


def test_part_1():

    data = [
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
        ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
    ]

    assert solve_problem(1, data) == 37


def test_part_2():
    data = [
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
        ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
    ]

    assert solve_problem(2, data) == 26
