def get_symbol_adjacent(data):
    symbol_adjacent = []
    for i, row in enumerate(data):
        max_i = len(data) - 1
        for j, value in enumerate(row):
            max_j = len(row) - 1

            if i == 0:
                if j == 0:
                    if value.isnumeric() and (
                        (data[i][j + 1] != "." and not data[i][j + 1].isnumeric())
                        or (  # destra
                            data[i + 1][j + 1] != "." and not data[i + 1][j + 1].isnumeric()
                        )
                        or (  # sotto destra
                            data[i + 1][j] != "." and not data[i + 1][j].isnumeric()
                        )  # sotto
                    ):
                        symbol_adjacent.append((i, j))
                elif 0 < j < max_j:
                    if value.isnumeric() and (
                        (data[i][j + 1] != "." and not data[i][j + 1].isnumeric())
                        or (  # destra
                            data[i + 1][j + 1] != "." and not data[i + 1][j + 1].isnumeric()
                        )
                        or (  # sotto destra
                            data[i + 1][j] != "." and not data[i + 1][j].isnumeric()
                        )
                        or (  # sotto
                            data[i + 1][j - 1] != "." and not data[i + 1][j - 1].isnumeric()
                        )
                        or (  # sotto sinistra
                            data[i][j - 1] != "." and not data[i][j - 1].isnumeric()
                        )  # sinistra
                    ):
                        symbol_adjacent.append((i, j))
                elif j == max_j:
                    if value.isnumeric() and (
                        (data[i + 1][j] != "." and not data[i + 1][j].isnumeric())
                        or (  # sotto
                            data[i + 1][j - 1] != "." and not data[i + 1][j - 1].isnumeric()
                        )
                        or (  # sotto sinistra
                            data[i][j - 1] != "." and not data[i][j - 1].isnumeric()
                        )  # sinistra
                    ):
                        symbol_adjacent.append((i, j))

            elif 0 < i < max_i:
                if j == 0:
                    if value.isnumeric() and (
                        (data[i - 1][j] != "." and not data[i - 1][j].isnumeric())
                        or (  # sopra
                            data[i - 1][j + 1] != "." and not data[i - 1][j + 1].isnumeric()
                        )
                        or (  # sopra destra
                            data[i][j + 1] != "." and not data[i][j + 1].isnumeric()
                        )
                        or (  # destra
                            data[i + 1][j + 1] != "." and not data[i + 1][j + 1].isnumeric()
                        )
                        or (  # sotto destra
                            data[i + 1][j] != "." and not data[i + 1][j].isnumeric()
                        )  # sotto
                    ):
                        symbol_adjacent.append((i, j))
                elif 0 < j < max_j:
                    if value.isnumeric() and (
                        (data[i - 1][j - 1] != "." and not data[i - 1][j - 1].isnumeric())
                        or (  # sopra sinistra
                            data[i - 1][j] != "." and not data[i - 1][j].isnumeric()
                        )
                        or (  # sopra
                            data[i - 1][j + 1] != "." and not data[i - 1][j + 1].isnumeric()
                        )
                        or (  # sopra destra
                            data[i][j + 1] != "." and not data[i][j + 1].isnumeric()
                        )
                        or (  # destra
                            data[i + 1][j + 1] != "." and not data[i + 1][j + 1].isnumeric()
                        )
                        or (  # sotto destra
                            data[i + 1][j] != "." and not data[i + 1][j].isnumeric()
                        )
                        or (  # sotto
                            data[i + 1][j - 1] != "." and not data[i + 1][j - 1].isnumeric()
                        )
                        or (  # sotto sinistra
                            data[i][j - 1] != "." and not data[i][j - 1].isnumeric()
                        )  # sinistra
                    ):
                        symbol_adjacent.append((i, j))
                elif j == max_j:
                    if value.isnumeric() and (
                        (data[i - 1][j - 1] != "." and not data[i - 1][j - 1].isnumeric())
                        or (  # sopra sinistra
                            data[i - 1][j] != "." and not data[i - 1][j].isnumeric()
                        )
                        or (data[i + 1][j] != "." and not data[i + 1][j].isnumeric())  # sopra
                        or (  # sotto
                            data[i + 1][j - 1] != "." and not data[i + 1][j - 1].isnumeric()
                        )
                        or (  # sotto sinistra
                            data[i][j - 1] != "." and not data[i][j - 1].isnumeric()
                        )  # sinistra
                    ):
                        symbol_adjacent.append((i, j))

            elif i == max_i:
                if j == 0:
                    if value.isnumeric() and (
                        (data[i - 1][j] != "." and not data[i - 1][j].isnumeric())
                        or (  # sopra
                            data[i - 1][j + 1] != "." and not data[i - 1][j + 1].isnumeric()
                        )
                        or (  # sopra destra
                            data[i][j + 1] != "." and not data[i][j + 1].isnumeric()
                        )  # destra
                    ):
                        symbol_adjacent.append((i, j))
                elif 0 < j < max_j:
                    if value.isnumeric() and (
                        (data[i - 1][j - 1] != "." and not data[i - 1][j - 1].isnumeric())
                        or (  # sopra sinistra
                            data[i - 1][j] != "." and not data[i - 1][j].isnumeric()
                        )
                        or (  # sopra
                            data[i - 1][j + 1] != "." and not data[i - 1][j + 1].isnumeric()
                        )
                        or (  # sopra destra
                            data[i][j + 1] != "." and not data[i][j + 1].isnumeric()
                        )
                        or (  # destra
                            data[i][j - 1] != "." and not data[i][j - 1].isnumeric()
                        )  # sinistra
                    ):
                        symbol_adjacent.append((i, j))
                elif j == max_j:
                    if value.isnumeric() and (
                        (data[i - 1][j - 1] != "." and not data[i - 1][j - 1].isnumeric())
                        or (  # sopra sinistra
                            data[i - 1][j] != "." and not data[i - 1][j].isnumeric()
                        )
                        or (  # sopra
                            data[i][j - 1] != "." and not data[i][j - 1].isnumeric()
                        )  # sinistra
                    ):
                        symbol_adjacent.append((i, j))

    for x, y in symbol_adjacent:
        if ((x, y + 1) in symbol_adjacent) and ((x, y + 2) in symbol_adjacent):
            symbol_adjacent.remove((x, y + 1))
            symbol_adjacent.remove((x, y + 2))
        elif (x, y + 1) in symbol_adjacent:
            symbol_adjacent.remove((x, y + 1))

    return symbol_adjacent


