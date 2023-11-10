def preprocessing(data):
    dict_ = {}
    for elem in data:
        rules = elem.split("contain")

        bags = rules[0].replace("bags", "").strip().replace(" ", "_")
        contains = rules[1].split(",")
        contains = [x.replace("bags", "").replace("bag", "").strip(" .") for x in contains]
        numbers = [int(x[0]) for x in contains if x[0].isnumeric()]
        contains = [x[2:].replace(" ", "_") for x in contains]

        dict_[bags] = {k: v for k, v in zip(contains, numbers)}
    return dict_


def find_bags_can_contain(bag, rules):
    return [outer for outer, contains in rules.items() if bag in contains.keys()]


def number_containing_bags(bags_to_find, rules):
    containing_bags = set()
    while bags_to_find:
        bag = bags_to_find.pop()
        found_bags = find_bags_can_contain(bag, rules)
        bags_to_find.extend(found_bags)
        containing_bags.update(found_bags)
    return len(containing_bags)


def bag_size(bag_name, rules):
    return sum(value + value * bag_size(bag, rules) for bag, value in rules[bag_name].items())
