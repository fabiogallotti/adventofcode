def read_one_line(filename):
    with open(filename, "r") as f:
        return [elem for elem in f.read()]


def read_multiple_lines_x_separated(filename):
    with open(filename, "r") as f:
        return [x.split("x") for x in f.read().split("\n")]


def read_multiple_lines(filename):
    with open(filename, "r") as f:
        return [elem for elem in f.read().split("\n")]
