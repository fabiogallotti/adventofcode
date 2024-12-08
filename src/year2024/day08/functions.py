import itertools

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def add(self, p2):
        return Point(x=self.x + p2.x, y=self.y + p2.y)

    def sub(self, p2):
        return Point(x=self.x - p2.x, y=self.y - p2.y)

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


def inside_borders(point, max_x, max_y):
    return 0 <= point.x <= max_x and 0 <= point.y <= max_y


def preprocessing(data):
    map_dict = {}
    for i, j in itertools.product(range(len(data)), range(len(data[0]))):
        elem = data[i][j]
        if elem != ".":
            if elem in map_dict:
                map_dict[elem].append(Point(x=i, y=j))
            else:
                map_dict[elem] = [Point(x=i, y=j)]

    return map_dict


def part_1(data):
    map_dict = preprocessing(data)
    max_x = len(data) - 1
    max_y = len(data[0]) - 1

    antennas = set()
    for values in map_dict.values():
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                p1 = values[i]
                p2 = values[j]

                x_dist = p1.x - p2.x
                y_dist = p1.y - p2.y

                new_point = p1.add(Point(x=x_dist, y=y_dist))
                if inside_borders(new_point, max_x, max_y):
                    antennas.add(new_point)

                new_point = p2.sub(Point(x=x_dist, y=y_dist))
                if inside_borders(new_point, max_x, max_y):
                    antennas.add(new_point)

    return len(antennas)


def part_2(data):
    map_dict = preprocessing(data)
    max_x = len(data) - 1
    max_y = len(data[0]) - 1

    antennas = set()
    for values in map_dict.values():
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                p1 = values[i]
                p2 = values[j]

                x_dist = p1.x - p2.x
                y_dist = p1.y - p2.y

                new_point = p1
                while inside_borders(new_point, max_x, max_y):
                    antennas.add(new_point)
                    new_point = new_point.add(Point(x=x_dist, y=y_dist))

                new_point = p2
                while inside_borders(new_point, max_x, max_y):
                    antennas.add(new_point)
                    new_point = new_point.sub(Point(x=x_dist, y=y_dist))

    return len(antennas)
