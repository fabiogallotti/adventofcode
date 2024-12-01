def x_char_different(x, data):
    for i in range(len(data) - x):
        chars = set()
        for j in range(i, i + x):
            chars.add(data[j])
        if len(chars) == x:
            return j + 1


def part_1(data):
    return x_char_different(4, data)


def part_2(data):
    return x_char_different(14, data)
