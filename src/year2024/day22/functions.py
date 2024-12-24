from collections import defaultdict


def part_1(data):
    initial_numbers = {int(x) for x in data}

    total = 0
    for number in initial_numbers:
        for _ in range(2000):
            first = first_step(number)
            second = second_step(first)
            third = third_step(second)
            number = third
        total += number

    return total


def first_step(number):
    result = number * 64
    mixed = mix(number, result)
    return prune(mixed)


def second_step(number):
    result = number // 32
    mixed = mix(number, result)
    return prune(mixed)


def third_step(number):
    result = number * 2048
    mixed = mix(number, result)
    return prune(mixed)


def mix(secret, value):
    return value ^ secret


def prune(secret):
    return secret % 16777216


def part_2(data):
    initial_numbers = {int(x) for x in data}

    sequences = defaultdict(int)

    for number in initial_numbers:
        buyer_price = [number % 10]

        for _ in range(2000):
            first = first_step(number)
            second = second_step(first)
            third = third_step(second)
            number = third
            buyer_price.append(number % 10)

        seen = set()
        for i in range(len(buyer_price) - 4):
            a, b, c, d, e = buyer_price[i : i + 5]
            seq = (b - a, c - b, d - c, e - d)

            if seq not in seen:
                seen.add(seq)
                sequences[seq] += e

    return max(sequences.values())
