from typing import (
    Deque,
    Set,
    Tuple,
)
from collections import deque


def load_data(filename: str):
    deck_1 = deque()
    deck_2 = deque()

    with open(filename) as file:
        next(file)
        for line in file:
            if line == '\n':
                break
            deck_1.append(int(line))
        next(file)
        for line in file:
            if line == '\n':
                break
            deck_2.append(int(line))
    return deck_1, deck_2


def play_game(deck_1: Deque[int], deck_2: Deque[int]):
    while deck_1 and deck_2:
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()
        if card_1 > card_2:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)


def calculate_score(deck_1: Deque[int], deck_2: Deque[int]):
    winner_deck = deck_1 if deck_1 else deck_2
    score = 0
    for multiplier, card in enumerate(reversed(winner_deck), 1):
        score += multiplier * card
    return score


def part_one():
    deck_1, deck_2 = load_data('input.txt')
    play_game(deck_1, deck_2)
    score = calculate_score(deck_1, deck_2)
    print(score)


def get_conf(deck_1: Deque[int], deck_2: Deque[int]):
    return tuple(deck_1), tuple(deck_2)


def play_game_2(deck_1: Deque[int], deck_2: Deque[int], cache: Set[Tuple]):
    while deck_1 and deck_2:
        conf = get_conf(deck_1, deck_2)
        if conf in cache:
            return 1
        cache.add(conf)

        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()

        if card_1 > len(deck_1) or card_2 > len(deck_2):
            winner = 1 if card_1 > card_2 else 2
        else:
            winner = play_game_2(deque(list(deck_1)[:card_1]), deque(list(deck_2)[:card_2]), set(cache))

        if winner == 1:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)

    return 1 if deck_1 else 2


def part_two():
    deck_1, deck_2 = load_data('input.txt')
    play_game_2(deck_1, deck_2, set())
    score = calculate_score(deck_1, deck_2)
    print(score)


if __name__ == '__main__':
    part_one()
    part_two()
