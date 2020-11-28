def convert_to_int(box):
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    return l, w, h


def calculate_area(box):
    l, w, h = convert_to_int(box)

    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def calculate_ribbon(box):
    l, w, h = convert_to_int(box)

    min_face = min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)
    volume = l * w * h
    return min_face + volume
