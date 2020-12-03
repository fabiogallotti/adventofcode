from functions.read_input import read_input
from inputs.path import PATH

from .functions import product_of_multiple_slopes

data = read_input(f"{PATH}/2020/day3.txt")

print(product_of_multiple_slopes(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))