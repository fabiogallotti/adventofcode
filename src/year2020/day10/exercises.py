from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_differences_one_three, find_distinct_ways

data = read_input(f"{PATH}/2020/day10.txt")
data = [int(elem) for elem in data]

print(f"First part: {find_differences_one_three(data)}")

print(f"Second part: {find_distinct_ways(data)}")
