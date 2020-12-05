from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate_area, calculate_ribbon

data = read_input(f"{PATH}/2015/day2.txt")
data = [elem.split("x") for elem in data]

print(f"First part: {sum([calculate_area(elem) for elem in data])}")

print(f"Second part: {sum([calculate_ribbon(elem) for elem in data])}")
