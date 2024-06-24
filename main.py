import pygame as pg
import logging

from argparse import ArgumentParser, BooleanOptionalAction
from board import Board
from screen import Screen
from consts import MoveCode
from chess import Move, Square, parse_square, Outcome, WHITE, Termination

logger = logging.getLogger(__name__)


def init_logger():
    logging.basicConfig(level=logging.INFO)
    logging.debug("logging started")


def main(debug=False, default=True):
    init_logger()
    board = Board(default)
    screen = Screen(default)
    screen.draw_pieces(board.board)

    flag_clicked = False
    start_square: Square = None

    while True:

        for event in pg.event.get():

            if debug:
                logger.info(pg.mouse.get_pos())

            if event.type == pg.QUIT:
                pg.quit()
                return

            if event.type == pg.MOUSEBUTTONDOWN:
                logger.info(f"flag_clicked before: {flag_clicked}")
                flag_clicked = not flag_clicked
                logger.info(f"flag_clicked after: {flag_clicked}")

                # print(pg.mouse.get_pos())
                chess_pos: str = board.get_pos_details(pg.mouse.get_pos())
                screen.draw_circle(pos=pg.mouse.get_pos())

                # detect first mouse click (start of move)
                if flag_clicked:
                    start_square = parse_square(chess_pos)

                # detect second mouse click (end of move)
                if not flag_clicked:
                    move = Move(start_square, parse_square(chess_pos))
                    is_valid = board.make_move(move)
                    if not is_valid:
                        if board.chess_board.is_checkmate():
                            logger.info("game end by checkmate")
                            winner = board.chess_board.outcome().winner
                            logger.info(f"game winner is {'white' if winner is WHITE else 'black'}")
                            return 
                        
                        if board.chess_board.is_stalemate():
                            logger.info("game end by stalemate")
                            result = board.chess_board.outcome().result
                            logger.info(f"game result: {result}")
                            return 

                    logger.info(board.chess_board.move_stack)
                    screen.setup()
                    screen.draw_pieces(board.board)
                    move = None

                pg.display.update()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--debug", help='DEBUG mode', action=BooleanOptionalAction, default=True)
    parser.add_argument("--default", help='Default board', action=BooleanOptionalAction, default=True)
    
    # for no debug mode
    # python main.py --no-debug

    args = parser.parse_args()
    debug_mode = args.debug  
    default = args.default
    print(f"{debug_mode = }")
    print(f"{default = }")
    main(debug_mode, default)
