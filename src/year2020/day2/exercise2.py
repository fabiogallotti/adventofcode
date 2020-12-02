from functions.read_input import read_input
from inputs.path import PATH

from .functions import solve_problem

data = read_input(f"{PATH}/2020day2.txt")
data = [elem.split(" ") for elem in data]

print(solve_problem(data, 2))
