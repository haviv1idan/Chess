from os import path

IMAGES_FOLDER_PATH = path.join('images')

# Small letter represent white piece, Big letter represent black piece
PIECE_IMAGE_NAME = {
    'r': path.join(IMAGES_FOLDER_PATH, 'BR.png'),
    'n': path.join(IMAGES_FOLDER_PATH, 'BN.png'),
    'b': path.join(IMAGES_FOLDER_PATH, 'BB.png'),
    'q': path.join(IMAGES_FOLDER_PATH, 'BQ.png'),
    'k': path.join(IMAGES_FOLDER_PATH, 'BK.png'),
    'p': path.join(IMAGES_FOLDER_PATH, 'BP.png'),
    'R': path.join(IMAGES_FOLDER_PATH, 'WR.png'),
    'N': path.join(IMAGES_FOLDER_PATH, 'WN.png'),
    'B': path.join(IMAGES_FOLDER_PATH, 'WB.png'),
    'Q': path.join(IMAGES_FOLDER_PATH, 'WQ.png'),
    'K': path.join(IMAGES_FOLDER_PATH, 'WK.png'),
    'P': path.join(IMAGES_FOLDER_PATH, 'WP.png'),
}

BOARD_IMAGE_PATH = path.join(IMAGES_FOLDER_PATH, 'board.png')


# Screen definitions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Board definitions
START_BOARD_X = 60
START_BOARD_Y = 60
SQUARE_SIZE = 60

# Rows indicator start position
ROWS_START_POS_X = SQUARE_SIZE // 2
ROWS_START_POS_Y = SQUARE_SIZE + SQUARE_SIZE // 3

# Columns indicator start position
COLS_START_POS_X = SQUARE_SIZE  + SQUARE_SIZE // 2
COLS_START_POS_Y = SCREEN_WIDTH - SQUARE_SIZE

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255

# Rows and Cols default orders
DEFAULT_ROWS_ORDER = list('87654321')
DEFAULT_COLS_ORDER = list('abcdefgh')