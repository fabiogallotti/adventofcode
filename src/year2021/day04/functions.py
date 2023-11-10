import itertools


def preprocessing(data):
    data = [x.split() for x in data]

    numbers_drawn = [n.split(",") for n in data[0]][0]
    numbers_drawn = [int(x) for x in numbers_drawn]

    list_cards = data[1:]
    cards = {i // 5: list_cards[i : i + 5] for i in range(0, len(list_cards), 5)}

    for number, card in cards.items():
        for i, row in enumerate(card):
            cards[number][i] = [x.split(",")[0] for x in row]

    for card in cards.values():
        for i in range(len(card)):
            for j in range(len(card[0])):
                card[i][j] = int(card[i][j])

    return numbers_drawn, cards


def find_first_winning(numbers_drawn, cards):
    n = 5
    for number in numbers_drawn:
        for number_card, card in cards.items():
            for i, j in itertools.product(range(n), range(n)):
                if number == card[i][j]:
                    card[i][j] = "X"

                if card[i][0] == card[i][1] == card[i][2] == card[i][3] == card[i][4] == "X":
                    return number, number_card

                if card[0][j] == card[1][j] == card[2][j] == card[3][j] == card[4][j] == "X":
                    return number, number_card


def part_1(data):
    numbers_drawn, cards = preprocessing(data)
    number, number_card = find_first_winning(numbers_drawn, cards)

    sum_unmarked = 0
    for row in cards[number_card]:
        for n in row:
            if isinstance(n, int):
                sum_unmarked += n

    return sum_unmarked * number


def find_last_winning(numbers_drawn, cards):
    all_cards_numbers = set(cards.keys())
    winning_cards = set()
    n = 5
    for number in numbers_drawn:
        for number_card, card in cards.items():
            for i, j in itertools.product(range(n), range(n)):
                if number == card[i][j]:
                    card[i][j] = "X"

                if card[i][0] == card[i][1] == card[i][2] == card[i][3] == card[i][4] == "X":
                    winning_cards.add(number_card)

                if card[0][j] == card[1][j] == card[2][j] == card[3][j] == card[4][j] == "X":
                    winning_cards.add(number_card)

            remaining_cards = all_cards_numbers - winning_cards
            if len(remaining_cards) == 0:
                return number, number_card


def part_2(data):
    numbers_drawn, cards = preprocessing(data)
    number, number_card = find_last_winning(numbers_drawn, cards)

    sum_unmarked = 0
    for row in cards[number_card]:
        for n in row:
            if isinstance(n, int):
                sum_unmarked += n

    return sum_unmarked * number
