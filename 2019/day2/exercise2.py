from utils import read_input, initial_state, calculate

for a in range(100):
    for b in range(100):
        input = read_input("input.txt")
        input = initial_state(input, a, b)
        input[2] = b
        result = calculate(input)
        if result[0] == 19690720:
            print(100* a + b)
