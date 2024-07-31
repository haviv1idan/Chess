from typing import TYPE_CHECKING
from src.logging_config import get_logger
from src.utils import ColorEnum, PieceTypeEnum
from src.player import Player
from src.pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King
    


class Square:

    def __init__(self, column: str, row: int, piece: 'Piece'):
        self.column = column
        self.row = row
        self.piece = piece
        if piece:
            self.piece.col = column
            self.piece.row = row

    def __str__(self):
        return f"{self.column= } {self.row= } self.piece= {self.piece if self.piece else None }"
    

class Board:

    def __init__(self, w_player: str = None, b_player: str = None):
        self._logger = get_logger(self.__class__.__name__)
        self._white_player = Player(name=w_player if w_player else 'white_player', color=ColorEnum.WHITE)
        self._white_player = Player(name=b_player if b_player else 'black_player', color=ColorEnum.BLACK)
        self._board: list[list[Square]] = self._setup_board()
        self._player_turn: ColorEnum = ColorEnum.WHITE

    
    def __call__(self) -> list[list[Square]]:
        return self._board
    

    def __str__(self) -> list[list[str]]:
        """
        return 2d array representation each square the piece str

        Returns:
            list[list[str]]: 2D array represent chess board pieces
        """
        board_str = []
        for row in self._board:
            pieces_row = []
            for square in row:
                pieces_row.append(square.piece.__str__() if square.piece else '')
            
            board_str.append(pieces_row)
        
        return board_str

    def get_square(self, chess_square: str) -> Square:
        squares_list: list[Square] = [square for row in self._board for square in row]
        return list(filter(lambda square: square.column == chess_square[0] and str(square.row) == chess_square[1], squares_list))[0]    

    def get_white_pieces(self) -> list[Square]:
        return [square for row in self._board for square in row if square.piece.color == ColorEnum.WHITE]
    

    def get_black_pieces(self) -> list[Square]:
        return [square for row in self._board for square in row if square.piece.color == ColorEnum.BLACK]


    def rotate_player_turn(self) -> None:
        self._player_turn = ColorEnum.WHITE if self._player_turn == ColorEnum.BLACK else ColorEnum.BLACK
        self._logger.info(f"Player turn: {self._player_turn}")


    def possible_moves(self) -> list[str]:
        """iterate over board and return a list of all possible moves

        Returns:
            list[str]: list of all possible moves
        """
        player_squares: list[Square] = [square for row in self._board for square in row if square.piece.color == self._player_turn]
        moves = []
        for square in player_squares:
            moves.append(square.piece.possible_moves())


    def _setup_board(self) -> list[list[Square]]:
        return \
        [
            [   # First row of board - Black pieces
                Square(column='a', row=8, piece=Rook(color=ColorEnum.BLACK)),
                Square(column='b', row=8, piece=Knight(color=ColorEnum.BLACK)),
                Square(column='c', row=8, piece=Bishop(color=ColorEnum.BLACK)),
                Square(column='d', row=8, piece=Queen(color=ColorEnum.BLACK)),
                Square(column='e', row=8, piece=King(color=ColorEnum.BLACK)),
                Square(column='f', row=8, piece=Bishop(color=ColorEnum.BLACK)),
                Square(column='g', row=8, piece=Knight(color=ColorEnum.BLACK)),
                Square(column='h', row=8, piece=Rook(color=ColorEnum.BLACK))
            ],
            [   # Second row of board - Black Pawns
                Square(column='a', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='b', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='c', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='d', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='e', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='f', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='g', row=7, piece=Pawn(color=ColorEnum.BLACK)),
                Square(column='h', row=7, piece=Pawn(color=ColorEnum.BLACK)),
            ],
                # Rows 6 - 3 are empty 
            [Square(column=column, row=6, piece=None) for column in 'abcdefgh'],
            [Square(column=column, row=5, piece=None) for column in 'abcdefgh'],
            [Square(column=column, row=4, piece=None) for column in 'abcdefgh'],
            [Square(column=column, row=3, piece=None) for column in 'abcdefgh'],

            [   # row 2 of board - White Pawns
                Square(column='a', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='b', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='c', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='d', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='e', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='f', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='g', row=2, piece=Pawn(color=ColorEnum.WHITE)),
                Square(column='h', row=2, piece=Pawn(color=ColorEnum.WHITE)),
            ],
            [   # row 1 of board - White Pieces
                Square(column='a', row=1, piece=Rook(color=ColorEnum.WHITE)),
                Square(column='b', row=1, piece=Knight(color=ColorEnum.WHITE)),
                Square(column='c', row=1, piece=Bishop(color=ColorEnum.WHITE)),
                Square(column='d', row=1, piece=Queen(color=ColorEnum.WHITE)),
                Square(column='e', row=1, piece=King(color=ColorEnum.WHITE)),
                Square(column='f', row=1, piece=Bishop(color=ColorEnum.WHITE)),
                Square(column='g', row=1, piece=Knight(color=ColorEnum.WHITE)),
                Square(column='h', row=1, piece=Rook(color=ColorEnum.WHITE)),
            ]
        ]

    def move(self, src_square: str, dest_square: str) -> None:
        src_square: Square = self.get_square(src_square)
        dest_square: Square = self.get_square(dest_square)

        piece = src_square.piece

        if not piece:
            self._logger.error('No piece')
            return

        if piece.color != self._player_turn:
            self._logger.error('wrong color')
            return

        if not piece.is_valid_move(dest_square, self):
            self._logger.error('ivalid move')
            return

        dest_square.piece = src_square.piece
        src_square.piece = None
        
        if piece.type == PieceTypeEnum.PAWN:
            piece.is_first_move = False

        self.rotate_player_turn()