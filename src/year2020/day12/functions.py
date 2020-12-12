try:
    from functions.functions import manhattan
except ModuleNotFoundError:
    from src.functions.functions import manhattan

DIRECTIONS = ["east", "sud", "ovest", "nord"]


def rotate(elem, direction):
    if elem[1:] == "90":
        return (
            DIRECTIONS[DIRECTIONS.index(direction) - 1]
            if elem[0] == "L"
            else DIRECTIONS[DIRECTIONS.index(direction) - 3]
        )
    elif elem[1:] == "180":
        return DIRECTIONS[DIRECTIONS.index(direction) - 2]
    elif elem[1:] == "270":
        return (
            DIRECTIONS[DIRECTIONS.index(direction) - 3]
            if elem[0] == "L"
            else DIRECTIONS[DIRECTIONS.index(direction) - 1]
        )


def move_east(x, elem):
    x += int(elem[1:])
    return x


def move_sud(y, elem):
    y -= int(elem[1:])
    return y


def move_west(x, elem):
    x -= int(elem[1:])
    return x


def move_north(y, elem):
    y += int(elem[1:])
    return y


def move(data):
    x, y = 0, 0
    direction = "east"
    for elem in data:
        if elem[0] == "N":
            y = move_north(y, elem)
        elif elem[0] == "S":
            y = move_sud(y, elem)
        elif elem[0] == "E":
            x = move_east(x, elem)
        elif elem[0] == "W":
            x = move_west(x, elem)
        elif elem[0] == "F":
            if direction == "east":
                x = move_east(x, elem)
            elif direction == "sud":
                y = move_sud(y, elem)
            elif direction == "ovest":
                x = move_west(x, elem)
            elif direction == "nord":
                y = move_north(y, elem)
        else:
            direction = rotate(elem, direction)
    return [(x, y)]


def move_forward_waypoint(xw, yw, x, y, elem):
    diffx = xw - x
    diffy = yw - y
    x += diffx * int(elem[1:])
    y += diffy * int(elem[1:])
    xw = x + diffx
    yw = y + diffy
    return xw, yw, x, y


def rotate_waypoint(xw, yw, x, y, elem):
    if elem in ("L90", "R270"):
        diffx = xw - x
        diffy = yw - y
        xw = x - diffy
        yw = y + diffx

    elif elem in ("L180", "R180"):
        diffx = xw - x
        diffy = yw - y
        xw = x - diffx
        yw = y - diffy

    elif elem in ("L270", "R90"):
        diffx = xw - x
        diffy = yw - y
        xw = x + diffy
        yw = y - diffx

    return xw, yw


def move_waypoint(data):
    xw, yw = 10, 1
    x, y = 0, 0
    direction = "east"
    for elem in data:
        if elem[0] == "N":
            yw = move_north(yw, elem)
        elif elem[0] == "S":
            yw = move_sud(yw, elem)
        elif elem[0] == "E":
            xw = move_east(xw, elem)
        elif elem[0] == "W":
            xw = move_west(xw, elem)
        elif elem[0] == "F":
            xw, yw, x, y = move_forward_waypoint(xw, yw, x, y, elem)
        else:
            xw, yw = rotate_waypoint(xw, yw, x, y, elem)
    return [(x, y)]


def solve_problem(problem, data):
    if problem == 1:
        points = move(data)
        return manhattan(points)[0]
    elif problem == 2:
        points_waypoint = move_waypoint(data)
        return manhattan(points_waypoint)[0]
