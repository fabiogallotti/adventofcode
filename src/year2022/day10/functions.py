def part_1(data):
    value = 1
    cycles = [value]

    for e in data:
        if e[0] == "noop":
            latest_value = cycles[-1]
            if value != latest_value:
                latest_value = value
            cycles.append(latest_value)
        if e[0] == "addx":
            for _ in range(2):
                latest_value = cycles[-1]
                if value != latest_value:
                    latest_value = value
                cycles.append(latest_value)
            value += int(e[1])

    c20 = cycles[20] * 20
    c60 = cycles[60] * 60
    c100 = cycles[100] * 100
    c140 = cycles[140] * 140
    c180 = cycles[180] * 180
    c220 = cycles[220] * 220

    return sum([c20, c60, c100, c140, c180, c220])


def part_2(data):
    value = 1
    cycles = [value]

    for e in data:
        if e[0] == "noop":
            latest_value = cycles[-1]
            if value != latest_value:
                latest_value = value
            cycles.append(latest_value)
        if e[0] == "addx":
            for _ in range(2):
                latest_value = cycles[-1]
                if value != latest_value:
                    latest_value = value
                cycles.append(latest_value)
            value += int(e[1])

    rows = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for i in range(len(cycles) - 1):
        row = i // 40
        j = i % 40

        if cycles[i + 1] in [j, j - 1, j + 1]:
            rows[row].append("#")
        else:
            rows[row].append(".")

    return [
        "".join(rows[0]),
        "".join(rows[1]),
        "".join(rows[2]),
        "".join(rows[3]),
        "".join(rows[4]),
        "".join(rows[5]),
    ]
