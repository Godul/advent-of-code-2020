from itertools import product


MAP_SIZE = 400


def load_tiles():
    with open('input.txt') as file:
        return [line[:-1] for line in file]


def normalize_tile(tile: str):
    x = MAP_SIZE // 2
    y = MAP_SIZE // 2
    idx = 0

    while idx < len(tile):
        if tile[idx] == 'e':
            x += 2
        elif tile[idx] == 'w':
            x -= 2
        else:  # ne, nw, se or sw
            if tile[idx] == 'n':
                y += 1
            else:  # tile[idx] == 's'
                y -= 1

            idx += 1

            if tile[idx] == 'e':
                x += 1
            else:  # tile[idx] == 'w'
                x -= 1
        idx += 1
    return x, y


def part_one():
    tiles = [normalize_tile(tile) for tile in load_tiles()]
    floor = set()

    for tile in tiles:
        if tile in floor:
            floor.remove(tile)
        else:
            floor.add(tile)

    print(len(floor))


def count_neighbours(x: int, y: int, floor: list):
    count = 0
    for d_x, d_y in [(2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if not 0 <= x + d_x < MAP_SIZE or not 0 <= y + d_y < MAP_SIZE:
            continue
        if floor[x + d_x][y + d_y] == 1:
            count += 1
    return count


def copy_floor(floor: list):
    return [[floor[x][y] for y in range(MAP_SIZE)] for x in range(MAP_SIZE)]


def part_two():
    floor = [[0] * MAP_SIZE for _ in range(MAP_SIZE)]
    tiles = [normalize_tile(tile) for tile in load_tiles()]
    for x, y in tiles:
        floor[x][y] = 1 - floor[x][y]

    for _ in range(100):
        floor_copy = copy_floor(floor)

        for x, y in product(range(MAP_SIZE), range(MAP_SIZE)):
            neigh_num = count_neighbours(x, y, floor)

            if floor[x][y] == 1:
                if neigh_num == 0 or neigh_num > 2:
                    floor_copy[x][y] = 0
            else:  # floor[x][y] == 0
                if neigh_num == 2:
                    floor_copy[x][y] = 1

        floor = floor_copy

    result = sum(sum(floor[x]) for x in range(MAP_SIZE))
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
