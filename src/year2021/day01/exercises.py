from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_single_increase, find_three_increase

data = read_input(f"{PATH}/2021/day01.txt")

data_int = [int(x) for x in data]

print(f"First part: {find_single_increase(data_int)}")

print(f"Second part: {find_three_increase(data_int)}")
