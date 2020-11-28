from functions.read_input import read_multiple_lines_separated
from inputs.path import PATH
from .functions import calculate_brightness

data = read_multiple_lines_separated(f"{PATH}/2015day6.txt", " ")

lights = [[0 for row in range(1000)] for column in range(1000)]

print(calculate_brightness(data, lights))
