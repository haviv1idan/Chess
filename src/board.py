import numpy as np
from src.utils import Color, ROWS, COLS, CHESS_BOARD
from src.player import Player
from src.piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class Square:

    def __init__(self, column: str, row: int, piece: Piece):
        self.column = column
        self.row = row
        self.piece = piece
        if piece:
            self.piece.chess_col = column
            self.piece.chess_row = row

    def __str__(self):
        return f"{self.column= } {self.row= } {self.piece.type= }"

class Board:

    def __init__(self, w_player: str = None, b_player: str = None):
        self._white_player = Player(name=w_player if w_player else 'white_player', color=Color.WHITE)
        self._white_player = Player(name=b_player if b_player else 'black_player', color=Color.BLACK)
        self._board: list[list[Square]] = self._setup_board()
        self._player_turn: Color = Color.WHITE

    def __call__(self) -> list[list[Square]]:
        return self._board

    def rotate_player_turn(self) -> None:
        self._player_turn = Color.BLACK if self._player_turn == Color.BLACK else Color.WHITE
        print(f"Player turn: {self._player_turn}")

    def possible_moves(self) -> list[str]:
        """iterate over board and return a list of all possible moves

        Returns:
            list[str]: list of all possible moves
        """
        pass

    def _setup_board(self) -> list[list[Square]]:
        return \
        [
            [   # First row of board - Black pieces
                Square(column='a', row=8, piece=Rook(color=Color.BLACK)),
                Square(column='b', row=8, piece=Knight(color=Color.BLACK)),
                Square(column='c', row=8, piece=Bishop(color=Color.BLACK)),
                Square(column='d', row=8, piece=Queen(color=Color.BLACK)),
                Square(column='e', row=8, piece=King(color=Color.BLACK)),
                Square(column='f', row=8, piece=Bishop(color=Color.BLACK)),
                Square(column='g', row=8, piece=Knight(color=Color.BLACK)),
                Square(column='h', row=8, piece=Rook(color=Color.BLACK))
            ],
            [   # Second row of board - Black Pawns
                Square(column='a', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='b', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='c', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='d', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='e', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='f', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='g', row=7, piece=Pawn(color=Color.BLACK)),
                Square(column='h', row=7, piece=Pawn(color=Color.BLACK)),
            ],
                # Rows 6 - 3 are empty 
            [Square(column=column, row=6, piece=None) for column in 'abcdefgh'],
            [Square(column=column, row=5, piece=None) for column in 'abcdefgh'],
            [Square(column=column, row=4, piece=None) for column in 'abcdefgh'],
            [Square(column=column, row=3, piece=None) for column in 'abcdefgh'],

            [   # row 2 of board - White Pawns
                Square(column='a', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='b', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='c', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='d', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='e', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='f', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='g', row=2, piece=Pawn(color=Color.WHITE)),
                Square(column='h', row=2, piece=Pawn(color=Color.WHITE)),
            ],
            [   # row 1 of board - White Pieces
                Square(column='a', row=1, piece=Rook(color=Color.WHITE)),
                Square(column='b', row=1, piece=Knight(color=Color.WHITE)),
                Square(column='c', row=1, piece=Bishop(color=Color.WHITE)),
                Square(column='d', row=1, piece=Queen(color=Color.WHITE)),
                Square(column='e', row=1, piece=King(color=Color.WHITE)),
                Square(column='f', row=1, piece=Bishop(color=Color.WHITE)),
                Square(column='g', row=1, piece=Knight(color=Color.WHITE)),
                Square(column='h', row=1, piece=Rook(color=Color.WHITE)),
            ]
        ]

    def print_board(self) -> str:
        for row in self._board:
            pieces_row = []
            for square in row:
                pieces_row.append(square.piece.__str__())
            
            print(pieces_row)

