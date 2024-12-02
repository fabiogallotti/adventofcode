from year2015.day08.functions import (
    difference_new_string,
    difference_string_memory,
    memory_representation_length,
    string_representation_length,
)


def test_string_representation_length():
    input = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    assert string_representation_length(input) == 23


def test_memory_representation_length():
    input = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    assert memory_representation_length(input) == 11


def test_difference_string_memory():
    input = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    assert difference_string_memory(input) == 12


def test_difference_new_memory():
    input = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    assert difference_new_string(input) == 19
