from src.year2019.day02.functions import calculate, set_initial_state


def test_calculate():
    assert calculate([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [
        3500,
        9,
        10,
        70,
        2,
        3,
        11,
        0,
        99,
        30,
        40,
        50,
    ]
    assert calculate([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert calculate([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert calculate([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert calculate([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_set_initial_state():
    data = [1, 0, 0, 0, 99]
    set_initial_state(data, 1, 2)
    assert data == [1, 1, 2, 0, 99]
