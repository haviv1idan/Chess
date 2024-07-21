from src.move import Move
from abc import abstractmethod
from enum import Enum

class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


class Piece:

    def __init__(self, type: Enum):
        self.type = type

    @abstractmethod
    def move(self, src: Move, dst: Move):
        pass


class Pawn(Piece):

    def __init__(self):
        super(Pawn, self).__init__(PieceType.PAWN)

    def move(self, src: Move, dst: Move):
        pass


class Knight(Piece):

    def __init__(self):
        super(Knight, self).__init__(PieceType.KNIGHT)

    def move(self, src: Move, dst: Move):
        pass


class Bishop(Piece):

    def __init__(self):
        super(Bishop, self).__init__(PieceType.BISHOP)

    def move(self, src: Move, dst: Move):
        pass
    

class Rook(Piece):

    def __init__(self):
        super(Rook, self).__init__(PieceType.ROOK)

    def move(self, src: Move, dst: Move):
        pass


class Queen(Piece):

    def __init__(self):
        super(Queen, self).__init__(PieceType.QUEEN)

    def move(self, src: Move, dst: Move):
        pass


class King(Piece):

    def __init__(self):
        super(King, self).__init__(PieceType.KING)

    def move(self, src: Move, dst: Move):
        pass