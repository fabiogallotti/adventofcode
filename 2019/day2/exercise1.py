from utils import read_input, initial_state, calculate

input = read_input("input.txt")
input = initial_state(input, 12, 2)
result = calculate(input)

print(result[0])
