from collections import defaultdict


def get_bag_id(feature: str, color: str):
    return f'{feature}_{color}'


def dfs_backward(bag: str, rules_backwards: dict, vis_bags: set):
    if bag in vis_bags:
        return
    vis_bags.add(bag)

    for outer_bag in rules_backwards[bag]:
        dfs_backward(outer_bag, rules_backwards, vis_bags)


def part_one():
    rules_backwards = defaultdict(list)
    vis_bags = set()

    with open('input.txt') as file:
        for line in file:
            rule = line.split()
            outer_bag = get_bag_id(rule[0], rule[1])

            if rule[4] == 'no':
                continue

            idx = 5
            while idx < len(rule):
                bag = get_bag_id(rule[idx], rule[idx + 1])
                rules_backwards[bag].append(outer_bag)
                idx += 4

    start_bag = get_bag_id('shiny', 'gold')
    dfs_backward(start_bag, rules_backwards, vis_bags)
    vis_bags.discard(start_bag)
    print(len(vis_bags))


def dfs_count(bag: str, rules: dict):
    result = 1
    for inner_bag, count in rules[bag]:
        result += count * dfs_count(inner_bag, rules)
    return result


def part_two():
    rules = defaultdict(list)

    with open('input.txt') as file:
        for line in file:
            rule = line.split()
            outer_bag = get_bag_id(rule[0], rule[1])

            if rule[4] == 'no':
                continue

            idx = 4
            while idx < len(rule):
                num_bags = int(rule[idx])
                inner_bag = get_bag_id(rule[idx + 1], rule[idx + 2])
                rules[outer_bag].append((inner_bag, num_bags))
                idx += 4

    start_bag = get_bag_id('shiny', 'gold')
    result = dfs_count(start_bag, rules) - 1
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
