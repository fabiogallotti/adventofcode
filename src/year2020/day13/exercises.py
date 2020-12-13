from functions.read_input import read_input
from inputs.path import PATH

from .functions import solve_problem

data = read_input(f"{PATH}/2020/day13.txt")

print(f"First part: {solve_problem(1, data.copy())}")

print(f"Second part: {solve_problem(2, data.copy())}")
