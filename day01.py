def load_numbers():
    with open('inputs/input1.txt', 'r') as file:
        return list(map(int, file))


def part_1():
    numbers = set(load_numbers())

    for n in numbers:
        if 2020 - n in numbers:
            print(n * (2020 - n))


def part_2():
    numbers = load_numbers()
    numbers_set = set(numbers)

    for i in range(len(numbers)):
        for j in range(i):
            candidate = 2020 - numbers[i] - numbers[j]
            if candidate in numbers_set:
                print(numbers[i] * numbers[j] * candidate)


if __name__ == '__main__':
    part_2()
