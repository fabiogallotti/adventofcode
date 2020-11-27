from common import read_input, nice_string_first

data = read_input("input.txt")

total = 0
for elem in data:
    if nice_string_first(elem):
        total += 1

print(total)
