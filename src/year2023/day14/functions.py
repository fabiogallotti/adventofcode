def part_1(data):
    transposed = list(map(list, zip(*data)))

    moved = True
    while moved:
        moved = move_north(transposed, moved)

    original = list(map(list, zip(*transposed)))

    loads = list(range(1, len(original) + 1))[::-1]
    total = 0
    for i, row in enumerate(original):
        count_o = row.count("O")
        total += count_o * loads[i]
    return total


def move_north(data, moved):
    moved = False
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "O":
                if i > -1 and j > 0:
                    if data[i][j - 1] == ".":
                        data[i][j - 1] = "O"
                        data[i][j] = "."
                        moved = True
    return moved


def part_2(data):
    transposed = data

    cycles = 1_000_000_000
    seen = []
    i = 0

    while True:
        transposed = list(map(list, zip(*transposed)))  # north

        moved = True
        while moved:
            moved = move_left(transposed, moved)

        transposed = list(map(list, zip(*transposed)))  # west

        moved = True
        while moved:
            moved = move_left(transposed, moved)

        transposed = list(map(list, zip(*transposed)))  # south
        moved = True
        while moved:
            moved = move_right(transposed, moved)

        transposed = list(map(list, zip(*transposed)))  # east
        moved = True
        while moved:
            moved = move_right(transposed, moved)

        if transposed in seen:
            n = seen.index(transposed)
            break
        seen.append(transposed)
        i += 1

    cycle_length = i - n
    seen_index = n + (cycles - n) % cycle_length - 1

    final = seen[seen_index]

    loads = list(range(1, len(final) + 1))[::-1]
    total = 0
    for j, row in enumerate(final):
        count_o = row.count("O")
        total += count_o * loads[j]

    return total


def move_left(data, moved):
    moved = False
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "O":
                if i > -1 and j > 0:
                    if data[i][j - 1] == ".":
                        data[i][j - 1] = "O"
                        data[i][j] = "."
                        moved = True
    return moved


def move_right(data, moved):
    moved = False
    max_row = len(data)
    max_col = len(data[0])
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "O":
                if i < max_row and j < max_col - 1:
                    if data[i][j + 1] == ".":
                        data[i][j + 1] = "O"
                        data[i][j] = "."
                        moved = True
    return moved
