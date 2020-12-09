def find_not_sum_preamble(data, length):
    for _ in range(len(data)):
        for i in range(length):
            for j in range(i + 1, length):
                if data[length] == data[i] + data[j]:
                    data.pop(0)
                    break
    else:
        return data[length]


def sum_weakness(data, invalid):
    for start in range(len(data) + 1):
        for end in range(start + 2, len(data) + 1):
            if (sum(data[start:end])) == invalid:
                return max(data[start:end]) + min(data[start:end])
