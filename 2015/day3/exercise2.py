from common import read_input, move

data = read_input("input.txt")

locations = {(0, 0)}
house_santa = [0, 0]
house_robo = [0, 0]

for i, elem in enumerate(data):
    if i % 2 == 0:
        move(elem, house_santa)
        locations.add(tuple(house_santa))
    else:
        move(elem, house_robo)
        locations.add(tuple(house_robo))
print(len(locations))
