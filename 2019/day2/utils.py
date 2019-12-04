def read_input(filename):
    with open(filename, "r") as f:
        return [ int(elem) for elem in f.read().split(",") ]

def calculate(data):
    for i in range(len(data) // 4):
        if data[4*i] == 1:
            data[data[4*i+3]] = data[data[4*i+1]] + data[data[4*i+2]] 
        elif data[4*i] == 2:
            data[data[4*i+3]] = data[data[4*i+1]] * data[data[4*i+2]] 
    return data

def initial_state(data, a, b):
    data[1] = a
    data[2] = b
    return data