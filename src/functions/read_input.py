def read_input(filename):
    with open(filename) as f:
        return list(f.read().split("\n"))
