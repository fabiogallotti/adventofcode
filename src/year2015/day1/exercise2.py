from functions.read_input import read_one_line
from inputs.path import PATH

from .functions import first_basement

data = read_one_line(f"{PATH}/2015day1.txt")

count = first_basement(data)

print(count)
