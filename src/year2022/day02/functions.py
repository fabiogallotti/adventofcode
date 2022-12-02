EQUIVALENCE = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

WORDING = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissor",
}

MY_SCORE = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
}

BEAT = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper",
}
BEATEN = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper",
}


RESULT_SCORE = {
    "win": 6,
    "draw": 3,
    "lose": 0,
}


def part_1(data):
    score = 0
    for elem in data:
        opponent = WORDING[EQUIVALENCE[elem[0]]]
        me = WORDING[elem[1]]
        score += MY_SCORE[me]
        if opponent == BEAT[me]:
            score += RESULT_SCORE["win"]
        elif opponent == me:
            score += RESULT_SCORE["draw"]
    return score


MAP_RESULT = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}
BEAT_REVERSE = {"scissor": "rock", "rock": "paper", "paper": "scissor"}


def part_2(data):
    score = 0
    for elem in data:
        opponent = WORDING[EQUIVALENCE[elem[0]]]
        result = MAP_RESULT[elem[1]]

        score += RESULT_SCORE[result]

        if result == "lose":
            me = BEATEN[opponent]
        elif result == "draw":
            me = opponent
        elif result == "win":
            me = BEAT_REVERSE[opponent]
        score += MY_SCORE[me]
    return score
