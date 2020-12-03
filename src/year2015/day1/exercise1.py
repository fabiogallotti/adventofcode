from functions.read_input import read_input
from inputs.path import PATH

from .functions import count_floors

data = read_input(f"{PATH}/2015/day1.txt")

floors = count_floors(data[0])

print(floors)
