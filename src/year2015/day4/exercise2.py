from functions.read_input import read_input
from inputs.path import PATH

from .functions import starting_zeros

key = read_input(f"{PATH}/2015/day4.txt")

print(starting_zeros(key[0], 6))
