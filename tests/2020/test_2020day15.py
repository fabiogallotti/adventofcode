from year2020.day15.functions import game


def test_game():
    assert game([0, 3, 6], 2020) == 436
    assert game([1, 3, 2], 2020) == 1
    assert game([2, 1, 3], 2020) == 10
    assert game([1, 2, 3], 2020) == 27
    assert game([2, 3, 1], 2020) == 78
    assert game([3, 2, 1], 2020) == 438
    assert game([3, 1, 2], 2020) == 1836
