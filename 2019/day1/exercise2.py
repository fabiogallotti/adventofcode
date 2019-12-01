from utils import read_input, fuel_recursive

data = read_input("input.txt")

result = [fuel_recursive(elem) for elem in data]

print(sum(result))
