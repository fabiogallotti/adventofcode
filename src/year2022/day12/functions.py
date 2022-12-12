import itertools
from copy import deepcopy


def preprocessing(data):
    h = len(data)
    w = len(data[0])

    unvisited_nodes = []
    for i, j in itertools.product(range(h), range(w)):
        if data[i][j] == "S":
            start = (i, j)
            data[i][j] = "a"
        elif data[i][j] == "E":
            end = (i, j)
            data[i][j] = "z"

        data[i][j] = ord(data[i][j]) - ord("a")
        unvisited_nodes.append((i, j))

    node_distance = dict(zip(unvisited_nodes, [99999] * h * w))

    return data, start, end, unvisited_nodes, node_distance


def possible_nodes_1(data):
    h = len(data)
    w = len(data[0])
    possible_nodes = {}
    for i, j in itertools.product(range(h), range(w)):
        adjacent_pos_nodes = []

        node = data[i][j]
        l = j - 1
        r = j + 1
        u = i - 1
        d = i + 1
        if l >= 0:
            left = data[i][l]
            if left - node <= 1:
                adjacent_pos_nodes.append((i, l))
        if r < w:
            right = data[i][r]
            if right - node <= 1:
                adjacent_pos_nodes.append((i, r))
        if u >= 0:
            up = data[u][j]
            if up - node <= 1:
                adjacent_pos_nodes.append((u, j))
        if d < h:
            down = data[d][j]
            if down - node <= 1:
                adjacent_pos_nodes.append((d, j))

        possible_nodes[(i, j)] = adjacent_pos_nodes

    return possible_nodes


def part_1(data):
    new_data = deepcopy(data)
    data, start, end, unvisited_nodes, node_distance = preprocessing(new_data)
    possible_nodes = possible_nodes_1(data)

    node_distance[start] = 0
    visited_nodes = []

    while end not in visited_nodes:
        current = min(unvisited_nodes, key=node_distance.get)
        for pos_node in possible_nodes[current]:
            if (
                pos_node not in visited_nodes
                and node_distance[current] + 1 < node_distance[pos_node]
            ):
                node_distance[pos_node] = node_distance[current] + 1

        visited_nodes.append(current)
        unvisited_nodes.remove(current)

    return node_distance[end]


def possible_nodes_2(data):
    h = len(data)
    w = len(data[0])
    possible_nodes = {}
    for i, j in itertools.product(range(h), range(w)):
        adjacent_pos_nodes = []

        node = data[i][j]
        l = j - 1
        r = j + 1
        u = i - 1
        d = i + 1
        if l >= 0:
            left = data[i][l]
            if left - node >= -1:
                adjacent_pos_nodes.append((i, l))
        if r < w:
            right = data[i][r]
            if right - node >= -1:
                adjacent_pos_nodes.append((i, r))
        if u >= 0:
            up = data[u][j]
            if up - node >= -1:
                adjacent_pos_nodes.append((u, j))
        if d < h:
            down = data[d][j]
            if down - node >= -1:
                adjacent_pos_nodes.append((d, j))

        possible_nodes[(i, j)] = adjacent_pos_nodes

    return possible_nodes


def part_2(data):
    new_data = deepcopy(data)
    data, _, end, unvisited_nodes, node_distance = preprocessing(new_data)
    possible_nodes = possible_nodes_2(data)

    visited_nodes = []
    node_distance[end] = 0

    current = end
    while data[current[0]][current[1]] > 0:
        current = min(unvisited_nodes, key=node_distance.get)
        for pos_node in possible_nodes[current]:
            if (
                pos_node not in visited_nodes
                and node_distance[current] + 1 < node_distance[pos_node]
            ):
                node_distance[pos_node] = node_distance[current] + 1

        visited_nodes.append(current)
        unvisited_nodes.remove(current)

    return node_distance[current]
