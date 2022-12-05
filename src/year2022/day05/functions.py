import contextlib


def preprocessing(data):
    starting_crates = []
    instructions = []

    for elem in data:
        if "move" in elem:
            instructions.append(elem.split(" "))
        elif elem == "":
            continue
        else:
            starting_crates.append(elem)

    num_crates_list = starting_crates.pop()
    crates = [[] for num in num_crates_list if num != " "]

    for elem in starting_crates:
        for i in range(len(crates)):
            with contextlib.suppress(IndexError):
                if elem[4 * i + 1] != " ":
                    crates[i].append(elem[4 * i + 1])
    return crates, instructions


def part_1(data):
    crates, instructions = preprocessing(data)
    for x in instructions:
        for _ in range(int(x[1])):
            removed = crates[int(x[3]) - 1].pop(0)
            crates[int(x[5]) - 1].insert(0, removed)

    top = [x[0] for x in crates]

    return "".join(top)


def part_2(data):
    crates, instructions = preprocessing(data)
    for x in instructions:
        removed = crates[int(x[3]) - 1][: int(x[1])]
        crates[int(x[3]) - 1] = crates[int(x[3]) - 1][int(x[1]) :]
        crates[int(x[5]) - 1] = removed + crates[int(x[5]) - 1]

    top = [x[0] for x in crates]

    return "".join(top)
