import hashlib


def part_1(data):
    key = data[0]
    return get_hash(key, 5)


def part_2(data):
    key = data[0]
    return get_hash(key, 6)


def get_hash(key, number):
    count = 1
    while True:
        phrase = key + str(count)
        result = hashlib.md5(phrase.encode("utf-8")).hexdigest()
        if result[:number] == "0" * number:
            return count
        count += 1
