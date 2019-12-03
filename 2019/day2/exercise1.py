def read_input(filename):
    with open(filename, "r") as f:
        return [ int(elem) for elem in f.read().split(",") ]

def calculate(data):
    for i in range(len(data) // 4):
        if data[4*i] == 1:
            data[data[4*i+3]] = data[data[4*i+1]] + data[data[4*i+2]] 
        elif data[4*i] == 2:
            data[data[4*i+3]] = data[data[4*i+1]] * data[data[4*i+2]] 
    return data

def initial_state(data):
    data[1] = 12
    data[2] = 2
    return data

input = read_input("input.txt")
input = initial_state(input)
result = calculate(input)

print(result[0])


for a in range(100):
    for b in range(100):
        input = read_input("input.txt")
        input[1] = a
        input[2] = b
        result = calculate(input)
        if result[0] == 19690720:
            print(100* a + b)





def test_calculate():
    assert calculate([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
    assert calculate([1,0,0,0,99]) == [2,0,0,0,99]
    assert calculate([2,3,0,3,99]) == [2,3,0,6,99]
    assert calculate([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert calculate([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]