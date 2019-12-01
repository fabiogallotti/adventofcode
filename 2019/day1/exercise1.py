from utils import read_input, fuel_computation

data = read_input("input.txt")

result = [fuel_computation(elem) for elem in data]

print(sum(result))
