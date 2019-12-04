from utils import read_input, move, find_intersections, count_steps

data = read_input("input.txt")

points1 = move(data[0])
points2 = move(data[1])

intersect = find_intersections(set(points1), set(points2))
steps = count_steps(points1, points2, intersect)
sums = [one+two for one,two in steps]

print(min(sums))