from src.year2022.day07.functions import part_1, part_2

INPUT = [
    ["$", "cd", "/"],
    ["$", "ls"],
    ["dir", "a"],
    ["14848514", "b.txt"],
    ["8504156", "c.dat"],
    ["dir", "d"],
    ["$", "cd", "a"],
    ["$", "ls"],
    ["dir", "e"],
    ["29116", "f"],
    ["2557", "g"],
    ["62596", "h.lst"],
    ["$", "cd", "e"],
    ["$", "ls"],
    ["584", "i"],
    ["$", "cd", ".."],
    ["$", "cd", ".."],
    ["$", "cd", "d"],
    ["$", "ls"],
    ["4060174", "j"],
    ["8033020", "d.log"],
    ["5626152", "d.ext"],
    ["7214296", "k"],
]


def test_part_1():
    assert part_1(INPUT) == 95437


def test_part_2():
    assert part_2(INPUT) == 24933642
