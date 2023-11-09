import operator


def preprocessing(data):
    wires = {elem[len(elem) - 1]: elem[: len(elem) - 2] for elem in data}

    for key, value in wires.items():
        if len(value) == 1 and value[0].isnumeric():
            wires[key] = int(value[0])
    return wires


def bitwise_not(elem):
    return -(~int(elem) ^ 65535) - 1


def assign_values(wires, wire, instruction, operation):
    if check_int(wires[instruction]):
        wires[wire] = operation(wires[instruction])


def check_int(elem):
    return isinstance(elem, int)


def check_operations(wires, wire, instruction, operation):
    operators = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
    }

    try:
        if instruction[0].isnumeric() and check_int(wires[instruction[2]]):
            wires[wire] = operators[operation](
                int(instruction[0]), int(wires[instruction[2]])
            )
        elif check_int(wires[instruction[0]]) and instruction[2].isnumeric():
            wires[wire] = operators[operation](
                int(wires[instruction[0]]), int(instruction[2])
            )
        elif check_int(wires[instruction[0]]) and check_int(wires[instruction[2]]):
            wires[wire] = operators[operation](
                int(wires[instruction[0]]), int(wires[instruction[2]])
            )
    except KeyError:
        pass


def decisions(wires, wire, instruction):
    if instruction[0] == "NOT":
        assign_values(wires, wire, instruction[1], bitwise_not)

    elif instruction[1] == "AND":
        check_operations(wires, wire, instruction, "AND")

    elif instruction[1] == "OR":
        check_operations(wires, wire, instruction, "OR")

    elif instruction[1] == "LSHIFT":
        check_operations(wires, wire, instruction, "LSHIFT")

    elif instruction[1] == "RSHIFT":
        check_operations(wires, wire, instruction, "RSHIFT")


def emulate_circuit(wires, stopping_condition):
    while True:
        for wire, instruction in wires.items():
            if not check_int(instruction):
                if len(instruction) > 1:
                    decisions(wires, wire, instruction)
                elif len(instruction) == 1:
                    assign_values(wires, wire, instruction[0], int)

        if check_int(wires[stopping_condition]):
            break
