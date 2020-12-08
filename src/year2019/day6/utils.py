def read_input(file):
    with open(file, "r") as f:
        data =  [ x.split(")") for x in f.read().split("\n")]
        return {value: key for key, value in data}

def calculate(data, elem, count):
    if data[elem] == "COM":
        count += 1
        return count
    else:
        return 1 + calculate(data, data[elem], count)


def calculate_path(data, elem, end, path):
    path.append(data[elem])
    if data[elem] == end:
        return path
    else:
        return calculate_path(data, data[elem], end, path)

def find_intersection(path1, path2):
    intersection = ""
    for one in path1:
        for two in path2:
            if one == two:
                intersection = two
                break
        if intersection:
            break
    return intersection