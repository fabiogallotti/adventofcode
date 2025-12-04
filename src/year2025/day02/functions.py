def preprocess_input(data):
    ranges = data[0].split(",")
    first_ranges = []
    last_ranges = []

    for elem in ranges:
        first, last = elem.split("-")
        first_ranges.append(int(first))
        last_ranges.append(int(last))
    return first_ranges, last_ranges


def part_1(data):
    first_ranges, last_ranges = preprocess_input(data)

    total = 0

    for i in range(len(first_ranges)):
        for num in range(first_ranges[i], last_ranges[i] + 1):
            len_num = len(str(num))
            if len_num % 2 == 0:
                half = len_num // 2
                first_half = str(num)[:half]
                last_half = str(num)[half:]
                if first_half == last_half:
                    total += num

    return total


def part_2(data):
    first_ranges, last_ranges = preprocess_input(data)
    total = 0

    for i in range(len(first_ranges)):
        for num in range(first_ranges[i], last_ranges[i] + 1):
            len_num = len(str(num))

            for j in range(1, len_num):
                if len_num % j == 0:
                    parts = [str(num)[k : k + j] for k in range(0, len_num, j)]
                    if all(part == parts[0] for part in parts):
                        total += num
                        break

    return total
