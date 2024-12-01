import contextlib
from enum import Enum

from pydantic import BaseModel


class Direction(Enum):
    L = "left"
    R = "right"
    U = "up"
    D = "down"


class Point(BaseModel):
    x: int
    y: int
    direction: Direction

    def __hash__(self):
        return hash((self.x, self.y))


class Connections(Enum):
    D = "."
    NS = "|"
    EW = "-"
    SW = "\\"
    SE = "/"


def part_1(data):
    p = Point(x=0, y=0, direction=Direction.R)
    energized = set()
    visited = set()
    to_be_checked = [p]

    while to_be_checked:
        new_points = evaluate_neighbors(to_be_checked[0], data, energized, visited)
        to_be_checked.pop(0)

        if new_points and all(new_point not in visited for new_point in new_points):
            to_be_checked.extend(new_points)

    return len(energized)


def evaluate_neighbors(p, data, energized, visited):
    with contextlib.suppress(IndexError):
        if p.x < 0 or p.y < 0 or p.x >= len(data) or p.y >= len(data[0]):
            return

        energized.add((p.x, p.y))
        visited.add(p)
        if p.direction == Direction.R:
            if data[p.x][p.y] == Connections.D.value:
                new_points = [Point(x=p.x, y=p.y + 1, direction=Direction.R)]
            elif data[p.x][p.y] == Connections.NS.value:
                new_points = [
                    Point(x=p.x - 1, y=p.y, direction=Direction.U),
                    Point(x=p.x + 1, y=p.y, direction=Direction.D),
                ]
            elif data[p.x][p.y] == Connections.EW.value:
                new_points = [Point(x=p.x, y=p.y + 1, direction=Direction.R)]
            elif data[p.x][p.y] == Connections.SW.value:
                new_points = [Point(x=p.x + 1, y=p.y, direction=Direction.D)]
            elif data[p.x][p.y] == Connections.SE.value:
                new_points = [Point(x=p.x - 1, y=p.y, direction=Direction.U)]

        elif p.direction == Direction.L:
            if data[p.x][p.y] == Connections.D.value:
                new_points = [Point(x=p.x, y=p.y - 1, direction=Direction.L)]
            elif data[p.x][p.y] == Connections.NS.value:
                new_points = [
                    Point(x=p.x - 1, y=p.y, direction=Direction.U),
                    Point(x=p.x + 1, y=p.y, direction=Direction.D),
                ]
            elif data[p.x][p.y] == Connections.EW.value:
                new_points = [Point(x=p.x, y=p.y - 1, direction=Direction.L)]
            elif data[p.x][p.y] == Connections.SW.value:
                new_points = [Point(x=p.x - 1, y=p.y, direction=Direction.U)]
            elif data[p.x][p.y] == Connections.SE.value:
                new_points = [Point(x=p.x + 1, y=p.y, direction=Direction.D)]

        elif p.direction == Direction.D:
            if data[p.x][p.y] == Connections.D.value:
                new_points = [Point(x=p.x + 1, y=p.y, direction=Direction.D)]
            elif data[p.x][p.y] == Connections.NS.value:
                new_points = [Point(x=p.x + 1, y=p.y, direction=Direction.D)]
            elif data[p.x][p.y] == Connections.EW.value:
                new_points = [
                    Point(x=p.x, y=p.y - 1, direction=Direction.L),
                    Point(x=p.x, y=p.y + 1, direction=Direction.R),
                ]
            elif data[p.x][p.y] == Connections.SW.value:
                new_points = [Point(x=p.x, y=p.y + 1, direction=Direction.R)]
            elif data[p.x][p.y] == Connections.SE.value:
                new_points = [Point(x=p.x, y=p.y - 1, direction=Direction.L)]

        elif p.direction == Direction.U:
            if data[p.x][p.y] == Connections.D.value:
                new_points = [Point(x=p.x - 1, y=p.y, direction=Direction.U)]
            elif data[p.x][p.y] == Connections.NS.value:
                new_points = [Point(x=p.x - 1, y=p.y, direction=Direction.U)]
            elif data[p.x][p.y] == Connections.EW.value:
                new_points = [
                    Point(x=p.x, y=p.y - 1, direction=Direction.L),
                    Point(x=p.x, y=p.y + 1, direction=Direction.R),
                ]
            elif data[p.x][p.y] == Connections.SW.value:
                new_points = [Point(x=p.x, y=p.y - 1, direction=Direction.L)]
            elif data[p.x][p.y] == Connections.SE.value:
                new_points = [Point(x=p.x, y=p.y + 1, direction=Direction.R)]

        return new_points


def part_2(data):
    max_x = len(data[0]) - 1
    max_y = len(data) - 1

    starting_points = []

    top_row = [Point(x=0, y=i, direction=Direction.D) for i in range(len(data))]
    starting_points.extend(top_row)

    bottom_row = [Point(x=max_x, y=i, direction=Direction.U) for i in range(len(data))]
    starting_points.extend(bottom_row)

    left_column = [Point(x=i, y=0, direction=Direction.R) for i in range(len(data))]
    starting_points.extend(left_column)

    right_column = [Point(x=i, y=max_y, direction=Direction.L) for i in range(len(data))]
    starting_points.extend(right_column)

    all_energized = []
    for p in starting_points:
        energized = set()
        visited = set()
        to_be_checked = [p]

        while to_be_checked:
            new_points = evaluate_neighbors(to_be_checked[0], data, energized, visited)
            to_be_checked.pop(0)

            if new_points and all(new_point not in visited for new_point in new_points):
                to_be_checked.extend(new_points)

        all_energized.append(len(energized))

    return max(all_energized)
