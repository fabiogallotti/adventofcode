from collections import defaultdict

import numpy as np
from pydantic import BaseModel, field_validator


class ClawMovement(BaseModel):
    x: int
    y: int

    @field_validator("x", "y", mode="before")
    @classmethod
    def split_value(cls, v: str) -> int:
        return int(v.strip().split("+")[1])


class Location(BaseModel):
    x: int
    y: int

    @field_validator("x", "y", mode="before")
    @classmethod
    def split_value(cls, v: str) -> int:
        return int(v.strip().split("=")[1])


class Machine(BaseModel):
    a: ClawMovement
    b: ClawMovement
    prize: Location


def get_machine_dict(data):
    machine_dict = defaultdict(list)
    machine_number = 0
    for row in data:
        if row:
            machine_dict[machine_number].append(row)
        else:
            machine_number += 1
    return machine_dict


def preprocessing(data):
    machine_dict = get_machine_dict(data)
    machine_dict_obj = defaultdict(Machine)

    for m_key in machine_dict:
        machine = machine_dict[m_key]

        a = machine[0].split(":")[1].split(",")
        b = machine[1].split(":")[1].split(",")
        prize = machine[2].split(":")[1].split(",")

        machine_obj = Machine(
            a=ClawMovement(x=a[0], y=a[1]),
            b=ClawMovement(x=b[0], y=b[1]),
            prize=Location(x=prize[0], y=prize[1]),
        )

        machine_dict_obj[m_key] = machine_obj

    return machine_dict_obj


def calculate_tokens(data, prize_modifier=None):
    machine_dict = preprocessing(data)
    a_cost = 3
    b_cost = 1
    total = 0

    for m_key in machine_dict:
        machine = machine_dict[m_key]
        a_vector = list(machine.a.model_dump().values())
        b_vector = list(machine.b.model_dump().values())

        prize_vector = list(machine.prize.model_dump().values())
        if prize_modifier:
            prize_vector = [x + prize_modifier for x in prize_vector]

        matrix = np.array([a_vector, b_vector]).T
        inv_matrix = np.linalg.inv(matrix)

        res = np.dot(inv_matrix, np.array([prize_vector]).T)
        res = np.round(res, decimals=2)

        if res[0][0] % 1 == 0 and res[1][0] % 1 == 0:
            a_moves = int(res[0, 0])
            b_moves = int(res[1, 0])

            if (
                prize_modifier is None and a_moves <= 100 and b_moves <= 100
            ) or prize_modifier is not None:
                tokens = (a_moves * a_cost) + (b_moves * b_cost)
                total += tokens
    return total


def part_1(data):
    return calculate_tokens(data)


def part_2(data):
    prize_modifier = 10000000000000
    return calculate_tokens(data, prize_modifier)
