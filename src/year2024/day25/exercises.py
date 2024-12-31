from functions.read_input import read_input
from inputs.path import PATH

from .functions import part_1

data = read_input(f"{PATH}/2024/day25.txt")

print(f"First part: {part_1(data)}")
