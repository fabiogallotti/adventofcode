def preprocessing_levels(data):
    return [[int(v) for v in row.split()] for row in data]


def part_1(data):
    levels = preprocessing_levels(data)

    return sum(bool(check_safe(level)) for level in levels)


def check_safe(level):
    decreasing = check_condition(level, lambda x, y: x > y)
    increasing = check_condition(level, lambda x, y: x < y)
    adjacent = check_condition(level, lambda x, y: 1 <= abs(x - y) <= 3)

    return bool((decreasing and adjacent) or (increasing and adjacent))


def check_condition(level, condition):
    if len(level) == 1:
        return True
    for i in range(len(level) - 1):
        return (
            check_condition(level[i + 1 :], condition)
            if condition(level[i], level[i + 1])
            else False
        )


def part_2(data):
    levels = preprocessing_levels(data)

    safe = 0
    for level in levels:
        if check_safe(level):
            safe += 1
        else:
            for i in range(len(level)):
                new_level = level[:i] + level[i + 1 :]
                if check_safe(new_level):
                    safe += 1
                    break

    return safe
