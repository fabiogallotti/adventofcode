from functions.read_input import read_input
from inputs.path import PATH

from .functions import preprocessing, number_containing_bags, bag_size

data = read_input(f"{PATH}/2020/day07.txt")

rules = preprocessing(data)

bags_to_find = ["shiny_gold"]
mine = "shiny_gold"

print(f"First part: {number_containing_bags(bags_to_find, rules)}")

print(f"Second part: {bag_size(mine, rules)}")
