from functions.read_input import read_input
from inputs.path import PATH

from .functions import calculate_ribbon

data = read_input(f"{PATH}/2015day2.txt")
data = [elem.split("x") for elem in data]


result = [calculate_ribbon(elem) for elem in data]
print(sum(result))
