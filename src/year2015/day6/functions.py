def get_points(elem):
    starting_x, starting_y = elem[0].split(",")
    ending_x, ending_y = elem[2].split(",")
    return int(starting_x), int(starting_y), int(ending_x), int(ending_y)


def loop_on_matrix(elem, matrix, action, amount=0):
    starting_x, starting_y, ending_x, ending_y = get_points(elem)

    for row in range(starting_x, ending_x + 1):
        for column in range(starting_y, ending_y + 1):
            if action == "off":
                matrix[row][column] = 0
            elif action in "on":
                matrix[row][column] = 1
            elif action == "toogle":
                matrix[row][column] = 1 if matrix[row][column] == 0 else 0
            elif action == "brightness":
                matrix[row][column] += amount
                matrix[row][column] = max(matrix[row][column], 0)


def turn_off(elem, matrix):
    loop_on_matrix(elem, matrix, "off")


def turn_on(elem, matrix):
    loop_on_matrix(elem, matrix, "on")


def toogle(elem, matrix):
    loop_on_matrix(elem, matrix, "toogle")


def increase_brightness(elem, matrix, amount):
    loop_on_matrix(elem, matrix, "brightness", amount)


def total_in_matrix(matrix):
    return sum(
        matrix[row][column]
        for row in range(len(matrix[:][0]))
        for column in range(len(matrix[0][:]))
    )


def calculate_lights_on(data, lights):
    for elem in data:
        if elem[0] == "turn" and elem[1] == "on":
            turn_on(elem[2:], lights)
        elif elem[0] == "turn" and elem[1] == "off":
            turn_off(elem[2:], lights)
        else:
            toogle(elem[1:], lights)

    return total_in_matrix(lights)


def calculate_brightness(data, lights):
    for elem in data:
        if elem[0] == "turn" and elem[1] == "on":
            increase_brightness(elem[2:], lights, 1)
        elif elem[0] == "turn" and elem[1] == "off":
            increase_brightness(elem[2:], lights, -1)
        else:
            increase_brightness(elem[1:], lights, 2)

    return total_in_matrix(lights)