def part_1(data):
    data = [list(row) for row in data]

    symbol_adjacent = get_symbol_adjacent(data)

    sum_numbers = 0
    for x, y in symbol_adjacent:
        left = check_left(data, x, y)
        right = check_right(data, x, y)

        number = []

        if left and right:
            number = left[::-1]
            number.append(data[x][y])
            number.extend(right)

        elif left:
            number = left[::-1]
            number.append(data[x][y])

        elif right:
            number.insert(0, data[x][y])
            number.extend(right)

        else:
            number.append(data[x][y])

        sum_numbers += int("".join(number))

    return sum_numbers


def check_left(data, x, y, left=None):
    try:
        if left is None:
            left = []
        if data[x][y - 1].isnumeric():
            left.append(data[x][y - 1])
            return check_left(data, x, y - 1, left)
        else:
            return left
    except IndexError:
        return left


def check_right(data, x, y, right=None):
    try:
        if right is None:
            right = []
        if data[x][y + 1].isnumeric():
            right.append(data[x][y + 1])
            return check_right(data, x, y + 1, right)
        else:
            return right
    except IndexError:
        return right


def part_2(data):
    data = [list(row) for row in data]

    symbol_adjacent = get_symbol_adjacent(data)
    number_adjacent = get_gear_adjacent(data, symbol_adjacent)

    sum_numbers = 0
    for list_adjacent in number_adjacent.values():
        if len(list_adjacent) == 2:
            prod_numbers = 1
            for x, y in list_adjacent:
                left = check_left(data, x, y)
                right = check_right(data, x, y)

                number = []

                if left and right:
                    number = left[::-1]
                    number.append(data[x][y])
                    number.extend(right)

                elif left:
                    number = left[::-1]
                    number.append(data[x][y])

                elif right:
                    number.insert(0, data[x][y])
                    number.extend(right)

                else:
                    number.append(data[x][y])

                prod_numbers *= int("".join(number))

            sum_numbers += prod_numbers

    return sum_numbers


