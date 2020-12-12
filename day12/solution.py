from math import (
    atan2,
    cos,
    degrees,
    radians,
    sin,
    sqrt,
)


def load_instructions():
    with open('input.txt') as file:
        return [(line[0], int(line[1:-1])) for line in file]


def get_deltas(action: str, value: int):
    dir_x, dir_y = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0),
    }[action]
    return dir_x * value, dir_y * value


def get_angle_delta(action: str, value: int):
    direction = 1 if action == 'L' else -1
    return value * direction


def calculate_angle(x: float, y: float):
    return degrees(atan2(y, x))


def calculate_cords(angle: float, dist: float):
    return cos(radians(angle)) * dist, sin(radians(angle)) * dist


def manhattan_dist(x1: float, y1: float, x2: float, y2: float):
    return abs(x1 - x2) + abs(y1 - y2)


def part_one():
    instructions = load_instructions()
    x, y = 0, 0
    angle = 0

    for action, value in instructions:
        if action in 'NSEW':
            dx, dy = get_deltas(action, value)
            x += dx
            y += dy
        elif action in 'LR':
            angle += get_angle_delta(action, value)
        elif action == 'F':
            dx, dy = calculate_cords(angle, value)
            x += dx
            y += dy
        else:
            raise NotImplementedError

    print(round(manhattan_dist(0, 0, x, y)))


def part_two():
    instructions = load_instructions()
    x, y = 0, 0
    w_x, w_y = 10, 1  # Waypoint coordinates
    angle = degrees(atan2(w_y, w_x))

    for action, value in instructions:
        if action in 'NSEW':
            dx, dy = get_deltas(action, value)
            w_x += dx
            w_y += dy
            angle = calculate_angle(w_x, w_y)
        elif action in 'LR':
            angle += get_angle_delta(action, value)
            dist = sqrt(w_x * w_x + w_y * w_y)
            w_x, w_y = calculate_cords(angle, dist)
        elif action == 'F':
            x += w_x * value
            y += w_y * value
        else:
            raise NotImplementedError

    print(round(manhattan_dist(0, 0, x, y)))


if __name__ == '__main__':
    part_one()
    part_two()
