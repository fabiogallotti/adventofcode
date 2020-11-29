from functions.read_input import read_multiple_lines_separated
from inputs.path import PATH

from .functions import emulate_circuit, preprocessing

data = read_multiple_lines_separated(f"{PATH}/2015day7.txt", " ")

wires = preprocessing(data)

emulate_circuit(wires)

print(wires["a"])