from functools import reduce


def part_1():
    num_trees = 0
    x = 0

    with open('day03/input.txt') as file:
        for line in file:
            if line[x] == '#':
                num_trees += 1
            x = (x + 3) % (len(line) - 1)
    print(num_trees)


def part_2():
    moves = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    xs = [0] * len(moves)
    results = [0] * len(moves)

    with open('day03/input.txt') as file:
        for y, line in enumerate(file):
            for i, (x_d, y_d) in enumerate(moves):
                if y % y_d != 0:
                    continue

                if line[xs[i]] == '#':
                    results[i] += 1

                xs[i] = (xs[i] + x_d) % (len(line) - 1)
    print(reduce(lambda x, y: x * y, results))


if __name__ == '__main__':
    part_1()
    part_2()
