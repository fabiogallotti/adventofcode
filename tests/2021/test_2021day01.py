from src.year2021.day01.functions import find_single_increase, find_three_increase

NUMBERS = [int(x) for x in ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]]


def test_single():
    assert find_single_increase(NUMBERS) == 7


def test_three():
    assert find_three_increase(NUMBERS) == 5
