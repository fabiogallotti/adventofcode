from common_day5 import read_input, nice_string_second

data = read_input("input.txt")

total = sum(1 for elem in data if nice_string_second(elem))
print(total)
