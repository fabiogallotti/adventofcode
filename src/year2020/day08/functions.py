def execute_instructions(data, i, value):
    if data[i][0] == "acc":
        value += int(data[i][1])
        i+=1
    elif data[i][0] == "jmp":
        i += int(data[i][1])
    elif data[i][0] == "nop":
        i+=1
    return i, value

def calculate_accumulator_value(data):
    value = 0
    i = 0
    visited = []
    while True:
        if i in visited:
            return value
        visited.append(i)
        i, value = execute_instructions(data, i, value)


def find_positions(data, cmd):
    return [i for i, elem in enumerate(data) if elem[0] == cmd]


def calculate_value_switching_positions(data, positions):
    for position in positions:
        value = 0
        i = 0
        visited = []
        while i<len(data):
            if i in visited:
                break
            elif i == position:
                i+=1

            visited.append(i)
            i, value = execute_instructions(data, i, value)

            if i == len(data):
                return value
