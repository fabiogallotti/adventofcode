def calculate_priority(x: str):
    if 96 < ord(x) < 123:
        return ord(x) - 96
    elif 64 < ord(x) < 91:
        return ord(x) - 38


def part_1(data):
    sum_priority = 0
    for elem in data:
        half = len(elem) // 2

        first = set(elem[:half])
        second = set(elem[half:])

        common = first & second

        sum_priority += calculate_priority(next(iter(common)))

    return sum_priority


def part_2(data):
    sum_priority = 0
    len_groups = 3
    num_groups = len(data) // len_groups

    groups = [data[i * len_groups : (i * len_groups) + len_groups] for i in range(num_groups)]

    for group in groups:
        first = set(group[0])
        second = set(group[1])
        third = set(group[2])

        common = first & second & third
        sum_priority += calculate_priority(next(iter(common)))

    return sum_priority
