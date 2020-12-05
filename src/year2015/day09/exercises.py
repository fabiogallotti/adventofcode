from functions.read_input import read_input
from inputs.path import PATH

from .functions import preprocessing, shortest_path_length, longest_path_length

data = read_input(f"{PATH}/2015/day9.txt")

cities, distances = preprocessing(data)

print(f"First part: {shortest_path_length(cities, distances)}")

print(f"Second part: {longest_path_length(cities, distances)}")
