from enum import Enum

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
    UP_RIGHT = (-1, 1)
    DOWN_RIGHT = (1, 1)
    DOWN_LEFT = (1, -1)
    UP_LEFT = (-1, -1)


def preprocessing(data):
    paper = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            elem = data[i][j]
            if elem == "@":
                paper.add(Position(x=i, y=j))

    return paper


def part_1(data):
    directions = list(Direction)
    paper = preprocessing(data)
    total = 0

    for elem in paper:
        count = 0
        for direction in directions:
            dx, dy = direction.value
            next_pos = Position(x=elem.x + dx, y=elem.y + dy)
            if next_pos in paper:
                count += 1
        if count < 4:
            total += 1
    return total


def part_2(data):
    directions = list(Direction)
    paper = preprocessing(data)
    total = 0

    while True:
        to_remove = set()
        for elem in paper:
            count = 0
            for direction in directions:
                dx, dy = direction.value
                next_pos = Position(x=elem.x + dx, y=elem.y + dy)
                if next_pos in paper:
                    count += 1
            if count < 4:
                total += 1
                to_remove.add(elem)
        if not to_remove:
            break
        paper -= to_remove
    return total
