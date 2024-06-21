import pygame as pg
import logging

from consts import (
    SCREEN_HEIGHT, SCREEN_WIDTH, 
    SQUARE_SIZE, 
    ROWS_START_POS_X, ROWS_START_POS_Y, 
    COLS_START_POS_X, COLS_START_POS_Y, 
    WHITE, BOARD_IMAGE_PATH, PIECE_IMAGE_NAME, BLUE,
    DEFAULT_COLS_ORDER, DEFAULT_ROWS_ORDER
)


class Screen:
    """
    Screen class represent all things about screen
    """

    def __init__(self, default: bool = True) -> None:
        pg.init()
        pg.font.init()
        self._logger = logging.getLogger(__name__)
        self.font = pg.font.SysFont('Ariel', 30)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cols_order = DEFAULT_COLS_ORDER[::-1] if not default else DEFAULT_COLS_ORDER
        self.rows_order = DEFAULT_ROWS_ORDER[::-1] if not default else DEFAULT_ROWS_ORDER
        self.setup()

    def setup(self):
        self.screen.fill(WHITE)
        self._display_row_numbers()
        self._display_col_letters()
        self._display_board()

    def _display_row_numbers(self):
        """Display the number of rows in the screen"""
        start_pos = (ROWS_START_POS_X, ROWS_START_POS_Y)
        for index, row in enumerate(self.rows_order):
            text_surface = self.font.render(str(row), False, (0, 0, 0))
            self.screen.blit(
                text_surface,
                (start_pos[0],
                 start_pos[1] +
                    index *
                    SQUARE_SIZE))

    def _display_col_letters(self):
        """Display the letters of files in the screen"""
        start_pos = (COLS_START_POS_X, COLS_START_POS_Y)
        for index, col in enumerate(self.cols_order):
            text_surface = self.font.render(col, False, (0, 0, 0))
            self.screen.blit(
                text_surface,
                (start_pos[0] +
                      index *
                      SQUARE_SIZE,
                      start_pos[1]))

    def _display_board(self):
        """Display the board"""
        background_image = pg.image.load(BOARD_IMAGE_PATH)
        self.screen.blit(background_image, (SQUARE_SIZE, SQUARE_SIZE))
        pg.display.update()

    def draw_pieces(self, board):
        size = SQUARE_SIZE

        # x represent the row index in board 2D array
        for x in range(8):

            # y represent the col index in board 2D array
            for y in range(8):

                # . represent empty square
                if board[x][y] != '.':
                    piece_img_path = PIECE_IMAGE_NAME[board[x][y]]
                    img = pg.image.load(piece_img_path)
                    self.screen.blit(img, ((y + 1) * size, (x + 1) * size))

        pg.display.update()

    def draw_circle(self, pos: tuple):
        pg.draw.circle(self.screen, BLUE, pos, 20, 3)
        pg.display.update()
