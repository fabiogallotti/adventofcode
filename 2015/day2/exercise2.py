from common_day2 import calculate_ribbon, read_input

data = read_input("input.txt")

result = [calculate_ribbon(elem) for elem in data]
print(sum(result))
