from functions.read_input import read_input
from inputs.path import PATH

from .functions import count_floors, first_basement

data = read_input(f"{PATH}/2015/day1.txt")
data = data[0]

print(f"First part: {count_floors(data)}")

print(f"Second part: {first_basement(data)}")
