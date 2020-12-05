from functions.read_input import read_input
from inputs.path import PATH

from .functions import preprocessing, valid_passport, validate_data_passport

data = read_input(f"{PATH}/2020/day04.txt")

passports = preprocessing(data)

print(f"First part: {sum(1 for passport in passports if valid_passport(passport))}")

print(
    f"Second part: {sum(1 for passport in passports if validate_data_passport(passport))}"
)
