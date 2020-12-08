QUESTIONS = list(map(chr, range(ord('a'), ord('z') + 1)))


def both_parts():
    anyone_set = set()
    everyone_set = set(QUESTIONS)
    anyone_count = 0
    everyone_count = 0

    with open('input.txt') as file:
        for line in file:
            if line == '\n':
                anyone_count += len(anyone_set)
                everyone_count += len(everyone_set)
                anyone_set.clear()
                everyone_set.update(QUESTIONS)
                continue

            anyone_set.update(line[:-1])
            everyone_set.intersection_update(line[:-1])
    print(anyone_count)
    print(everyone_count)


if __name__ == '__main__':
    both_parts()
