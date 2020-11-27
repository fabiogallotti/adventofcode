from common import read_input, move

data = read_input("input.txt")

locations = {(0, 0)}

house = [0, 0]

for elem in data:
    move(elem, house)
    locations.add(tuple(house))

print(len(locations))
