from functions.read_input import read_input
from inputs.path import PATH

from .functions import next_password, next_word

data = read_input(f"{PATH}/2015/day11.txt")
data = data[0]

next_pwd = next_password(data)
next_word = next_word(next_pwd)

print(f"First part: {next_pwd}")

print(f"Second part: {next_password(next_word)}")

