import itertools
from enum import Enum

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int
    value: int

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


def check_around(point, map_dict, max_x, max_y):
    if point.value == 9:
        return 1
    new_value = point.value + 1

    u_point = Point(x=point.x - 1, y=point.y, value=point.value + 1)
    r_point = Point(x=point.x, y=point.y + 1, value=point.value + 1)
    d_point = Point(x=point.x + 1, y=point.y, value=point.value + 1)
    l_point = Point(x=point.x, y=point.y - 1, value=point.value + 1)

    total = 0
    if u_point in map_dict[new_value]:
        total += check_around(u_point, map_dict, max_x, max_y)
    if r_point in map_dict[new_value]:
        total += check_around(r_point, map_dict, max_x, max_y)
    if d_point in map_dict[new_value]:
        total += check_around(d_point, map_dict, max_x, max_y)
    if l_point in map_dict[new_value]:
        total += check_around(l_point, map_dict, max_x, max_y)

    return total


def check_around_1(point, map_dict, max_x, max_y, seen_nines):
    if point.value == 9:
        seen_nines.add(point)
        return
    new_value = point.value + 1

    u_point = Point(x=point.x - 1, y=point.y, value=point.value + 1)
    r_point = Point(x=point.x, y=point.y + 1, value=point.value + 1)
    d_point = Point(x=point.x + 1, y=point.y, value=point.value + 1)
    l_point = Point(x=point.x, y=point.y - 1, value=point.value + 1)

    if u_point in map_dict[new_value]:
        check_around_1(u_point, map_dict, max_x, max_y, seen_nines)
    if r_point in map_dict[new_value]:
        check_around_1(r_point, map_dict, max_x, max_y, seen_nines)
    if d_point in map_dict[new_value]:
        check_around_1(d_point, map_dict, max_x, max_y, seen_nines)
    if l_point in map_dict[new_value]:
        check_around_1(l_point, map_dict, max_x, max_y, seen_nines)

    return len(seen_nines)


def preprocessing(data):
    trailheads = []
    map_dict = {}
    for i, j in itertools.product(range(len(data)), range(len(data[0]))):
        elem = int(data[i][j])
        if elem == 0:
            trailheads.append(Point(x=i, y=j, value=elem))

        elif elem in map_dict:
            map_dict[elem].append(Point(x=i, y=j, value=elem))
        else:
            map_dict[elem] = [Point(x=i, y=j, value=elem)]

    return trailheads, map_dict


def part_1(data):
    trailheads, map_dict = preprocessing(data)
    max_x = len(data)
    max_y = len(data[0])

    total = 0
    for trail in trailheads:
        seen_nines = set()
        total += check_around_1(trail, map_dict, max_x, max_y, seen_nines)

    return total


def part_2(data):
    trailheads, map_dict = preprocessing(data)
    max_x = len(data)
    max_y = len(data[0])
    return sum(check_around(trail, map_dict, max_x, max_y) for trail in trailheads)
