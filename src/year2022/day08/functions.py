import itertools
from typing import List


def part_1(data):
    length = len(data)
    visible = 4 * (length - 1)

    for i, j in itertools.product(range(1, length - 1), range(1, length - 1)):
        value = data[i][j]

        left = data[i][:j]
        right = data[i][j + 1 :]

        up = [x[j] for x in data[:i]]
        down = [x[j] for x in data[i + 1 :]]

        if (
            all(value > x for x in left)
            or all(value > x for x in right)
            or all(value > x for x in up)
            or all(value > x for x in down)
        ):
            visible += 1
    return visible


def get_viewing_distance(value: int, direction: List[int]):
    view_distance = 0
    for e in direction:
        view_distance += 1
        if value <= e:
            break
    return view_distance


def part_2(data):
    length = len(data)

    max_scenic_score = 0
    for i, j in itertools.product(range(1, length - 1), range(1, length - 1)):
        value = data[i][j]

        left = data[i][:j][::-1]
        right = data[i][j + 1 :]
        up = [x[j] for x in data[:i]][::-1]
        down = [x[j] for x in data[i + 1 :]]

        left_vd = get_viewing_distance(value, left)
        right_vd = get_viewing_distance(value, right)
        up_vd = get_viewing_distance(value, up)
        down_vd = get_viewing_distance(value, down)

        scenic_score = left_vd * right_vd * up_vd * down_vd

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

    return max_scenic_score
