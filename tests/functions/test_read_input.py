from src.functions.read_input import read_input

PATH = "tests/functions/resources"


def test_read_one_line():
    assert read_input(f"{PATH}/one_line.txt") == ["abc()#"]


def test_multiple_lines_x_separated():
    assert read_input(f"{PATH}/multiple_lines_x_separated.txt") == ["1x2x3", "10x11x12"]


def test_multiple_lines():
    assert read_input(f"{PATH}/multiple_lines.txt") == [
        "wkzasuyckmgwddwy",
        "eixpkpdhsjmynxhi",
    ]


def test_multiple_lines_space_separated():
    assert read_input(f"{PATH}/multiple_lines_space_separated.txt") == [
        "turn on 887,9 through 959,629",
        "turn on 454,398 through 844,448",
    ]
