from functions.read_input import read_input
from inputs.path import PATH

from .functions import how_many_in_group, preprocessing, solve_problem

data = read_input(f"{PATH}/2020/day06.txt")

forms = preprocessing(data)

how_many = how_many_in_group(forms, data)

print(f"First part: {solve_problem(1, forms)}")

print(f"Second part: {solve_problem(2, forms, how_many)}")
