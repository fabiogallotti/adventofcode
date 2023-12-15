def part_1(data):
    data = [row.split(",") for row in data][0]
    return sum(hash_algoritm(elem) for elem in data)


def hash_algoritm(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part_2(data):
    boxes = {}

    data = [row.split(",") for row in data][0]

    data = [row.strip("-").split("=") for row in data]

    for elem in data:
        if len(elem) == 1:
            label = elem[0]
            hash_value = hash_algoritm(label)

            if hash_value in boxes:
                for lens in boxes[hash_value]:
                    if lens[0] == label:
                        boxes[hash_value].remove(lens)

        if len(elem) == 2:
            label = elem[0]
            focal = elem[1]
            hash_value = hash_algoritm(label)

            if hash_value not in boxes:
                boxes[hash_value] = [elem]
            else:
                labels = [lens[0] for lens in boxes[hash_value]]

                if label in labels:
                    pos = labels.index(label)
                    boxes[hash_value][pos][1] = focal
                else:
                    boxes[hash_value].append(elem)

    focusing_power = 0
    for box, value in boxes.items():
        box_power = sum(
            (1 + int(box)) * (boxes[box].index(lens) + 1) * int(lens[1]) for lens in value
        )
        focusing_power += box_power

    return focusing_power
