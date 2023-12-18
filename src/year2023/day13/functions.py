import itertools


def preprocessing(data):
    patterns = []
    pattern = []
    for row in data:
        if row:
            pattern.append(row)
        else:
            patterns.append(pattern)
            pattern = []

    patterns.append(pattern)
    return patterns


def part_1(data):
    patterns = preprocessing(data)

    total = 0
    for pattern in patterns:
        if row := mirror_row(pattern):
            total += row * 100

        reverse = list(zip(*pattern))
        if col := mirror_row(reverse):
            total += col

    return total


def mirror_row(pattern):
    for row in range(1, len(pattern)):
        below = pattern[row:]
        above = pattern[:row][::-1]

        above = above[: len(below)]
        below = below[: len(above)]

        if above == below:
            return row


def part_2(data):
    patterns = preprocessing(data)

    total = 0
    for pattern in patterns:
        if row := mirror_row_2(pattern):
            total += row * 100

        reverse = list(zip(*pattern))
        if col := mirror_row_2(reverse):
            total += col

    return total


def mirror_row_2(pattern):
    for row in range(1, len(pattern)):
        below = pattern[row:]
        above = pattern[:row][::-1]

        above = above[: len(below)]
        below = below[: len(above)]

        len_ = len(above[0])
        count = sum(
            above[i][j] == below[i][j] for i, j in itertools.product(range(len(above)), range(len_))
        )

        if count == (len_ * len(above)) - 1:
            return row
