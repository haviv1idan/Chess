import pygame as pg

class Screen:

    """
    Screen class represent all things about screen
    """

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
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

        for x in range(1, 9):
            for y in range(1, 9):
                if (x + y) % 2 == 0:
                    pg.draw.rect(self.screen, self.WHITE ,[size*x,size*y,size,size])
                else:
                     pg.draw.rect(self.screen, self.GREEN, [size*y,size*x,size,size])

        #Add a nice boarder
        pg.draw.rect(self.screen, self.BLACK, [size,size,8*size,8*size],1)
        pg.display.update()


    def draw_pieces(self, board):
        size = self.SQUARE_SIZE
        for x in range(1, 9):
            for y in range(1, 9):
                if board[x-1][y-1] != '.':
                    img = pg.image.load(f"images/{board[x-1][y-1]}.png")
                    self.screen.blit(img, (y * size, x * size))
        pg.display.update()

class Board():

    def __init__(self):
        return self.generate_board()

    def generate_board(self):
        # P, N, B, R, Q or K for white pieces or the lower-case variants for the black pieces.
        self.board = """r n b q k b n r
                        p p p p p p p p
                        . . . . . . . .
                        . . . . . . . .
                        . . . . . . . .
                        . . . . . . . .
                        P P P P P P P P
                        R N B Q K B N R """
        self.board = [row.split(' ') for row in self.board.split('\n')]
        self.board = [[item for item in row if item != ''] for row in self.board]
        print(self.board)
