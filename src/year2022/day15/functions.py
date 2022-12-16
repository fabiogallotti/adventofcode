import itertools


def preprocessing(data):
    data = [row.split() for row in data]

    closest_beacon = {}
    manhattan_distances = {}
    for row in data:
        xs = int(row[2].split("=")[1].strip(","))
        ys = int(row[3].split("=")[1].strip(":"))

        xb = int(row[8].split("=")[1].strip(","))
        yb = int(row[9].split("=")[1].strip(":"))

        closest_beacon[(xs, ys)] = (xb, yb)
        manhattan_distances[(xs, ys)] = manhattan((xs, ys), (xb, yb))

    return manhattan_distances, closest_beacon


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def check_row(distances, closest, row):
    not_present = set()
    beacon_xs = set()

    for point, d in distances.items():
        xs, ys = point
        xb, yb = closest[point]

        if yb == row:
            beacon_xs.add(xb)

        if (window := d - abs(row - ys)) >= 0:
            not_present.update(list(range(xs - window, xs + window + 1)))

    not_present.difference_update(beacon_xs)
    return len(not_present)


def part_1(data, row):
    manhattan_distances, closest_beacon = preprocessing(data)
    return check_row(manhattan_distances, closest_beacon, row)


def part_2(data, max_coordinate):
    manhattan_distances, _ = preprocessing(data)

    checked_points = set()
    for point, d in manhattan_distances.items():
        xs, ys = point

        for side, i in itertools.product(range(4), range(d + 1)):
            if side == 0:
                xc = xs + d + 1 - i
                yc = ys + i
            elif side == 1:
                xc = xs - i
                yc = ys + d + 1 - i
            elif side == 2:
                xc = xs - d - 1 + i
                yc = ys - i
            elif side == 3:
                xc = xs + i
                yc = ys - d - 1 + i

            if (
                0 <= xc <= max_coordinate
                and 0 <= yc <= max_coordinate
                and (xc, yc) not in checked_points
            ):
                found = all(
                    (abs(xc - otherx) + abs(yc - othery)) > other_distance
                    for (otherx, othery), other_distance in manhattan_distances.items()
                )
                if found:
                    return 4000000 * xc + yc
                else:
                    checked_points.add((xc, yc))
