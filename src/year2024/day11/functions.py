from collections import defaultdict


def transform(stone):
    str_stone = str(stone)
    if stone == 0:
        return [1]
    elif len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        return [int(str_stone[:mid]), int(str_stone[mid:])]
    else:
        return [stone * 2024]


def flatten_list(original):
    expanded_list = []
    for elem in original:
        if isinstance(elem, list):
            expanded_list.extend(elem)
        else:
            expanded_list.append(elem)

    return expanded_list


def part_1(data):
    initial = [int(v) for elem in data for v in elem.split()]

    new_arrangement = initial.copy()
    for _ in range(25):
        for i in range(len(initial)):
            stone = initial[i]
            new_arrangement[i] = transform(stone)

        new_arrangement = flatten_list(new_arrangement)
        initial = new_arrangement.copy()

    return len(new_arrangement)


def part_2(data):
    initial = [int(v) for elem in data for v in elem.split()]

    stone_counts = defaultdict(int)
    for stone in initial:
        stone_counts[stone] += 1

    stone_counts = apply_blink(stone_counts, 75)

    return sum(stone_counts.values())


def apply_blink(stone_counts, blinks):
    if blinks == 0:
        return stone_counts

    new_stone_counts = defaultdict(int)

    for stone, count in stone_counts.items():
        transformed_stones = transform(stone)
        for transformed_stone in transformed_stones:
            new_stone_counts[transformed_stone] += count

    return apply_blink(new_stone_counts, blinks - 1)
