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

result = [elem for elem in INPUT if check_no_decrease(str(elem)) and check_double(str(elem))]

print(len(result))