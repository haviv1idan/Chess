from src.utils import PieceTypeEnum, ColorEnum, convert_chess_square_to_board_index, ROWS, COLS, CHESS_BOARD
from abc import abstractmethod


class Piece:

    def __init__(self, type: PieceTypeEnum, color: ColorEnum):
        self.type = type
        self.color = color

    @abstractmethod
    def possible_objects(self, col: str, row: int, board: list[list[object]]):
        pass

    def __hash__(self) -> int:
        return hash(self)
    

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
    


class Pawn(Piece):

    def __init__(self, **kwargs):
        super(Pawn, self).__init__(PieceTypeEnum.PAWN, **kwargs)


    def possible_objects(self, board: list[list[object]]):
        possible_objects: list[str] = []
        board_col, board_row = convert_chess_square_to_board_index(self.chess_col + str(self.chess_row))
        print(f"{board_col= }, {board_row= }")
        print(f"{self.color= }")
        if self.color == ColorEnum.WHITE:
            # Check if in starting square
            if self.chess_row == 2:
                # In case of pawn is in starting square, There are few possible objects.
                for square in (board[board_row - 1][board_col], board[board_row - 2][board_col]):
                    if square.piece == None:
                        possible_objects.append(square.column + str(square.row))

            # Check capture

            # Check promote
        return possible_objects

    def __str__(self):
        return 'p' if self.color == ColorEnum.BLACK else 'P'


class Knight(Piece):

    def __init__(self, **kwargs):
        super(Knight, self).__init__(PieceTypeEnum.KNIGHT, **kwargs)

    def __str__(self):
        return 'n' if self.color == ColorEnum.BLACK else 'N'


class Bishop(Piece):

    def __init__(self, **kwargs):
        super(Bishop, self).__init__(PieceTypeEnum.BISHOP, **kwargs)

    def __str__(self):
        return 'b' if self.color == ColorEnum.BLACK else 'B'
    

class Rook(Piece):

    def __init__(self, **kwargs):
        super(Rook, self).__init__(PieceTypeEnum.ROOK, **kwargs)

    def __str__(self):
        return 'r' if self.color == ColorEnum.BLACK else 'R'


class Queen(Piece):

    def __init__(self, **kwargs):
        super(Queen, self).__init__(PieceTypeEnum.QUEEN, **kwargs)

    def __str__(self):
        return 'q' if self.color == ColorEnum.BLACK else 'Q'


class King(Piece):

    def __init__(self, **kwargs):
        super(King, self).__init__(PieceTypeEnum.KING, **kwargs)

    def __str__(self):
        return 'k' if self.color == ColorEnum.BLACK else 'K'


class Board:

    def __init__(self, w_player: str = None, b_player: str = None):
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
            
            print(pieces_row)
            board_str.append(pieces_row)
        
        return board_str
    
    def move(self, src: str, dest: str) -> None:
        dict_board: dict[str, Piece] = self.convert_board_to_dict()

        src_square: Square =  dict_board[src]
        dest_square: Square = dict_board[dest]

        dest_square.piece = src_square.piece
        src_square.piece = None


    def rotate_player_turn(self) -> None:
        self._player_turn = ColorEnum.BLACK if self._player_turn == ColorEnum.BLACK else ColorEnum.WHITE
        print(f"Player turn: {self._player_turn}")


    def convert_board_to_dict(self) -> dict[str, Piece]:
        """
        setup board hashmap to access squares by chess square

        Example:
        'a8' => Square(column='a', row=8, piece=Rook(color=ColorEnum.BLACK)) => black Rook

        Returns:
            dict[str, Square]: dict of chess square hashmap to square
        """
        board_dict = {}
        for row in self._board:
            for square in row:
                chess_col = square.column
                chess_row = str(square.row)
                board_dict[chess_col + chess_row] = square
        
        return board_dict


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


class Move:

    def __init__(self, start_square: str, end_square: str, piece: object):
        self.start_square = start_square
        self.end_square = end_square
        self.piece = piece

    
    def is_valid(self) -> bool:
        """
        returns if the move is valid

        Returns:
            bool: True if the move is valid, False otherwise
        """
        if self.start_square == self.end_square:
            return False
        
        if self.end_square not in self.piece.possible_moves():
            return False
        
        return True
    

class Player:

    def __init__(self, name: str, color: ColorEnum = None):
        self.name = name
        self.color = color
