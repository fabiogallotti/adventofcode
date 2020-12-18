from functions.read_input import read_input
from inputs.path import PATH

from .functions import solve_problem, preprocessing, find_invalid_values, valid_tickets

data = read_input(f"{PATH}/2020/day16.txt")

print(f"First part: {solve_problem(1, data)}")

# print(f"Second part: {solve_problem(2, data)}")
