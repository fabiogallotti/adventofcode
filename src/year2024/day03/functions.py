import re


def calculate_sum_of_product(occurrences):
    sum_ = 0
    for occ in occurrences:
        strip_occ = occ.lstrip("mul(").rstrip(")").split(",")

        prod = 1
        for val in strip_occ:
            prod *= int(val)

        sum_ += prod

    return sum_


def part_1(data):
    occurrences = [match for row in data for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", row)]

    return calculate_sum_of_product(occurrences)


def search(row, do, dont, enabled):
    match = re.search(r"don\'t\(\)|do\(\)", row)

    if not match:
        (do if enabled else dont).append(row)
        return do, dont, enabled

    if pre_text := row[: match.start()]:
        (do if enabled else dont).append(pre_text)

    enabled = match.group() == "do()"

    return search(row[match.end() :], do, dont, enabled)


def part_2(data):
    total_do = []
    total_dont = []
    enabled = True

    for row in data:
        do, dont, enabled = search(row, [], [], enabled)
        total_do.extend(do)
        total_dont.extend(dont)

    occurrences = [
        match for row in total_do for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", row)
    ]

    return calculate_sum_of_product(occurrences)
