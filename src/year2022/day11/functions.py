import contextlib
import math


def preprocessing(data):
    data = [e.split() for e in data]

    monkeys = {}
    for e in data:
        with contextlib.suppress(IndexError):
            if "monkey" in e[0].lower():
                monkey = int(e[1].strip(":"))
                monkeys[monkey] = {}

            if "starting" in e[0].lower():
                s_it = [e.strip(",") for e in e[2:]]
                s_it = [int(i) for i in s_it]
                monkeys[monkey]["s_it"] = s_it

            if "operation" in e[0].lower():
                ope = [e[4], e[5]]
                monkeys[monkey]["ope"] = ope

            if "test" in e[0].lower():
                monkeys[monkey]["test"] = [int(e[3])]

            if "true" in e[1].lower():
                monkeys[monkey]["test"].append(int(e[5]))

            if "false" in e[1].lower():
                monkeys[monkey]["test"].append(int(e[5]))
    return monkeys


def part_1(data):
    monkeys = preprocessing(data)
    for _ in range(20):
        for monkey, value in monkeys.items():
            ope = value["ope"]
            test = value["test"][0]
            for it in value["s_it"]:
                if ope[0] == "*" and ope[1] == "old":
                    new_it = it * it
                elif ope[0] == "+" and ope[1] == "old":
                    new_it = it + it
                elif ope[0] == "*":
                    new_it = it * int(ope[1])
                elif ope[0] == "+":
                    new_it = it + int(ope[1])

                new_it = new_it // 3

                if new_it % test == 0:
                    true = value["test"][1]
                    monkeys[true]["s_it"].append(new_it)
                else:
                    false = value["test"][2]
                    monkeys[false]["s_it"].append(new_it)

                monkeys[monkey]["s_it"] = monkeys[monkey]["s_it"][1:]

                if "inspected" not in monkeys[monkey]:
                    monkeys[monkey]["inspected"] = 1
                else:
                    monkeys[monkey]["inspected"] += 1

    inspected = [monkeys[monkey]["inspected"] for monkey in monkeys]
    inspected = sorted(inspected, reverse=True)

    return inspected[0] * inspected[1]


def part_2(data):
    monkeys = preprocessing(data)
    divisors = [monkey["test"][0] for monkey in monkeys.values()]
    ops = [int(monkey["ope"][1]) for monkey in monkeys.values() if monkey["ope"][1] != "old"]

    lcm = math.lcm(*divisors, *ops)

    for _ in range(10000):
        for monkey, value in monkeys.items():
            ope = value["ope"]
            for it in value["s_it"]:
                if ope[0] == "*" and ope[1] == "old":
                    new_it = it * it
                elif ope[0] == "+" and ope[1] == "old":
                    new_it = it + it
                elif ope[0] == "*":
                    new_it = it * int(ope[1])
                elif ope[0] == "+":
                    new_it = it + int(ope[1])

                new_it = new_it % lcm

                test = monkeys[monkey]["test"][0]
                if new_it % test == 0:
                    true = monkeys[monkey]["test"][1]
                    monkeys[true]["s_it"].append(new_it)
                else:
                    false = monkeys[monkey]["test"][2]
                    monkeys[false]["s_it"].append(new_it)

                monkeys[monkey]["s_it"] = monkeys[monkey]["s_it"][1:]

                if "inspected" not in monkeys[monkey]:
                    monkeys[monkey]["inspected"] = 1
                else:
                    monkeys[monkey]["inspected"] += 1

    inspected = [value_["inspected"] for value_ in monkeys.values()]
    inspected = sorted(inspected, reverse=True)

    return inspected[0] * inspected[1]
