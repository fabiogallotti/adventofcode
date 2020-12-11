def no_occupied_seats(data, i, j):
    if (
        data[i - 1][j - 1] != "#"
        and data[i - 1][j] != "#"
        and data[i - 1][j + 1] != "#"
        and data[i][j - 1] != "#"
        and data[i][j + 1] != "#"
        and data[i + 1][j - 1] != "#"
        and data[i + 1][j] != "#"
        and data[i + 1][j + 1] != "#"
    ):
        return "#"
    return "L"


def no_occupied_top_row(data, j):
    if (
        data[0][j - 1] != "#"
        and data[0][j + 1] != "#"
        and data[1][j - 1] != "#"
        and data[1][j] != "#"
        and data[1][j + 1] != "#"
    ):
        return "#"
    return "L"


def no_occupied_top_left(data):
    if data[0][1] != "#" and data[1][0] != "#" and data[1][1] != "#":
        return "#"


def no_occupied_top_right(data, j):
    if data[0][j - 1] != "#" and data[1][j] != "#" and data[1][j - 1] != "#":
        return "#"


def no_occupied_bottom_left(data, i):
    if data[i][1] != "#" and data[i - 1][0] != "#" and data[i - 1][1] != "#":
        return "#"


def no_occupied_bottom_row(data, i, j):
    if (
        data[i][j - 1] != "#"
        and data[i][j + 1] != "#"
        and data[i - 1][j - 1] != "#"
        and data[i - 1][j] != "#"
        and data[i - 1][j + 1] != "#"
    ):
        return "#"
    return "L"


def no_occupied_bottom_right(data, i, j):
    if data[i][j - 1] != "#" and data[i - 1][j] != "#" and data[i - 1][j - 1] != "#":
        return "#"


def no_occupied_left_column(data, i):
    if (
        data[i - 1][0] != "#"
        and data[i + 1][0] != "#"
        and data[i - 1][1] != "#"
        and data[i][1] != "#"
        and data[i + 1][1] != "#"
    ):
        return "#"
    return "L"


def no_occupied_right_column(data, i, j):
    if (
        data[i - 1][j] != "#"
        and data[i + 1][j] != "#"
        and data[i - 1][j - 1] != "#"
        and data[i][j - 1] != "#"
        and data[i + 1][j - 1] != "#"
    ):
        return "#"
    return "L"


def how_many_occupied(data, i, j):
    how_many = 0
    if data[i - 1][j - 1] == "#":
        how_many += 1
    if data[i - 1][j] == "#":
        how_many += 1
    if data[i - 1][j + 1] == "#":
        how_many += 1
    if data[i][j - 1] == "#":
        how_many += 1
    if data[i][j + 1] == "#":
        how_many += 1
    if data[i + 1][j - 1] == "#":
        how_many += 1
    if data[i + 1][j] == "#":
        how_many += 1
    if data[i + 1][j + 1] == "#":
        how_many += 1
    return "L" if how_many > 3 else "#"


def how_many_occupied_top_row(data, j):
    how_many = 0
    if data[0][j - 1] == "#":
        how_many += 1
    if data[0][j + 1] == "#":
        how_many += 1
    if data[1][j - 1] == "#":
        how_many += 1
    if data[1][j] == "#":
        how_many += 1
    if data[1][j + 1] == "#":
        how_many += 1
    return "L" if how_many > 3 else "#"


def how_many_occupied_bottom_row(data, i, j):
    how_many = 0
    if data[i][j - 1] == "#":
        how_many += 1
    if data[i][j + 1] == "#":
        how_many += 1
    if data[i - 1][j - 1] == "#":
        how_many += 1
    if data[i - 1][j] == "#":
        how_many += 1
    if data[i - 1][j + 1] == "#":
        how_many += 1
    return "L" if how_many > 3 else "#"


def how_many_occupied_left_column(data, i):
    how_many = 0
    if data[i - 1][0] == "#":
        how_many += 1
    if data[i + 1][0] == "#":
        how_many += 1
    if data[i - 1][1] == "#":
        how_many += 1
    if data[i][1] == "#":
        how_many += 1
    if data[i + 1][1] == "#":
        how_many += 1
    return "L" if how_many > 3 else "#"


def how_many_occupied_right_column(data, i, j):
    how_many = 0
    if data[i - 1][j] == "#":
        how_many += 1
    if data[i + 1][j] == "#":
        how_many += 1
    if data[i - 1][j - 1] == "#":
        how_many += 1
    if data[i][j - 1] == "#":
        how_many += 1
    if data[i + 1][j - 1] == "#":
        how_many += 1
    return "L" if how_many > 3 else "#"


def check_top_row(data, new_data, i, j, length):
    if j == 0:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_top_left(data)
        elif data[i][j] == "#":
            new_data[i][j] = "#"
    elif j in range(1, length - 1):
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_top_row(data, j)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_top_row(data, j)
    elif j == length - 1:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_top_right(data, j)
        elif data[i][j] == "#":
            new_data[i][j] = "#"


