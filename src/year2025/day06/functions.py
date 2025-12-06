def preprocessing(data):
    list_numbers = []
    operations = [elem for elem in data[-1].split(" ") if elem]

    for elem in data[:-1]:
        numbers = elem.split(" ")
        list_numbers.append([int(num) for num in numbers if num])

    vertical_list = list(zip(*list_numbers))

    return vertical_list, operations


def part_1(data):
    list_numbers, operations = preprocessing(data)
    list_total = []
    for i in range(len(list_numbers)):
        if operations[i] == "+":
            list_total.append(sum(list_numbers[i]))
        elif operations[i] == "*":
            product = 1
            for num in list_numbers[i]:
                product *= num
            list_total.append(product)

    return sum(list_total)


def preprocessing_part2(data):
    list_numbers = []
    operations_with_whitespaces = [elem for elem in data[-1].split(" ")]
    operations = [elem for elem in data[-1].split(" ") if elem]
    i = [i for i, x in enumerate(operations_with_whitespaces) if x]
    lengths = [j - k for k, j in zip(i, [*i[1:], len(operations_with_whitespaces)])]

    for elem in data[:-1]:
        numbers = elem.split(" ")

        for i in range(len(numbers)):
            if numbers[i] == "":
                numbers[i] = "0"

        numbers = [n for num in numbers for n in num]

        for i in range(len(numbers)):
            if numbers[i] == "0":
                numbers[i] = ""

        list_numbers.append(numbers)

        vertical_list = list(zip(*list_numbers))
        vertical_list_of_list = [
            vertical_list[sum(lengths[:i]) : sum(lengths[: i + 1])] for i in range(len(lengths))
        ]

    list_numbers = [
        [int("".join(x for x in elem if x != "")) for elem in list_ if any(x != "" for x in elem)]
        for list_ in vertical_list_of_list
    ]

    return list_numbers, operations


def part_2(data):
    list_numbers, operations = preprocessing_part2(data)

    list_total = []
    for i in range(len(list_numbers)):
        if operations[i] == "+":
            list_total.append(sum(list_numbers[i]))
        elif operations[i] == "*":
            product = 1
            for num in list_numbers[i]:
                product *= num
            list_total.append(product)

    return sum(list_total)
