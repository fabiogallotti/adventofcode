from functions.read_input import read_input
from inputs.path import PATH

from .functions import nice_string_first, nice_string_second

data = read_input(f"{PATH}/2015/day05.txt")

print(f"First part: {sum(1 for elem in data if nice_string_first(elem))}")

print(f"Second part: {sum(1 for elem in data if nice_string_second(elem))}")
