PRIME = 20201227


def load_public_keys():
    with open('input2.txt') as file:
        card_key = int(next(file))
        door_key = int(next(file))
    return card_key, door_key


def guess_loop_size(key: int):
    i = 0
    a = 1

    while a != key:
        a *= 7
        a %= PRIME
        i += 1
    return i


def transform(key: int, loop_size: int):
    return pow(key, loop_size, PRIME)


def part_one():
    card_pkey, door_pkey = load_public_keys()
    door_loop_size = guess_loop_size(door_pkey)
    encryption_key = transform(card_pkey, door_loop_size)
    print(encryption_key)


if __name__ == '__main__':
    part_one()
