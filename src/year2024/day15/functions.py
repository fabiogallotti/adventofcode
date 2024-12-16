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


def preprocessing(data):
    walls = []
    boxes = []
    movements = []

    for i, row in enumerate(data):
        if row == "":
            movements = "".join(data[i + 1 :])
            break
        for j in range(len(row)):
            value = data[i][j]
            if value == "#":
                walls.append(Position(x=i, y=j))
            elif value == "@":
                start = Position(x=i, y=j)
            elif value == "O":
                boxes.append(Position(x=i, y=j))

    mov_directions = []
    for elem in movements:
        if elem == "^":
            mov_directions.append(Direction.UP)
        elif elem == ">":
            mov_directions.append(Direction.RIGHT)
        elif elem == "v":
            mov_directions.append(Direction.DOWN)
        elif elem == "<":
            mov_directions.append(Direction.LEFT)

    return walls, boxes, start, mov_directions


def move(pos, direction, walls, boxes):
    new_pos = Position(x=pos.x + direction.value[0], y=pos.y + direction.value[1])
    if (new_pos not in walls) and (new_pos not in boxes):
        return new_pos

    elif new_pos in walls:
        return pos

    else:
        new_box_pos = move(new_pos, direction, walls, boxes)

        if new_box_pos == new_pos:
            return pos
        boxes.remove(new_pos)
        boxes.append(new_box_pos)

        return new_pos


def part_1(data):
    walls, boxes, start, mov_directions = preprocessing(data)

    for direction in mov_directions:
        start = move(start, direction, walls, boxes)

    return sum(100 * box.x + box.y for box in boxes)


class Position2(BaseModel):
    x: int
    y: int
    value: str

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


def preprocessing_2(data):
    walls = []
    boxes = []
    movements = []

    for i, row in enumerate(data):
        if data[i] == "":
            movements = "".join(data[i + 1 :])
            break
        else:
            data[i] = list(data[i])
            for j in range(len(row)):
                elem = data[i][j]
                if elem == "#":
                    data[i][j] = ["#", "#"]
                elif elem == "@":
                    data[i][j] = ["@", "."]
                elif elem == "O":
                    data[i][j] = ["[", "]"]
                else:
                    data[i][j] = [".", "."]

            data[i] = "".join(["".join(elem) for elem in data[i]])

    for i, row in enumerate(data):
        if row == "":
            break
        for j in range(len(row)):
            value = data[i][j]
            if value == "#":
                walls.append(Position2(x=i, y=j, value=value))
            elif value in ["[", "]"]:
                boxes.append(Position2(x=i, y=j, value=value))
            elif value == "@":
                start = Position2(x=i, y=j, value=value)

    mov_directions = []
    for elem in movements:
        if elem == "<":
            mov_directions.append(Direction.LEFT)
        elif elem == ">":
            mov_directions.append(Direction.RIGHT)
        elif elem == "^":
            mov_directions.append(Direction.UP)
        elif elem == "v":
            mov_directions.append(Direction.DOWN)
    return walls, boxes, start, mov_directions


def check_if_can_move_2(pos, direction, walls, boxes, can_move):
    new_pos = Position2(x=pos.x + direction.value[0], y=pos.y + direction.value[1], value=pos.value)

    new_pos_coords = (new_pos.x, new_pos.y)
    walls_coords = {(wall.x, wall.y) for wall in walls}
    boxes_coords = {(box.x, box.y) for box in boxes}

    if (new_pos_coords not in walls_coords) and (new_pos_coords not in boxes_coords):
        can_move.append(True)
        return new_pos, can_move

    elif new_pos_coords in walls_coords:
        can_move.append(False)
        return pos, can_move

    else:
        if direction == Direction.LEFT:
            new_pos_l = Position2(
                x=pos.x + direction.value[0], y=pos.y + direction.value[1] - 1, value="["
            )
            new_box_pos_l, can_move = check_if_can_move_2(
                new_pos_l, direction, walls, boxes, can_move
            )
            new_box_pos_r = Position2(x=new_box_pos_l.x, y=new_box_pos_l.y + 1, value="]")

            if (new_box_pos_r.x, new_box_pos_r.y) == new_pos_coords:
                can_move.append(False)
                return pos, can_move

            can_move.append(True)
            return new_pos, can_move

        elif direction == Direction.RIGHT:
            new_pos_r = Position2(
                x=pos.x + direction.value[0], y=pos.y + direction.value[1] + 1, value="]"
            )

            new_box_pos_r, can_move = check_if_can_move_2(
                new_pos_r, direction, walls, boxes, can_move
            )
            new_box_pos_l = Position2(x=new_box_pos_r.x, y=new_box_pos_r.y - 1, value="[")

            if (new_box_pos_l.x, new_box_pos_l.y) == new_pos_coords:
                can_move.append(False)
                return pos, can_move

            can_move.append(True)
            return new_pos, can_move

        elif direction in [Direction.UP, Direction.DOWN]:
            for elem in boxes:
                if (elem.x, elem.y) == (pos.x + direction.value[0], pos.y + direction.value[1]):
                    value_ = elem.value
                    break

            new_pos_c = Position2(
                x=pos.x + direction.value[0], y=pos.y + direction.value[1], value=value_
            )

            if new_pos_c.value == "[":
                new_pos_l = new_pos_c
                new_pos_r = Position2(x=new_pos_c.x, y=new_pos_c.y + 1, value="]")
            elif new_pos_c.value == "]":
                new_pos_l = Position2(x=new_pos_c.x, y=new_pos_c.y - 1, value="[")
                new_pos_r = new_pos_c

            new_box_pos_l, can_move = check_if_can_move_2(
                new_pos_l, direction, walls, boxes, can_move
            )
            new_box_pos_r, can_move = check_if_can_move_2(
                new_pos_r, direction, walls, boxes, can_move
            )

            if (new_box_pos_l.x, new_box_pos_l.y) == new_pos_coords or (
                new_box_pos_r.x,
                new_box_pos_r.y,
            ) == new_pos_coords:
                can_move.append(False)
                return pos, can_move

            can_move.append(True)
            return new_pos, can_move


