def part_1(data):
    instructions = data[0]
    up = instructions.count("(")
    down = instructions.count(")")
    return up - down


def part_2(data):
    instructions = data[0]
    floor = 0
    for index, char in enumerate(instructions):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return index + 1
