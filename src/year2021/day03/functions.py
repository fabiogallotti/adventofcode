def part_1(data):
    bit_columns = {x: {"0": 0, "1": 0} for x in range(len(data[0]))}

    for elem in data:
        for i, value in enumerate(elem):
            bit_columns[i][value] += 1

    gamma_rate_binary = [
        "0" if bit_freq["0"] > bit_freq["1"] else "1" for bit_freq in bit_columns.values()
    ]
    gamma_rate_dec = int("".join(gamma_rate_binary), 2)

    epsilon_rate_binary = [
        "1" if bit_freq["0"] > bit_freq["1"] else "0" for bit_freq in bit_columns.values()
    ]
    epsilon_rate_dec = int("".join(epsilon_rate_binary), 2)

    return gamma_rate_dec * epsilon_rate_dec


def _calculate_oxygen_rating(data):
    possible_values = data.copy()

    for col_num in range(len(possible_values[0])):
        bit_column = {"0": 0, "1": 0}
        for elem in possible_values:
            bit_column[elem[col_num]] += 1

        most_common = "1" if bit_column["1"] >= bit_column["0"] else "0"
        possible_values[:] = [elem for elem in possible_values if elem[col_num] == most_common]

        if len(possible_values) == 1:
            rating = int("".join(possible_values), 2)

    return rating


def _calculate_co2_rating(data):
    possible_values = data.copy()

    for col_num in range(len(possible_values[0])):
        bit_column = {"0": 0, "1": 0}
        for elem in possible_values:
            bit_column[elem[col_num]] += 1

        least_common = "0" if bit_column["0"] <= bit_column["1"] else "1"
        possible_values[:] = [elem for elem in possible_values if elem[col_num] == least_common]

        if len(possible_values) == 1:
            rating = int("".join(possible_values), 2)

    return rating


def part_2(data):
    oxygen_rating = _calculate_oxygen_rating(data)
    co2_rating = _calculate_co2_rating(data)
    return oxygen_rating * co2_rating
