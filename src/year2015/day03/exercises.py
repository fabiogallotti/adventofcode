from functions.read_input import read_input
from inputs.path import PATH

from .functions import santa_and_robo_delivers, santa_delivers

data = read_input(f"{PATH}/2015/day3.txt")
data = data[0]

print(f"First part: {santa_delivers(data)}")

print(f"Second part: {santa_and_robo_delivers(data)}")
