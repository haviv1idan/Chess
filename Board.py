import chess
import pygame as pg

images_pieces = {
    'r': 'WR',
    'n': 'WN',
    'b': 'WB',
    'q': 'WQ',
    'k': 'WK',
    'p': 'WP',
    'R': 'BR',
    'N': 'BN',
    'B': 'BB',
    'Q': 'BQ',
    'K': 'BK',
    'P': 'BP',
}

class Screen:
    """
    Screen class represent all things about screen
    """

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    START_BOARD_X = 60
    START_BOARD_Y = 60
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    SQUARE_SIZE = 60
    
    # Rows indicator start position
    ROWS_START_POS_X = SQUARE_SIZE // 2
    ROWS_START_POS_Y = SQUARE_SIZE + SQUARE_SIZE // 3

    # Columns indicator start position
    COLS_START_POS_X = SCREEN_WIDTH - (2 * SQUARE_SIZE) + SQUARE_SIZE // 2
    COLS_START_POS_Y = SCREEN_WIDTH - SQUARE_SIZE


    def __init__(self) -> None:
        pg.init()
        pg.font.init()
        self.font = pg.font.SysFont('Ariel', 30)
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.WHITE)
        self._setup()

    def _setup(self):
        self._display_row_numbers()
        self._display_row_numbers()
        self._display_board()

    def _display_row_numbers(self):
        """Display the number of rows in the screen"""
        start_pos = (self.ROWS_START_POS_X, self.ROWS_START_POS_Y)
        for row in range(8):
            text_surface = self.font.render(str(row + 1), False, (0, 0, 0))
            self.screen.blit(text_surface, (start_pos[0], start_pos[1] + row * self.SQUARE_SIZE))

    def _display_cols_letters(self):
        """Display the letters of files in the screen"""
        start_pos = (self.COLS_START_POS_X, self.COLS_START_POS_Y)
        for index, col in enumerate('abcdefgh'):
            text_surface = self.font.render(col, False, (0, 0, 0))
            self.screen.blit(text_surface, (start_pos[0] - index * self.SQUARE_SIZE, start_pos[1]))

    def _display_board(self):
        background_image = pg.image.load("images/board.png")
        self.screen.blit(background_image, (self.SQUARE_SIZE, self.SQUARE_SIZE))
        pg.display.update()

    def draw_pieces(self, board):
        size = self.SQUARE_SIZE
        for x in range(8):
            for y in range(8):
                if board[x][y] != '.':
                    piece_img_name = images_pieces[board[x][y]]
                    img = pg.image.load(f"images/{piece_img_name}.png")
                    self.screen.blit(img, ((y + 1) * size, (x + 1) * size))
        pg.display.update()


class Board:

    def __init__(self):
        self.chess_rows = list("abcdefgh")
        self.chess_cols = list(range(8, 0, -1))
        self.chess_board = chess.Board()
        self.board = self.convert_fen_to_2d_array()
        self.locations_board = self.locations_board()

    def convert_fen_to_2d_array(self) -> list:
        board = self.chess_board.fen().split(' ')[0]
        split_board = board.split('/')
        final_board = []
        for row in split_board:
            if row[0] == '8':
                final_board.append(['.'] * 8)
            else:
                board_row = [item for item in row]
                final_board.append(board_row)

        return final_board

    def locations_board(self):
        start_board_x = Screen.START_BOARD_X
        start_board_y = Screen.START_BOARD_Y
        size = Screen.SQUARE_SIZE

        row_indexes = list(range(1, 9))[::-1]
        col_indexes = list('abcdefgh')
        locations_board = {}
        for row in range(8):
            start_y = start_board_y + (size * row)
            for col in range(8):
                start_x = start_board_x + (size * col)
                square_value = self.board[row][col]
                locations_board[(start_x, start_y)] = BoardSquare(start_x, start_y, square_value, row_indexes[row], col_indexes[col])
                print(f"create square: \n  "
                      f"value: {square_value}\n  "
                      f"start_x, start_y= ({start_x}, {start_y})\n"
                      f"row, col= {row_indexes[row]}, {col_indexes[col]}")
        return locations_board

    def get_pos_details(self, pos: tuple):
        x, y = pos
        square_size = Screen.SQUARE_SIZE
        row = self.chess_cols[(y // square_size) - 1]
        col = self.chess_rows[(x // square_size) - 1]
        print(f"x: {x}, y: {y}, row: {row}, col: {col}")


class BoardSquare:

    def __init__(self, start_x, start_y, value, row, col) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.value = value
        self.row = row
        self.col = col
