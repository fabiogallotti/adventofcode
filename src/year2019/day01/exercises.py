from functions.read_input import read_input
from inputs.path import PATH

from .functions import fuel_computation, fuel_recursive

data = read_input(f"{PATH}/2019/day1.txt")

print(f"First part: {sum(fuel_computation(int(elem)) for elem in data)}")

print(f"Second part: {sum(fuel_recursive(int(elem)) for elem in data)}")
