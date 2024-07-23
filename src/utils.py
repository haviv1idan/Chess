from enum import Enum


CHESS_BOARD = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]


ROWS: tuple[int] = (8, 7, 6, 5, 4, 3, 2, 1)
COLS: tuple[str] = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Color(Enum):
    WHITE = 0
    BLACK = 1


def convert_chess_square_to_board_index(chess_square: str) -> tuple[int, int]:
    """convert chess square to board index.
    for example: a8 -> (0,0)

    Args:
        chess_square (tuple[int, int]): tuple of row and col board indexs
    """
    col, row = chess_square
    print(f"{col= }, {row= }")
    return COLS.index(col), ROWS.index(int(row))