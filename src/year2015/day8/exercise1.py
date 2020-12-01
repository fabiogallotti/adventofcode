from functions.read_input import read_multiple_lines
from inputs.path import PATH

from .functions import difference_string_memory

data = read_multiple_lines(f"{PATH}/2015day8.txt")

print(difference_string_memory(data))
