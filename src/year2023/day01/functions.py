import contextlib


def part_1(data):
    calibration = ["", ""]
    total = 0

    for row in data:
        calibration[0] = calculate_digit(row)
        calibration[1] = calculate_digit(row[::-1])

        total += int("".join(calibration))

    return total


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_2(data):
    calibration = ["", ""]
    total = 0

    for row in data:
        for digit, value in DIGITS.items():
            if digit in row:
                replace = f"{digit}{value}{digit}"
                row = row.replace(digit, replace)

        calibration[0] = calculate_digit(row)
        calibration[1] = calculate_digit(row[::-1])

        total += int("".join(calibration))

    return total


def calculate_digit(row):
    for char in row:
        with contextlib.suppress(ValueError):
            if int(char):
                return char
