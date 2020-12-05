from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_seat_ids

data = read_input(f"{PATH}/2020/day5.txt")

seat_ids = find_seat_ids(data)

print(max(seat_ids))
