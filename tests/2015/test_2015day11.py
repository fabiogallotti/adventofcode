from year2015.day11.functions import (
    check_increasing_straight,
    check_iol,
    check_two_pairs,
    check_valid,
    next_password,
    next_word,
)


def test_check_increasing_straight():
    assert check_increasing_straight("hijklmmn") == True
    assert check_increasing_straight("abbceffg") == False
    assert check_increasing_straight("abbcegjk") == False


def test_check_iol():
    assert check_iol("hijklmmn") == False
    assert check_iol("abbceffg") == True
    assert check_iol("abbcegjk") == True


def test_check_two_pairs():
    assert check_two_pairs("hijklmmn") == False
    assert check_two_pairs("abbceffg") == True
    assert check_two_pairs("abbcegjk") == False


def test_check_valid():
    assert check_valid("hijklmmn") == False
    assert check_valid("abbceffg") == False
    assert check_valid("abbcegjk") == False
    assert check_valid("abcdffaa") == True
    assert check_valid("ghjaabcc") == True


def test_next_password():
    assert next_password("abcdefgh") == "abcdffaa"


def test_next_word():
    assert next_word("abcdefgh") == "abcdefgi"
