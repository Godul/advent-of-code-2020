from itertools import product
from typing import Union


def parse_rule(line: str):
    line = line.split(':')
    rule_idx = int(line[0])
    rule = []
    for fork in line[1][1:-1].split('|'):
        rule.append([token[1] if token[0] == '"' else int(token) for token in fork.split()])
    return rule_idx, rule


def load_data(filename: str):
    rules = {}
    words = []

    with open(filename) as file:
        for line in file:
            if line == '\n':
                break

            rule_idx, rule = parse_rule(line)
            rules[rule_idx] = rule

        for line in file:
            words.append(line[:-1])

    return rules, words


def generate_words(rules: dict, rule_n: Union[int, str]):
    if isinstance(rule_n, str):
        return [rule_n]

    res = []
    for fork in rules[rule_n]:
        to_product = []
        for n in fork:
            to_product.append(generate_words(rules, n))
        for to_join in product(*to_product):
            res.append(''.join(to_join))

    return res


def part_one():
    rules, words = load_data('input.txt')
    good_set = set(generate_words(rules, 0))
    result = sum(1 for word in words if word in good_set)
    print(result)


def is_8(word: str, set_42: set, subword_length: int):
    for i in range(0, len(word), subword_length):
        if word[i:i+subword_length] not in set_42:
            return False
    return True


def is_11(word: str, set_42: set, set_31: set, subword_length: int):
    for i in range(0, len(word) // 2, subword_length):
        if word[i:i+subword_length] not in set_42:
            return False
    for i in range(len(word) // 2, len(word), subword_length):
        if word[i:i+subword_length] not in set_31:
            return False
    return True


def is_8_11(word: str, set_42: set, set_31: set, subword_length: int):
    if len(word) % subword_length:
        print(f'bad length {len(word)}: {word}')
        return False

    for i in range(subword_length, len(word), subword_length):
        if is_8(word[:i], set_42, subword_length) and is_11(word[i:], set_42, set_31, subword_length):
            return True
    return False


def part_two():
    rules, words = load_data('input.txt')
    set_42 = set(generate_words(rules, 42))
    set_31 = set(generate_words(rules, 31))
    result = sum(1 for word in words if is_8_11(word, set_42, set_31, subword_length=8))
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
