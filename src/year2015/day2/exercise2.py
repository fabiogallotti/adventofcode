from functions.read_input import read_multiple_lines_x_separated
from inputs.path import PATH

from .functions import calculate_ribbon

data = read_multiple_lines_x_separated(f"{PATH}/2015day2.txt")

result = [calculate_ribbon(elem) for elem in data]
print(sum(result))
