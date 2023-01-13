from Board import Board, Screen
import pygame as pg

def main():
    board = Board()
    screen = Screen()
    screen.draw_board()
    screen.draw_pieces(board.board)
    
    while True:

        for event in pg.event.get():
            if event == pg.QUIT:
                break

if __name__ == "__main__":
    main()
