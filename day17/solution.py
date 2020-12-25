from copy import deepcopy
from itertools import product


MAX_X = 20
MAX_Y = 20
MAX_Z = 13
MAX_W = 13


def load_data():
    with open('input.txt') as file:
        return [list(line[:-1]) for line in file]


def initialize_state(initial_slice: list):
    state = [[[0] * MAX_Z for _ in range(MAX_Y)] for _ in range(MAX_X)]

    for x, y in product(range(len(initial_slice)), range(len(initial_slice[0]))):
        mid_x = x - len(initial_slice) // 2
        mid_y = y - len(initial_slice[0]) // 2
        state[MAX_X // 2 + mid_x][MAX_Y // 2 + mid_y][MAX_Z // 2] = 1 if initial_slice[x][y] == '#' else 0

    return state


def move_state(source_state: list, dest_state: list):
    for x, y, z in product(range(MAX_X), range(MAX_Y), range(MAX_Z)):
        dest_state[x][y][z] = source_state[x][y][z]


def count_active_neighbours(state: list, x: int, y: int, z: int):
    active_num = 0
    for d_x, d_y, d_z in product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1)):
        if d_x == d_y == d_z == 0:
            continue
        if not 0 <= x + d_x < MAX_X:
            continue
        if not 0 <= y + d_y < MAX_Y:
            continue
        if not 0 <= z + d_z < MAX_Z:
            continue
        active_num += state[x + d_x][y + d_y][z + d_z]
    return active_num


def count_active(state: list):
    return sum(state[x][y][z] for x in range(MAX_X) for y in range(MAX_Y) for z in range(MAX_Z))


def part_one():
    initial_slice = load_data()
    state = initialize_state(initial_slice)
    state_copy = deepcopy(state)

    for _ in range(6):
        for x, y, z in product(range(MAX_X), range(MAX_Y), range(MAX_Z)):
            active_num = count_active_neighbours(state, x, y, z)

            if state[x][y][z] == 1 and active_num != 2 and active_num != 3:
                state_copy[x][y][z] = 0
            elif state[x][y][z] == 0 and active_num == 3:
                state_copy[x][y][z] = 1

        move_state(state_copy, state)

    result = count_active(state)
    print(result)


def initialize_state_2(initial_slice: list):
    state = [[[[0] * MAX_W for _ in range(MAX_Z)] for _ in range(MAX_Y)] for _ in range(MAX_X)]

    for x, y in product(range(len(initial_slice)), range(len(initial_slice[0]))):
        mid_x = x - len(initial_slice) // 2
        mid_y = y - len(initial_slice[0]) // 2
        state[MAX_X // 2 + mid_x][MAX_Y // 2 + mid_y][MAX_Z // 2][MAX_Z // 2] = 1 if initial_slice[x][y] == '#' else 0

    return state


def move_state_2(source_state: list, dest_state: list):
    for x, y, z, w in product(range(MAX_X), range(MAX_Y), range(MAX_Z), range(MAX_W)):
        dest_state[x][y][z][w] = source_state[x][y][z][w]


def count_active_neighbours_2(state: list, x: int, y: int, z: int, w: int):
    active_num = 0
    for d_x, d_y, d_z, d_w in product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1), (-1, 0, 1)):
        if d_x == d_y == d_z == d_w == 0:
            continue
        if not 0 <= x + d_x < MAX_X:
            continue
        if not 0 <= y + d_y < MAX_Y:
            continue
        if not 0 <= z + d_z < MAX_Z:
            continue
        if not 0 <= w + d_w < MAX_W:
            continue
        active_num += state[x + d_x][y + d_y][z + d_z][w + d_w]
    return active_num


def count_active_2(state: list):
    return sum(state[x][y][z][w] for x in range(MAX_X) for y in range(MAX_Y) for z in range(MAX_Z) for w in range(MAX_W))


def part_two():
    initial_slice = load_data()
    state = initialize_state_2(initial_slice)
    state_copy = deepcopy(state)

    for _ in range(6):
        for x, y, z, w in product(range(MAX_X), range(MAX_Y), range(MAX_Z), range(MAX_W)):
            active_num = count_active_neighbours_2(state, x, y, z, w)

            if state[x][y][z][w] == 1 and active_num != 2 and active_num != 3:
                state_copy[x][y][z][w] = 0
            elif state[x][y][z][w] == 0 and active_num == 3:
                state_copy[x][y][z][w] = 1

        move_state_2(state_copy, state)

    result = count_active_2(state)
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
