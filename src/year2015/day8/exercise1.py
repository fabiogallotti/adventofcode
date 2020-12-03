from functions.read_input import read_input
from inputs.path import PATH

from .functions import difference_string_memory

data = read_input(f"{PATH}/2015/day8.txt")

print(difference_string_memory(data))
