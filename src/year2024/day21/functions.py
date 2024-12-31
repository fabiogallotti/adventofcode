NUMERIC_KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"],
]
DIRECTIONAL_KEYPAD = [
    ["", "^", "A"],
    ["<", "v", ">"],
]

# fmt: off
NUMERIC_KEYPAD  = {
    "7":  (0, 0), "8": (0, 1), "9": (0, 2),
    "4":  (1, 0), "5": (1, 1), "6": (1, 2),
    "1":  (2, 0), "2": (2, 1), "3": (2, 2),
    None: (3, 0), "0": (3, 1), "A": (3, 2),
}
DIRECTIONAL_KEYPAD = {
    None: (0, 0), "^": (0, 1), "A": (0, 2),
    "<":  (1, 0), "v": (1, 1), ">": (1, 2),
}
# fmt: on


def create_shortest_paths(keypad, invalid):
    paths = {}
    for value1, (x1, y1) in keypad.items():
        for value2, (x2, y2) in keypad.items():
            path = "<" * (y1 - y2) + "v" * (x2 - x1) + "^" * (x1 - x2) + ">" * (y2 - y1)
            if invalid in [(x1, y2), (x2, y1)]:
                path = path[::-1]
            paths[(value1, value2)] = f"{path}A"
    return paths


def create_sequence(string, paths):
    sequence = ""
    prev = "A"
    for char in string:
        if (prev, char) in paths:
            sequence += paths[(prev, char)]
            prev = char
    return sequence


def part_1(data):
    numeric_paths = create_shortest_paths(NUMERIC_KEYPAD, NUMERIC_KEYPAD[None])
    directional_paths = create_shortest_paths(DIRECTIONAL_KEYPAD, DIRECTIONAL_KEYPAD[None])

    total_complexity = 0
    for row in data:
        numeric_part = int(row[:-1])
        sequence = create_sequence(row, numeric_paths)

        for _ in range(2):
            sequence = create_sequence(sequence, directional_paths)

        total_complexity += numeric_part * len(sequence)

    return total_complexity


def get_length(sequence, iterations, directional_paths, cache=None) -> int:
    if cache is None:
        cache = {}

    key = (sequence, iterations)

    if key in cache:
        return cache[key]

    if iterations == 0:
        return len(sequence)
    prev = "A"
    total_length = 0
    for char in sequence:
        total_length += get_length(
            directional_paths[(prev, char)], iterations - 1, directional_paths, cache
        )
        prev = char

    cache[key] = total_length
    return total_length


def part_2(data):
    numeric_paths = create_shortest_paths(NUMERIC_KEYPAD, NUMERIC_KEYPAD[None])
    directional_paths = create_shortest_paths(DIRECTIONAL_KEYPAD, DIRECTIONAL_KEYPAD[None])

    total_complexity = 0
    for row in data:
        numeric_part = int(row[:-1])
        sequence = create_sequence(row, numeric_paths)

        total_complexity += numeric_part * get_length(sequence, 25, directional_paths)

    return total_complexity