def move_2(pos, direction, walls, boxes):
    new_pos = Position2(x=pos.x + direction.value[0], y=pos.y + direction.value[1], value=pos.value)

    new_pos_coords = (new_pos.x, new_pos.y)
    walls_coords = {(wall.x, wall.y) for wall in walls}
    boxes_coords = {(box.x, box.y) for box in boxes}

    if (new_pos_coords not in walls_coords) and (new_pos_coords not in boxes_coords):
        return new_pos

    elif new_pos_coords in walls:
        return pos

    else:
        if direction == Direction.LEFT:
            new_pos_l = Position2(
                x=pos.x + direction.value[0], y=pos.y + direction.value[1] - 1, value="["
            )
            new_box_pos_l = move_2(new_pos_l, direction, walls, boxes)
            new_box_pos_r = Position2(x=new_box_pos_l.x, y=new_box_pos_l.y + 1, value="]")

            if (new_box_pos_r.x, new_box_pos_r.y) == new_pos_coords:
                return pos

            if any((box.x, box.y) == (new_pos_l.x, new_pos_l.y) for box in boxes):
                for elem in boxes:
                    if (elem.x, elem.y) == (new_pos_l.x, new_pos_l.y):
                        boxes.remove(elem)
                        break
            if any((box.x, box.y) == (new_pos_l.x, new_pos_l.y + 1) for box in boxes):
                for elem in boxes:
                    if (elem.x, elem.y) == (new_pos_l.x, new_pos_l.y + 1):
                        boxes.remove(elem)
                        break

            boxes.append(new_box_pos_l)
            boxes.append(new_box_pos_r)

            return new_pos

        elif direction == Direction.RIGHT:
            new_pos_r = Position2(
                x=pos.x + direction.value[0], y=pos.y + direction.value[1] + 1, value="]"
            )

            new_box_pos_r = move_2(new_pos_r, direction, walls, boxes)
            new_box_pos_l = Position2(x=new_box_pos_r.x, y=new_box_pos_r.y - 1, value="[")

            if (new_box_pos_l.x, new_box_pos_l.y) == new_pos_coords:
                return pos

            if any((box.x, box.y) == (new_pos_r.x, new_pos_r.y) for box in boxes):
                for elem in boxes:
                    if (elem.x, elem.y) == (new_pos_r.x, new_pos_r.y):
                        boxes.remove(elem)
                        break
            if any((box.x, box.y) == (new_pos_r.x, new_pos_r.y - 1) for box in boxes):
                for elem in boxes:
                    if (elem.x, elem.y) == (new_pos_r.x, new_pos_r.y - 1):
                        boxes.remove(elem)
                        break

            boxes.append(new_box_pos_l)
            boxes.append(new_box_pos_r)

            return new_pos

        elif direction in [Direction.UP, Direction.DOWN]:
            for elem in boxes:
                if (elem.x, elem.y) == (pos.x + direction.value[0], pos.y + direction.value[1]):
                    value_ = elem.value
                    break

            new_pos_c = Position2(
                x=pos.x + direction.value[0], y=pos.y + direction.value[1], value=value_
            )

            if new_pos_c.value == "[":
                new_pos_l = new_pos_c
                new_pos_r = Position2(x=new_pos_c.x, y=new_pos_c.y + 1, value="]")
            elif new_pos_c.value == "]":
                new_pos_l = Position2(x=new_pos_c.x, y=new_pos_c.y - 1, value="[")
                new_pos_r = new_pos_c

            new_box_pos_l = move_2(new_pos_l, direction, walls, boxes)
            new_box_pos_r = move_2(new_pos_r, direction, walls, boxes)

            if (new_box_pos_l.x, new_box_pos_l.y) == new_pos_coords or (
                new_box_pos_r.x,
                new_box_pos_r.y,
            ) == new_pos_coords:
                return pos

            if any((box.x, box.y) == (new_pos_l.x, new_pos_l.y) for box in boxes):
                for elem in boxes:
                    if (elem.x, elem.y) == (new_pos_l.x, new_pos_l.y):
                        boxes.remove(elem)
                        break
            if any((box.x, box.y) == (new_pos_r.x, new_pos_r.y) for box in boxes):
                for elem in boxes:
                    if (elem.x, elem.y) == (new_pos_r.x, new_pos_r.y):
                        boxes.remove(elem)
                        break

            boxes.append(new_box_pos_l)
            boxes.append(new_box_pos_r)
            return new_pos


def part_2(data):
    walls, boxes, start, mov_directions = preprocessing_2(data)

    for direction in mov_directions:
        can_move = []
        _, can_move = check_if_can_move_2(start, direction, walls, boxes, can_move)

        if all(m == True for m in can_move):
            start = move_2(start, direction, walls, boxes)

    return sum(100 * box.x + box.y for box in boxes if box.value == "[")
