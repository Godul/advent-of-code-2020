from collections import defaultdict
from typing import (
    Dict,
    List,
    Set,
    Tuple,
)


def load_data(filename: str):
    result = []
    with open(filename) as file:
        for line in file:
            products, allergens = line.split('(')
            products = products.split()
            allergens = allergens.split(', ')
            allergens[0] = allergens[0].split(' ')[1]
            allergens[-1] = allergens[-1][:-2]
            result.append((products, allergens))
    return result


def calc_possible_dict(food_list: List[Tuple[List[str], List[str]]]):
    possible_dict = {}

    for products, allergens in food_list:
        for allergen in allergens:
            if allergen not in possible_dict:
                possible_dict[allergen] = set(products)
            else:
                possible_dict[allergen].intersection_update(products)

    return possible_dict


def find_safe_ingredients(food_list: List[Tuple[List[str], List[str]]]):
    product_set = set()
    for products, _ in food_list:
        product_set.update(products)

    possible_set = calc_possible_dict(food_list)

    for endangered_products in possible_set.values():
        product_set.difference_update(endangered_products)

    return product_set


def count_safe_ingredient_occurrences(safe_products: Set[str], food_list: List[Tuple[List[str], List[str]]]):
    count_dict = defaultdict(int)
    for products, _ in food_list:
        for product in products:
            if product in safe_products:
                count_dict[product] += 1
    return sum(count_dict.values())


def part_one():
    food_list = load_data('input.txt')
    safe_ingredients = find_safe_ingredients(food_list)
    result = count_safe_ingredient_occurrences(safe_ingredients, food_list)
    print(result)


def find_canonical_dangerous(possible_dict: Dict[str, Set[str]]):
    not_finished = True
    while not_finished:
        not_finished = False

        for product, allergen_set in possible_dict.items():
            if len(allergen_set) != 1:
                not_finished = True
                continue

            allergen = next(iter(allergen_set))
            for product, allergen_set in possible_dict.items():
                if len(allergen_set) > 1:
                    allergen_set.discard(allergen)

    return ','.join(next(iter(allergen_set)) for product, allergen_set in sorted(possible_dict.items()))


def part_two():
    food_list = load_data('input.txt')
    possible_dict = calc_possible_dict(food_list)
    canonical_list = find_canonical_dangerous(possible_dict)
    print(canonical_list)


if __name__ == '__main__':
    part_one()
    part_two()
