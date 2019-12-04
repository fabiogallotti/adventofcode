INPUT = range(136818,685980,1)

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
        if i == 0:
            if data[i] == data[i+1] and data[i+1] != data[i+2]:
                return True
        elif i == 1:
            if data[i] == data[i-1] and data[i+1] != data[i]:
                return True
        elif i == 4:
            if data[i] == data[i+1] and data[i-1] != data[i]:
                return True
        elif i == 5:
            if data[i-1] == data[i] and data[i] != data[i-2]:
                return True
        else:
            if data[i] == data[i-1] and data[i] != data[i+1] and data[i-2] != data[i]:
                    return True
            elif data[i] == data[i+1] and data[i] != data[i-1] and data[i+2] != data[i]:
                    return True
    return False

result = [elem for elem in INPUT if check_no_decrease(str(elem)) and check_double(str(elem))]

result2 = [elem for elem in result if check_no_larger_group(str(elem))]

print(len(result2))