try:
    from functions.functions import manhattan
except ModuleNotFoundError:
    from src.functions.functions import manhattan


def preprocessing(data):
    points1 = move(data[0])
    points2 = move(data[1])
    intersections = find_intersections(set(points1), set(points2))

    return points1, points2, intersections


def move(data):
    points = []
    x, y = 0, 0
    for elem in data:
        for _ in range(1, int(elem[1:]) + 1):
            if elem[0] == "R":
                x += 1
                points.append((x, y))
            elif elem[0] == "L":
                x -= 1
                points.append((x, y))
            elif elem[0] == "U":
                y += 1
                points.append((x, y))
            elif elem[0] == "D":
                y -= 1
                points.append((x, y))
    return points


def find_intersections(points1, points2):
    return [elem for elem in points1 if elem in points2]


def count_steps(intersections, points1, points2):
    return [(points1.index(elem) + 1, points2.index(elem) + 1) for elem in intersections]


def solve_problem(problem, intersections, points1=None, points2=None):
    if problem == 1:
        return min(manhattan(intersections))
    elif problem == 2:
        steps = count_steps(intersections, points1, points2)
        return min(one + two for one, two in steps)
