from year2019.day01.functions import fuel_computation, fuel_recursive


def test_fuel_computation():
    assert fuel_computation(12) == 2
    assert fuel_computation(14) == 2
    assert fuel_computation(1969) == 654
    assert fuel_computation(100756) == 33583


def test_fuel_recursive():
    assert fuel_recursive(14) == 2
    assert fuel_recursive(1969) == 966
    assert fuel_recursive(100756) == 50346
