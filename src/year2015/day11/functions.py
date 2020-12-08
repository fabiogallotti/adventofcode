import string


def increment(data, position):
    if data[position] in string.ascii_lowercase[: len(string.ascii_lowercase) - 1]:
        data[position] = chr(ord(data[position]) + 1)
    elif data[position] == "z":
        data[position] = "a"
        position += -1
        return increment(data, position)


def next_password(data):
    position = -1
    j = 0
    while not check_valid(data):
        data = list(data)
        increment(data, position)
        j += 1

    return "".join(data)


def next_word(data):
    next_word = list(data)
    increment(next_word, -1)
    return "".join(next_word)


def check_increasing_straight(data):
    return any(
        ord(data[i]) + 1 == ord(data[i + 1])
        and ord(data[i + 1]) + 1 == ord(data[i + 2])
        for i in range(len(data) - 2)
    )


def check_iol(data):
    return "i" not in data and "o" not in data and "l" not in data


def check_two_pairs(data):
    pairs = 0
    i = 0
    while i < len(data) - 1:
        if data[i] == data[i + 1]:
            pairs += 1
            i += 1
        i += 1
    return pairs == 2


def check_valid(data):
    return check_increasing_straight(data) and check_iol(data) and check_two_pairs(data)
