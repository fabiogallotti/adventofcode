from functions.read_input import read_multiple_lines_separated
from inputs.path import PATH

from .functions import solve_problem

data = read_multiple_lines_separated(f"{PATH}/2020day2.txt", " ")

print(solve_problem(data, 2))
