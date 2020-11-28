from src.year2015.day3.functions import (
    move,
    move_and_add,
    santa_delivers,
    santa_and_robo_delivers,
)


def test_move():
    house = [0, 0]
    move(">", house)
    assert house == [1, 0]
    move("<", house)
    assert house == [0, 0]
    move("^", house)
    assert house == [0, 1]
    move("v", house)
    assert house == [0, 0]


def test_move_and_add():
    locations = {(0, 0)}
    move_and_add(">", [0, 0], locations)

    assert locations == {(0, 0), (1, 0)}


def test_santa_delivers():
    assert santa_delivers(">") == 2
    assert santa_delivers(["^", ">", "v", "<"]) == 4
    assert santa_delivers(["^", "v", "^", "v", "^", "v", "^", "v", "^", "v"]) == 2


def test_santa_and_robo_delivers():
    assert santa_and_robo_delivers(["^", "v"]) == 3
    assert santa_and_robo_delivers(["^", ">", "v", "<"]) == 3
    assert (
        santa_and_robo_delivers(["^", "v", "^", "v", "^", "v", "^", "v", "^", "v"])
        == 11
    )
