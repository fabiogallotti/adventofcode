def calculate(data):
    for i in range(len(data) // 4):
        if data[4 * i] == 1:
            data[data[4 * i + 3]] = data[data[4 * i + 1]] + data[data[4 * i + 2]]
        elif data[4 * i] == 2:
            data[data[4 * i + 3]] = data[data[4 * i + 1]] * data[data[4 * i + 2]]
    return data


def set_initial_state(data, a, b):
    data[1] = a
    data[2] = b
