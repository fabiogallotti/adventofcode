def get_points(elem):
    starting_x, starting_y = elem[0].split(",")
    ending_x, ending_y = elem[2].split(",")
    return starting_x, starting_y, ending_x, ending_y


def turn_lights(elem, matrix, action):
    starting_x, starting_y, ending_x, ending_y = get_points(elem)

    for row in range(int(starting_x), int(ending_x) + 1):
        for column in range(int(starting_y), int(ending_y) + 1):
            matrix[row][column] = action


def toogle_lights(elem, matrix):
    starting_x, starting_y, ending_x, ending_y = get_points(elem)

    for row in range(int(starting_x), int(ending_x) + 1):
        for column in range(int(starting_y), int(ending_y) + 1):
            matrix[row][column] = 1 if matrix[row][column] == 0 else 0
