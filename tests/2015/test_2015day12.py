from year2015.day12.functions import sum_ints, sum_ints_no_red


def test_sum_ints():
    assert sum_ints([1, 2, 3]) == 6
    assert sum_ints({"a": 2, "b": 4}) == 6
    assert sum_ints([[[3]]]) == 3
    assert sum_ints({"a": {"b": 4}, "c": -1}) == 3
    assert sum_ints({"a": [-1, 1]}) == 0
    assert sum_ints([-1, {"a": 1}]) == 0
    assert sum_ints([]) == 0
    assert sum_ints({}) == 0


def test_sum_ints_no_red():
    assert sum_ints_no_red([1, 2, 3]) == 6
    assert sum_ints_no_red([1, {"c": "red", "b": 2}, 3]) == 4
    assert sum_ints_no_red({"d": "red", "e": [1, 2, 3, 4], "f": 5}) == 0
    assert sum_ints_no_red([1, "red", 5]) == 6
    assert sum_ints_no_red({"a": {"b": 4}, "c": -1}) == 3
