from year2020.day01.functions import find_set_of_n_candidates, multiply_elements_set


def test_two_elements():
    numbers = find_set_of_n_candidates(["1721", "979", "366", "299", "675", "1456"], 2, 2020)

    assert multiply_elements_set(numbers) == 514579


def test_three_elements():
    numbers = find_set_of_n_candidates(["1721", "979", "366", "299", "675", "1456"], 3, 2020)

    assert multiply_elements_set(numbers) == 241861950
