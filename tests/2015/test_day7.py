from src.year2015.day7.functions import emulate_circuit, preprocessing


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
        "a": ["x"],
        "b": ["c", "AND", "j"],
        "c": ["d", "OR", "y"],
        "j": ["h", "AND", "i"],
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
                ["c", "AND", "j", "->", "b"],
                ["d", "OR", "y", "->", "c"],
                ["h", "AND", "i", "->", "j"],
            ]
        )
        == wires
    )

    emulate_circuit(wires, "b")
    assert wires == {
        "a": 123,
        "b": 0,
        "c": 456,
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "j": 65028,
        "x": 123,
        "y": 456,
    }
