def preprocessing(data):
    rocks = {}
    for row in data:
        p = [x.split(",") for x in row.split("->")]

        points = [(int(x[0]), int(x[1])) for x in p]

        for p1, p2 in zip(points, points[1:]):
            x1, y1 = p1
            x2, y2 = p2

            for x in range(min(x1, x2), max(x1, x2) + 1):
                rocks[(x, y1)] = "#"

            for y in range(min(y1, y2), max(y1, y2) + 1):
                rocks[(x1, y)] = "#"

    return rocks


def sand_movement(pos, rocks):
    x = pos[0]
    y = pos[1]
    if (x, y + 1) not in rocks:
        return sand_movement((x, y + 1), rocks)
    elif (x - 1, y + 1) not in rocks:
        return sand_movement((x - 1, y + 1), rocks)
    elif (x + 1, y + 1) not in rocks:
        return sand_movement((x + 1, y + 1), rocks)
    else:
        rocks[pos] = "o"
        return 1


def part_1(data):
    rocks = preprocessing(data)
    sand_start = (500, 0)

    num_sand = 0
    while True:
        try:
            num_sand += sand_movement(sand_start, rocks)
        except RecursionError:
            break
    return num_sand


def sand_movement_part_2(pos, rocks):
    x = pos[0]
    y = pos[1]
    if (x, y + 1) not in rocks:
        return sand_movement_part_2((x, y + 1), rocks)
    elif (x - 1, y + 1) not in rocks:
        return sand_movement_part_2((x - 1, y + 1), rocks)
    elif (x + 1, y + 1) not in rocks:
        return sand_movement_part_2((x + 1, y + 1), rocks)
    else:
        rocks[pos] = "o"
        return (1, pos)


def part_2(data):
    rocks = preprocessing(data)
    sand_start = (500, 0)

    max_y = max(y for (_, y) in rocks.keys())

    floor = [(x, max_y + 2) for x in range(-1000, 1000)]
    for elem in floor:
        rocks[elem] = "#"

    num_sand = 0
    while True:
        num, pos = sand_movement_part_2(sand_start, rocks)
        num_sand += num

        if pos == sand_start:
            break

    return num_sand
