from functions.read_input import read_input
from inputs.path import PATH

from .functions import part_1, part_2

data = read_input(f"{PATH}/2024/day24.txt")

print(f"First part: {part_1(data)}")

print(f"Second part: {part_2(data)}")  # manually

# a = ["z08", "mvb", "z18", "wss", "z23", "bmn", "rds", "jss"]
# ",".join(sorted(a))
# 'bmn,jss,mvb,rds,wss,z08,z18,z23'
