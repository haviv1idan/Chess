import logging
import chess

from chess import Move, InvalidMoveError
from consts import SQUARE_SIZE, DEFAULT_COLS_ORDER ,DEFAULT_ROWS_ORDER, MoveCode

class Board:

    def __init__(self, default: bool = True):
        self._logger = logging.getLogger(__name__)
        self.chess_board = chess.Board()
        self.convert_fen_to_2d_array()
        self.cols_order = DEFAULT_COLS_ORDER[::-1] if not default else DEFAULT_COLS_ORDER
        self.rows_order = DEFAULT_ROWS_ORDER[::-1] if not default else DEFAULT_ROWS_ORDER


    def make_move(self, move: Move) -> int:
        """validate move and execute if move is valid

        Args:
            move (Move): Move information

        Returns:
            int: Enum const of move code
        """
        legal_moves = self.chess_board.legal_moves
        try:
            chess_move = move.from_uci(move.uci())
        except InvalidMoveError as e:
            self._logger.error(f"move: {move.uci()} isn't valid")
            return MoveCode.NO_VALID

        if chess_move not in legal_moves:
            self._logger.error(f"move: {chess_move.uci()} isn't in legal moves")
            return MoveCode.NO_VALID

        self.chess_board.push(move)
        if self.chess_board.is_checkmate():
            return MoveCode.CHECKMATE
        
        self.convert_fen_to_2d_array()
        return MoveCode.VALID


    def convert_fen_to_2d_array(self) -> None:
        self.board = self.chess_board.__str__()
        self.board = self.board.split('\n')
        self.board = [row.replace(' ', '') for row in self.board]

    def get_pos_details(self, pos: tuple) -> str:
        """
        Given a position (x, y) representing a screen location, return a chess board location

        Args:
            pos (tuple): (x, y) screen location

        Returns:
            tuple: str(col+row) chess board location
        """
        x, y = pos
        square_size = SQUARE_SIZE
        row = self.rows_order[(y // square_size) - 1]
        col = self.cols_order[(x // square_size) - 1]
        self._logger.info(f"x: {x}, y: {y}, row: {row}, col: {col}")
        return col + row


class BoardSquare:

    def __init__(self, start_x, start_y, value, row, col) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.value = value
        self.row = row
        self.col = col

