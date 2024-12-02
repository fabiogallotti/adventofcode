from functions.functions import manhattan


def test_manhattan():
    assert manhattan([(-1056, 121), (1, -1)]) == [1177, 2]
