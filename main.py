import pygame as pg
from Board import Board, Screen

def main():
    board = Board()
    screen = Screen()
    screen.draw_board()
    screen.draw_pieces(board.board)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                break

            if event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())

if __name__ == "__main__":
    main()
