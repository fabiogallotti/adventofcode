def part_1(data):
    x = 0
    y = 0

    for elem in data:
        if elem[0] == "forward":
            x += int(elem[1])
        elif elem[0] == "down":
            y += int(elem[1])
        elif elem[0] == "up":
            y -= int(elem[1])
    return x * y


def part_2(data):
    x = 0
    y = 0
    aim = 0

    for elem in data:
        if elem[0] == "forward":
            x += int(elem[1])
            y += aim * int(elem[1])
        elif elem[0] == "down":
            aim += int(elem[1])
        elif elem[0] == "up":
            aim -= int(elem[1])
    return x * y
