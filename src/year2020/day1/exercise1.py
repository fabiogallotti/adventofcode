from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_set_of_n_candidates, multiply_elements_set

data = read_input(f"{PATH}/2020/day1.txt")

numbers = find_set_of_n_candidates(data, 2, 2020)

print(multiply_elements_set(numbers))
