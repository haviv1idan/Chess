from enum import Enum
from typing import Any
from src.player import Player
from src.piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class Board:

    def __init__(self, w_player: Player, b_player: Player):
        self.white_player = w_player or Player(name='white_player')
        self.black_player = b_player or Player(name='black_player')
        self.board: list[list[object]] = self._setup_board()

    def __call__(self) -> list[list[object]]:
        return self.board


    def _setup_board() -> list[list[object]]:
        return \
        [
            [   # First row of board - Black pieces
                Square(column=8, row='a', piece=Rook()),
                Square(column=8, row='b', piece=Knight()),
                Square(column=8, row='c', piece=Bishop()),
                Square(column=8, row='d', piece=Queen()),
                Square(column=8, row='e', piece=King()),
                Square(column=8, row='f', piece=Bishop()),
                Square(column=8, row='g', piece=Knight()),
                Square(column=8, row='h', piece=Rook())
            ],
            [   # Second row of board - Black Pawns
                Square(column=7, row='a', piece=Pawn()),
                Square(column=7, row='b', piece=Pawn()),
                Square(column=7, row='c', piece=Pawn()),
                Square(column=7, row='d', piece=Pawn()),
                Square(column=7, row='e', piece=Pawn()),
                Square(column=7, row='f', piece=Pawn()),
                Square(column=7, row='g', piece=Pawn()),
                Square(column=7, row='h', piece=Pawn()),
            ],
                # Rows 6 - 3 are empty 
            [Square(column=6, row=row, piece=None) for row in 'abcdefgh'],
            [Square(column=5, row=row, piece=None) for row in 'abcdefgh'],
            [Square(column=4, row=row, piece=None) for row in 'abcdefgh'],
            [Square(column=3, row=row, piece=None) for row in 'abcdefgh'],

            [   # row 2 of board - White Pawns
                Square(column=2, row='a', piece=Pawn()),
                Square(column=2, row='b', piece=Pawn()),
                Square(column=2, row='c', piece=Pawn()),
                Square(column=2, row='d', piece=Pawn()),
                Square(column=2, row='e', piece=Pawn()),
                Square(column=2, row='f', piece=Pawn()),
                Square(column=2, row='g', piece=Pawn()),
                Square(column=2, row='h', piece=Pawn()),
            ],
            [   # row 1 of board - White Pieces
                Square(column=1, row='a', piece=Rook()),
                Square(column=1, row='b', piece=Knight()),
                Square(column=1, row='c', piece=Bishop()),
                Square(column=1, row='d', piece=Queen()),
                Square(column=1, row='e', piece=King()),
                Square(column=1, row='f', piece=Bishop()),
                Square(column=1, row='g', piece=Knight()),
                Square(column=1, row='h', piece=Rook()),
            ]
        ]


class Square:

    def __init__(self, column: str, row: int, piece: Piece):
        self.column = column
        self.row = row
        self.piece = piece
