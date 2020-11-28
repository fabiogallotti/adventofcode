from functions.read_input import read_multiple_lines
from inputs.path import PATH

from .functions import nice_string_second

data = read_multiple_lines(f"{PATH}/2015day5.txt")

total = sum(1 for elem in data if nice_string_second(elem))
print(total)
