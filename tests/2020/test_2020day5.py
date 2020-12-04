from src.year2020.day5.functions import find_seat_ids, find_missing_seat_id

def test_find_seat_ids():
    assert find_seat_ids(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]) == [357, 567, 119, 820]

def test_find_missing_seat_id():
    assert find_missing_seat_id([5,3,2,1,7,6]) == 4