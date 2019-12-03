import pandas

def load_input(filename):
    df = pandas.read_csv(filename, header=None)
    return df[0].values.tolist()

def fuel_computation(data):
    return (data // 3) - 2

def fuel_recursive(data):
    fuel = fuel_computation(data)
    if fuel <= 0:
        return 0 
    else:
        return fuel + fuel_recursive(fuel)
