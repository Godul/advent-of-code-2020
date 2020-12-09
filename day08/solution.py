def load_program():
    program = []
    with open('input.txt') as file:
        for line in file:
            line = line.split()
            program.append((line[0], int(line[1])))
    return program


def run_till_loop(program: list):
    vis = [False] * len(program)
    acc = 0
    ip = 0

    while not vis[ip]:
        vis[ip] = True
        instr, value = program[ip]
        if instr == 'nop':
            ip += 1
        elif instr == 'acc':
            acc += value
            ip += 1
        else:
            ip += value
    return acc


def part_one():
    program = load_program()
    acc = run_till_loop(program)
    print(acc)


def find_beginning(program: list):
    vis = set()
    ip = 0

    while ip not in vis:
        vis.add(ip)
        instr, value = program[ip]
        if instr == 'nop' or instr == 'acc':
            ip += 1
        else:
            ip += value
    return vis


def find_ending(program: list):
    vis = {len(program)}
    changed = True

    while changed:
        changed = False
        for ip in range(len(program) - 1, -1, -1):
            if ip in vis:
                continue

            instr, value = program[ip]

            if (instr == 'nop' or instr == 'acc') and ip + 1 in vis:
                vis.add(ip)
                changed = True
                continue

            if instr == 'jmp' and ip + value in vis:
                vis.add(ip)
                changed = True
                continue
    return vis


def find_corrupted_line(program: list, beginning: set, ending: set):
    for ip in beginning:
        instr, value = program[ip]
        if instr == 'nop':
            if ip + value in ending:
                return ip
        elif instr == 'jmp':
            if ip + 1 in ending:
                return ip


def fix_program(program: list, bad_ip: int):
    instr, value = program[bad_ip]
    program[bad_ip] = ('nop', value) if instr == 'jmp' else ('jmp', value)


def run_program(program: list):
    ip = 0
    acc = 0
    while ip != len(program):
        instr, value = program[ip]
        if instr == 'nop':
            ip += 1
        elif instr == 'acc':
            acc += value
            ip += 1
        else:
            ip += value
    return acc


def part_two():
    program = load_program()
    beginning = find_beginning(program)
    ending = find_ending(program)
    bad_ip = find_corrupted_line(program, beginning, ending)
    fix_program(program, bad_ip)
    acc = run_program(program)
    print(acc)


if __name__ == '__main__':
    part_one()
    part_two()
