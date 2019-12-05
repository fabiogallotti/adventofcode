def read_input(filename):
    with open(filename, "r") as f:
        return [ x.split("x") for x in f.read().split("\n") ]

def calculate_area(box):
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])

    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def calculate_ribbon(box):
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    min_face = min(2*l+2*w, 2*l+2*h, 2*w+2*h)
    volume = l*w*h
    return min_face + volume

data = read_input("input.txt")

result1 = [calculate_area(elem) for elem in data]
print(sum(result1))

result2 = [calculate_ribbon(elem) for elem in data]
print(sum(result2))


def test_calculate_area():
    assert calculate_area([2,3,4]) == 58
    assert calculate_area([1,1,10]) == 43

def test_calculate_ribbon():
    assert calculate_ribbon([2,3,4]) == 34
    assert calculate_ribbon([1,1,10]) == 14
