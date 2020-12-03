from functions.read_input import read_input
from inputs.path import PATH

from .functions import fuel_computation

data = read_input(f"{PATH}/2019/day1.txt")

print(sum(fuel_computation(int(elem)) for elem in data))
