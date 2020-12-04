from functions.read_input import read_input
from inputs.path import PATH

from .functions import find_seat_ids, find_missing_seat_id

data = read_input(f"{PATH}/2020/day5.txt")

seat_ids = find_seat_ids(data)

print(find_missing_seat_id(seat_ids))