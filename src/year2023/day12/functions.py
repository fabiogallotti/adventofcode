def part_1(data):
    springs = [row.split()[0] for row in data]
    groups = [row.split()[1].split(",") for row in data]
    groups = [[int(n) for n in g] for g in groups]

    return sum(recursion(springs[i], groups[i]) for i in range(len(springs)))


def recursion(spring, group):
    if spring == "":
        return 1 if group == [] else 0

    if group == []:
        return 0 if "#" in spring else 1

    result = 0

    if spring[0] in [".", "?"]:
        result += recursion(spring[1:], group)
    if spring[0] in ["#", "?"]:
        if (
            group[0] <= len(spring)
            and "." not in spring[: group[0]]
            and (group[0] == len(spring) or spring[group[0]] != "#")
        ):
            result += recursion(spring[group[0] + 1 :], group[1:])

    return result


def part_2(data):
    springs = [row.split()[0] for row in data]
    groups = [row.split()[1].split(",") for row in data]
    groups = [[int(n) for n in g] for g in groups]

    for i in range(len(springs)):
        springs[i] = "?".join([springs[i]] * 5)
        groups[i] *= 5

    checked = {}

    return sum(recursion_2(springs[i], groups[i], checked) for i in range(len(springs)))


def recursion_2(spring, group, checked):
    if spring == "":
        return 1 if group == [] else 0

    if group == []:
        return 0 if "#" in spring else 1

    key = (spring, tuple(group))
    if key in checked:
        return checked[key]

    result = 0

    if spring[0] in [".", "?"]:
        result += recursion_2(spring[1:], group, checked)
    if spring[0] in ["#", "?"]:
        if (
            group[0] <= len(spring)
            and "." not in spring[: group[0]]
            and (group[0] == len(spring) or spring[group[0]] != "#")
        ):
            result += recursion_2(spring[group[0] + 1 :], group[1:], checked)

    checked[key] = result
    return result
