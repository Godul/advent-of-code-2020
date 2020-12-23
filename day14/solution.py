WORD_LEN = 36


def load_program():
    program = []
    with open('input.txt') as file:
        for line in file:
            if line[:4] == 'mask':
                program.append((line.split()[2],))
            else:  # line[:3] == mem
                line = line.split()
                program.append((int(line[0][4:-1]), int(line[2])))
    return program


def val_to_list(val: int):
    result = bin(val)[2:]
    return [0] * (WORD_LEN - len(result)) + list(map(int, result))


def list_to_val(addr_list: list):
    return int(''.join(map(str, addr_list)), 2)


def apply_mask(val: int, mask: str):
    val_list = val_to_list(val)

    for i in range(len(mask)):
        if mask[i] == '1':
            val_list[i] = 1
        elif mask[i] == '0':
            val_list[i] = 0

    return list_to_val(val_list)


def part_one():
    program = load_program()
    mem = {}
    mask = None

    for line in program:
        if len(line) == 1:
            mask = line[0]
        else:
            idx, val = line
            mem[idx] = apply_mask(val, mask)

    print(sum(mem.values()))


def gen_all_addresses_h(addr_list: list, mask: str, pos: int):
    if pos == len(mask):
        yield list_to_val(addr_list)
    elif mask[pos] == '1':
        addr_list[pos] = 1
        yield from gen_all_addresses_h(addr_list, mask, pos + 1)
    elif mask[pos] == 'X':
        addr_list[pos] = 0
        yield from gen_all_addresses_h(addr_list, mask, pos + 1)
        addr_list[pos] = 1
        yield from gen_all_addresses_h(addr_list, mask, pos + 1)
    elif mask[pos] == '0':
        yield from gen_all_addresses_h(addr_list, mask, pos + 1)


def gen_all_addresses(idx: int, mask: str):
    addr_list = val_to_list(idx)
    yield from gen_all_addresses_h(addr_list, mask, 0)


def write_many(idx: int, val: int, mask: str, mem: dict):
    for addr in gen_all_addresses(idx, mask):
        mem[addr] = val


def part_two():
    program = load_program()
    mem = {}
    mask = None

    for line in program:
        if len(line) == 1:
            mask = line[0]
        else:
            idx, val = line
            write_many(idx, val, mask, mem)

    print(sum(mem.values()))


if __name__ == '__main__':
    part_one()
    part_two()
