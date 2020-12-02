def read_input(filename):
    with open(filename, "r") as f:
        return [elem for elem in f.read().split("\n")]
