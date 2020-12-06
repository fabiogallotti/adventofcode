from src.year2019.day03.functions import preprocessing, solve_problem


def test_preprocessing():
    points1, points2, intersections = preprocessing(
        [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
    )

    assert points1 == [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (8, 0),
        (8, 1),
        (8, 2),
        (8, 3),
        (8, 4),
        (8, 5),
        (7, 5),
        (6, 5),
        (5, 5),
        (4, 5),
        (3, 5),
        (3, 4),
        (3, 3),
        (3, 2),
    ]
    assert points2 == [
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
        (6, 6),
        (6, 5),
        (6, 4),
        (6, 3),
        (5, 3),
        (4, 3),
        (3, 3),
        (2, 3),
    ]
    assert intersections == [(6, 5), (3, 3)]


def test_solve_problem():
    points1, points2, intersections = preprocessing(
        [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
    )

    assert solve_problem(1, intersections) == 6
    assert solve_problem(2, intersections, points1, points2) == 30

    points1, points2, intersections = preprocessing(
        [
            ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
            ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        ]
    )

    assert solve_problem(1, intersections) == 159
    assert solve_problem(2, intersections, points1, points2) == 610

    points1, points2, intersections = preprocessing(
        [
            [
                "R98",
                "U47",
                "R26",
                "D63",
                "R33",
                "U87",
                "L62",
                "D20",
                "R33",
                "U53",
                "R51",
            ],
            ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
        ]
    )

    assert solve_problem(1, intersections) == 135
    assert solve_problem(2, intersections, points1, points2) == 410
