from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate, set_initial_state

data = read_input(f"{PATH}/2019/day02.txt")
data = [int(elem) for elem in data[0].split(",")]

data1 = data.copy()
set_initial_state(data1, 12, 2)
calculate(data1)

print(f"First part: {data1[0]}")

for a in range(100):
    for b in range(100):
        data2 = data.copy()

        set_initial_state(data2, a, b)
        calculate(data2)

        if data2[0] == 19690720:
            print(f"Second part: {100 * a + b}")
            break
