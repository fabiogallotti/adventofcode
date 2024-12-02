from year2015.day01.functions import count_floors, first_basement, up_down


def test_count_floors():
    assert count_floors(["(", "(", ")", ")"]) == 0
    assert count_floors(["(", ")", "(", ")"]) == 0
    assert count_floors(["(", "(", "("]) == 3
    assert count_floors(["(", "(", ")", "(", "(", ")", "("]) == 3
    assert count_floors([")", ")", "(", "(", "(", "(", "("]) == 3
    assert count_floors(["(", ")", ")"]) == -1
    assert count_floors([")", ")", "("]) == -1
    assert count_floors([")", ")", ")"]) == -3
    assert count_floors([")", "(", ")", ")", "(", ")", ")"]) == -3


def test_up_down():
    assert up_down("(") == 1
    assert up_down(")") == -1


def test_first_basement():
    assert first_basement(")") == 1
    assert first_basement(["(", ")", "(", ")", ")"]) == 5
