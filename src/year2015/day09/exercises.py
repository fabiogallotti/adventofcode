from functions.read_input import read_input
from inputs.path import PATH

from .functions import longest_path_length, preprocessing, shortest_path_length

data = read_input(f"{PATH}/2015/day09.txt")

cities, distances = preprocessing(data)

print(f"First part: {shortest_path_length(cities, distances)}")

print(f"Second part: {longest_path_length(cities, distances)}")
