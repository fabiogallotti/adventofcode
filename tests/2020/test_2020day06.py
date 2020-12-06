from src.year2020.day06.functions import how_many_in_group, preprocessing, solve_problem


def test_preprocessing():
    data = ["abc", "", "a", "b", "c"]

    assert preprocessing(data) == [{"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1, "c": 1}]


def test_how_many_in_group():
    data = ["abc", "", "a", "b", "c"]
    forms = [{"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1, "c": 1}]

    assert how_many_in_group(forms, data) == [1, 3]


def test_solve_problem():
    data = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    ]

    forms = preprocessing(data)
    how_many = how_many_in_group(forms, data)

    assert solve_problem(1, forms) == 11
    assert solve_problem(2, forms, how_many) == 6
