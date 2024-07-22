from src.move import Move
from abc import abstractmethod
from src.utils import PieceType, Color


class Piece:

    def __init__(self, type: PieceType, color: Color):
        self.type = type
        self.color = color

    @abstractmethod
    def move(self, src: Move, dst: Move):
        pass


class Pawn(Piece):

    def __init__(self, color: Color):
        super(Pawn, self).__init__(PieceType.PAWN, color)

    def move(self, src: Move, dst: Move):
        pass
    
    def __str__(self):
        return 'p' if self.color == Color.BLACK else 'P'

class Knight(Piece):

    def __init__(self, color: Color):
        super(Knight, self).__init__(PieceType.KNIGHT, color)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'n' if self.color == Color.BLACK else 'N'

class Bishop(Piece):

    def __init__(self, color: Color):
        super(Bishop, self).__init__(PieceType.BISHOP, color)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'b' if self.color == Color.BLACK else 'B'
    

class Rook(Piece):

    def __init__(self, color: Color):
        super(Rook, self).__init__(PieceType.ROOK, color)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'r' if self.color == Color.BLACK else 'R'

class Queen(Piece):

    def __init__(self, color: Color):
        super(Queen, self).__init__(PieceType.QUEEN, color)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'q' if self.color == Color.BLACK else 'Q'

class King(Piece):

    def __init__(self, color: Color):
        super(King, self).__init__(PieceType.KING, color)

    def move(self, src: Move, dst: Move):
        pass

    def __str__(self):
        return 'k' if self.color == Color.BLACK else 'K'