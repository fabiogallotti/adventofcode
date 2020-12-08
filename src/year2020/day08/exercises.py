from functions.read_input import read_input
from inputs.path import PATH

from .functions import (
    calculate_accumulator_value,
    calculate_value_switching_positions,
    find_positions,
)

data = read_input(f"{PATH}/2020/day08.txt")
data = [elem.split() for elem in data]

print(data)

print(f"First part: {calculate_accumulator_value(data)}")

jmp_positions = find_positions(data, "jmp")

print(f"Second part: {calculate_value_switching_positions(data,jmp_positions)}")
