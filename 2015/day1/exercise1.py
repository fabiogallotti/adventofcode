from read_input import read_input

data = read_input("input.txt")

up = data.count("(")
down = data.count(")")

print(up - down)
