SIGN_NS = {"n": 1, "s": -1, "o": 0, "e": 0}
SIGN_OE = {"o": 1, "e": -1, "n": 0, "s": 0}


def check_not_empty(elem):
    return elem in ("#", "L")


def problem1_or_occupied(problem, elem):
    return problem == 1 or elem == "#"


def problem2_and_empty(problem, elem):
    return problem == 2 and elem == "."


def validate_borders(data, i, j, length, ns, oe):
    return (0 <= i - SIGN_NS[ns] <= len(data) - 1) and (
        0 <= j - SIGN_OE[oe] <= length - 1
    )


def check_occupied(problem, data, i, j, length, ns, oe):
    if not validate_borders(data, i, j, length, ns, oe):
        return None

    elem = data[i - SIGN_NS[ns]][j - SIGN_OE[oe]]

    if problem1_or_occupied(problem, elem):
        return elem
    elif problem2_and_empty(problem, elem):
        while validate_borders(data, i, j, length, ns, oe):
            if check_not_empty(data[i - SIGN_NS[ns]][j - SIGN_OE[oe]]):
                return data[i - SIGN_NS[ns]][j - SIGN_OE[oe]]
            i -= SIGN_NS[ns]
            j -= SIGN_OE[oe]
    else:
        return "L"


def adjacents(problem, data, i, j, length):
    no = check_occupied(problem, data, i, j, length, "n", "o")
    n = check_occupied(problem, data, i, j, length, "n", "n")
    ne = check_occupied(problem, data, i, j, length, "n", "e")
    e = check_occupied(problem, data, i, j, length, "e", "e")
    se = check_occupied(problem, data, i, j, length, "s", "e")
    s = check_occupied(problem, data, i, j, length, "s", "s")
    so = check_occupied(problem, data, i, j, length, "s", "o")
    o = check_occupied(problem, data, i, j, length, "o", "o")

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
