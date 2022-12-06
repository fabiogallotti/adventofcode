from functions.read_input import read_input
from inputs.path import PATH

from .functions import part_1, part_2

data = read_input(f"{PATH}/2021/day04.txt")

data = [elem.strip().split("\n")[0] for elem in data if elem]

print(f"First part: {part_1(data)}")

print(f"Second part: {part_2(data)}")
