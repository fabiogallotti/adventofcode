from functions.read_input import read_input
from inputs.path import PATH

from .functions import longest_path_length, preprocessing

data = read_input(f"{PATH}/2015/day9.txt")

cities, distances = preprocessing(data)

print(longest_path_length(cities, distances))
