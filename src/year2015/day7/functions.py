import operator


def preprocessing(data):
    wires = {elem[len(elem) - 1]: elem[: len(elem) - 2] for elem in data}

    for key, value in wires.items():
        if len(value) == 1 and value[0].isnumeric():
            wires[key] = int(value[0])
    return wires


def bitwise_not(elem):
    return -(~int(elem) ^ 65535) - 1


def assign_value(wires, wire, instruction):
    if type(wires[instruction[0]]) == int:
        wires[wire] = int(wires[instruction[0]])


def check_not(wires, wire, instruction):
    if type(wires[instruction[1]]) == int:
        wires[wire] = bitwise_not(wires[instruction[1]])


def check_operations(wires, wire, instruction, operation):

    operators = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
    }

    try:
        if instruction[0].isnumeric() and type(wires[instruction[2]]) == int:
            wires[wire] = operators[operation](
                int(instruction[0]), int(wires[instruction[2]])
            )
        elif type(wires[instruction[0]]) == int and instruction[2].isnumeric():
            wires[wire] = operators[operation](
                int(wires[instruction[0]]), int(instruction[2])
            )
        elif type(wires[instruction[0]]) == int and type(wires[instruction[2]]) == int:
            wires[wire] = operators[operation](
                int(wires[instruction[0]]), int(wires[instruction[2]])
            )
    except:
        pass


def emulate_circuit(wires, stopping_condition):
    while True:
        for wire, instruction in wires.items():
            if type(instruction) is not int:
                if len(instruction) > 1:
                    if instruction[0] == "NOT":
                        check_not(wires, wire, instruction)

                    elif instruction[1] == "AND":
                        check_operations(wires, wire, instruction, "AND")

                    elif instruction[1] == "OR":
                        check_operations(wires, wire, instruction, "OR")

                    elif instruction[1] == "LSHIFT":
                        check_operations(wires, wire, instruction, "LSHIFT")

                    elif instruction[1] == "RSHIFT":
                        check_operations(wires, wire, instruction, "RSHIFT")

                elif len(instruction) == 1:
                    assign_value(wires, wire, instruction)

        if type(wires[stopping_condition]) is int:
            break
