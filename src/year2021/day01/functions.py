def find_single_increase(data):
    previous = None
    increase = 0
    for elem in data:
        if previous is not None and elem > previous:
            increase += 1
        previous = elem

    return increase


def find_three_increase(data):
    previous = None
    increase = 0
    for i in range(len(data) - 2):
        sum_ = sum(data[i : i + 3])
        if previous is not None and sum_ > previous:
            increase += 1
        previous = sum_

    return increase
