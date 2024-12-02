from year2020.day10.functions import find_differences_one_three, find_distinct_ways


def test_find_differences_one_three():
    data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    assert find_differences_one_three(data) == 35

    data = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]

    assert find_differences_one_three(data) == 220


def test_find_distinct_ways():
    data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    assert find_distinct_ways(data) == 8

    data = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]

    assert find_distinct_ways(data) == 19208
