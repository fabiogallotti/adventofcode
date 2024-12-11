from entities.direction import Direction
from entities.point import Point


def part_1(data):
    house = Point(x=0, y=0)
    locations = {house}

    for elem in data[0]:
        house = move(elem, house)
        locations.add(house)

    return len(locations)


def part_2(data):
    house_santa = Point(x=0, y=0)
    house_robo = Point(x=0, y=0)
    locations = {house_santa}

    for i, elem in enumerate(data[0]):
        if i % 2 != 0:
            house_santa = move(elem, house_santa)
            locations.add(house_santa)
        else:
            house_robo = move(elem, house_robo)
            locations.add(house_robo)

    return len(locations)


def move(elem, house: Point):
    if elem == ">":
        house = house.move(Direction.RIGHT)
    elif elem == "<":
        house = house.move(Direction.LEFT)
    elif elem == "^":
        house = house.move(Direction.UP)
    elif elem == "v":
        house = house.move(Direction.DOWN)
    return house
