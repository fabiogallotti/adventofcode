from utils import load_input, fuel_recursive

data = load_input("input.txt")

result = [fuel_recursive(elem) for elem in data]

print(sum(result))
