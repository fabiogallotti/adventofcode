from collections import defaultdict
from itertools import permutations


def preprocessing(data):
    cities = set()
    distances = defaultdict(dict)

    data = [elem.split(" ")[::2] for elem in data]
    for elem in data:
        cities.add(elem[0])
        cities.add(elem[1])
        distances[elem[0]][elem[1]] = int(elem[2])

    return cities, distances


def max_distance(distances):
    return sum(
        value2 for key, value in distances.items() for key2, value2 in value.items()
    )


def sum_distance_path(path, distances):
    distance = 0
    for i in range(len(path) - 1):
        try:
            distance += distances[path[i]][path[i + 1]]
        except KeyError:
            distance += distances[path[i + 1]][path[i]]
    return distance


def shortest_path_length(cities, distances):
    paths = permutations(cities)

    shortest = max_distance(distances)
    for path in paths:
        distance = sum_distance_path(path, distances)
        shortest = min(shortest, distance)

    return shortest


def longest_path_length(cities, distances):
    paths = permutations(cities)

    longest = 0
    for path in paths:
        distance = sum_distance_path(path, distances)
        longest = max(longest, distance)

    return longest
