from functions.read_input import read_input
from inputs.path import PATH

from .functions import part_1, part_2

data = read_input(f"{PATH}/2022/day15.txt")

print(f"First part: {part_1(data, 2000000)}")

print(f"Second part: {part_2(data, 4000000)}")