def get_gear_adjacent(data, symbol_adjacent):
    GEAR_SYMBOL = "*"
    number_adjacent = {}
    for i, row in enumerate(data):
        max_i = len(data) - 1
        for j, value in enumerate(row):
            max_j = len(row) - 1

            if i == 0:
                if j == 0:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if data[i][j + 1].isnumeric() and (i, j + 1) in symbol_adjacent:  # destra
                            number_adjacent[(i, j)].append((i, j + 1))
                        if (
                            data[i + 1][j + 1].isnumeric() and (i + 1, j + 1) in symbol_adjacent
                        ):  # sotto destra
                            number_adjacent[(i, j)].append((i + 1, j + 1))
                        if data[i + 1][j].isnumeric() and (i + 1, j) in symbol_adjacent:  # sotto
                            number_adjacent[(i, j)].append((i + 1, j))

                elif 0 < j < max_j:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if data[i][j + 1].isnumeric() and (i, j + 1) in symbol_adjacent:  # destra
                            number_adjacent[(i, j)].append((i, j + 1))
                        if (
                            data[i + 1][j + 1].isnumeric() and (i + 1, j + 1) in symbol_adjacent
                        ):  # sotto destra
                            number_adjacent[(i, j)].append((i + 1, j + 1))
                        if data[i + 1][j].isnumeric() and (i + 1, j) in symbol_adjacent:  # sotto
                            number_adjacent[(i, j)].append((i + 1, j))
                        if (
                            data[i + 1][j - 1].isnumeric() and (i + 1, j - 1) in symbol_adjacent
                        ):  # sotto sinistra
                            number_adjacent[(i, j)].append((i + 1, j - 1))
                        if data[i][j - 1].isnumeric() and (i, j - 1) in symbol_adjacent:  # sinistra
                            number_adjacent[(i, j)].append((i, j - 1))

                elif j == max_j:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if data[i + 1][j].isnumeric() and (i + 1, j) in symbol_adjacent:  # sotto
                            number_adjacent[(i, j)].append((i + 1, j))
                        if (
                            data[i + 1][j - 1].isnumeric() and (i + 1, j - 1) in symbol_adjacent
                        ):  # sotto sinistra
                            number_adjacent[(i, j)].append((i + 1, j - 1))
                        if data[i][j - 1].isnumeric() and (i, j - 1) in symbol_adjacent:  # sinistra
                            number_adjacent[(i, j)].append((i, j - 1))

            elif 0 < i < max_i:
                if j == 0:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if data[i - 1][j].isnumeric() and (i - 1, j) in symbol_adjacent:  # sopra
                            number_adjacent[(i, j)].append((i - 1, j))
                        if (
                            data[i - 1][j + 1].isnumeric() and (i - 1, j + 1) in symbol_adjacent
                        ):  # sopra destra
                            number_adjacent[(i, j)].append((i - 1, j + 1))
                        if data[i][j + 1].isnumeric() and (i, j + 1) in symbol_adjacent:  # destra
                            number_adjacent[(i, j)].append((i, j + 1))
                        if (
                            data[i + 1][j + 1].isnumeric() and (i + 1, j + 1) in symbol_adjacent
                        ):  # sotto destra
                            number_adjacent[(i, j)].append((i + 1, j + 1))
                        if data[i + 1][j].isnumeric() and (i + 1, j) in symbol_adjacent:  # sotto
                            number_adjacent[(i, j)].append((i + 1, j))

                elif 0 < j < max_j:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if (
                            data[i - 1][j - 1].isnumeric() and (i - 1, j - 1) in symbol_adjacent
                        ):  # sopra sinistra
                            number_adjacent[(i, j)].append((i - 1, j - 1))
                        if data[i - 1][j].isnumeric() and (i - 1, j) in symbol_adjacent:  # sopra
                            number_adjacent[(i, j)].append((i - 1, j))
                        if (
                            data[i - 1][j + 1].isnumeric() and (i - 1, j + 1) in symbol_adjacent
                        ):  # sopra destra
                            number_adjacent[(i, j)].append((i - 1, j + 1))
                        if data[i][j + 1].isnumeric() and (i, j + 1) in symbol_adjacent:  # destra
                            number_adjacent[(i, j)].append((i, j + 1))
                        if (
                            data[i + 1][j + 1].isnumeric() and (i + 1, j + 1) in symbol_adjacent
                        ):  # sotto destra
                            number_adjacent[(i, j)].append((i + 1, j + 1))
                        if data[i + 1][j].isnumeric() and (i + 1, j) in symbol_adjacent:  # sotto
                            number_adjacent[(i, j)].append((i + 1, j))
                        if (
                            data[i + 1][j - 1].isnumeric() and (i + 1, j - 1) in symbol_adjacent
                        ):  # sotto sinistra
                            number_adjacent[(i, j)].append((i + 1, j - 1))
                        if data[i][j - 1].isnumeric() and (i, j - 1) in symbol_adjacent:  # sinistra
                            number_adjacent[(i, j)].append((i, j - 1))

                elif j == max_j:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if (
                            data[i - 1][j - 1].isnumeric() and (i - 1, j - 1) in symbol_adjacent
                        ):  # sopra sinistra
                            number_adjacent[(i, j)].append((i - 1, j - 1))
                        if data[i - 1][j].isnumeric() and (i - 1, j) in symbol_adjacent:  # sopra
                            number_adjacent[(i, j)].append((i - 1, j))
                        if data[i + 1][j].isnumeric() and (i + 1, j) in symbol_adjacent:  # sotto
                            number_adjacent[(i, j)].append((i + 1, j))
                        if (
                            data[i + 1][j - 1].isnumeric() and (i + 1, j - 1) in symbol_adjacent
                        ):  # sotto sinistra
                            number_adjacent[(i, j)].append((i + 1, j - 1))
                        if data[i][j - 1].isnumeric() and (i, j - 1) in symbol_adjacent:  # sinistra
                            number_adjacent[(i, j)].append((i, j - 1))

            elif i == max_i:
                if j == 0:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if data[i - 1][j].isnumeric() and (i - 1, j) in symbol_adjacent:  # sopra
                            number_adjacent[(i, j)].append((i - 1, j))
                        if (
                            data[i - 1][j + 1].isnumeric() and (i - 1, j + 1) in symbol_adjacent
                        ):  # sopra destra
                            number_adjacent[(i, j)].append((i - 1, j + 1))
                        if data[i][j + 1].isnumeric() and (i, j + 1) in symbol_adjacent:  # destra
                            number_adjacent[(i, j)].append((i, j + 1))

                elif 0 < j < max_j:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if (
                            data[i - 1][j - 1].isnumeric() and (i - 1, j - 1) in symbol_adjacent
                        ):  # sopra sinistra
                            number_adjacent[(i, j)].append((i - 1, j - 1))
                        if data[i - 1][j].isnumeric() and (i - 1, j) in symbol_adjacent:  # sopra
                            number_adjacent[(i, j)].append((i - 1, j))
                        if (
                            data[i - 1][j + 1].isnumeric() and (i - 1, j + 1) in symbol_adjacent
                        ):  # sopra destra
                            number_adjacent[(i, j)].append((i - 1, j + 1))
                        if data[i][j + 1].isnumeric() and (i, j + 1) in symbol_adjacent:  # destra
                            number_adjacent[(i, j)].append((i, j + 1))
                        if data[i][j - 1].isnumeric() and (i, j - 1) in symbol_adjacent:  # sinistra
                            number_adjacent[(i, j)].append((i, j - 1))

                elif j == max_j:
                    if value == GEAR_SYMBOL:
                        if (i, j) not in number_adjacent:
                            number_adjacent[(i, j)] = []

                        if (
                            data[i - 1][j - 1].isnumeric() and (i - 1, j - 1) in symbol_adjacent
                        ):  # sopra sinistra
                            number_adjacent[(i, j)].append((i - 1, j - 1))
                        if data[i - 1][j].isnumeric() and (i - 1, j) in symbol_adjacent:  # sopra
                            number_adjacent[(i, j)].append((i - 1, j))
                        if data[i][j - 1].isnumeric() and (i, j - 1) in symbol_adjacent:  # sinistra
                            number_adjacent[(i, j)].append((i, j - 1))

    return number_adjacent
