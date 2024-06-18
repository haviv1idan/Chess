import pygame as pg
import logging

from argparse import ArgumentParser
from Board import Board, Screen

logger = logging.getLogger(__name__)

def init_logger():
    logging.basicConfig(level=logging.INFO)
    logging.debug("logging started")


def main(debug=False):
    init_logger()
    board = Board()
    screen = Screen()
    screen.draw_pieces(board.board)
    
    flag_clicked = False 

    while True:
        for event in pg.event.get():
            
            if debug:
                logging.DEBUG(event)
    
            if event.type == pg.QUIT:
                pg.quit()
                return

            if event.type == pg.MOUSEBUTTONDOWN:
                logger.info(f"flag_clicked before: {flag_clicked}")
                flag_clicked = not flag_clicked
                logger.info(f"flag_clicked after: {flag_clicked}")

                # print(pg.mouse.get_pos())
                board.get_pos_details(pg.mouse.get_pos())
                screen.draw_circle(pos=pg.mouse.get_pos())

                if not flag_clicked:
                    screen.setup()
                    screen.draw_pieces(board.board)



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--debug", help='DEBUG mode')

    args = parser.parse_args()
    debug_mode = args.debug
    main(debug_mode)
