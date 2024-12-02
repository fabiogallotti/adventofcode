from year2019.day04.functions import check_double, check_no_decrease, check_no_larger_group


def test_check_double():
    assert check_double("111111") == True
    assert check_double("223450") == True
    assert check_double("123789") == False


def test_check_no_decrease():
    assert check_no_decrease("111111") == True
    assert check_no_decrease("223450") == False
    assert check_no_decrease("123789") == True


def test_check_no_larger_group():
    assert check_no_larger_group("112233") == True
    assert check_no_larger_group("123444") == False
    assert check_no_larger_group("111122") == True
    assert check_no_larger_group("475578") == True
    assert check_no_larger_group("455978") == True
