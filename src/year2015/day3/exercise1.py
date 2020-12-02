from functions.read_input import read_input
from inputs.path import PATH

from .functions import santa_delivers

data = read_input(f"{PATH}/2015day3.txt")

print(santa_delivers(data[0]))
