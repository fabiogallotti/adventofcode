import itertools
from collections import defaultdict
from enum import Enum

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


def preprocessing(data):
    map_dict = defaultdict(set)
    for i, j in itertools.product(range(len(data)), range(len(data[0]))):
        elem = data[i][j]
        map_dict[elem].add(Point(x=i, y=j))
    return map_dict


def check_around(start_point, points, seen):
    stack = [start_point]
    region = set()

    while stack:
        point = stack.pop()
        if point in seen:
            continue
        seen.add(point)
        region.add(point)

        for direction in Direction:
            neighbor = Point(x=point.x + direction.value[0], y=point.y + direction.value[1])
            if neighbor in points and neighbor not in seen:
                stack.append(neighbor)
    return region


def calc_perimeter(point, points):
    u_point = Point(x=point.x + Direction.UP.value[0], y=point.y + Direction.UP.value[1])
    r_point = Point(x=point.x + Direction.RIGHT.value[0], y=point.y + Direction.RIGHT.value[1])
    d_point = Point(x=point.x + Direction.DOWN.value[0], y=point.y + Direction.DOWN.value[1])
    l_point = Point(x=point.x + Direction.LEFT.value[0], y=point.y + Direction.LEFT.value[1])

    new_points = [u_point, r_point, d_point, l_point]
    return 4 - sum(point in points for point in new_points)


def part_1(data):
    map_dict = preprocessing(data)

    seen = set()
    regions = defaultdict(list)

    for elem, points in map_dict.items():
        for point in points:
            if point not in seen:
                new_region = check_around(point, points, seen)
                regions[elem].append(new_region)

    price = 0

    for region in regions.values():
        for points in region:
            area = len(points)
            perimeter = sum(calc_perimeter(point, points) for point in points)
            price += area * perimeter

    return price


def compute_sides(points):
    sides = 0

    for point in points:
        u_point = Point(x=point.x + Direction.UP.value[0], y=point.y + Direction.UP.value[1])
        l_point = Point(x=point.x + Direction.LEFT.value[0], y=point.y + Direction.LEFT.value[1])
        ul_point = Point(x=point.x + Direction.UP.value[0], y=point.y + Direction.LEFT.value[1])

        if u_point not in points:
            same_edge = (l_point in points) and (ul_point not in points)
            if not same_edge:
                sides += 1

        d_point = Point(x=point.x + Direction.DOWN.value[0], y=point.y + Direction.DOWN.value[1])
        dl_point = Point(x=point.x + Direction.DOWN.value[0], y=point.y + Direction.LEFT.value[1])

        if d_point not in points:
            same_edge = (l_point in points) and (dl_point not in points)
            if not same_edge:
                sides += 1

        if l_point not in points:
            same_edge = (u_point in points) and (ul_point not in points)
            if not same_edge:
                sides += 1

        r_point = Point(x=point.x + Direction.RIGHT.value[0], y=point.y + Direction.RIGHT.value[1])
        ur_point = Point(x=point.x + Direction.UP.value[0], y=point.y + Direction.RIGHT.value[1])

        if r_point not in points:
            same_edge = (u_point in points) and (ur_point not in points)
            if not same_edge:
                sides += 1

    return sides


def part_2(data):
    map_dict = preprocessing(data)

    seen = set()
    regions = defaultdict(list)

    for elem, points in map_dict.items():
        for point in points:
            if point not in seen:
                new_region = check_around(point, points, seen)
                regions[elem].append(new_region)

    price = 0

    for region in regions.values():
        for points in region:
            area = len(points)
            sides = compute_sides(points)
            price += area * sides

    return price
