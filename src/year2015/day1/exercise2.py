from functions.read_input import read_input
from inputs.path import PATH

from .functions import first_basement

data = read_input(f"{PATH}/2015day1.txt")

count = first_basement(data[0])

print(count)
