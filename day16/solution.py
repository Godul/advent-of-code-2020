from collections import defaultdict
from functools import reduce


def load_data():
    with open('input.txt') as file:
        rules = {}
        line = next(file).split()
        while line:
            name = ' '.join(line[:-3])[:-1]
            min_1, max_1 = map(int, line[-3].split('-'))
            min_2, max_2 = map(int, line[-1].split('-'))
            rules[name] = min_1, max_1, min_2, max_2
            line = next(file).split()

        next(file)
        line = next(file)
        ticket = list(map(int, line.split(',')))

        next(file), next(file)

        nearby_tickets = []
        for line in file:
            values = list(map(int, line.split(',')))
            nearby_tickets.append(values)

    return rules, ticket, nearby_tickets


def is_valid_value(value: int, rules: dict):
    for min_1, max_1, min_2, max_2 in rules.values():
        if min_1 <= value <= max_1 or min_2 <= value <= max_2:
            return True
    return False


def is_valid_ticket(ticket: list, rules: dict):
    for value in ticket:
        if not is_valid_value(value, rules):
            return False
    return True


def part_one():
    rules, _, nearby_tickets = load_data()

    res = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not is_valid_value(value, rules):
                res += value
    print(res)


def satisfy_rule(values: list, rule: tuple):
    name, (min_1, max_1, min_2, max_2) = rule
    for value in values:
        if not min_1 <= value <= max_1 and not min_2 <= value <= max_2:
            return False
    return True


def match_rules_with_columns(tickets: list, rules: dict):
    match_dict = defaultdict(set)
    assignment = {}

    for i in range(len(tickets[0])):
        values = [ticket[i] for ticket in tickets]
        for rule in rules.items():
            if satisfy_rule(values, rule):
                match_dict[rule[0]].add(i)

    while True:
        for name, possible_set in match_dict.items():
            i = next(iter(possible_set))
            if len(possible_set) == 1:
                break
        else:
            break

        del match_dict[name]
        assignment[name] = i

        for possible_set in match_dict.values():
            possible_set.discard(i)

    return assignment


def part_two():
    rules, my_ticket, tickets = load_data()
    tickets = [ticket for ticket in tickets if is_valid_ticket(ticket, rules)]
    tickets.append(my_ticket)
    assignment = match_rules_with_columns(tickets, rules)
    result_values = (my_ticket[i] for name, i in assignment.items() if name.startswith('departure'))
    result = reduce(lambda x, y: x * y, result_values)
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
