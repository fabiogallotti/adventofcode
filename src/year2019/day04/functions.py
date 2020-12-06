def check_double(data):
    return any(data[i] == data[i + 1] for i in range(5))


def check_no_decrease(data):
    return all(data[i] <= data[i + 1] for i in range(5))


def check_extremes(data):
    return (data[0] == data[1] and data[1] != data[2]) or (
        data[4] == data[5] and data[3] != data[4]
    )


def check_inside(data, i):
    return (
        data[i] == data[i - 1] and data[i] != data[i + 1] and data[i - 2] != data[i]
    ) or (data[i] == data[i + 1] and data[i] != data[i - 1] and data[i + 2] != data[i])


def check_no_larger_group(data):
    return any(
        i in [1, 4]
        and check_extremes(data)
        or i not in [1, 4]
        and check_inside(data, i)
        for i in range(1, 5)
    )
