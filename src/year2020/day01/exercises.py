from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_set_of_n_candidates, multiply_elements_set

data = read_input(f"{PATH}/2020/day01.txt")

numbers2 = find_set_of_n_candidates(data, 2, 2020)
numbers3 = find_set_of_n_candidates(data, 3, 2020)

print(f"First part: {multiply_elements_set(numbers2)}")

print(f"Second part: {multiply_elements_set(numbers3)}")
