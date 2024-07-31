from abc import abstractmethod
from typing import TYPE_CHECKING
from src.logging_config import get_logger
from src.utils import ColorEnum, PieceTypeEnum, COLS, ROWS, convert_chess_square_to_board_index

if TYPE_CHECKING:
    from src.board import Board, Square


class Piece:

    def __init__(self, type: PieceTypeEnum, color: ColorEnum, chess_col: str = None, chess_row: int = None):
        self.type = type
        self.color = color
        self.col = chess_col
        self.row = chess_row

    def __hash__(self) -> int:
        return hash(self)
    
    @abstractmethod
    def is_valid_move(self, dest_square: 'Square', board: 'Board') -> bool:
        pass

    @abstractmethod
    def possible_moves(self, board: 'Board'):
        pass



class Pawn(Piece):

    def __init__(self, color: ColorEnum):
        super(Pawn, self).__init__(PieceTypeEnum.PAWN, color)
        self._logger = get_logger(self.__class__.__name__)
        self.is_first_move = True
        self._cordinates = {
            # (column, row)
            ColorEnum.WHITE: [
                (0, 1),     # one square forward
                (0, 2),     # two squares forward in case of starting position
                (-1, 1),    # left capture
                (1, 1),     # right capture
            ],
            ColorEnum.BLACK: [
                (0, -1),    # one square forward
                (0, -2),    # two squares forward in case of starting position
                (-1, -1),   # left capture
                (1, -1),    # right capture
            ],
        }

    def __str__(self):
        return 'p' if self.color == ColorEnum.BLACK else 'P'

    def is_valid_move(self, dest_square: 'Square', board: 'Board') -> bool:
        possible_moves = self.possible_moves(board)

        if possible_moves == []:
            self._logger.warning("No possible moves")

        return dest_square in self.possible_moves(board)
    
    def possible_moves(self, board: 'Board') -> list['Square']:
        
        squares: list['Square'] = []

        for column, row in self._cordinates[self.color]:
            chess_column = COLS[COLS.index(self.col) + column]
            chess_row = self.row + row
            self._logger.info(f"{chess_column= }, {chess_row= }")

            square: 'Square' = board.get_square(chess_column + str(chess_row))
            # check capture squares
            if abs(column) == abs(row) == 1:
                if not square.piece:
                    continue

                if square.piece.color != self.color:
                    squares.append(board.get_square(chess_column + str(chess_row)))
            else:
                if board.get_square(chess_column + str(chess_row)).piece is None:
                    squares.append(board.get_square(chess_column + str(chess_row)))
        
        self._logger.info(f"possible moves: {[square.__str__() for square in squares]}")
        return squares
    

class Knight(Piece):

    def __init__(self, color=ColorEnum):
        super(Knight, self).__init__(PieceTypeEnum.KNIGHT, color)
        self._logger = get_logger(self.__class__.__name__)
        self._cordinates = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]


    def __str__(self):
        return 'n' if self.color == ColorEnum.BLACK else 'N'
    
    def is_valid_move(self, dest_square: 'Square', board: 'Board') -> bool:
        return dest_square in self.possible_moves(board)

    def possible_moves(self, board: 'Board') -> list['Square']:
        squares: list['Square'] = []
        
        for col, row in self._cordinates:
            if COLS.index(self.col) + col < 0 or COLS.index(self.col) + col > 7:
                continue

            if self.row + row <= 0 or self.row + row > 7:
                continue

            chess_column = COLS[COLS.index(self.col) + col]
            chess_row = self.row + row

            square: 'Square' = board.get_square(chess_column + str(chess_row))
            self._logger.info(f"{chess_column= }, {chess_row= }, piece= {square.piece}")

            if square.piece is None or square.piece.color != self.color:
                squares.append(square)

        self._logger.info(f"possible moves: {[square.__str__() for square in squares]}")
        return squares




class Bishop(Piece):

    def __init__(self, color: ColorEnum):
        super(Bishop, self).__init__(PieceTypeEnum.BISHOP, color)
        self._logger = get_logger(self.__class__.__name__)

    def __str__(self):
        return 'b' if self.color == ColorEnum.BLACK else 'B'
    
    def possible_moves(self, board: 'Board') -> list['Square']:
        
        return []
    

class Rook(Piece):

    def __init__(self, color: ColorEnum):
        super(Rook, self).__init__(PieceTypeEnum.ROOK, color)
        self._logger = get_logger(self.__class__.__name__)

    def __str__(self):
        return 'r' if self.color == ColorEnum.BLACK else 'R'


class Queen(Piece):

    def __init__(self, color: ColorEnum):
        super(Queen, self).__init__(PieceTypeEnum.QUEEN, color)
        self._logger = get_logger(self.__class__.__name__)

    def __str__(self):
        return 'q' if self.color == ColorEnum.BLACK else 'Q'


class King(Piece):

    def __init__(self, color: ColorEnum):
        super(King, self).__init__(PieceTypeEnum.KING, color)
        self._logger = get_logger(self.__class__.__name__)

    def __str__(self):
        return 'k' if self.color == ColorEnum.BLACK else 'K'
