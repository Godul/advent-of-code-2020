from copy import deepcopy
from typing import (
    Callable,
    List,
)


class Tile:
    def __init__(self, tile_id: int, board: List[str]):
        self.tile_id = tile_id
        self.board = board

    def left_edge(self):
        return ''.join(row[0] for row in self.board)

    def right_edge(self):
        return ''.join(row[-1] for row in self.board)

    def top_edge(self):
        return self.board[0]

    def bottom_edge(self):
        return self.board[-1]

    def flip(self):
        for i in range(len(self.board)):
            self.board[i] = ''.join(reversed(self.board[i]))

    def rotate(self):
        temp = self.board
        self.board = []
        for i in range(len(temp[0])):
            self.board.append(''.join(row[i] for row in reversed(temp)))

    def flip_copy(self):
        res = deepcopy(self)
        res.flip()
        return res

    def rotate_copy(self):
        res = deepcopy(self)
        res.rotate()
        return res

    def rotations(self):
        cur = deepcopy(self)
        for i in range(4):
            yield cur
            cur = cur.rotate_copy()

    def transformations(self):
        for rotation in self.rotations():
            yield rotation
            yield rotation.flip_copy()

    def fits_right(self, other: 'Tile'):
        if self.right_edge() == other.left_edge():
            return True
        return False

    def fits_left(self, other: 'Tile'):
        if self.left_edge() == other.right_edge():
            return True
        return False

    def fits_top(self, other: 'Tile'):
        if self.top_edge() == other.bottom_edge():
            return True
        return False

    def fits_bottom(self, other: 'Tile'):
        if self.bottom_edge() == other.top_edge():
            return True
        return False

    def transform_to_fit(self, neighbours: List['Tile'], fit_functions: List[Callable[['Tile', 'Tile'], bool]]):
        for trans in self.transformations():
            ok = True
            for neigh, fit_func in zip(neighbours, fit_functions):
                if not fit_func(trans, neigh):
                    ok = False
                    break
            if ok:
                return trans
        return None

    def __str__(self):
        return f'Tile({self.tile_id})'
