from functions.read_input import read_input
from inputs.path import PATH

from .functions import preprocessing, validate_data_passport

data = read_input(f"{PATH}/2020/day4.txt")
passports = preprocessing(data)

print(sum(1 for passport in passports if validate_data_passport(passport)))
