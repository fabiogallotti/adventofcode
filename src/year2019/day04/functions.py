def check_double(data):
    return any(data[i] == data[i+1] for i in range(5))

def check_no_decrease(data):
    return all(data[i] <= data[i+1] for i in range(5))

def check_no_larger_group(data):
    for i in range(6):
        if i in [0, 1]:
            if data[0] == data[1] and data[1] != data[2]:
                return True
        elif i in [4, 5]:
            if data[4] == data[5] and data[3] != data[4]:
                return True
        else:
            if data[i] == data[i-1] and data[i] != data[i+1] and data[i-2] != data[i]:
                    return True
            elif data[i] == data[i+1] and data[i] != data[i-1] and data[i+2] != data[i]:
                    return True
    return False
