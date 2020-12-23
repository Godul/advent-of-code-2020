def load_input():
    with open('input.txt') as file:
        return list(map(int, next(file).split(',')))


def get_nth_number(start_numbers: list, n: int):
    occurrences = {number: idx for idx, number in enumerate(start_numbers[:-1])}
    last = start_numbers[-1]

    for i in range(len(start_numbers) - 1, n - 1):
        if last in occurrences:
            dist = i - occurrences[last]
            occurrences[last] = i
            last = dist
        else:
            occurrences[last] = i
            last = 0
    return last


def both_parts():
    start_numbers = load_input()

    part_one = get_nth_number(start_numbers, 2020)
    print(part_one)

    part_two = get_nth_number(start_numbers, 30000000)
    print(part_two)


if __name__ == '__main__':
    both_parts()
