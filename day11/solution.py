from itertools import product


def load_map():
    with open('input.txt') as file:
        return list(list(line[:-1]) for line in file)


def copy_map(seats: list):
    return [[seat for seat in row] for row in seats]


def has_n_occupied_adjacent(seats: list, i: int, j: int, n: int):
    count = 0

    for i_d, j_d in product((-1, 0, 1), (-1, 0, 1)):
        if i_d == j_d == 0:
            continue

        adj_i = i + i_d
        adj_j = j + j_d

        if 0 <= adj_i < len(seats) and 0 <= adj_j < len(seats[0]) and seats[i + i_d][j + j_d] == '#':
            count += 1
    return count >= n


def count_occupied(seats: list):
    result = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                result += 1
    return result


def part_one():
    seats = load_map()
    seats_copy = copy_map(seats)

    changed = True
    while changed:
        changed = False

        for i, j in product(range(len(seats)), range(len(seats[0]))):
            if seats[i][j] == 'L' and not has_n_occupied_adjacent(seats, i, j, 1):
                seats_copy[i][j] = '#'
                changed = True
            elif seats[i][j] == '#' and has_n_occupied_adjacent(seats, i, j, 4):
                seats_copy[i][j] = 'L'
                changed = True

        seats = seats_copy
        seats_copy = copy_map(seats)

    result = count_occupied(seats)
    print(result)


def has_n_visible_occupied(seats: list, i: int, j: int, n: int):
    count = 0

    for i_d, j_d in product((-1, 0, 1), (-1, 0, 1)):
        if i_d == j_d == 0:
            continue

        vis_i = i + i_d
        vis_j = j + j_d

        while 0 <= vis_i < len(seats) and 0 <= vis_j < len(seats[0]) and seats[vis_i][vis_j] == '.':
            vis_i += i_d
            vis_j += j_d

        if 0 <= vis_i < len(seats) and 0 <= vis_j < len(seats[0]) and seats[vis_i][vis_j] == '#':
            count += 1

    return count >= n


def part_two():
    seats = load_map()
    seats_copy = copy_map(seats)

    changed = True
    while changed:
        changed = False
        for i, j in product(range(len(seats)), range(len(seats[0]))):
            if seats[i][j] == 'L' and not has_n_visible_occupied(seats, i, j, 1):
                seats_copy[i][j] = '#'
                changed = True
            elif seats[i][j] == '#' and has_n_visible_occupied(seats, i, j, 5):
                seats_copy[i][j] = 'L'
                changed = True

        seats = seats_copy
        seats_copy = copy_map(seats)

    result = count_occupied(seats)
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
