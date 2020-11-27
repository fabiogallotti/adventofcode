from common_day5 import read_input, nice_string_second

data = read_input("input.txt")

total = 0
for elem in data:
    if nice_string_second(elem):
        total += 1

print(total)
