BAG = {"red": 12, "green": 13, "blue": 14}


def part_1(data):
    not_acceptable = set()

    games_dict = parsing(data)

    for game_id, game_dict in games_dict.items():
        for color, values in game_dict.items():
            if any(int(value) > BAG[color] for value in values):
                not_acceptable.add(game_id)

    keys = list(games_dict.keys())
    na = list(not_acceptable)

    res = [i for i in keys if i not in na]

    return sum(res)


def part_2(data):
    games_dict = parsing(data)

    sum_ = 0
    for game_dict in games_dict.values():
        prod = 1
        for values in game_dict.values():
            fewest = max(values)
            prod *= int(fewest)

        sum_ += prod

    return sum_


def parsing(data):
    games_dict = {}

    for row in data:
        row = row.removeprefix("Game ")

        row = row.split(":")

        games = {int(row[0]): row[1]}
        for game_id, game_list in games.items():
            games[game_id] = [game.strip() for game in game_list.split(";")]
            games[game_id] = [game_list.split(",") for game_list in games[game_id]]

        game_dict = {int(row[0]): {"red": [], "blue": [], "green": []}}
        for game_id, game_list in games.items():
            for game in game_list:
                for g in game:
                    a = g.split()
                    game_dict[game_id][a[1]].append(int(a[0]))

        games_dict |= game_dict

    return games_dict
