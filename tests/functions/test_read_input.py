from src.functions.read_input import (
    read_one_line,
    read_multiple_lines_x_separated,
    read_multiple_lines,
)

PATH = "tests/functions/resources"


def test_read_one_line():
    assert read_one_line(f"{PATH}/one_line.txt") == ["a", "b", "c", "(", ")", "#"]


def test_multiple_lines_x_separated():
    assert read_multiple_lines_x_separated(
        f"{PATH}/multiple_lines_x_separated.txt"
    ) == [["1", "2", "3"], ["10", "11", "12"]]


def test_multiple_lines():
    assert read_multiple_lines(f"{PATH}/multiple_lines.txt") == [
        "wkzasuyckmgwddwy",
        "eixpkpdhsjmynxhi",
    ]
