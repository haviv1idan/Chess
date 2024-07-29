from abc import abstractmethod
from typing import TYPE_CHECKING
from src import Board, Square
from src.utils import ColorEnum, PieceTypeEnum, COLS, ROWS, convert_chess_square_to_board_index

if TYPE_CHECKING:
    from src import Board, Square


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


class Pawn(Piece):

    def __init__(self, color: ColorEnum):
        super(Pawn, self).__init__(PieceTypeEnum.PAWN, color)
        self.is_first_move = True

    def __str__(self):
        return 'p' if self.color == ColorEnum.BLACK else 'P'
    
    def is_valid_move(self, dest_square: 'Square', board: 'Board') -> bool:
        possible_squares_cordinates = {
            ColorEnum.WHITE: [
                (0, 1),     # one square forward
                (0, 2),     # two squares forward in case of starting position
                (1, -1),    # left capture
                (1, 1),     # right capture
            ],
            ColorEnum.BLACK: [
                (0, -1),    # one square forward
                (0, -2),    # two squares forward in case of starting position
                (-1, 1),    # left capture
                (-1, -1),   # right capture
            ], 
        } 
        board_row, board_col = convert_chess_square_to_board_index(self.col + str(self.row))
        for col, row in possible_squares_cordinates[self.color]:
            if board_col + col == dest_square.col and board_row + row == dest_square.row:
                return dest_square.piece == None
            


    


    def _check_2_squares_forward(self, square: 'Square', board: 'Board') -> bool:
        """TODO

        Args:
            square (Square): _description_
            board (Board): _description_

        Returns:
            bool: _description_
        """
        # First pawn move can be 2 squares forward
        dst_square: Square = board.get_square(square.column + str(square.row + 2 if self.color == ColorEnum.WHITE else square.row - 2))
        return dst_square.piece == None

    
    def possible_moves(self, square: 'Square', board: 'Board') -> list[str]:
        """
        returns a list of all possible moves for a piece in given row and column

        Args:
            col (str): chess column
            row (int): chess row
            board (list[list[Sqaure]]): chess board
        """      
        moves: list[str] = []

        if self.color == ColorEnum.WHITE:

            if square.row == 2 and self._check_2_squares_forward(square, board):
                moves.append(square.column + str(square.row + 2))

            # one square forward                
            if board.get_square(square.column + str(square.row + 1)).piece == None:
                moves.append(square.column + str(square.row + 1))

            # check capture
            if square.column == 'a' and board.get_square('b' + str(square.row + 1)).piece.color == ColorEnum.BLACK:
                moves.append('b' + str(square.row + 1))

            elif square.column == 'h' and board.get_square('g' + str(square.row + 1)).piece.color == ColorEnum.BLACK:
                moves.append('g' + str(square.row + 1))

            else:
                left_column: str = COLS[COLS.index(square.column) - 1]
                if board.get_square(left_column + str(square.row + 1)).piece.color == ColorEnum.BLACK:
                    moves.append(left_column + str(square.row + 1))
                
                right_column: str = COLS[COLS.index(square.column) + 1]
                if board.get_square(right_column + str(square.row + 1)).piece.color == ColorEnum.BLACK:
                    moves.append(right_column + str(square.row + 1))

        else:
            pass

        return moves
    

class Knight(Piece):

    def __init__(self, color=ColorEnum):
        super(Knight, self).__init__(PieceTypeEnum.KNIGHT, color)

    def __str__(self):
        return 'n' if self.color == ColorEnum.BLACK else 'N'


class Bishop(Piece):

    def __init__(self, color: ColorEnum):
        super(Bishop, self).__init__(PieceTypeEnum.BISHOP, color)

    def __str__(self):
        return 'b' if self.color == ColorEnum.BLACK else 'B'
    

class Rook(Piece):

    def __init__(self, color: ColorEnum):
        super(Rook, self).__init__(PieceTypeEnum.ROOK, color)

    def __str__(self):
        return 'r' if self.color == ColorEnum.BLACK else 'R'


class Queen(Piece):

    def __init__(self, color: ColorEnum):
        super(Queen, self).__init__(PieceTypeEnum.QUEEN, color)

    def __str__(self):
        return 'q' if self.color == ColorEnum.BLACK else 'Q'


class King(Piece):

    def __init__(self, color: ColorEnum):
        super(King, self).__init__(PieceTypeEnum.KING, color)

    def __str__(self):
        return 'k' if self.color == ColorEnum.BLACK else 'K'


class Knight(Piece):

    def __init__(self, color: ColorEnum):
        super(Knight, self).__init__(PieceTypeEnum.KNIGHT, color)

    def __str__(self):
        return 'n' if self.color == ColorEnum.BLACK else 'N'


class Bishop(Piece):

    def __init__(self, color: ColorEnum):
        super(Bishop, self).__init__(PieceTypeEnum.BISHOP, color)

    def __str__(self):
        return 'b' if self.color == ColorEnum.BLACK else 'B'
    

class Rook(Piece):

    def __init__(self, color: ColorEnum):
        super(Rook, self).__init__(PieceTypeEnum.ROOK, color)

    def __str__(self):
        return 'r' if self.color == ColorEnum.BLACK else 'R'


class Queen(Piece):

    def __init__(self, color: ColorEnum):
        super(Queen, self).__init__(PieceTypeEnum.QUEEN, color)

    def __str__(self):
        return 'q' if self.color == ColorEnum.BLACK else 'Q'


class King(Piece):

    def __init__(self, color: ColorEnum):
        super(King, self).__init__(PieceTypeEnum.KING, color)

    def __str__(self):
        return 'k' if self.color == ColorEnum.BLACK else 'K'
