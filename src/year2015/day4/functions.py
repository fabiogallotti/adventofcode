import hashlib


def starting_zeros(key, number):
    count = 1
    while True:
        phrase = key + str(count)
        result = hashlib.md5(phrase.encode("utf-8")).hexdigest()
        if result[:number] == "0" * number:
            return count
        count += 1
