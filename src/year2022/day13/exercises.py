from functions.read_input import read_input
from inputs.path import PATH
from .functions import part_1, part_2
import json

data = read_input(f"{PATH}/2022/day13.txt")
data = [json.loads(x) for x in data if x != ""]

print(f"First part: {part_1(data)}")

print(f"Second part: {part_2(data)}")
