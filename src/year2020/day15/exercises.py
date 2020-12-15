from functions.read_input import read_input
from inputs.path import PATH

# from .functions import solve_problem

data = read_input(f"{PATH}/2020/day15.txt")
data = data[0].split(",")
data = [int(elem) for elem in data]

print(f"First part: {game(data, 2020)}")

print(f"Second part: {game(data, 30000000)}")
