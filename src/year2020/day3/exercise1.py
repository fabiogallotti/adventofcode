from functions.read_input import read_input
from inputs.path import PATH

from .functions import trees_for_given_slope

data = read_input(f"{PATH}/2020/day3.txt")


print(trees_for_given_slope(data, 3, 1))