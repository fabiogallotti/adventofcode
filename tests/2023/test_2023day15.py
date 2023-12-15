from src.year2023.day15.functions import part_1, part_2

EXAMPLE = [
    "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7",
]


def test_part_1():
    assert part_1(EXAMPLE) == 1320


def test_part_2():
    assert part_2(EXAMPLE) == 145
