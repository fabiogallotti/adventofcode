from common import calculate_area, calculate_ribbon


def test_calculate_area():
    assert calculate_area([2, 3, 4]) == 58
    assert calculate_area([1, 1, 10]) == 43


def test_calculate_ribbon():
    assert calculate_ribbon([2, 3, 4]) == 34
    assert calculate_ribbon([1, 1, 10]) == 14
