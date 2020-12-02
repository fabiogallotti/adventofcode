from functions.read_input import read_multiple_lines
from inputs.path import PATH

from .functions import fuel_recursive

data = read_multiple_lines(f"{PATH}/2019day1.txt")


print(sum(fuel_recursive(int(elem)) for elem in data))
