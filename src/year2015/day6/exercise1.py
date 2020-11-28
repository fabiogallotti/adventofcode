from functions.read_input import read_multiple_lines_separated
from inputs.path import PATH

from .functions import toogle_lights, turn_lights

data = read_multiple_lines_separated(f"{PATH}/2015day6.txt", " ")

lights = [[0 for row in range(1000)] for column in range(1000)]

for elem in data:
    if elem[0] == "turn" and elem[1] == "on":
        turn_lights(elem[2:], lights, 1)
    elif elem[0] == "turn" and elem[1] == "off":
        turn_lights(elem[2:], lights, 0)
    else:
        toogle_lights(elem[1:], lights)


lights_on = sum(lights[row][column] for row in range(1000) for column in range(1000))

print(lights_on)
