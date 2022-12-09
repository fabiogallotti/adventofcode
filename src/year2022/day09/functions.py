from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and getattr(other, "x", None) == self.x
            and getattr(other, "y", None) == self.y
        )

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


def move_tail(tail, head):
    new_tail = Point(x=tail.x, y=tail.y)
    if head.x - tail.x > 1 and head.y - tail.y == 0:
        new_tail.x += 1
    elif tail.x - head.x > 1 and head.y - tail.y == 0:
        new_tail.x -= 1
    elif head.y - tail.y > 1 and head.x - tail.x == 0:
        new_tail.y += 1
    elif tail.y - head.y > 1 and head.x - tail.x == 0:
        new_tail.y -= 1

    elif (head.x - tail.x >= 1 and head.y - tail.y > 1) or (
        head.x - tail.x > 1 and head.y - tail.y >= 1
    ):
        new_tail.x += 1
        new_tail.y += 1

    elif (tail.x - head.x >= 1 and head.y - tail.y > 1) or (
        tail.x - head.x > 1 and head.y - tail.y >= 1
    ):
        new_tail.x -= 1
        new_tail.y += 1

    elif (tail.x - head.x >= 1 and tail.y - head.y > 1) or (
        tail.x - head.x > 1 and tail.y - head.y >= 1
    ):
        new_tail.x -= 1
        new_tail.y -= 1

    elif (head.x - tail.x >= 1 and tail.y - head.y > 1) or (
        head.x - tail.x > 1 and tail.y - head.y >= 1
    ):
        new_tail.x += 1
        new_tail.y -= 1

    return new_tail


def part_1(data):
    head = Point(x=0, y=0)
    tail = Point(x=0, y=0)

    visited = set()

    for e in data:
        if e[0] == "R":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.x += 1
                tail = move_tail(tail, head)
                visited.add(tail)

        elif e[0] == "L":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.x -= 1
                tail = move_tail(tail, head)
                visited.add(tail)

        elif e[0] == "U":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.y += 1
                tail = move_tail(tail, head)
                visited.add(tail)

        elif e[0] == "D":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.y -= 1
                tail = move_tail(tail, head)
                visited.add(tail)

    return len(visited)


def part_2(data):
    head = Point(x=0, y=0)
    one = Point(x=0, y=0)
    two = Point(x=0, y=0)
    three = Point(x=0, y=0)
    four = Point(x=0, y=0)
    five = Point(x=0, y=0)
    six = Point(x=0, y=0)
    seven = Point(x=0, y=0)
    eight = Point(x=0, y=0)
    tail = Point(x=0, y=0)

    visited = set()

    for e in data:
        if e[0] == "R":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.x += 1
                one = move_tail(one, head)
                two = move_tail(two, one)
                three = move_tail(three, two)
                four = move_tail(four, three)
                five = move_tail(five, four)
                six = move_tail(six, five)
                seven = move_tail(seven, six)
                eight = move_tail(eight, seven)
                tail = move_tail(tail, eight)
                visited.add(tail)

        elif e[0] == "L":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.x -= 1
                one = move_tail(one, head)
                two = move_tail(two, one)
                three = move_tail(three, two)
                four = move_tail(four, three)
                five = move_tail(five, four)
                six = move_tail(six, five)
                seven = move_tail(seven, six)
                eight = move_tail(eight, seven)
                tail = move_tail(tail, eight)
                visited.add(tail)

        elif e[0] == "U":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.y += 1
                one = move_tail(one, head)
                two = move_tail(two, one)
                three = move_tail(three, two)
                four = move_tail(four, three)
                five = move_tail(five, four)
                six = move_tail(six, five)
                seven = move_tail(seven, six)
                eight = move_tail(eight, seven)
                tail = move_tail(tail, eight)
                visited.add(tail)

        elif e[0] == "D":
            moves = int(e[1])
            for _ in range(1, moves + 1):
                head.y -= 1
                one = move_tail(one, head)
                two = move_tail(two, one)
                three = move_tail(three, two)
                four = move_tail(four, three)
                five = move_tail(five, four)
                six = move_tail(six, five)
                seven = move_tail(seven, six)
                eight = move_tail(eight, seven)
                tail = move_tail(tail, eight)
                visited.add(tail)

    return len(visited)
