from functions.read_input import read_input
from inputs.path import PATH

from .functions import set_initial_state, calculate

data = read_input(f"{PATH}/2019day2.txt")
data = [int(elem) for elem in data[0].split(",")]

set_initial_state(data, 12, 2)
calculate(data)

print(data[0])
