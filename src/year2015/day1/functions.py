def count_floors(data):
    up = data.count("(")
    down = data.count(")")
    return up - down


def up_down(elem, floor=0):
    if elem == "(":
        floor += 1
    elif elem == ")":
        floor -= 1
    return floor


def first_basement(data, floor=0, count=0):
    for elem in data:
        count += 1
        floor = up_down(elem, floor)
        if floor == -1:
            return count
