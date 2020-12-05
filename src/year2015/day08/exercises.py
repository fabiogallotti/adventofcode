from functions.read_input import read_input
from inputs.path import PATH

from .functions import difference_string_memory, difference_new_string

data = read_input(f"{PATH}/2015/day8.txt")

print(f"First part: {difference_string_memory(data)}")

print(f"Second part: {difference_new_string(data)}")
