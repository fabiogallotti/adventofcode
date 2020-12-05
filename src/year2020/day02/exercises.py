from functions.read_input import read_input
from inputs.path import PATH

from .functions import solve_problem

data = read_input(f"{PATH}/2020/day2.txt")
data = [elem.split(" ") for elem in data]

print(f"First part: {solve_problem(data, 1)}")

print(f"Second part: {solve_problem(data, 2)}")
