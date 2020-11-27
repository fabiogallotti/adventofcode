def read_input(filename):
    with open(filename, "r") as f:
        return [x.split("x") for x in f.read().split("\n")]


def calculate_area(box):
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])

    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def calculate_ribbon(box):
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    min_face = min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)
    volume = l * w * h
    return min_face + volume
