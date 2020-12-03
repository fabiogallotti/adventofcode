from src.year2020.day3.functions import trees_for_given_slope, product_of_multiple_slopes

def test_trees_for_given_slope():
    data = [
                "..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#",
            ]

    assert trees_for_given_slope(data, 3 ,1 ) == 7

def test_product_of_multiple_slopes():
    data = [
                "..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#",
            ]
    assert product_of_multiple_slopes(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]) == 336
