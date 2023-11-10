from functions.read_input import read_input
from inputs.path import PATH

from .functions import check_double, check_no_decrease, check_no_larger_group

data = read_input(f"{PATH}/2019/day04.txt")
data = data[0].split("-")
data = [int(elem) for elem in data]

passwords = range(data[0], data[1], 1)

result = [elem for elem in passwords if check_no_decrease(str(elem)) and check_double(str(elem))]
result2 = [elem for elem in result if check_no_larger_group(str(elem))]

print(f"First part: {len(result)}")

print(f"Second part: {len(result2)}")
