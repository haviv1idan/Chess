import logging
import chess

from move import Move

from consts import SQUARE_SIZE, DEFAULT_COLS_ORDER ,DEFAULT_ROWS_ORDER

class Board:

    def __init__(self, default: bool = True):
        self._logger = logging.getLogger(__name__)
        self.chess_board = chess.Board()
        self.convert_fen_to_2d_array()
        self.cols_order = DEFAULT_COLS_ORDER[::-1] if not default else DEFAULT_COLS_ORDER
        self.rows_order = DEFAULT_ROWS_ORDER[::-1] if not default else DEFAULT_ROWS_ORDER
        # self.locations = self.locations_board()

    def make_move(self, move: Move) -> None:
        self.chess_board.push_san(move.uci_move())
        self.convert_fen_to_2d_array()
        # self.locations = self.locations_board()

    def convert_fen_to_2d_array(self) -> None:
        self.board = self.chess_board.__str__()
        self.board = self.board.split('\n')
        self.board = [row.replace(' ', '') for row in self.board]


    # def locations_board(self):
    #     start_board_x = START_BOARD_X
    #     start_board_y = START_BOARD_Y
    #     size = SQUARE_SIZE

    #     locations_board_dict = {}
    #     for row in range(8):
    #         start_y = start_board_y + (size * row)
    #         for col in range(8):
    #             start_x = start_board_x + (size * col)
    #             square_value = self.board[row][col]
    #             locations_board_dict[(start_x, start_y)] = BoardSquare(start_x, start_y, square_value, self.rows_order[row], self.cols_order[col])
    #             self._logger.info(f"create square: \n  "
    #                   f"value: {square_value}\n  "
    #                   f"start_x, start_y= ({start_x}, {start_y})\n"
    #                   f"row, col= {self.rows_order[row]}, {self.cols_order[col]}")
    #     return locations_board_dict

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

