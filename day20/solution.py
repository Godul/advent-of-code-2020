from collections import defaultdict
from itertools import product
from math import sqrt
from typing import (
    Callable,
    Dict,
    List,
)

from tile import Tile


def load_tiles(filename: str):
    tiles = []
    with open(filename) as file:
        tile_id = None
        board = None

        for line in file:
            if line == '\n':
                tiles.append(Tile(tile_id, board))
            elif line[:4] == 'Tile':
                tile_id = int(line[5:-2])
                board = []
            else:
                board.append(line[:-1])
    return tiles


def has_fitting_candidate(tile: Tile, fit_func: Callable[['Tile', 'Tile'], bool], candidates: List[Tile]):
    for i, cand in enumerate(candidates):
        for cand_trans in cand.transformations():
            if fit_func(tile, cand_trans):
                candidates.pop(i)
                return True
    return False


def count_candidates(tiles: list):
    result = defaultdict(list)

    for i, tile in enumerate(tiles):
        candidates = tiles[:i] + tiles[i+1:]
        neigh_count = 0
        for fit_func in [Tile.fits_top, Tile.fits_right, Tile.fits_bottom, Tile.fits_left]:
            if has_fitting_candidate(tile, fit_func, candidates):
                neigh_count += 1

        result[neigh_count].append(tile)
    return result


def arrange_first_row(count_dict: Dict[int, List[Tile]], board: List[List[Tile]], first_tile: Tile):
    # Upper left corner
    board[0][0] = first_tile

    # Upper edge
    for i in range(0, len(board) - 2):
        for j, cand in enumerate(count_dict[3]):
            transformed = cand.transform_to_fit([board[0][i]], [Tile.fits_left])
            if transformed:
                count_dict[3].pop(j)
                board[0][i + 1] = transformed
                break

    # Upper right corner
    for i, cand in enumerate(count_dict[2]):
        transformed = cand.transform_to_fit([board[0][-2]], [Tile.fits_left])
        if transformed:
            count_dict[2].pop(i)
            board[0][-1] = transformed
            break


def arrange_nth_row(count_dict: Dict[int, List[Tile]], board: List[List[Tile]], n: int):
    # Left edge
    for i, cand in enumerate(count_dict[3]):
        transformed = cand.transform_to_fit([board[n - 1][0]], [Tile.fits_top])
        if transformed:
            count_dict[3].pop(i)
            board[n][0] = transformed
            break

    # Middle cells
    for i in range(1, len(board) - 1):
        for j, cand in enumerate(count_dict[4]):
            transformed = cand.transform_to_fit([board[n - 1][i], board[n][i - 1]], [Tile.fits_top, Tile.fits_left])
            if transformed:
                count_dict[4].pop(j)
                board[n][i] = transformed
                break

    # Right edge
    for i, cand in enumerate(count_dict[3]):
        transformed = cand.transform_to_fit([board[n - 1][-1], board[n][-2]], [Tile.fits_top, Tile.fits_left])
        if transformed:
            count_dict[3].pop(i)
            board[n][-1] = transformed
            break


def arrange_last_row(count_dict: Dict[int, List[Tile]], board: List[List[Tile]]):
    # Bottom left corner
    for i, cand in enumerate(count_dict[2]):
        transformed = cand.transform_to_fit([board[-2][0]], [Tile.fits_top])
        if transformed:
            count_dict[2].pop(i)
            board[-1][0] = transformed
            break

    # Bottom edge
    for i in range(1, len(board) - 1):
        for j, cand in enumerate(count_dict[3]):
            transformed = cand.transform_to_fit([board[-1][i - 1], board[-2][i]], [Tile.fits_left, Tile.fits_top])
            if transformed:
                count_dict[3].pop(j)
                board[-1][i] = transformed
                break

    # Bottom right corner
    for i, cand in enumerate(count_dict[2]):
        transformed = cand.transform_to_fit([board[-1][-2]], [Tile.fits_left])
        if transformed:
            count_dict[2].pop(i)
            board[-1][-1] = transformed
            break


def arrange_board(tiles: List[Tile], board: List[List[Tile]]):
    count_dict = count_candidates(tiles)
    tile = count_dict[2].pop()

    for rotation in tile.rotations():
        count_dict = count_candidates(tiles)
        count_dict[2].pop()

        try:
            arrange_first_row(count_dict, board, rotation)
            for n in range(1, len(board) - 1):
                arrange_nth_row(count_dict, board, n)
            arrange_last_row(count_dict, board)
        except AttributeError:
            continue
        return board


def solve(tiles: List[Tile]):
    board_len = round(sqrt(len(tiles)))
    board = [[None] * board_len for _ in range(board_len)]
    arrange_board(tiles, board)
    return board


def load_monster():
    with open('monster.txt') as file:
        return Tile(-1, [line[:-1] for line in file])


def convert_to_image(board: List[List[Tile]]):
    image = []
    for i in range(len(board)):
        for j in range(1, 9):
            image_row = []
            for k in range(len(board[0])):
                for w in range(1, 9):
                    image_row.append(board[i][k].board[j][w])
            image.append(image_row)
    return image


def matches_monster(image: List[List[str]], i: int, j: int, monster_board: List[str]):
    for di, dj in product(range(len(monster_board)), range(len(monster_board[0]))):
        if not 0 <= i + di < len(image) or not 0 <= j + dj < len(image[0]):
            return False
        if monster_board[di][dj] == '#' and image[i + di][j + dj] == '.':
            return False
    return True


def mark_monster(image: List[List[str]], i: int, j: int, monster_board: List[str]):
    for di, dj in product(range(len(monster_board)), range(len(monster_board[0]))):
        if monster_board[di][dj] == '#':
            image[i + di][j + dj] = 'O'


def mark_monsters(image: List[List[str]], monster: Tile):
    for i, j in product(range(len(image)), range(len(image[0]))):
        for monster_trans in monster.transformations():
            if matches_monster(image, i, j, monster_trans.board):
                mark_monster(image, i, j, monster_trans.board)
    return sum(sum(1 for cell in row if cell == '#') for row in image)


def count_hashes(image: List[List[str]]):
    return sum(sum(1 for cell in row if cell == '#') for row in image)


def both_parts():
    tiles = load_tiles('input.txt')
    board = solve(tiles)
    print(board[0][0].tile_id * board[0][-1].tile_id * board[-1][0].tile_id * board[-1][-1].tile_id)

    image = convert_to_image(board)
    monster = load_monster()
    mark_monsters(image, monster)
    print(count_hashes(image))


if __name__ == '__main__':
    both_parts()
