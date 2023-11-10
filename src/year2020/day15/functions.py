def game(data, times):
    num_pos = {num: pos for pos, num in enumerate(data)}
    number_to_check = data[-1]

    for i in range(len(data), times):
        newitem = (i - 1) - num_pos[number_to_check] if number_to_check in num_pos else 0
        num_pos[number_to_check] = i - 1
        number_to_check = newitem

    return number_to_check
