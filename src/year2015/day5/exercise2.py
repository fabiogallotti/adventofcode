from functions.read_input import read_input
from inputs.path import PATH

from .functions import nice_string_second

data = read_input(f"{PATH}/2015/day5.txt")

total = sum(1 for elem in data if nice_string_second(elem))
print(total)
