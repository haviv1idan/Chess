from src.move import Move
from abc import abstractmethod
from src.utils import PieceType, Color, convert_chess_square_to_board_index


class Piece:

    def __init__(self, type: PieceType, color: Color, chess_col: str = None, chess_row: int = None):
        self.type = type
        self.color = color
        self.chess_col = chess_col
        self.chess_row = chess_row

    @abstractmethod
    def move(self, src: Move, dst: Move):
        pass

    @abstractmethod
    def possible_moves(self, col: str, row: int, board: list[list[object]]):
        pass


class Pawn(Piece):

    def __init__(self, **kwargs):
        super(Pawn, self).__init__(PieceType.PAWN, **kwargs)

    def move(self, src: Move, dst: Move):
        pass

    def possible_moves(self, board: list[list[object]]):
        possible_moves: list[str] = []
        board_col, board_row = convert_chess_square_to_board_index(self.chess_col + str(self.chess_row))
        print(f"{board_col= }, {board_row= }")
        print(f"{self.color= }")
        if self.color == Color.WHITE:
            # Check if in starting square
            if self.chess_row == 2:
                # In case of pawn is in starting square, There are few possible moves.
                for square in (board[board_row - 1][board_col], board[board_row - 2][board_col]):
                    if square.piece == None:
                        possible_moves.append(square.column + str(square.row))

            # Check capture

            # Check promote
        return possible_moves

    def __str__(self):
        return 'p' if self.color == Color.BLACK else 'P'

class Knight(Piece):

    def __init__(self, **kwargs):
        super(Knight, self).__init__(PieceType.KNIGHT, **kwargs)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'n' if self.color == Color.BLACK else 'N'

class Bishop(Piece):

    def __init__(self, **kwargs):
        super(Bishop, self).__init__(PieceType.BISHOP, **kwargs)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'b' if self.color == Color.BLACK else 'B'
    

class Rook(Piece):

    def __init__(self, **kwargs):
        super(Rook, self).__init__(PieceType.ROOK, **kwargs)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'r' if self.color == Color.BLACK else 'R'

class Queen(Piece):

    def __init__(self, **kwargs):
        super(Queen, self).__init__(PieceType.QUEEN, **kwargs)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'q' if self.color == Color.BLACK else 'Q'

class King(Piece):

    def __init__(self, **kwargs):
        super(King, self).__init__(PieceType.KING, **kwargs)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'k' if self.color == Color.BLACK else 'K'