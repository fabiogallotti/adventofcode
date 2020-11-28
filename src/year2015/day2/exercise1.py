from functions.read_input import read_multiple_lines_separated
from inputs.path import PATH

from .functions import calculate_area

data = read_multiple_lines_separated(f"{PATH}/2015day2.txt", "x")

result = [calculate_area(elem) for elem in data]
print(sum(result))
