def read_one_line(filename):
    with open(filename, "r") as f:
        return [elem for elem in f.read()]


def read_multiple_lines_separated(filename, separator):
    with open(filename, "r") as f:
        return [elem.split(separator) for elem in f.read().split("\n")]


def read_multiple_lines(filename):
    with open(filename, "r") as f:
        return [elem for elem in f.read().split("\n")]

