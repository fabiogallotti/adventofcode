def part_1(data):
    data = [list(map(int, elem.split("x"))) for elem in data]
    return sum(calculate_area(box) for box in data)


def part_2(data):
    data = [list(map(int, elem.split("x"))) for elem in data]
    return sum(calculate_ribbon(box) for box in data)


def calculate_area(box):
    l = box[0]
    w = box[1]
    h = box[2]

    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def calculate_ribbon(box):
    l = box[0]
    w = box[1]
    h = box[2]

    min_face = min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)
    volume = l * w * h
    return min_face + volume
