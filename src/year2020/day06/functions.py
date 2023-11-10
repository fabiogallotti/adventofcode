def preprocessing(data):
    forms = [[]]
    i = 0
    for elem in data:
        if elem != "":
            forms[i].extend(elem)
        else:
            i += 1
            forms.append([])

    dict_forms = []
    for form in forms:
        dict_ = {}
        for elem in form:
            if elem in dict_:
                dict_[elem] += 1
            else:
                dict_[elem] = 1
        dict_forms.append(dict_)

    return dict_forms


def how_many_in_group(forms, data):
    how_many = [0] * len(forms)
    i = 0
    for elem in data:
        if elem != "":
            how_many[i] += 1
        else:
            i += 1
    return how_many


def solve_problem(problem, forms, how_many=None):
    if problem == 1:
        return sum(len(elem) for elem in forms)
    elif problem == 2:
        return sum(
            1 for i, elem in enumerate(forms) for value in elem.values() if value == how_many[i]
        )
