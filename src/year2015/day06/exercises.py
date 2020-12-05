from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate_lights_on, calculate_brightness

data = read_input(f"{PATH}/2015/day6.txt")
data = [elem.split(" ") for elem in data]

print(f"First part: {calculate_lights_on(data)}")

print(f"Second part: {calculate_brightness(data)}")
