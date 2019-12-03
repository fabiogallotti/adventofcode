from utils import load_input, fuel_computation

data = load_input("input.txt")

result = [fuel_computation(elem) for elem in data]

print(sum(result))
