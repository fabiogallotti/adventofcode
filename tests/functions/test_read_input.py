from src.functions.read_input import (
    read_multiple_lines,
    read_multiple_lines_separated,
    read_one_line,
)

PATH = "tests/functions/resources"


def test_read_one_line():
    assert read_one_line(f"{PATH}/one_line.txt") == ["a", "b", "c", "(", ")", "#"]


def test_multiple_lines_x_separated():
    assert read_multiple_lines_separated(
        f"{PATH}/multiple_lines_x_separated.txt", "x"
    ) == [["1", "2", "3"], ["10", "11", "12"]]

def test_multiple_lines():
    assert read_multiple_lines(f"{PATH}/multiple_lines.txt") == [
        "wkzasuyckmgwddwy",
        "eixpkpdhsjmynxhi",
    ]

def test_multiple_lines_space_separated():
    assert read_multiple_lines_separated(
        f"{PATH}/multiple_lines_space_separated.txt", " "
    ) == [["turn", "on", "887,9", "through", "959,629"], ["turn", "on", "454,398", "through", "844,448"]]