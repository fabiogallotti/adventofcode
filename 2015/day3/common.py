def read_input(filename):
    with open(filename, "r") as f:
        return [elem for elem in f.read()]


def move(elem, house):
    if elem == ">":
        house[0] += 1
    elif elem == "<":
        house[0] += -1
    elif elem == "^":
        house[1] += 1
    elif elem == "v":
        house[1] += -1
