import chess
import pygame as pg


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

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.WHITE)

    def draw_board(self):
        size = self.SQUARE_SIZE
        start_board_x = self.START_BOARD_X
        start_board_y = self.START_BOARD_Y

        for row in range(8):
            for col in range(8):
                start_square_x = start_board_x + (size * col)
                start_square_y = start_board_y + (size * row)
                if (row + col) % 2 == 0:
                    pg.draw.rect(self.screen, self.WHITE, [start_square_x, start_square_y, size, size])
                else:
                    pg.draw.rect(self.screen, self.GREEN, [start_square_x, start_square_y, size, size])

        # Add a nice boarder
        pg.draw.rect(self.screen, self.BLACK, [size, size, 8 * size, 8 * size], 1)
        pg.display.update()

    def draw_pieces(self, board):
        size = self.SQUARE_SIZE
        for x in range(8):
            for y in range(8):
                if board[x][y] != '.':
                    img = pg.image.load(f"images/{board[x][y]}.png")
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
