from collections import defaultdict


def part_1(data):
    wires = defaultdict(int)
    instructions = defaultdict(list)

    operation_map = {"and_op": and_op, "or_op": or_op, "xor_op": xor_op}

    for row in data:
        if row != "" and ":" in row:
            wires[row.split(": ")[0]] = int(row.split(": ")[1])

        if row != "" and " AND" in row:
            instructions["and_op"].append(
                (row.split(" AND ")[0], *row.split(" AND ")[1].split(" -> "))
            )
        if row != "" and " OR" in row:
            instructions["or_op"].append(
                (row.split(" OR ")[0], *row.split(" OR ")[1].split(" -> "))
            )
        if row != "" and " XOR" in row:
            instructions["xor_op"].append(
                (row.split(" XOR ")[0], *row.split(" XOR ")[1].split(" -> "))
            )

    while any(instructions[op] for op in instructions):
        for op, value in instructions.items():
            operation = operation_map[op]
            for elem in value:
                if elem[0] in wires and elem[1] in wires:
                    a = wires[elem[0]]
                    b = wires[elem[1]]
                    wires[elem[2]] = operation(a, b)

                    instructions[op].remove(elem)

    sorted_z_bits = "".join(
        str(value)
        for _, value in sorted(
            ((wire, value) for wire, value in wires.items() if wire.startswith("z")),
            key=lambda item: item[0],
            reverse=True,
        )
    )

    return int(sorted_z_bits, 2)


def and_op(a, b):
    return int((a & b) != 0)


def or_op(a, b):
    return int((a | b) != 0)


def xor_op(a, b):
    return int(a != b)


def part_2(data):
    pass