def check_central(data, new_data, i, j, length):
    if j == 0:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_left_column(data, i)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_left_column(data, i)
    elif j in range(1, length - 1):
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_seats(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied(data, i, j)
    elif j == length - 1:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_right_column(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_right_column(data, i, j)


def check_bottom_row(data, new_data, i, j, length):
    if j == 0:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_bottom_left(data, i)
        elif data[i][j] == "#":
            new_data[i][j] = "#"
    elif j in range(1, length - 1):
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_bottom_row(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_bottom_row(data, i, j)
    elif j == length - 1:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_bottom_right(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = "#"


def apply_rules(data):
    new_data = [["."] * len(elem) for elem in data]

    for i in range(len(data)):
        length = len(data[i])
        for j in range(length):
            if i == 0:
                check_top_row(data, new_data, i, j, length)
            elif i in range(1, len(data) - 1):
                check_central(data, new_data, i, j, length)
            elif i == len(data) - 1:
                check_bottom_row(data, new_data, i, j, length)

    return new_data


def part_1(data):
    count = 0
    while True:
        data = apply_rules(data)

        inside_count = sum(elem.count("#") for elem in data)

        if inside_count == count:
            return count
        else:
            count = inside_count


def check_occupied_no(data, i, j):
    if data[i - 1][j - 1] == "#":
        return "L"
    elif data[i - 1][j - 1] == ".":
        z = i - 2
        k = j - 2
        while z > -1 and k > -1:
            if data[z][k] == "#":
                return "L"
            elif data[z][k] == "L":
                return "#"
            z -= 1
            k -= 1
    return "#"


def check_occupied_n(data, i, j):
    if data[i - 1][j] == "#":
        return "L"
    elif data[i - 1][j] == ".":
        for k in range(i - 2, -1, -1):
            if data[k][j] == "#":
                return "L"
            elif data[k][j] == "L":
                return "#"
    return "#"


def check_occupied_ne(data, i, j, length):
    if data[i - 1][j + 1] == "#":
        return "L"
    elif data[i - 1][j + 1] == ".":
        z = i - 2
        k = j + 2
        while z > -1 and k < length:
            if data[z][k] == "#":
                return "L"
            elif data[z][k] == "L":
                return "#"
            z -= 1
            k += 1
    return "#"


def check_occupied_e(data, i, j, length):
    if data[i][j + 1] == "#":
        return "L"
    elif data[i][j + 1] == ".":
        for k in range(j + 2, length):
            if data[i][k] == "#":
                return "L"
            elif data[i][k] == "L":
                return "#"
    return "#"


def check_occupied_se(data, i, j, length):
    if data[i + 1][j + 1] == "#":
        return "L"
    elif data[i + 1][j + 1] == ".":
        z = i + 2
        k = j + 2
        while z < len(data) and k < length:
            if data[z][k] == "#":
                return "L"
            elif data[z][k] == "L":
                return "#"
            z += 1
            k += 1
    return "#"


def check_occupied_s(data, i, j):
    if data[i + 1][j] == "#":
        return "L"
    elif data[i + 1][j] == ".":
        for k in range(i + 2, len(data)):
            if data[k][j] == "#":
                return "L"
            elif data[k][j] == "L":
                return "#"
    return "#"


def check_occupied_so(data, i, j):
    if data[i + 1][j - 1] == "#":
        return "L"
    elif data[i + 1][j - 1] == ".":
        z = i + 2
        k = j - 2
        while z < len(data) and k > -1:
            if data[z][k] == "#":
                return "L"
            elif data[z][k] == "L":
                return "#"
            z += 1
            k -= 1
    return "#"


def check_occupied_o(data, i, j):
    if data[i][j - 1] == "#":
        return "L"
    elif data[i][j - 1] == ".":
        for k in range(j - 2, -1, -1):
            if data[i][k] == "#":
                return "L"
            if data[i][k] == "L":
                return "#"
    return "#"


def no_occupied_seats_part2(data, i, j, length):
    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if no == n == ne == e == se == s == so == o == "#":
        return "#"
    else:
        return "L"


def no_occupied_top_row_part2(data, i, j, length):
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if e == se == s == so == o == "#":
        return "#"
    else:
        return "L"


def no_occupied_top_left_part2(data, i, j, length):
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)

    if e == se == s == "#":
        return "#"


def no_occupied_top_right_part2(data, i, j):
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if s == so == o == "#":
        return "#"


def no_occupied_bottom_left_part2(data, i, j, length):
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)

    if n == ne == e == "#":
        return "#"


def no_occupied_bottom_row_part2(data, i, j, length):
    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    o = check_occupied_o(data, i, j)

    if no == n == ne == e == o == "#":
        return "#"
    else:
        return "L"


def no_occupied_bottom_right_part2(data, i, j):
    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    o = check_occupied_o(data, i, j)

    if no == n == o == "#":
        return "#"


def no_occupied_left_column_part2(data, i, j, length):
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)

    if n == ne == e == se == s == "#":
        return "#"
    else:
        return "L"


def no_occupied_right_column_part2(data, i, j):
    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if no == n == s == so == o == "#":
        return "#"
    else:
        return "L"


def how_many_occupied_part2(data, i, j, length):
    how_many = 0

    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if no == "L":
        how_many += 1
    if n == "L":
        how_many += 1
    if ne == "L":
        how_many += 1
    if e == "L":
        how_many += 1
    if se == "L":
        how_many += 1
    if s == "L":
        how_many += 1
    if so == "L":
        how_many += 1
    if o == "L":
        how_many += 1

    if how_many > 4:
        return "L"
    else:
        return "#"


def how_many_occupied_top_row_part2(data, i, j, length):
    how_many = 0

    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if e == "L":
        how_many += 1
    if se == "L":
        how_many += 1
    if s == "L":
        how_many += 1
    if so == "L":
        how_many += 1
    if o == "L":
        how_many += 1

    if how_many > 4:
        return "L"
    else:
        return "#"


def how_many_occupied_bottom_row_part2(data, i, j, length):
    how_many = 0

    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    o = check_occupied_o(data, i, j)

    if no == "L":
        how_many += 1
    if n == "L":
        how_many += 1
    if ne == "L":
        how_many += 1
    if e == "L":
        how_many += 1
    if o == "L":
        how_many += 1

    if how_many > 4:
        return "L"
    else:
        return "#"


def how_many_occupied_left_column_part2(data, i, j, length):
    how_many = 0

    n = check_occupied_n(data, i, j)
    ne = check_occupied_ne(data, i, j, length)
    e = check_occupied_e(data, i, j, length)
    se = check_occupied_se(data, i, j, length)
    s = check_occupied_s(data, i, j)

    if n == "L":
        how_many += 1
    if ne == "L":
        how_many += 1
    if e == "L":
        how_many += 1
    if se == "L":
        how_many += 1
    if s == "L":
        how_many += 1

    if how_many > 4:
        return "L"
    else:
        return "#"


def how_many_occupied_right_column_part2(data, i, j):
    how_many = 0

    no = check_occupied_no(data, i, j)
    n = check_occupied_n(data, i, j)
    s = check_occupied_s(data, i, j)
    so = check_occupied_so(data, i, j)
    o = check_occupied_o(data, i, j)

    if no == "L":
        how_many += 1
    if n == "L":
        how_many += 1
    if s == "L":
        how_many += 1
    if so == "L":
        how_many += 1
    if o == "L":
        how_many += 1

    if how_many > 4:
        return "L"
    else:
        return "#"


def check_top_row_part2(data, new_data, i, j, length):
    if j == 0:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_top_left_part2(data, i, j, length)
        elif data[i][j] == "#":
            new_data[i][j] = "#"
    elif j in range(1, length - 1):
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_top_row_part2(data, i, j, length)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_top_row_part2(data, i, j, length)
    elif j == length - 1:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_top_right_part2(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = "#"


def check_central_part2(data, new_data, i, j, length):
    if j == 0:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_left_column_part2(data, i, j, length)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_left_column_part2(data, i, j, length)
    elif j in range(1, length - 1):
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_seats_part2(data, i, j, length)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_part2(data, i, j, length)
    elif j == length - 1:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_right_column_part2(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_right_column_part2(data, i, j)


def check_bottom_row_part2(data, new_data, i, j, length):
    if j == 0:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_bottom_left_part2(data, i, j, length)
        elif data[i][j] == "#":
            new_data[i][j] = "#"
    elif j in range(1, length - 1):
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_bottom_row_part2(data, i, j, length)
        elif data[i][j] == "#":
            new_data[i][j] = how_many_occupied_bottom_row_part2(data, i, j, length)
    elif j == length - 1:
        if data[i][j] == "L":
            new_data[i][j] = no_occupied_bottom_right_part2(data, i, j)
        elif data[i][j] == "#":
            new_data[i][j] = "#"


def apply_rules_part2(data):
    new_data = [["."] * len(elem) for elem in data]

    for i in range(len(data)):
        length = len(data[i])
        for j in range(length):
            if i == 0:
                check_top_row_part2(data, new_data, i, j, length)
            elif i in range(1, len(data) - 1):
                check_central_part2(data, new_data, i, j, length)
            elif i == len(data) - 1:
                check_bottom_row_part2(data, new_data, i, j, length)
    return new_data


def part_2(data):
    count = 0
    while True:
        data = apply_rules_part2(data)
        inside_count = sum(elem.count("#") for elem in data)

        if inside_count == count:
            return count
        else:
            count = inside_count