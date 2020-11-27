from common_day2 import read_input, calculate_ribbon

data = read_input("input.txt")

result = [calculate_ribbon(elem) for elem in data]
print(sum(result))
