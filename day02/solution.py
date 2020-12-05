def load_input():
    input_list = []
    with open('input.txt') as file:
        for line in file:
            line = line.split()
            r = map(int, line[0].split('-'))
            letter = line[1][0]
            password = line[2]
            input_list.append((r, letter, password))
    return input_list


def part_1():
    result = 0
    for (min_occ, max_occ), letter, password in load_input():
        occ = sum(1 for c in password if c == letter)
        if min_occ <= occ <= max_occ:
            result += 1
    print(result)


def part_2():
    result = 0
    for (pos_1, pos_2), letter, password in load_input():
        char_1 = password[pos_1 - 1]
        char_2 = password[pos_2 - 1]
        if char_1 != char_2 and (char_1 == letter or char_2 == letter):
            result += 1
    print(result)


if __name__ == '__main__':
    part_1()
    part_2()
