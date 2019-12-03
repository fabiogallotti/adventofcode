def read_input(file):
    with open(file, "r") as f:
        return [x.split(",") for x in f.read().split('\n')]


def move(data):
    points = []
    x = 0
    y = 0
    for elem in data:
        if elem[0] == "R":
            for i in range(1, int(elem[1:])+1):
                x += 1
                points.append((x, y))
        elif elem[0] == "L":
            for i in range(1, int(elem[1:])+1):
                x -= 1
                points.append((x, y))
        elif elem[0] == "U":
            for i in range(1, int(elem[1:])+1):
                y += 1
                points.append((x, y))
        elif elem[0] == "D":
            for i in range(1, int(elem[1:])+1):
                y -= 1
                points.append((x, y))
    return points


def find_intersections(points1, points2):
    return [elem for elem in points1 if elem in points2]


def manhattan(data):
    dist = []
    for (x, y) in data:
        dist.append(abs(x)+abs(y))
    return dist


def count_steps(points1, points2, intersect):
    return [(points1.index(elem)+1, points2.index(elem)+1) for elem in intersect]

data = read_input("input.txt")
points1 = move(data[0])
points2 = move(data[1])

intersect = find_intersections(set(points1), set(points2))

steps = count_steps(points1, points2, intersect)

sums = [one+two for one,two in steps]

print(min(sums))