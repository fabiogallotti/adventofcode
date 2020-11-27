from common_day5 import (
    three_vowels,
    twice_in_a_row,
    contains,
    nice_string_first,
    pair_two_letters,
    repeats_with_one_between,
    nice_string_second,
)


def test_three_vowels():
    assert three_vowels("aei") == True
    assert three_vowels("aba") == False


def test_twice_in_a_row():
    assert twice_in_a_row("xx") == True
    assert twice_in_a_row("abcdde") == True
    assert twice_in_a_row("aabbccdd") == True
    assert twice_in_a_row("abcd") == False


def test_contains():
    assert contains("xyz") == True
    assert contains("aaa") == False


def test_nice_string_first():
    assert nice_string_first("ugknbfddgicrmopn") == True
    assert nice_string_first("aaa") == True
    assert nice_string_first("jchzalrnumimnmhp") == False
    assert nice_string_first("haegwjzuvuyypxyu") == False
    assert nice_string_first("dvszwmarrgswjxmb") == False


def test_pair_two_letters():
    assert pair_two_letters("aaa") == False
    assert pair_two_letters("xyxy") == True
    assert pair_two_letters("aabcdefgaa") == True


def test_repeats_with_one_between():
    assert repeats_with_one_between("xyx") == True
    assert repeats_with_one_between("abcdefeghi") == True
    assert repeats_with_one_between("abc") == False


def test_nice_string_second():
    assert nice_string_second("qjhvhtzxzqqjkmpb") == True
    assert nice_string_second("xxyxx") == True
    assert nice_string_second("uurcxstgmygtbstg") == False
    assert nice_string_second("ieodomkazucvgmuy") == False
