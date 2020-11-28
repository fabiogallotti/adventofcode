from src.year2015.day6.functions import (
    calculate_brightness,
    calculate_lights_on,
    get_points,
)


def test_get_points():
    assert get_points(["0,0", "through", "999,999"]) == (0, 0, 999, 999)


def test_calculate_lights_on():
    lights = [[0 for row in range(1000)] for column in range(1000)]
    assert (
        calculate_lights_on([["turn", "on", "0,0", "through", "999,999"]], lights)
        == 1000000
    )
    assert (
        calculate_lights_on([["turn", "off", "499,499", "through", "500,500"]], lights)
        == 999996
    )

    lights = [[0 for row in range(1000)] for column in range(1000)]
    assert calculate_lights_on([["toogle", "0,0", "through", "999,0"]], lights) == 1000


def test_calculate_brightness():
    lights = [[0 for row in range(1000)] for column in range(1000)]
    assert calculate_brightness([["turn", "on", "0,0", "through", "0,0"]], lights) == 1

    lights = [[0 for row in range(1000)] for column in range(1000)]
    assert (
        calculate_brightness([["toggle", "0,0", "through", "999,999"]], lights)
        == 2000000
    )
