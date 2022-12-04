def part_1(data):
    fully_contains = 0
    for couple in data:
        first_range = range(int(couple[0][0]), int(couple[0][1]) + 1)
        second_range = range(int(couple[1][0]), int(couple[1][1]) + 1)

        first = set(first_range)
        second = set(second_range)

        common = first & second

        if common in [first, second]:
            fully_contains += 1

    return fully_contains


def part_2(data):
    overlaps = 0
    for couple in data:
        first_range = range(int(couple[0][0]), int(couple[0][1]) + 1)
        second_range = range(int(couple[1][0]), int(couple[1][1]) + 1)

        first = set(first_range)
        second = set(second_range)

        common = first & second

        if common:
            overlaps += 1

    return overlaps
