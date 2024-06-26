import logging

from chess import Board, Move, InvalidMoveError
from consts import SQUARE_SIZE, DEFAULT_COLS_ORDER ,DEFAULT_ROWS_ORDER

class BoardObject:

    def __init__(self, default: bool = True):
        self._logger = logging.getLogger(__name__)
        self._default = default
        self._chess_board = Board()
        self._display_board = []
        self.cols_order = DEFAULT_COLS_ORDER[::-1] if not default else DEFAULT_COLS_ORDER
        self.rows_order = DEFAULT_ROWS_ORDER[::-1] if not default else DEFAULT_ROWS_ORDER
        self.update_display_board()

    @property
    def chess_board(self):
        return self._chess_board
    
    @property
    def display_board(self):
        return self._display_board
    
    def update_display_board(self):
        board_fen: list[str] = self._chess_board.__str__().replace(' ', '').split('\n')
        if not self._default:
            self._display_board = [row[::-1] for row in board_fen[::-1]]
        else:
            self._display_board = board_fen


    def make_move(self, move: Move) -> bool:
        """validate move and execute if move is valid

        Args:
            move (Move): Move information

        Returns:
            bool: is move succeed or not
        """
        legal_moves = self.chess_board.legal_moves
        try:
            chess_move = move.from_uci(move.uci())
        except InvalidMoveError:
            self._logger.error(f"move: {move.uci()} isn't valid")
            return False

        if chess_move not in legal_moves:
            self._logger.error(f"move: {chess_move.uci()} isn't in legal moves")
            return False

        self.chess_board.push(move)
        self.update_display_board()
        return True

    def get_pos_details(self, pos: tuple) -> str:
        """
        Given a position (x, y) representing a screen location, return a chess board location

        Args:
            pos (tuple): (x, y) screen location

        Returns:
            str: (col+row) chess board location
        """
        x, y = pos
        square_size = SQUARE_SIZE
        try:
            row = self.rows_order[(y // square_size) - 1]
            col = self.cols_order[(x // square_size) - 1]
        except IndexError:
            return None

        self._logger.info(f"x: {x}, y: {y}, row: {row}, col: {col}")
        return col + row
