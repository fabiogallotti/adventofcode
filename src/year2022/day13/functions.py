import json

CONTINUE = 2


def preprocessing_part_1(data):
    return [[data[i], data[i + 1]] for i in range(0, len(data) - 1, 2)]


def is_ordered(v1, v2):
    if isinstance(v1, int) and isinstance(v2, int):
        if v1 < v2:
            return 1
        elif v1 > v2:
            return 0
        else:
            return CONTINUE

    elif isinstance(v1, list) and isinstance(v2, list):
        min_len = min(len(v1), len(v2))
        for i in range(min_len):
            check = is_ordered(v1[i], v2[i])
            if check != CONTINUE:
                return check

        if len(v1) < len(v2):
            return 1
        elif len(v1) > len(v2):
            return 0
        else:
            return CONTINUE

    elif isinstance(v1, int) and isinstance(v2, list):
        return is_ordered([v1], v2)
    elif isinstance(v1, list) and isinstance(v2, int):
        return is_ordered(v1, [v2])


def part_1(data):
    new_data = preprocessing_part_1(data)

    ordered = [0]
    ordered.extend(is_ordered(couple[0], couple[1]) for couple in new_data)

    ordered = [i * v for i, v in enumerate(ordered)]
    return sum(ordered)


def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    less = []
    equal = []
    greater = []

    for x in array:
        if is_ordered(x, pivot) == 1:
            less.append(x)
        elif is_ordered(x, pivot) == CONTINUE:
            equal.append(x)
        elif is_ordered(x, pivot) == 0:
            greater.append(x)
    return quicksort(less) + equal + quicksort(greater)


def part_2(data):
    a = [[2]]
    b = [[6]]
    data.extend([[], a, b])

    data = quicksort(data)
    decoder_keys = [i for i, v in enumerate(data) if v in [a, b]]

    return decoder_keys[0] * decoder_keys[1]
