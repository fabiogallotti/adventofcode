def find_differences_one_three(data):
    data.sort()

    difference_one = 0 if data[0] != 1 else 1
    difference_three = 1 if data[0] != 3 else 2

    for i in range(len(data) - 1):
        if data[i + 1] - data[i] == 1:
            difference_one += 1
        elif data[i + 1] - data[i] == 3:
            difference_three += 1

    return difference_one * difference_three


def calculate_difference(data):
    data.append(0)
    data.sort()

    diff = [0] * (len(data) - 1)

    for i in range(len(data) - 1):
        diff[i] = data[i + 1] - data[i]

    return diff


def find_distinct_ways(data):

    diff = calculate_difference(data)

    two_consecutive = 0
    three_consecutive = 0
    four_consecutive = 0

    i = 0
    while i < len(diff) - 3:
        if diff[i] == 1 and diff[i + 1] == 1:
            if diff[i + 2] == 1 and diff[i + 3] == 1:
                four_consecutive += 1
                i += 3
            elif diff[i + 2] == 1:
                three_consecutive += 1
                i += 2
            else:
                two_consecutive += 1
                i += 1
        i += 1

    return 7**four_consecutive * 4**three_consecutive * 2**two_consecutive
