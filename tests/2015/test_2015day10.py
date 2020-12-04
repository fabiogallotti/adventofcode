from src.year2015.day10.functions import apply_look_and_say_n_times


def test_apply_look_and_say_n_times():
    assert apply_look_and_say_n_times("211", 1) == 4
    assert apply_look_and_say_n_times("1", 5) == 6
