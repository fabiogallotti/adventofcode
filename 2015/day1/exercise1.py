def read_input(filename):
    with open(filename, "r") as f:
        return [ elem for elem in f.read() ]


data = read_input("input.txt")

up = data.count("(")
down = data.count(")")

print(up-down)