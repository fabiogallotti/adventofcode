from year2022.day06.functions import part_1, part_2


def test_part_1():
    assert part_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_part_2():
    assert part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert part_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert part_2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
