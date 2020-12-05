import re


def is_year_between(input_str: str, min_year: int, max_year: int):
    if re.fullmatch('[0-9]{4}', input_str) is None:
        return False

    if int(input_str) < min_year or max_year < int(input_str):
        return False
    return True


def is_valid_height(input_str: str):
    if re.fullmatch('[0-9]{2,3}(in|cm)', input_str) is None:
        return False

    value = int(input_str[:-2])
    unit = input_str[-2:]

    if unit == 'cm' and (value < 150 or 193 < value):
        return False

    if unit == 'in' and (value < 59 or 76 < value):
        return False

    return True


def is_valid_color(input_str: str):
    return re.fullmatch('#[a-f0-9]{6}', input_str) is not None


def is_valid_hair_color(input_str: str):
    return input_str in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_valid_pid(input_str: str):
    return re.fullmatch('[0-9]{9}', input_str) is not None


def are_values_valid(data: dict):
    if not is_year_between(data['byr'], min_year=1920, max_year=2002):
        return False

    if not is_year_between(data['iyr'], min_year=2010, max_year=2020):
        return False

    if not is_year_between(data['eyr'], min_year=2020, max_year=2030):
        return False

    if not is_valid_height(data['hgt']):
        return False

    if not is_valid_color(data['hcl']):
        return False

    if not is_valid_hair_color(data['ecl']):
        return False

    if not is_valid_pid(data['pid']):
        return False

    return True


def has_required_fields(data: dict):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return len(required_keys.difference(data.keys())) == 0


def both_parts():
    num_valid_1 = 0
    num_valid_2 = 0
    data = {}

    with open('inputs/input4.txt') as file:
        for line in file:
            if line == '\n':
                if not has_required_fields(data):
                    data.clear()
                    continue

                num_valid_1 += 1

                if are_values_valid(data):
                    num_valid_2 += 1

                data.clear()
                continue

            for entry in line[:-1].split():
                key, val = entry.split(':')
                data[key] = val

    print(num_valid_1)
    print(num_valid_2)


if __name__ == '__main__':
    both_parts()
