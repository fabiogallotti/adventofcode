from year2020.day13.functions import solve_problem


def test_solve_problem_1():
    assert solve_problem(1, ["939", "7,13,x,x,59,x,31,19"]) == 295


def test_solve_problem_2():
    assert solve_problem(2, ["x", "7,13,x,x,59,x,31,19"]) == 1068781
    assert solve_problem(2, ["x", "17,x,13,19"]) == 3417
    assert solve_problem(2, ["x", "67,7,59,61"]) == 754018
    assert solve_problem(2, ["x", "67,x,7,59,61"]) == 779210
    assert solve_problem(2, ["x", "67,7,x,59,61"]) == 1261476
    assert solve_problem(2, ["x", "1789,37,47,1889"]) == 1202161486
