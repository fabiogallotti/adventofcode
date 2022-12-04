from functions.read_input import read_input
from inputs.path import PATH

from .functions import part_1, part_2

data = read_input(f"{PATH}/2022/day04.txt")
data = [x.split(",") for x in data]
data = [[y.split("-") for y in x] for x in data]

print(f"First part: {part_1(data)}")

print(f"Second part: {part_2(data)}")
