from itertools import combinations

from pydantic import BaseModel


class Galaxy(BaseModel):
    x: int
    y: int


def part_1(data, expansion):
    galaxies = preprocessing(data, expansion)

    return sum(
        abs(galaxy_1.x - galaxy_2.x) + abs(galaxy_1.y - galaxy_2.y)
        for galaxy_1, galaxy_2 in combinations(galaxies, 2)
    )


def part_2(data, expansion):
    galaxies = preprocessing(data, expansion)

    return sum(
        abs(galaxy_1.x - galaxy_2.x) + abs(galaxy_1.y - galaxy_2.y)
        for galaxy_1, galaxy_2 in combinations(galaxies, 2)
    )


def preprocessing(data, expansion):
    galaxies = []
    not_empty_rows = set()
    not_empty_cols = set()
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == "#":
                galaxies.append(Galaxy(x=int(i), y=int(j)))
                not_empty_rows.add(int(i))
                not_empty_cols.add(int(j))

    empty_rows = sorted(list(set(range(len(data))) - not_empty_rows))
    empty_cols = sorted(list(set(range(len(data[0]))) - not_empty_cols))

    for galaxy in galaxies:
        new_galaxy_x = galaxy.x
        new_galaxy_y = galaxy.y
        for row in empty_rows:
            if galaxy.x > row:
                new_galaxy_x += expansion

        for col in empty_cols:
            if galaxy.y > col:
                new_galaxy_y += expansion

        galaxy.x = new_galaxy_x
        galaxy.y = new_galaxy_y

    return galaxies
