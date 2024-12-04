import itertools
import re


def get_columns(data):
    return ["".join([data[i][j] for i in range(len(data))]) for j in range(len(data[0]))]


def get_diagonals(data):
    diagonals = []
    n = len(data) - 1
    increment = len(data) - 3
    for k in range(increment):
        diagonal = ["".join([data[i][i + k] for i in range(len(data)) if i + k < len(data)])]
        diagonals.extend(diagonal)

    for k in range(1, increment):
        diagonal = ["".join([data[i + k][i] for i in range(len(data)) if i + k < len(data)])]
        diagonals.extend(diagonal)

    for k in range(increment):
        diagonal = ["".join([data[n - i][i + k] for i in range(len(data)) if i + k < len(data)])]
        diagonals.extend(diagonal)

    for k in range(1, increment):
        diagonal = ["".join([data[n - i - k][i] for i in range(len(data)) if n - i - k >= 0])]
        diagonals.extend(diagonal)

    return diagonals


def part_1(data):
    rows = data
    columns = get_columns(data)
    diagonals = get_diagonals(data)

    total = 0
    for string in rows + columns + diagonals:
        matches = re.findall(r"(?=(XMAS|SAMX))", string)
        total += len(matches)
    return total


def part_2(data):
    count = 0
    n = len(data) - 1

    for i, j in itertools.product(range(1, n), range(1, n)):
        if data[i][j] == "A":
            top_left = data[i - 1][j - 1]
            top_right = data[i - 1][j + 1]
            bottom_left = data[i + 1][j - 1]
            bottom_right = data[i + 1][j + 1]

            if (top_left == "M" and bottom_right == "S") and (
                bottom_left == "M" and top_right == "S"
            ):
                count += 1
            elif (top_left == "S" and bottom_right == "M") and (
                bottom_left == "S" and top_right == "M"
            ):
                count += 1
            elif (top_left == "M" and bottom_right == "S") and (
                bottom_left == "S" and top_right == "M"
            ):
                count += 1
            elif (top_left == "S" and bottom_right == "M") and (
                bottom_left == "M" and top_right == "S"
            ):
                count += 1
    return count
