def part_1(data):
    return sum(
        contains_at_least_three_vowels(string)
        and contains_twice_in_a_row(string)
        and not contains_string(string)
        for string in data
    )


def part_2(data):
    return sum(
        contains_pair_two_letters(string) and repeats_with_one_between(string) for string in data
    )


def contains_at_least_three_vowels(string):
    count = sum(string.count(vowel) for vowel in "aeiou")
    return count > 2


def contains_twice_in_a_row(string):
    return check_after_n_letters(string, 1)


def check_after_n_letters(string, n):
    return any(string[i] == string[i + n] for i in range(len(string) - n))


def contains_string(string):
    return any(sub in string for sub in ["ab", "cd", "pq", "xy"])


def contains_pair_two_letters(string):
    seen = set()
    for i in range(len(string) - 1):
        pair = string[i : i + 2]
        if pair in seen:
            return True
        seen.add(string[i - 1 : i + 1] if i > 0 else "")
    return False


def repeats_with_one_between(string):
    return check_after_n_letters(string, 2)
