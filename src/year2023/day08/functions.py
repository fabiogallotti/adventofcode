from math import lcm

from pydantic import BaseModel


class Node(BaseModel):
    left: str
    right: str


def parsing(data):
    data = [x.split("=") for x in data[2:]]
    data = [[x[0], *x[1].split(",")] for x in data]

    return {x[0].strip(): Node(left=x[1].strip(" ("), right=x[2].strip(" )")) for x in data}


def part_1(data):
    instructions = list(data[0])
    nodes = parsing(data)
    node = "AAA"
    steps = 0

    while node != "ZZZ":
        for i in instructions:
            if i == "L":
                node = nodes[node].left
                steps += 1
            elif i == "R":
                node = nodes[node].right
                steps += 1

    return steps


def part_2(data):
    instructions = list(data[0])
    nodes = parsing(data)

    starting_nodes = [node for node in nodes if node.endswith("A")]
    ending_nodes = [node for node in nodes if node.endswith("Z")]

    steps = [0] * len(starting_nodes)
    for pos, node in enumerate(starting_nodes):
        while node not in ending_nodes:
            for i in instructions:
                if i == "L":
                    node = nodes[node].left
                    steps[pos] += 1
                elif i == "R":
                    node = nodes[node].right
                    steps[pos] += 1

    return lcm(*steps)
