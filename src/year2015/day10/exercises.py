from functions.read_input import read_input
from inputs.path import PATH

from .functions import apply_look_and_say_n_times

data = read_input(f"{PATH}/2015/day10.txt")
data = data[0]

print(f"First part: {apply_look_and_say_n_times(data, 40)}")

print(f"Second part: {apply_look_and_say_n_times(data, 50)}")
