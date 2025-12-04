def part_1(data):
    total = 0
    for elem in data:
        max_num = 0
        for i in range(len(elem)):
            for j in range(i + 1, len(elem)):
                num = "".join([elem[i], elem[j]])

                int_num = int(num)

                if int_num > max_num:
                    max_num = int_num
        total += max_num

    return total


def part_2(data):
    total = 0
    for elem in data:
        number = []
        i = 0
        n = len(elem)

        for j in range(12, 0, -1):
            max_num = max(elem[i : n - j + 1])
            number.append(max_num)

            i = elem.index(max_num, i, n - j + 1) + 1

        total += int("".join(number))
    return total
