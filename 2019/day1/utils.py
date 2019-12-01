import math

def read_input(filename):
    with open(filename, "r") as f:
        return [ int(elem) for elem in f.read().split("\n") ]

def fuel_computation(data):
    return math.floor(data / 3) - 2

def fuel_recursive(data):
    fuel = fuel_computation(data)
    if fuel <= 0:
        return 0 
    else:
        return fuel + fuel_recursive(fuel)
