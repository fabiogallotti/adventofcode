from pydantic import BaseModel

from entities.direction import Direction


class Point(BaseModel):
    """Represents a point in a 2D grid"""

    x: int
    y: int

    def __hash__(self):
        return hash(str(self.x) + str(self.y))

    def move(self, direction: Direction):
        return Point(x=self.x + direction.value[0], y=self.y + direction.value[1])
