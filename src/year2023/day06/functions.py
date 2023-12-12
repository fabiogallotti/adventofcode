def part_1(data):
    times = [int(x) for x in data[0].split(":")[1].split()]
    distances = [int(x) for x in data[1].split(":")[1].split()]

    ways = 1
    for time in times:
        win = 0
        for t in range(time + 1):
            move = t * (time - t)
            pos = times.index(time)

            if move > distances[pos]:
                win += 1
        ways *= win

    return ways


def part_2(data):
    times = list(data[0].split(":")[1].split())
    distances = list(data[1].split(":")[1].split())
    times = int("".join(times))
    distances = int("".join(distances))

    win = 0
    for t in range(times + 1):
        move = t * (times - t)
        if move > distances:
            win += 1
    return win
