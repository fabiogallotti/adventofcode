def concatenate_string(number_of_digits, digits):
    look_and_say=""
    for i, elem in enumerate(number_of_digits):
        look_and_say += number_of_digits[i] + digits[i]
    return look_and_say

def look_and_say(data):
    number_of_digits = []
    digits = []
    digit = data[0]
    times=0

    for i in range(len(data)):
        if data[i] == digit:
            times += 1
        else:
            number_of_digits.append(str(times))
            digits.append(digit)
            digit = data[i]
            times = 1
    number_of_digits.append(str(times))
    digits.append(digit)

    return concatenate_string(number_of_digits, digits)


def apply_look_and_say_n_times(data, n):
    for _ in range(n):
        data = look_and_say(data)
    return len(data)