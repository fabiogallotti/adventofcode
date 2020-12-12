from src.year2020.day12.functions import solve_problem


def test_solve_problem_1():

    data = ["F10", "N3", "F7", "R90", "F11", "R180", "F1", "W1", "R270", "F1", "S1", "E3"]
    assert solve_problem(1, data) == 26


def test_solve_problem_2():

    data = ["F10", "N3", "F7", "R90", "F11", "R180", "W1", "R270", "S1", "E3"]
    assert solve_problem(2, data) == 286
