import contextlib
from enum import Enum

from pydantic import BaseModel


class Point(BaseModel):
    point: str
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


class Direction(BaseModel):
    x: int
    y: int


class Connections(Enum):
    NS = "|"
    EW = "-"
    NE = "L"
    NW = "J"
    SW = "7"
    SE = "F"
    S = "S"


VALUES = [member.value for member in Connections]


def part_1(data):
    data = [list(row) for row in data]

    visited_points = []
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "S":
                s = Point(point="S", x=i, y=j)
                visited_points.append(s)

    next_point = evaluate_neighbors(s, data, visited_points)
    while next_point is not None:
        next_point = evaluate_neighbors(next_point, data, visited_points)

    visited_points.append(s)
    return len(visited_points) // 2


def evaluate_neighbors(point, data, visited_points):
    with contextlib.suppress(IndexError):
        u = Point(point=data[point.x - 1][point.y], x=point.x - 1, y=point.y)
        if (
            point.point == "S"
            and u.point in [Connections.NS.value, Connections.SE.value, Connections.SW.value]
        ) or (
            u not in visited_points
            and point.point in [Connections.NS.value, Connections.NE.value, Connections.NW.value]
        ):
            visited_points.append(u)
            return u

    with contextlib.suppress(IndexError):
        r = Point(point=data[point.x][point.y + 1], x=point.x, y=point.y + 1)
        if (
            point.point == "S"
            and r.point in [Connections.EW.value, Connections.NW.value, Connections.SW.value]
        ) or (
            r not in visited_points
            and point.point in [Connections.EW.value, Connections.NE.value, Connections.SE.value]
        ):
            visited_points.append(r)
            return r

    with contextlib.suppress(IndexError):
        d = Point(point=data[point.x + 1][point.y], x=point.x + 1, y=point.y)
        if (
            point.point == "S"
            and d.point in [Connections.NS.value, Connections.NW.value, Connections.NE.value]
        ) or (
            d not in visited_points
            and point.point in [Connections.NS.value, Connections.SW.value, Connections.SE.value]
        ):
            visited_points.append(d)
            return d

    with contextlib.suppress(IndexError):
        l = Point(point=data[point.x][point.y - 1], x=point.x, y=point.y - 1)

        if (
            point.point == "S"
            and l.point in [Connections.EW.value, Connections.NE.value, Connections.SE.value]
        ) or (
            l not in visited_points
            and point.point in [Connections.EW.value, Connections.NW.value, Connections.SW.value]
        ):
            visited_points.append(l)
            return l


def part_2(data):
    data = [list(row) for row in data]

    visited_points = []
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "S":
                s = Point(point="S", x=i, y=j)
                visited_points.append(s)

    next_point = evaluate_neighbors(s, data, visited_points)
    while next_point is not None:
        next_point = evaluate_neighbors(next_point, data, visited_points)

    visited_points.append(s)

    max_column = len(data[0])
    enclosed = 0

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            p = Point(point=data[i][j], x=i, y=j)
            if p not in visited_points:
                k = p.y + 1
                count = 0
                while k < max_column:
                    new_p = Point(point=data[i][k], x=i, y=k)
                    if (
                        new_p.point
                        in [
                            Connections.NS.value,
                            Connections.SW.value,
                            Connections.SE.value,
                        ]
                        and new_p in visited_points
                    ):
                        count += 1
                    elif new_p.point == "S":
                        previous_p = visited_points[1]
                        next_p = visited_points[-2]

                        if abs(next_p.x - previous_p.x) == 2:
                            count += 1
                        elif (
                            abs(next_p.x - previous_p.x) == 1 and abs(next_p.y - previous_p.y) == 1
                        ):
                            count += 1

                    k += 1

                if count % 2 != 0:
                    enclosed += 1
    return enclosed
