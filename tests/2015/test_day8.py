from src.year2015.day8.functions import (
    string_representation_length,
    memory_representation_length,
    difference_string_memory,
)


def test_string_representation_length():
    input = [['""'], ['"abc"'], ['"aaa\\"aaa"'], ['"\\x27"']]
    assert string_representation_length(input) == 23


def test_memory_representation_length():
    input = [['""'], ['"abc"'], ['"aaa\\"aaa"'], ['"\\x27"']]
    assert memory_representation_length(input) == 11


def test_difference_string_memory():
    input = [['""'], ['"abc"'], ['"aaa\\"aaa"'], ['"\\x27"']]
    assert difference_string_memory(input) == 12
