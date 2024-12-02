from year2015.day06.functions import calculate_brightness, calculate_lights_on, get_points


def test_get_points():
    assert get_points(["0,0", "through", "999,999"]) == (0, 0, 999, 999)


def test_calculate_lights_on():
    assert calculate_lights_on([["turn", "on", "0,0", "through", "999,999"]]) == 1000000
    assert (
        calculate_lights_on(
            [
                ["turn", "on", "0,0", "through", "999,999"],
                ["turn", "off", "499,499", "through", "500,500"],
            ]
        )
        == 999996
    )

    assert calculate_lights_on([["toogle", "0,0", "through", "999,0"]]) == 1000


def test_calculate_brightness():
    assert calculate_brightness([["turn", "on", "0,0", "through", "0,0"]]) == 1
    assert calculate_brightness([["turn", "off", "0,0", "through", "0,0"]]) == 0

    assert calculate_brightness([["toggle", "0,0", "through", "999,999"]]) == 2000000
