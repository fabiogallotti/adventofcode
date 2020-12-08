from utils import read_input, calculate

data = read_input("input.txt")

def orbits(data):
    count = 0
    for key in data.keys():
        count = calculate(data, key, count)   
    return count

print(orbits(data))