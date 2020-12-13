def preprocessing(data):
    data[0] = int(data[0])
    data[1] = [int(value) for value in data[1].split(",") if value != "x"]
    return data


def positions(data):
    data.pop(0)
    data = data[0].split(",")
    return {int(value): position for position, value in enumerate(data) if value != "x"}


def part_1(data):
    minimum = 1000000
    prod = 0
    for elem in data[1]:
        diff = elem - data[0] % elem
        if diff < minimum:
            minimum = diff
            prod = diff * elem

    return prod


def part_2(values_position):
    values = [value for value in values_position]

    step = values[0]
    timestamp = 0

    for value in values[1:]:
        diff = values_position[value]
        for i in range(timestamp, step * value, step):
            if not (i + diff) % value:
                step = step * value
                timestamp = i
                break
    return timestamp


def solve_problem(problem, data):
    if problem == 1:
        data = preprocessing(data)
        return part_1(data)
    elif problem == 2:
        values_position = positions(data)
        return part_2(values_position)
