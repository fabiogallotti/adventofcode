from src.year2015.day7.functions import preprocessing, emulate_circuit


def test_emulate_circuit():

    wires = {
        "x": 123,
        "y": 456,
        "d": ["x", "AND", "y"],
        "e": ["x", "OR", "y"],
        "f": ["x", "LSHIFT", "2"],
        "g": ["y", "RSHIFT", "2"],
        "h": ["NOT", "x"],
        "i": ["NOT", "y"],
        "a": ["x"]
    }

    assert (
        preprocessing(
            [
                ["123", "->", "x"],
                ["456", "->", "y"],
                ["x", "AND", "y", "->", "d"],
                ["x", "OR", "y", "->", "e"],
                ["x", "LSHIFT", "2", "->", "f"],
                ["y", "RSHIFT", "2", "->", "g"],
                ["NOT", "x", "->", "h"],
                ["NOT", "y", "->", "i"],
                ["x", "->", "a"],
            ]
        )
        == wires
    )

    emulate_circuit(wires, "i")
    assert wires == {
        "a": 123,
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }
