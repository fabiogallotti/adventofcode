from src.year2020.day08.functions import find_positions, calculate_accumulator_value, calculate_value_switching_positions

def test_find_positions():
    data = [['nop', '+0'], ['acc', '+1'], ['jmp', '+4'], ['acc', '+3'], ['jmp', '-3'], ['acc', '-99'], ['acc', '+1'], ['jmp', '-4'], ['acc', '+6']]

    assert find_positions(data, "jmp") == [2, 4, 7]

def test_calculate_accumulator_value():
    data = [['nop', '+0'], ['acc', '+1'], ['jmp', '+4'], ['acc', '+3'], ['jmp', '-3'], ['acc', '-99'], ['acc', '+1'], ['jmp', '-4'], ['acc', '+6']]

    assert calculate_accumulator_value(data) == 5

def test_calculate_value_switching_positions():
    data = [['nop', '+0'], ['acc', '+1'], ['jmp', '+4'], ['acc', '+3'], ['jmp', '-3'], ['acc', '-99'], ['acc', '+1'], ['jmp', '-4'], ['acc', '+6']]

    jmp_positions = find_positions(data, "jmp")

    assert calculate_value_switching_positions(data, jmp_positions) == 8