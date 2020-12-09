import json

from functions.read_input import read_input
from inputs.path import PATH

from .functions import sum_ints, sum_ints_no_red

data = read_input(f"{PATH}/2015/day12.txt")
data = data[0]
data = json.loads(data)

print(f"First part: {sum_ints(data)}")

print(f"Second part: {sum_ints_no_red(data)}")
