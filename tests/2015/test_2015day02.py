from src.year2015.day02.functions import calculate_area, calculate_ribbon, convert_to_int


def test_calculate_area():
    assert calculate_area(["2", "3", "4"]) == 58
    assert calculate_area(["1", "1", "10"]) == 43


def test_calculate_ribbon():
    assert calculate_ribbon(["2", "3", "4"]) == 34
    assert calculate_ribbon(["1", "1", "10"]) == 14


def test_convert_to_int():
    assert convert_to_int(["2", "3", "4"]) == (2, 3, 4)
