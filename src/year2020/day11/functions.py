def check_not_empty(elem):
    return elem in ("#", "L")


def problem1_or_occupied(problem, elem):
    return problem == 1 or elem == "#"


def problem2_and_empty(problem, elem):
    return problem == 2 and elem == "."


def check_occupied_no(problem, data, i, j):
    if i <= 0 or j <= 0:
        return None
    elem = data[i - 1][j - 1]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while i > 0 and j > 0:
            if check_not_empty(data[i - 1][j - 1]):
                return data[i - 1][j - 1]
            i -= 1
            j -= 1
    else:
        return "L"


def check_occupied_n(problem, data, i, j):
    if i <= 0:
        return None
    elem = data[i - 1][j]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while i > 0:
            if check_not_empty(data[i - 1][j]):
                return data[i - 1][j]
            i -= 1
    else:
        return "L"


def check_occupied_ne(problem, data, i, j, length):
    if i <= 0 or j >= length - 1:
        return None
    elem = data[i - 1][j + 1]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while i > 0 and j < length - 1:
            if check_not_empty(data[i - 1][j + 1]):
                return data[i - 1][j + 1]
            i -= 1
            j += 1
    else:
        return "L"


def check_occupied_e(problem, data, i, j, length):
    if j >= length - 1:
        return None
    elem = data[i][j + 1]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while j < length - 1:
            if check_not_empty(data[i][j + 1]):
                return data[i][j + 1]
            j += 1
    else:
        return "L"


def check_occupied_se(problem, data, i, j, length):
    if i >= len(data) - 1 or j >= length - 1:
        return None
    elem = data[i + 1][j + 1]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while i < len(data) - 1 and j < length - 1:
            if check_not_empty(data[i + 1][j + 1]):
                return data[i + 1][j + 1]
            i += 1
            j += 1
    else:
        return "L"


def check_occupied_s(problem, data, i, j):
    if i >= len(data) - 1:
        return None
    elem = data[i + 1][j]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while i < len(data) - 1:
            if check_not_empty(data[i + 1][j]):
                return data[i + 1][j]
            i += 1
    else:
        return "L"


def check_occupied_so(problem, data, i, j):
    if i >= len(data) - 1 or j <= 0:
        return None
    elem = data[i + 1][j - 1]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while i < len(data) - 1 and j > 0:
            if check_not_empty(data[i + 1][j - 1]):
                return data[i + 1][j - 1]
            i += 1
            j -= 1
    else:
        return "L"


def check_occupied_o(problem, data, i, j):
    if j <= 0:
        return None
    elem = data[i][j - 1]
    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while j > 0:
            if check_not_empty(data[i][j - 1]):
                return data[i][j - 1]
            j -= 1
    else:
        return "L"


def adjacents(problem, data, i, j, length):
    no = check_occupied_no(problem, data, i, j)
    n = check_occupied_n(problem, data, i, j)
    ne = check_occupied_ne(problem, data, i, j, length)
    e = check_occupied_e(problem, data, i, j, length)
    se = check_occupied_se(problem, data, i, j, length)
    s = check_occupied_s(problem, data, i, j)
    so = check_occupied_so(problem, data, i, j)
    o = check_occupied_o(problem, data, i, j)

    return [no, n, ne, e, se, s, so, o]


def no_occupied_adjacent(problem, data, i, j):
    adj = adjacents(problem, data, i, j, len(data[i]))
    return "#" if adj.count("#") == 0 else "L"


def how_many_adjacents(problem, data, i, j):
    adj = adjacents(problem, data, i, j, len(data[i]))
    return "L" if adj.count("#") > problem + 2 else "#"


def apply_rules(problem, data):
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
        data = apply_rules(problem, data)
        inside_count = sum(elem.count("#") for elem in data)

        if inside_count == count:
            return count
        else:
            count = inside_count
