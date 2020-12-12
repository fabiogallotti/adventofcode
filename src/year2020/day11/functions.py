def adjacents(data, i, j, length):
    no = data[i - 1][j - 1] if i > 0 and j > 0 else None
    n = data[i - 1][j] if i > 0 else None
    ne = data[i - 1][j + 1] if i > 0 and j < length - 1 else None
    e = data[i][j + 1] if j < length - 1 else None
    se = data[i + 1][j + 1] if i < len(data) - 1 and j < length - 1 else None
    s = data[i + 1][j] if i < len(data) - 1 else None
    so = data[i + 1][j - 1] if i < len(data) - 1 and j > 0 else None
    o = data[i][j - 1] if j > 0 else None

    return [no, n, ne, e, se, s, so, o]


def check_occupied_no(data, i, j):
    if i <= 0 or j <= 0:
        return None
    if data[i - 1][j - 1] == "#":
        return data[i - 1][j - 1]
    elif data[i - 1][j - 1] == ".":
        while i > 0 and j > 0:
            if data[i - 1][j - 1] in ("#", "L"):
                return data[i - 1][j - 1]
            i -= 1
            j -= 1
    else:
        return "L"


def check_occupied_n(data, i, j):
    if i <= 0:
        return None
    if data[i - 1][j] == "#":
        return data[i - 1][j]
    elif data[i - 1][j] == ".":
        while i > 0:
            if data[i - 1][j] in ("#", "L"):
                return data[i - 1][j]
            i -= 1
    else:
        return "L"


def check_occupied_ne(data, i, j, length):
    if i <= 0 or j >= length - 1:
        return None
    if data[i - 1][j + 1] == "#":
        return data[i - 1][j + 1]
    elif data[i - 1][j + 1] == ".":
        while i > 0 and j < length - 1:
            if data[i - 1][j + 1] in ("#", "L"):
                return data[i - 1][j + 1]
            i -= 1
            j += 1
    else:
        return "L"


def check_occupied_e(data, i, j, length):
    if j >= length - 1:
        return None
    if data[i][j + 1] == "#":
        return data[i][j + 1]
    elif data[i][j + 1] == ".":
        while j < length - 1:
            if data[i][j + 1] in ("#", "L"):
                return data[i][j + 1]
            j += 1
    else:
        return "L"


def check_occupied_se(data, i, j, length):
    if i >= len(data) - 1 or j >= length - 1:
        return None

    if data[i + 1][j + 1] == "#":
        return data[i + 1][j + 1]
    elif data[i + 1][j + 1] == ".":
        while i < len(data) - 1 and j < length - 1:
            if data[i + 1][j + 1] in ("#", "L"):
                return data[i + 1][j + 1]
            i += 1
            j += 1
    else:
        return "L"


def check_occupied_s(data, i, j):
    if i >= len(data) - 1:
        return None
    if data[i + 1][j] == "#":
        return data[i + 1][j]
    elif data[i + 1][j] == ".":
        while i < len(data) - 1:
            if data[i + 1][j] in ("#", "L"):
                return data[i + 1][j]
            i += 1
    else:
        return "L"


def check_occupied_so(data, i, j):
    if i >= len(data) - 1 or j <= 0:
        return None
    if data[i + 1][j - 1] == "#":
        return data[i + 1][j - 1]
    elif data[i + 1][j - 1] == ".":
        while i < len(data) - 1 and j > 0:
            if data[i + 1][j - 1] in ("#", "L"):
                return data[i + 1][j - 1]
            i += 1
            j -= 1
    else:
        return "L"


def check_occupied_o(data, i, j):
    if j <= 0:
        return None
    if data[i][j - 1] == "#":
        return data[i][j - 1]
    elif data[i][j - 1] == ".":
        while j > 0:
            if data[i][j - 1] in ("#", "L"):
                return data[i][j - 1]
            j -= 1
    else:
        return "L"


def adjacents_part2(data, i, j, length):
    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    return [no, n, ne, e, se, s, so, o]


def calculate_adjacent_per_problem(problem, data, i, j):
    if problem == 1:
        adj = adjacents(data, i, j, len(data[i]))
    elif problem == 2:
        adj = adjacents_part2(data, i, j, len(data[i]))
    return adj


def no_occupied_adjacent(problem, data, i, j):
    adj = calculate_adjacent_per_problem(problem, data, i, j)
    return "#" if adj.count("#") == 0 else "L"


def how_many_adjacents(problem, data, i, j):
    adj = calculate_adjacent_per_problem(problem, data, i, j)
    return "L" if adj.count("#") > problem + 2 else "#"


def apply_rules(data, problem):
    new_data = [["."] * len(elem) for elem in data]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "L":
                new_data[i][j] = no_occupied_adjacent(problem, data, i, j)
            elif data[i][j] == "#":
                new_data[i][j] = how_many_adjacents(problem, data, i, j)
    return new_data


def solve_problem(problem, data):
    count = 0

    while True:
        data = apply_rules(data, problem)
        inside_count = sum(elem.count("#") for elem in data)

        if inside_count == count:
            return count
        else:
            count = inside_count
