def part_1(data):
    winning_dict, my_numbers_dict = parsing(data)

    points = 0
    for card_id, winning in winning_dict.items():
        my_winning_numbers = sum(number in my_numbers_dict[card_id] for number in winning)
        if my_winning_numbers > 0:
            points += pow(2, (my_winning_numbers - 1))

    return points


def part_2(data):
    winning_dict, my_numbers_dict = parsing(data)

    count_dict = {x: 1 for x in winning_dict.keys()}

    for card_id, winning in winning_dict.items():
        my_winning_numbers = sum(number in my_numbers_dict[card_id] for number in winning)
        if my_winning_numbers > 0:
            for i in list(range(1, my_winning_numbers + 1)):
                count_dict[card_id + i] += 1 * count_dict[card_id]

    return sum(count_dict.values())


def parsing(data):
    winning_dict_all = {}
    my_numbers_dict_all = {}

    for row in data:
        row = row.removeprefix("Card ")
        row = row.split(":")

        cards = {int(row[0]): row[1]}

        winning = set()
        my_numbers = set()

        for cards_id, card_list in cards.items():
            cards[cards_id] = [card.strip() for card in card_list.split("|")]
            cards[cards_id] = [card_list.split() for card_list in cards[cards_id]]

            winning.update(int(c) for c in cards[cards_id][0])
            my_numbers.update(int(c) for c in cards[cards_id][1])

            winning_dict = {cards_id: winning}
            my_numbers_dict = {cards_id: my_numbers}

        winning_dict_all |= winning_dict
        my_numbers_dict_all |= my_numbers_dict

    return winning_dict_all, my_numbers_dict_all
