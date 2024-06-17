import pygame as pg
from Board import Board, Screen

def main():
    board = Board()
    screen = Screen()
    screen.draw_pieces(board.board)
    
    while True:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                pg.quit()
                return

            if event.type == pg.MOUSEBUTTONDOWN:
                # print(pg.mouse.get_pos())
                board.get_pos_details(pg.mouse.get_pos())


if __name__ == "__main__":
    main()
