from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate_area

data = read_input(f"{PATH}/2015/day2.txt")
data = [elem.split("x") for elem in data]

result = [calculate_area(elem) for elem in data]
print(sum(result))
