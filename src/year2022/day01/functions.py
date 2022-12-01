def part_1(data):
    max_calories = 0

    elf_calories = 0
    for i, elem in enumerate(data):
        if elem == "":
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
        elif i == len(data) - 1:
            elf_calories += int(elem)
            if elf_calories > max_calories:
                max_calories = elf_calories
        else:
            elf_calories += int(elem)

    return max_calories


def part_2(data):
    calories = []
    elf_calories = 0
    for i, elem in enumerate(data):
        if elem == "":
            calories.append(elf_calories)
            elf_calories = 0
        elif i == len(data) - 1:
            elf_calories += int(elem)
            calories.append(elf_calories)
        else:
            elf_calories += int(elem)

    sort_calories = sorted(calories, reverse=True)

    return sort_calories[0] + sort_calories[1] + sort_calories[2]
