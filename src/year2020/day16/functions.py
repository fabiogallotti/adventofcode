def preprocessing(data):
    notes = [[]]
    i = 0
    for elem in data:
        if elem != "":
            notes[i].append(elem)
        else:
            i += 1
            notes.append([])

    fields = notes[0]
    myticket = notes[1][1]
    nearby = notes[2][1:]
    nearby = [list(map(int, elem.split(","))) for elem in nearby]

    fields = [elem.split(" ") for elem in fields]

    intervals = [elem[1:] if len(elem) == 4 else elem[2:] for elem in fields]
    fields = [elem[:1] if len(elem) == 4 else [f"{elem[0]}_{elem[1]}"] for elem in fields]

    for i, elem in enumerate(intervals):
        intervals[i].remove("or")

    return fields, intervals, myticket, nearby


def set_of_possible_values(data):
    fields, intervals, myticket, nearby = preprocessing(data)
    intervals = [elem for sublist in intervals for elem in sublist]

    setofvalues = set()
    for elem in intervals:
        lower, upper = elem.split("-")
        for i in range(int(lower), int(upper) + 1):
            setofvalues.add(i)

    return fields, intervals, myticket, nearby, setofvalues


def find_invalid_values(data):
    _fields, _intervals, _myticket, nearby, setofvalues = set_of_possible_values(data)

    return [value for ticket in nearby for value in ticket if value not in setofvalues]


def valid_tickets(nearby, invalid):
    for elem in invalid:
        for ticket in nearby:
            if elem in ticket:
                nearby.pop(nearby.index(ticket))
    return nearby


def part_1(data):
    return sum(find_invalid_values(data))


def part_2(data):
    pass
