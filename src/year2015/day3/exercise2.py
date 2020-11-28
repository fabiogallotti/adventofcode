from functions.read_input import read_one_line
from inputs.path import PATH

from .functions import santa_and_robo_delivers

data = read_one_line(f"{PATH}/2015day3.txt")

print(santa_and_robo_delivers(data))
