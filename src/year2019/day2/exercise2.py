from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate, set_initial_state

for a in range(100):
    for b in range(100):
        data = read_input(f"{PATH}/2019/day2.txt")
        data = [int(elem) for elem in data[0].split(",")]

        set_initial_state(data, a, b)
        calculate(data)

        if data[0] == 19690720:
            print(100 * a + b)
            break
