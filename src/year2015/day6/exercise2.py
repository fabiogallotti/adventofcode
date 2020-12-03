from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate_brightness

data = read_input(f"{PATH}/2015/day6.txt")
data = [elem.split(" ") for elem in data]

lights = [[0 for row in range(1000)] for column in range(1000)]

print(calculate_brightness(data, lights))
