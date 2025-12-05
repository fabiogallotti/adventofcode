def preprocess(data):
    fresh = []
    available = []

    for elem in data:
        if elem == "":
            continue
        elif "-" in elem:
            start, end = elem.split("-")
            fresh.append((int(start), int(end)))
        else:
            available.append(int(elem))

    return sorted(fresh), sorted(available)


def part_1(data):
    fresh, available = preprocess(data)

    count = 0
    for num in available:
        for start, end in fresh:
            if start <= num <= end:
                count += 1
                break

    return count


def part_2(data):
    fresh, _ = preprocess(data)

    intervals = []
    for start, end in fresh:
        if not intervals or start > intervals[-1][1] + 1:
            intervals.append([start, end])
        else:
            intervals[-1][1] = max(intervals[-1][1], end)

    return sum(end - start + 1 for start, end in intervals)
