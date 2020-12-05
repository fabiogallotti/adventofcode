def search_seat_id(elem):
    rows = range(128)
    columns = range(8)

    for char in elem[:7]:
        rows = binary_search(char, "F", "B", rows)
    for char in elem[7:]:
        columns = binary_search(char, "L", "R", columns)

    return rows[0] * 8 + columns[0]


def binary_search(char, left, right, data):
    if char == left:
        data = data[: len(data) // 2]
    elif char == right:
        data = data[len(data) // 2 :]
    return data


def find_seat_ids(data):
    return [search_seat_id(elem) for elem in data]


def find_missing_seat_id(seat_ids):
    seat_ids.sort()

    for i, elem in enumerate(seat_ids):
        if seat_ids[i + 1] - elem != 1:
            return elem + 1
