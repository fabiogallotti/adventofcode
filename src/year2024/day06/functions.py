import itertools
from enum import Enum

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def add(self, p2):
        return Point(x=self.x + p2.x, y=self.y + p2.y)

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


class Direction(Enum):
    UP = Point(x=-1, y=0)
    RIGHT = Point(x=0, y=1)
    DOWN = Point(x=1, y=0)
    LEFT = Point(x=0, y=-1)


def next_direction(d):
    if d == Direction.UP:
        return Direction.RIGHT
    elif d == Direction.RIGHT:
        return Direction.DOWN
    elif d == Direction.DOWN:
        return Direction.LEFT
    elif d == Direction.LEFT:
        return Direction.UP


def inside_borders(point, max_x, max_y):
    return 0 <= point.x <= max_x and 0 <= point.y <= max_y


def preprocessing(data):
    obstacles = []

    for i, j in itertools.product(range(len(data)), range(len(data[0]))):
        if data[i][j] == "#":
            obstacles.append(Point(x=i, y=j))
        elif data[i][j] == "^":
            starting_point = Point(x=i, y=j)

    return obstacles, starting_point


def part_1(data):
    obstacles, starting_point = preprocessing(data)
    direction = Direction.UP

    point = starting_point.model_copy()

    visited = set()
    while inside_borders(point, len(data) - 1, len(data[0]) - 1):
        visited.add(point)

        next_point = point.add(direction.value)

        if next_point in obstacles:
            direction = next_direction(direction)
        else:
            point = next_point

    return len(visited)


def part_2(data):
    obstacles, starting_point = preprocessing(data)
    direction = Direction.UP

    point = starting_point.model_copy()
    visited = set()
    while inside_borders(point, len(data) - 1, len(data[0]) - 1):
        visited.add(point)

        next_point = point.add(direction.value)

        if next_point in obstacles:
            direction = next_direction(direction)
        else:
            point = next_point

    count = 0
    for elem in visited:
        point = starting_point.model_copy()
        direction = Direction.UP

        obstacles.append(elem)
        visited = set()
        while inside_borders(point, len(data) - 1, len(data[0]) - 1):
            visited.add((point, direction))

            next_point = point.add(direction.value)
            if next_point in obstacles:
                direction = next_direction(direction)
            elif (next_point, direction) in visited:
                count += 1
                print(count)
                break
            else:
                point = next_point

        obstacles.remove(elem)

    return count
