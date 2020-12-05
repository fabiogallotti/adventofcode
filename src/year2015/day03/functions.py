def move(elem, house):
    if elem == ">":
        house[0] += 1
    elif elem == "<":
        house[0] += -1
    elif elem == "^":
        house[1] += 1
    elif elem == "v":
        house[1] += -1


def move_and_add(elem, house, locations):
    move(elem, house)
    locations.add(tuple(house))


def santa_delivers(data):
    locations = {(0, 0)}
    house = [0, 0]

    for elem in data:
        move_and_add(elem, house, locations)

    return len(locations)


def santa_and_robo_delivers(data):
    locations = {(0, 0)}
    house_santa = [0, 0]
    house_robo = [0, 0]

    for i, elem in enumerate(data):
        if i % 2 == 0:
            move_and_add(elem, house_santa, locations)
        else:
            move_and_add(elem, house_robo, locations)
    return len(locations)
