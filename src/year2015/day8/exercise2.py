from functions.read_input import read_input
from inputs.path import PATH

from .functions import difference_new_string

data = read_input(f"{PATH}/2015day8.txt")

print(difference_new_string(data))
