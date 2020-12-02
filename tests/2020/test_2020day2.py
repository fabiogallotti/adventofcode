from src.year2020.day2.functions import preprocessing, solve_problem


def test_preprocessing():
    minimum, maximum, letter, password = preprocessing(["1-3", "a:", "abcde"])
    assert minimum == 1
    assert maximum == 3
    assert letter == "a"
    assert password == "abcde"


def test_solve_problem_1():
    assert (
        solve_problem(
            [
                ["1-3", "a:", "abcde"],
                ["1-3", "b:", "cdefg"],
                ["2-9", "c:", "ccccccccc"],
            ],
            1,
        )
        == 2
    )


def test_solve_problem_2():
    assert (
        solve_problem(
            [
                ["1-3", "a:", "abcde"],
                ["1-3", "b:", "cdefg"],
                ["2-9", "c:", "ccccccccc"],
            ],
            2,
        )
        == 1
    )


def test_solve_problem_2_custom():
    assert (
        solve_problem(
            [
                ["1-3", "a:", "abcde"],
                ["1-3", "b:", "cdbfg"],
                ["2-9", "c:", "ccccccccc"],
            ],
            2,
        )
        == 2
    )
