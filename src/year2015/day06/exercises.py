from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate_brightness, calculate_lights_on

data = read_input(f"{PATH}/2015/day06.txt")
data = [elem.split(" ") for elem in data]

print(f"First part: {calculate_lights_on(data)}")

print(f"Second part: {calculate_brightness(data)}")
