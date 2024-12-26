from collections import defaultdict


def get_heights(list):
    heights = defaultdict(int)

    for i, key in enumerate(list):
        heights[i] = defaultdict(int)
        for row in key:
            for j, elem in enumerate(row):
                if elem == "#":
                    heights[i][j] += 1

    return heights


def preprocessing(data):
    locks = []
    keys = []

    current = []
    for row in data:
        if row == "" and current:
            (locks if current[0].startswith("#") else keys).append(current)
            current = []
        elif row != "":
            current.append(row)

    if current:
        (locks if current[0].startswith("#") else keys).append(current)

    return locks, keys


def part_1(data):
    locks, keys = preprocessing(data)
    locks_heights = get_heights(locks)
    keys_heights = get_heights(keys)
    max_height = len(locks[0])

    count = 0
    for i in range(len(locks_heights)):
        lock_heights = locks_heights[i]
        for j in range(len(keys_heights)):
            key_heights = keys_heights[j]

            fits = all(
                lock_heights[k] + key_heights[k] <= max_height for k in range(len(lock_heights))
            )
            if fits:
                count += 1

    return count
