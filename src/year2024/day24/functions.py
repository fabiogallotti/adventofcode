from collections import defaultdict


def preprocessing(data):
    wires = defaultdict(int)
    instructions = defaultdict(list)

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

    return wires, instructions


def and_op(a, b):
    return int((a & b) != 0)


def or_op(a, b):
    return int((a | b) != 0)


def xor_op(a, b):
    return int(a != b)


def sorted_bits_startswith(wires, char):
    return "".join(
        str(value)
        for _, value in sorted(
            ((wire, value) for wire, value in wires.items() if wire.startswith(char)),
            key=lambda item: item[0],
            reverse=True,
        )
    )


def execute_instructions(wires, instructions):
    operation_map = {"and_op": and_op, "or_op": or_op, "xor_op": xor_op}

    while any(instructions[op] for op in instructions):
        for op, value in instructions.items():
            operation = operation_map[op]
            for elem in value:
                if elem[0] in wires and elem[1] in wires:
                    a = wires[elem[0]]
                    b = wires[elem[1]]
                    wires[elem[2]] = operation(a, b)
                    instructions[op].remove(elem)


def part_1(data):
    wires, instructions = preprocessing(data)

    execute_instructions(wires, instructions)

    sorted_z_bits = sorted_bits_startswith(wires, "z")

    return int(sorted_z_bits, 2)


def part_2(data):
    _wires, instructions = preprocessing(data)

    # execute_instructions(wires, instructions)

    # sorted_x_bits = sorted_bits_startswith(wires, "x")
    # sorted_y_bits = sorted_bits_startswith(wires, "y")
    # sorted_z_bits = sorted_bits_startswith(wires, "z")

    # print(sorted_z_bits)
    # expected_z_bits = bin(int(sorted_x_bits, 2) + int(sorted_y_bits, 2))[2:]

    # print(expected_z_bits)
    # print(int(sorted_x_bits, 2))
    # print(int(sorted_y_bits, 2))
    # print(int(sorted_z_bits, 2))

    from graphviz import Graph

    graph = Graph(format="png", engine="neato")

    for op, elem in instructions.items():
        for inp1, inp2, output in elem:
            graph.node(inp1, inp1, shape="ellipse", style="filled", fillcolor="lightblue")
            graph.node(inp2, inp2, shape="ellipse", style="filled", fillcolor="lightblue")

            graph.node(output, output, shape="ellipse", style="filled", fillcolor="lightgreen")

            gate_node = f"{inp1}-{op}-{inp2}"
            graph.node(gate_node, op, shape="box", style="filled", fillcolor="lightgrey")

            graph.edge(inp1, gate_node)
            graph.edge(inp2, gate_node)

            graph.edge(gate_node, output)

    graph.render("circuit_diagram", view=True)
