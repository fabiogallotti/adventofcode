from common_day5 import nice_string_first, read_input

data = read_input("input.txt")

total = sum(1 for elem in data if nice_string_first(elem))
print(total)
