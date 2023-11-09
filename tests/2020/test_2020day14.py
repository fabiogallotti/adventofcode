from src.year2020.day14.functions import solve_problem


def test_solve_problem_1():
    data = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]

    assert solve_problem(1, data) == 165


def test_solve_problem_2():
    data = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]

    assert solve_problem(2, data) == 208
