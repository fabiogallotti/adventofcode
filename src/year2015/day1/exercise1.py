from functions.read_input import read_one_line
from inputs.path import PATH
from .functions import count_floors

data = read_one_line(f"{PATH}/2015day1.txt")

floors = count_floors(data)

print(floors)
