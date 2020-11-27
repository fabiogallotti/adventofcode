from common_day2 import read_input, calculate_area

data = read_input("input.txt")

result = [calculate_area(elem) for elem in data]
print(sum(result))
