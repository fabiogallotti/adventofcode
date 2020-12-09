from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_not_sum_preamble,sum_weakness

data = read_input(f"{PATH}/2020/day09.txt")
data = [int(elem) for elem in data]

invalid = find_not_sum_preamble(data.copy(),25)

print(f"First part: {invalid}")

print(f"Second part: {sum_weakness(data,invalid)}")
