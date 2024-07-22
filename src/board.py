from enum import Enum
from typing import Any
from src.utils import Color
from src.player import Player
from src.piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class Board:

    def __init__(self, w_player: str = None, b_player: str = None):
        self.white_player = Player(name=w_player if w_player else 'white_player', color=Color.WHITE)
        self.white_player = Player(name=b_player if b_player else 'black_player', color=Color.BLACK)
        self.board: list[list[object]] = self._setup_board()

    def __call__(self) -> list[list[object]]:
        return self.board


    def _setup_board(self) -> list[list[object]]:
        return \
        [
            [   # First row of board - Black pieces
                Square(column=8, row='a', piece=Rook(color=Color.BLACK)),
                Square(column=8, row='b', piece=Knight(color=Color.BLACK)),
                Square(column=8, row='c', piece=Bishop(color=Color.BLACK)),
                Square(column=8, row='d', piece=Queen(color=Color.BLACK)),
                Square(column=8, row='e', piece=King(color=Color.BLACK)),
                Square(column=8, row='f', piece=Bishop(color=Color.BLACK)),
                Square(column=8, row='g', piece=Knight(color=Color.BLACK)),
                Square(column=8, row='h', piece=Rook(color=Color.BLACK))
            ],
            [   # Second row of board - Black Pawns
                Square(column=7, row='a', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='b', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='c', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='d', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='e', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='f', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='g', piece=Pawn(color=Color.BLACK)),
                Square(column=7, row='h', piece=Pawn(color=Color.BLACK)),
            ],
                # Rows 6 - 3 are empty 
            [Square(column=6, row=row, piece=None) for row in 'abcdefgh'],
            [Square(column=5, row=row, piece=None) for row in 'abcdefgh'],
            [Square(column=4, row=row, piece=None) for row in 'abcdefgh'],
            [Square(column=3, row=row, piece=None) for row in 'abcdefgh'],

            [   # row 2 of board - White Pawns
                Square(column=2, row='a', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='b', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='c', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='d', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='e', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='f', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='g', piece=Pawn(color=Color.WHITE)),
                Square(column=2, row='h', piece=Pawn(color=Color.WHITE)),
            ],
            [   # row 1 of board - White Pieces
                Square(column=1, row='a', piece=Rook(color=Color.WHITE)),
                Square(column=1, row='b', piece=Knight(color=Color.WHITE)),
                Square(column=1, row='c', piece=Bishop(color=Color.WHITE)),
                Square(column=1, row='d', piece=Queen(color=Color.WHITE)),
                Square(column=1, row='e', piece=King(color=Color.WHITE)),
                Square(column=1, row='f', piece=Bishop(color=Color.WHITE)),
                Square(column=1, row='g', piece=Knight(color=Color.WHITE)),
                Square(column=1, row='h', piece=Rook(color=Color.WHITE)),
            ]
        ]

    def print_board(self) -> str:
        for row in self.board:
            pieces_row = []
            for square in row:
                pieces_row.append(square.piece.__str__())
            
            print(pieces_row)


class Square:

    def __init__(self, column: str, row: int, piece: Piece):
        self.column = column
        self.row = row
        self.piece = piece
