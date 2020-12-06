from functions.read_input import read_input
from inputs.path import PATH

from .functions import preprocessing, solve_problem

data = read_input(f"{PATH}/2019/day03.txt")
data = [elem.split(",") for elem in data]

points1, points2, intersections = preprocessing(data)

print(f"First part: {solve_problem(1, intersections)}")

print(f"Second part: {solve_problem(2, intersections, points1, points2)}")
