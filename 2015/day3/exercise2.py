from common import read_input, move

data = read_input("input.txt")

locations = {(0, 0)}
house_santa = [0, 0]
house_robo = [0, 0]

i = 0
for elem in data:
    if i % 2 == 0:
        move(elem, house_santa)
        locations.add(tuple(house_santa))
        i += 1
    else:
        move(elem, house_robo)
        locations.add(tuple(house_robo))
        i += 1

print(len(locations))
