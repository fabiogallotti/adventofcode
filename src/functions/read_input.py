def read_input(filename):
    with open(filename, "r") as f:
        return list(f.read().split("\n"))
