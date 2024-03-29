from functions.read_input import read_input
from inputs.path import PATH

from .functions import product_of_multiple_slopes, trees_for_given_slope

data = read_input(f"{PATH}/2020/day03.txt")

print(f"First part: {trees_for_given_slope(data, 3, 1)}")

print(f"Second part: {product_of_multiple_slopes(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])}")
