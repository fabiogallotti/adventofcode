from functions.read_input import read_multiple_lines_separated
from inputs.path import PATH

from .functions import calculate_lights_on

data = read_multiple_lines_separated(f"{PATH}/2015day6.txt", " ")

lights = [[0 for row in range(1000)] for column in range(1000)]

print(calculate_lights_on(data, lights))
