from math import (
    gcd,
    inf,
)


def load_input():
    with open('input.txt') as file:
        ts = int(next(file))
        buses = []
        for idx, bus_id in enumerate(next(file).split(',')):
            if bus_id != 'x':
                buses.append((idx, int(bus_id)))
        return ts, buses


def part_one():
    ts, buses = load_input()
    min_wait_time = inf
    min_id = None

    for _, bus_id in buses:
        wait_time = bus_id - ts % bus_id if ts % bus_id != 0 else 0

        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_id = bus_id

    print(min_id * min_wait_time)


def lcd(a: int, b: int):
    return a * b // gcd(a, b)


def calculate_partial_lcds(buses: list):
    partial_lcds = [1]
    for _, bus_id in buses:
        partial_lcds.append(lcd(partial_lcds[-1], bus_id))
    return partial_lcds


def part_two():
    _, buses = load_input()
    partial_lcds = calculate_partial_lcds(buses)
    ts = 0

    for (idx, bus_id), partial_lcd in zip(buses, partial_lcds):
        while (ts + idx) % bus_id != 0:
            ts += partial_lcd

    print(ts)


if __name__ == '__main__':
    part_one()
    part_two()
