def calculate_id(input_str: str):
    min_row = 0
    max_row = 127

    for a in input_str[:7]:
        if a == 'F':
            max_row = (max_row + min_row) // 2
        else:
            min_row = (max_row + min_row + 1) // 2

    min_col = 0
    max_col = 7
    for a in input_str[7:10]:
        if a == 'L':
            max_col = (max_col + min_col) // 2
        else:
            min_col = (max_col + min_col + 1) // 2

    return 8 * min_row + min_col


def get_ids():
    with open('input.txt') as file:
        return list(map(calculate_id, file))


def part_1():
    ids = get_ids()
    print(max(ids))


def part_2():
    ids = get_ids()
    free_seats = set(range(0, 1024)).difference(ids)

    for seat_id in free_seats:
        if seat_id - 1 not in free_seats and seat_id + 1 not in free_seats:
            print(seat_id)


if __name__ == '__main__':
    part_1()
    part_2()
