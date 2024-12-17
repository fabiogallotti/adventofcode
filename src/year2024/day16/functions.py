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

    def rotate_clockwise(self):
        rotation_order = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        current_index = rotation_order.index(self)
        return rotation_order[(current_index + 1) % 4]

    def rotate_counterclockwise(self):
        rotation_order = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        current_index = rotation_order.index(self)
        return rotation_order[(current_index - 1) % 4]


def preprocessing(data):
    walls = []

    for i, row in enumerate(data):
        for j in range(len(row)):
            value = data[i][j]
            if value == "#":
                walls.append(Position(x=i, y=j))
            elif value == "S":
                start = Position(x=i, y=j)
            elif value == "E":
                end = Position(x=i, y=j)

    return walls, start, end


def build_graph(walls, max_x, max_y):
    graph = nx.DiGraph()

    directions = list(Direction)

    nodes = []
    edges = []
    visited_nodes = set()

    for i in range(max_x):
        for j in range(max_y):
            pos = Position(x=i, y=j)

            if pos in walls:
                continue

            for direction in directions:
                if ((i, j), direction) not in visited_nodes:
                    visited_nodes.add(((i, j), direction))

                nodes.append((pos, direction))

                dx, dy = direction.value
                next_pos = Position(x=i + dx, y=j + dy)
                if 0 <= next_pos.x < max_x and 0 <= next_pos.y < max_y and next_pos not in walls:
                    edges.append(((pos, direction), (next_pos, direction), 1))

                direction_clockwise = direction.rotate_clockwise()
                edges.append(((pos, direction), (pos, direction_clockwise), 1000))

                direction_counterclockwise = direction.rotate_counterclockwise()
                edges.append(((pos, direction), (pos, direction_counterclockwise), 1000))

    graph.add_nodes_from(nodes)
    graph.add_edges_from((u, v, {"weight": w}) for u, v, w in edges)
    return graph


def part_1(data):
    max_x = len(data)
    max_y = len(data[0])
    walls, start, end = preprocessing(data)

    graph = build_graph(walls, max_x, max_y)

    start_node = (start, Direction.RIGHT)
    end_node = (end, Direction.UP)

    return nx.dijkstra_path_length(graph, start_node, end_node, weight="weight")


def part_2(data):
    max_x = len(data)
    max_y = len(data[0])
    walls, start, end = preprocessing(data)

    graph = build_graph(walls, max_x, max_y)

    start_node = (start, Direction.RIGHT)
    end_node = (end, Direction.UP)

    paths = nx.all_shortest_paths(graph, start_node, end_node, weight="weight", method="dijkstra")

    elem_paths = set()
    for path in paths:
        for elem in path:
            elem_paths.add(elem[0])

    return len(elem_paths)
