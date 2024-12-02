from year2023.day12.functions import part_1, part_2

EXAMPLE = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
]


def test_part_1():
    assert part_1(EXAMPLE) == 21


def test_part_2():
    assert part_2(EXAMPLE) == 525152
