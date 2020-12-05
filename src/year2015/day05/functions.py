def three_vowels(string):
    count = sum(string.count(vowel) for vowel in "aeiou")
    return count > 2


def check_after_n_letters(string, n):
    return any(string[i] == string[i + n] for i in range(len(string) - n))


def twice_in_a_row(string):
    return check_after_n_letters(string, 1)


def contains(string):
    return "ab" in string or "cd" in string or "pq" in string or "xy" in string


def nice_string_first(string):
    return three_vowels(string) and twice_in_a_row(string) and not contains(string)


def pair_two_letters(string):
    if len(string) < 4:
        return False
    for i in range(len(string) - 1):
        for j in range(i + 2, len(string) - 1):
            if string[i] == string[j] and string[i + 1] == string[j + 1]:
                return True
    return False


def repeats_with_one_between(string):
    return check_after_n_letters(string, 2)


def nice_string_second(string):
    return pair_two_letters(string) and repeats_with_one_between(string)
