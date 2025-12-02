def preprocess_input(data):
    directions = []
    steps = []

    for elem in data:
        d = elem[0]
        s = elem[1:]
        directions.append(d)
        steps.append(int(s))

    return directions, steps


def part_1(data):
    pos = 50
    directions, steps = preprocess_input(data)
    count = 0

    for d in directions:
        if d == "L":
            pos -= steps.pop(0)
            while pos < 0:
                pos += 100
        elif d == "R":
            pos += steps.pop(0)
            while pos > 99:
                pos -= 100

        if pos == 0:
            count += 1
    return count


def part_2(data):
    pos = 50
    directions, steps = preprocess_input(data)
    count = 0

    for d in directions:
        step = steps.pop(0)
        while step > 0:
            if d == "L":
                pos -= 1
                while pos < 0:
                    pos += 100
            elif d == "R":
                pos += 1
                while pos > 99:
                    pos -= 100

            if pos == 0:
                count += 1

            step -= 1
    return count
