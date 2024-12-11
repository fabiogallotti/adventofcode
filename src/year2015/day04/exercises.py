import hashlib


def part_1(data):
    key = data[0]
    return get_hash(key, 5)


def part_2(data):
    key = data[0]
    return get_hash(key, 6)


def get_hash(key, zero_count):
    target = "0" * zero_count
    count = 1
    while True:
        phrase = f"{key}{count}"
        result = hashlib.md5(phrase.encode("utf-8")).hexdigest()
        if result.startswith(target):
            return count
        count += 1
