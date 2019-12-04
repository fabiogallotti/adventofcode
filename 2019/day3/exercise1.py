from utils import read_input, move, find_intersections, manhattan

data = read_input("input.txt")

points1 = set(move(data[0]))
points2 = set(move(data[1]))

intersect = find_intersections(points1, points2)
distances = manhattan(intersect)

print(min(distances))