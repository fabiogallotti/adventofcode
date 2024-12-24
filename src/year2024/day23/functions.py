import networkx as nx


def part_1(data):
    nodes = [row.split("-") for row in data]

    graph = nx.Graph()
    graph.add_edges_from(nodes)

    triangles = [
        list(triangle) for triangle in nx.enumerate_all_cliques(graph) if len(triangle) == 3
    ]
    return sum(any(elem.startswith("t") for elem in triangle) for triangle in triangles)


def part_2(data):
    nodes = [row.split("-") for row in data]

    graph = nx.Graph()
    graph.add_edges_from(nodes)

    cliques = list(nx.find_cliques(graph))

    largest_clique = max(cliques, key=len)

    return ",".join(sorted(largest_clique))
