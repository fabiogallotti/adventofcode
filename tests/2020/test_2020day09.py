from src.year2020.day09.functions import find_not_sum_preamble, sum_weakness


def test_find_not_sum_preamble():
    data = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]

    assert find_not_sum_preamble(data, 5) == 127


def test_sum_weakness():
    data = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]

    assert sum_weakness(data, 127) == 62
