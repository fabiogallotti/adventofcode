from itertools import product


def part_1(data):
    return evaluate_combinations(data, ["+", "*"])


def evaluate_combinations(data, operations):
    result = 0
    for row in data:
        total, operands = [x.strip() for x in row.split(":")]
        total = int(total)

        operands = operands.split()

        num_operations = len(operands) - 1

        possible_combinations = list(product(operations, repeat=num_operations))
        for comb in possible_combinations:
            calc = f"{operands[0]}"
            for num, op in zip(operands[1:], list(comb)):
                calc += f"{op}{num}"

                calc = str(eval(calc))

            if eval(calc) == total:
                result += total
                break

    return result


def part_2(data):
    return evaluate_combinations(data, ["+", "*", ""])
