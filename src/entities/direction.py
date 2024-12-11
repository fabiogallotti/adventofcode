from enum import Enum


class Direction(Enum):
    """Represents movements in a 2D grid"""

    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
