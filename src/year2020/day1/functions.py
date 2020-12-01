def multiply_elements_set(set_):
    total = 1

    for elem in set_:
        total *= elem

    return total

def difference_with_two(data, number):
    return [number-int(x) for x in data]

def difference_with_three(data, number):
    return [number-int(elem1)-int(elem2) for elem1 in data for elem2 in data]

def return_set_elements(data, list_candidates):
    return {elem for elem in list_candidates if str(elem) in data}

def find_set_of_n_candidates(data, n, number):
    if n == 2:
        list_candidates = difference_with_two(data, number)
    elif n == 3:
        list_candidates = difference_with_three(data, number)
    return return_set_elements(data, list_candidates)