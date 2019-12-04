def check_double(data):
    for i in range(5):
        if data[i] == data[i+1]:
            return True
    return False


def check_no_decrease(data):
    for i in range(5):
        if data[i] > data[i+1]:
            return False 
    return True

def check_no_larger_group(data):
    for i in range(6):
        if i == 0 or i == 1:
            if data[0] == data[1] and data[1] != data[2]:
                return True
        elif i == 4 or i == 5:
            if data[4] == data[5] and data[3] != data[4]:
                return True
        else:
            if data[i] == data[i-1] and data[i] != data[i+1] and data[i-2] != data[i]:
                    return True
            elif data[i] == data[i+1] and data[i] != data[i-1] and data[i+2] != data[i]:
                    return True
    return False
