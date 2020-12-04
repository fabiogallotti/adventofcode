from src.year2015.day9.functions import (
    longest_path_length,
    preprocessing,
    shortest_path_length,
)


def test_preprocessing():
    data = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    cities, distances = preprocessing(data)

    assert cities == {"London", "Dublin", "Belfast"}
    assert distances == {
        "London": {"Belfast": 518, "Dublin": 464},
        "Dublin": {"Belfast": 141},
    }


def test_shortest_path_length():
    cities = {"London", "Dublin", "Belfast"}
    distances = {"London": {"Belfast": 518, "Dublin": 464}, "Dublin": {"Belfast": 141}}

    assert shortest_path_length(cities, distances) == 605


def test_longest_path_length():
    cities = {"London", "Dublin", "Belfast"}
    distances = {"London": {"Belfast": 518, "Dublin": 464}, "Dublin": {"Belfast": 141}}

    assert longest_path_length(cities, distances) == 982
