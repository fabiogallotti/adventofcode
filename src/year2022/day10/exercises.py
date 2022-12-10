from functions.read_input import read_input
from inputs.path import PATH

from .functions import part_1, part_2

data = read_input(f"{PATH}/2022/day10.txt")

data = [e.split() for e in data]

print(f"First part: {part_1(data)}")

print(f"Second part: {chr(10)}{chr(10).join(part_2(data))}")
