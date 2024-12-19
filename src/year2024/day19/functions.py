def find_ways(d, available, cache=None):
    if cache is None:
        cache = {}

    key = (d, tuple(available))
    if key in cache:
        return cache[key]

    if not d:
        return 1

    total_ways = 0
    for towel in available:
        if d.startswith(towel):
            remaining_d = d[len(towel) :]
            total_ways += find_ways(remaining_d, available, cache)

    cache[key] = total_ways
    return total_ways


def preprocessing(data):
    available = [x.strip() for x in data[0].split(",")]
    desired = data[2:]

    return available, desired


def part_1(data):
    available, desired = preprocessing(data)

    ways = [find_ways(d, tuple(available)) for d in desired]
    return sum(way > 0 for way in ways)


def part_2(data):
    available, desired = preprocessing(data)

    ways = [find_ways(d, available) for d in desired]
    return sum(ways)
