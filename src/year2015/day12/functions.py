def sum_ints(data):
    sum_ = 0
    if isinstance(data, int):
        sum_ += data
    elif isinstance(data, list):
        for elem in data:
            sum_ += sum_ints(elem)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum_ += sum_ints(value)
    return sum_


def sum_ints_no_red(data):
    sum_ = 0
    if isinstance(data, int):
        sum_ += data
    elif isinstance(data, list):
        for elem in data:
            sum_ += sum_ints_no_red(elem)
    elif isinstance(data, dict):
        if "red" not in data.values():
            for key, value in data.items():
                sum_ += sum_ints_no_red(value)
    return sum_
