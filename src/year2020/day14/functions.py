import itertools


def get_bin(x, n=0):
    return format(x, "b").zfill(n)


def save_in_memory(binary_repr, memory, memory_position):
    binary_repr = "".join(binary_repr)
    new_value = int(binary_repr, 2)
    memory[memory_position] = new_value


def save_in_memory_part2(binary_repr, memory, value):
    binary_repr = "".join(binary_repr)
    new_position = int(binary_repr, 2)
    memory[new_position] = int(value)


def get_mask_bits_to_change(problem, elem):
    mask = elem[-36:]
    bits_to_change = (
        {position: value for position, value in enumerate(mask) if value != "X"}
        if problem == 1
        else {position: value for position, value in enumerate(mask) if value != "0"}
    )

    return mask, bits_to_change


def get_infos(problem, elem):
    a = elem.find("]")
    memory_position = elem[4:a]
    e = elem.find("=")
    value = elem[e + 2 :]
    binary_repr = (
        list(get_bin(int(value), 36)) if problem == 1 else list(get_bin(int(memory_position), 36))
    )

    return memory_position, value, binary_repr


def apply_mask(binary_repr, bits_to_change):
    for position, val in bits_to_change.items():
        binary_repr[position] = val


def change_all_x_values(binary_repr, bits_to_change, memory, value):
    possible_x_values = [p for p in itertools.product("01", repeat=binary_repr.count("X"))]
    x_to_change = [position for position, value in bits_to_change.items() if value == "X"]

    for x_values in possible_x_values:
        binary_repr = list(binary_repr)
        for i, x_value in enumerate(x_values):
            binary_repr[x_to_change[i]] = x_value
        save_in_memory_part2(binary_repr, memory, value)


def solve_problem(problem, data):
    memory = {}
    for elem in data:
        if "mask" in elem:
            _mask, bits_to_change = get_mask_bits_to_change(problem, elem)
        elif "mem" in elem:
            memory_position, value, binary_repr = get_infos(problem, elem)

            apply_mask(binary_repr, bits_to_change)

            if problem == 1:
                save_in_memory(binary_repr.copy(), memory, memory_position)
            elif problem == 2:
                change_all_x_values(binary_repr, bits_to_change, memory, value)

    return sum(elem for elem in memory.values() if elem != 0)
