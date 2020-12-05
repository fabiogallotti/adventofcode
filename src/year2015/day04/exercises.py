from functions.read_input import read_input
from inputs.path import PATH

from .functions import starting_zeros

key = read_input(f"{PATH}/2015/day4.txt")
key = key[0]

print(f"First part: {starting_zeros(key, 5)}")

print(f"Second part: {starting_zeros(key, 6)}")
