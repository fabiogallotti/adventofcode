from enum import Enum
from itertools import product

from pydantic import BaseModel


class Position(BaseModel):
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
    walls = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            value = data[i][j]
            if value == "#":
                walls.add(Position(x=i, y=j))
            elif value == "S":
                start = Position(x=i, y=j)
            elif value == "E":
                end = Position(x=i, y=j)

    return walls, start, end


def get_distances(start, end, max_x, max_y, walls):
    distances = [[-1] * max_y for _ in range(max_x)]
    distances[start.x][start.y] = 0

    directions = list(Direction)

    pos = start
    while pos != end:
        for direction in directions:
            dx, dy = direction.value
            next_pos = Position(x=pos.x + dx, y=pos.y + dy)

            if (
                0 <= next_pos.x < max_x
                and 0 <= next_pos.y < max_y
                and next_pos not in walls
                and distances[next_pos.x][next_pos.y] == -1
            ):
                distances[next_pos.x][next_pos.y] = distances[pos.x][pos.y] + 1
                pos = next_pos

    return distances


def part_1(data, min_time_saved=100):
    walls, start, end = preprocessing(data)

    max_x = len(data)
    max_y = len(data[0])

    distances = get_distances(start, end, max_x, max_y, walls)

    cheat_directions = [Position(x=2, y=0), Position(x=0, y=2)]

    count = 0
    for i, j in product(range(max_x), range(max_y)):
        pos = Position(x=i, y=j)
        if pos in walls:
            continue

        for direction in cheat_directions:
            next_pos = Position(x=i + direction.x, y=j + direction.y)
            if 0 <= next_pos.x < max_x and 0 <= next_pos.y < max_y and next_pos not in walls:
                diff = abs(distances[i][j] - distances[next_pos.x][next_pos.y]) - 2
                if diff >= min_time_saved:
                    count += 1

    return count


def part_2(data, min_time_saved=100):
    walls, start, end = preprocessing(data)

    max_x = len(data)
    max_y = len(data[0])

    distances = get_distances(start, end, max_x, max_y, walls)

    count = 0
    for i, j in product(range(max_x), range(max_y)):
        pos = Position(x=i, y=j)
        if pos in walls:
            continue

        for p in range(2, 21):
            for dx in range(p + 1):
                dy = p - dx
                cheat_positions = {
                    Position(x=i + dx, y=j + dy),
                    Position(x=i + dx, y=j - dy),
                    Position(x=i - dx, y=j + dy),
                    Position(x=i - dx, y=j - dy),
                }

                for next_pos in cheat_positions:
                    if (
                        0 <= next_pos.x < max_x
                        and 0 <= next_pos.y < max_y
                        and next_pos not in walls
                    ):
                        diff = distances[i][j] - distances[next_pos.x][next_pos.y] - p
                        if diff >= min_time_saved:
                            count += 1

    return count
