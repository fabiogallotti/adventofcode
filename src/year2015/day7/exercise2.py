from functions.read_input import read_input
from inputs.path import PATH

from .functions import emulate_circuit, preprocessing

data = read_input(f"{PATH}/2015/day7.txt")
data = [elem.split(" ") for elem in data]

wires = preprocessing(data)

wires["b"] = 16076

emulate_circuit(wires, "a")

print(wires["a"])
