from functions.read_input import read_input
from inputs.path import PATH

from .functions import apply_look_and_say_n_times

data = read_input(f"{PATH}/2015/day10.txt")
data = data[0]

print(apply_look_and_say_n_times(data, 50))
