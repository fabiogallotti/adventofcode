from enum import Enum

import networkx as nx
from pydantic import BaseModel


class Position(BaseModel):
    x: int
    y: int

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


def preprocessing(data):
    points = []
    for row in data:
        x, y = row.split(",")
        points.append(Position(x=x, y=y))
    return points


def build_graph(corrupted, max_x, max_y):
    graph = nx.Graph()
    directions = list(Direction)

    for i in range(max_x):
        for j in range(max_y):
            pos = Position(x=i, y=j)

            if pos in corrupted:
                continue

            graph.add_node(pos)
            for direction in directions:
                dx, dy = direction.value
                next_pos = Position(x=i + dx, y=j + dy)
                if (
                    0 <= next_pos.x < max_x
                    and 0 <= next_pos.y < max_y
                    and next_pos not in corrupted
                ):
                    graph.add_edge(pos, next_pos)

    return graph


def part_1(data, max_x=71, max_y=71, fallen=1024):
    points = preprocessing(data)

    start = Position(x=0, y=0)
    end = Position(x=max_x - 1, y=max_y - 1)

    corrupted = points[:fallen]

    graph = build_graph(set(corrupted), max_x, max_y)

    return nx.shortest_path_length(graph, start, end)


def part_2(data, max_x=71, max_y=71):
    points = preprocessing(data)

    start = Position(x=0, y=0)
    end = Position(x=max_x - 1, y=max_y - 1)

    for i in range(10000):
        try:
            corrupted = points[:i]
            graph = build_graph(set(corrupted), max_x, max_y)
            nx.shortest_path(graph, start, end)
        except nx.exception.NetworkXNoPath:
            last_point = corrupted[-1]
            break

    return ",".join([str(last_point.x), str(last_point.y)])
