def trees_for_given_slope(data, right, down):
    num_rows = len(data)
    num_columns = len(data[0])

    return sum(
        1
        for i in range(num_rows)
        if i * down < num_rows and data[i * down][i * right % num_columns] == "#"
    )


def product_of_multiple_slopes(data, slopes):
    prod = 1
    for right, down in slopes:
        prod *= trees_for_given_slope(data, right, down)

    return prod
