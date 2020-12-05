def preprocessing(elem):
    minimum, maximum = elem[0].split("-")
    minimum = int(minimum)
    maximum = int(maximum)
    letter = elem[1][0]
    password = elem[2]

    return minimum, maximum, letter, password


def occurences_between_min_max(minimum, maximum, letter, password, counter):
    occurrences = password.count(letter)
    if minimum <= occurrences and occurrences <= maximum:
        counter += 1
    return counter


def check_positions(minimum, maximum, letter, password, counter):
    if password[minimum - 1] == letter and password[maximum - 1] != letter:
        counter += 1
    elif password[minimum - 1] != letter and password[maximum - 1] == letter:
        counter += 1
    return counter


def solve_problem(data, problem):
    counter = 0
    for elem in data:
        minimum, maximum, letter, password = preprocessing(elem)

        if problem == 1:
            counter = occurences_between_min_max(
                minimum, maximum, letter, password, counter
            )
        elif problem == 2:
            counter = check_positions(minimum, maximum, letter, password, counter)

    return counter
