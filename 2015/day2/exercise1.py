from common_day2 import calculate_area, read_input

data = read_input("input.txt")

result = [calculate_area(elem) for elem in data]
print(sum(result))
