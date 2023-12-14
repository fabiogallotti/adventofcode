def part_1(data):
    histories = [row.split() for row in data]
    histories = [[int(x) for x in row] for row in histories]
    lasts = []
    for history in histories:
        diffs = [history]
        diffs = check_diff(history, diffs)
        lasts.append(sum(diff[-1] for diff in diffs))

    return sum(lasts)


def check_diff(data, diffs):
    if all(x == 0 for x in data):
        return diffs

    diff = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    diffs.append(diff)
    return check_diff(diff, diffs)


def part_2(data):
    histories = [row.split() for row in data]
    histories = [[int(x) for x in row] for row in histories]
    lasts = []
    for history in histories:
        diffs = [history[::-1]]
        diffs = check_diff(history[::-1], diffs)
        lasts.append(sum(diff[-1] for diff in diffs))

    return sum(lasts)
