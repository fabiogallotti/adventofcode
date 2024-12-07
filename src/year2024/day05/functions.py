def preprocessing_rules_pages(data):
    rules = {}
    pages = []
    for elem in data:
        if "|" in elem:
            before, after = elem.split("|")
            before = int(before)
            after = int(after)

            if before in rules:
                rules[before].append(after)
            else:
                rules[before] = [after]

        elif "," in elem:
            pages.append([int(x) for x in elem.split(",")])

    return rules, pages


def part_1(data):
    rules, pages = preprocessing_rules_pages(data)

    correct_pages = []

    for page in pages:
        correct = True
        for i in range(len(page)):
            elem = page[i]
            if elem in rules and correct == True:
                previous = page[:i]
                if any(p in previous for p in rules[elem]):
                    correct = False
        if correct == True:
            correct_pages.append(page)

    return sum(page[len(page) // 2] for page in correct_pages)


def part_2(data):
    rules, pages = preprocessing_rules_pages(data)
    incorrect_pages = []

    for page in pages:
        incorrect = False
        for i in range(len(page)):
            elem = page[i]
            if elem in rules and incorrect == False:
                previous = page[:i]
                if any(p in previous for p in rules[elem]):
                    incorrect = True
        if incorrect == True:
            incorrect_pages.append(page)

    for page in incorrect_pages:
        i = 1
        while i < len(page):
            elem = page[i]
            prev_elem = page[i - 1]

            if elem in rules and prev_elem in rules[elem]:
                tmp = page[i - 1]
                page[i - 1] = page[i]
                page[i] = tmp
                i = 0
            i += 1

    return sum(page[len(page) // 2] for page in incorrect_pages)
