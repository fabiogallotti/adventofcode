from pathlib import Path

from pydantic import BaseModel


class Robot(BaseModel):
    x: int
    y: int
    v_x: int
    v_y: int
    max_x: int
    max_y: int

    def move(self):
        new_x = self.x + self.v_x
        if new_x >= self.max_x:
            new_x = 0 + new_x - self.max_x
        elif new_x < 0:
            new_x = self.max_x + new_x

        new_y = self.y + self.v_y

        if new_y >= self.max_y:
            new_y = 0 + new_y - self.max_y
        elif new_y < 0:
            new_y = self.max_y + new_y
        return Robot(
            x=new_x, y=new_y, v_x=self.v_x, v_y=self.v_y, max_x=self.max_x, max_y=self.max_y
        )


def preprocessing(data, max_x, max_y):
    robots = []
    for row in data:
        point, velocity = row.split(" ")

        point = point.split("=")[1].split(",")
        velocity = velocity.split("=")[1].split(",")

        robots.append(
            Robot(
                x=int(point[0]),
                y=int(point[1]),
                v_x=int(velocity[0]),
                v_y=int(velocity[1]),
                max_x=max_x,
                max_y=max_y,
            ),
        )

    return robots


def get_robots_in_quadrant(robots, x_min, x_max, y_min, y_max):
    return [
        robot
        for robot in robots
        if (robot.x >= x_min) and (robot.x <= x_max) and (robot.y >= y_min) and (robot.y <= y_max)
    ]


def part_1(data, max_x=101, max_y=103):
    robots = preprocessing(data, max_x, max_y)

    for _ in range(100):
        for i in range(len(robots)):
            robots[i] = robots[i].move()

    q1_x = (0, max_x // 2 - 1)
    q1_y = (0, max_y // 2 - 1)
    q2_x = (max_x // 2 + 1, max_x - 1)
    q2_y = (0, max_y // 2 - 1)
    q3_x = (0, max_x // 2 - 1)
    q3_y = (max_y // 2 + 1, max_y - 1)
    q4_x = (max_x // 2 + 1, max_x - 1)
    q4_y = (max_y // 2 + 1, max_y - 1)

    q1 = get_robots_in_quadrant(
        robots=robots, x_min=q1_x[0], x_max=q1_x[1], y_min=q1_y[0], y_max=q1_y[1]
    )
    q2 = get_robots_in_quadrant(
        robots=robots, x_min=q2_x[0], x_max=q2_x[1], y_min=q2_y[0], y_max=q2_y[1]
    )
    q3 = get_robots_in_quadrant(
        robots=robots, x_min=q3_x[0], x_max=q3_x[1], y_min=q3_y[0], y_max=q3_y[1]
    )
    q4 = get_robots_in_quadrant(
        robots=robots, x_min=q4_x[0], x_max=q4_x[1], y_min=q4_y[0], y_max=q4_y[1]
    )

    return len(q1) * len(q2) * len(q3) * len(q4)


class Position(BaseModel):
    x: int
    y: int


def get_positions(robots):
    return [(robot.x, robot.y) for robot in robots]


def part_2(data, max_x=101, max_y=103):
    from PIL import Image

    robots = preprocessing(data, max_x, max_y)

    path = Path(__file__).parent / "grids"

    for t in range(10000):
        positions = get_positions(robots)

        image = Image.new("RGB", (max_y, max_x), "white")
        pixels = image.load()

        for i in range(max_x):
            for j in range(max_y):
                if (i, j) in positions:
                    pixels[j, i] = (0, 0, 0)

        image.save(f"{path}/grid_{t}.png")

        for i in range(len(robots)):
            robots[i] = robots[i].move()

    return None
