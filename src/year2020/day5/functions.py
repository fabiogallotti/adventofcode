def find_seat_ids(data):
    seat_ids = []

    for elem in data:
        rows = range(128)
        columns = range(8)

        for char in elem[:7]:
            if char == "F":
                rows = rows[: len(rows) // 2]
            elif char == "B":
                rows = rows[len(rows) // 2 :]

        for char in elem[7:]:
            if char == "L":
                columns = columns[: len(columns) // 2]
            elif char == "R":
                columns = columns[len(columns) // 2 :]

        seat_ids.append(rows[0] * 8 + columns[0])
    return seat_ids


def find_missing_seat_id(seat_ids):
    seat_ids.sort()

    for i, elem in enumerate(seat_ids):
        if seat_ids[i + 1] - elem != 1:
            return elem + 1
