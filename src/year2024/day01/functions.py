from collections import Counter


def preprocess_lists(data):
    first = []
    second = []

    for elem in data:
        f, s = elem.split()
        first.append(int(f))
        second.append(int(s))

    return first, second


def part_1(data):
    first, second = preprocess_lists(data)

    first_ordered = sorted(first)
    second_ordered = sorted(second)

    diff = [abs(a - b) for a, b in zip(first_ordered, second_ordered)]

    return sum(diff)


def part_2(data):
    first, second = preprocess_lists(data)

    second_counter = Counter(second)

    times_second = [elem * second_counter[elem] for elem in first]

    return sum(times_second)
