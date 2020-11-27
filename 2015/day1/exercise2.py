from read_input import read_input

data = read_input("input.txt")

floor = 0
count = 0
for elem in data:
    count += 1
    if elem == "(":
        floor += 1
    elif elem == ")":
        floor -= 1
    if floor == -1:
        print(count)
        break
