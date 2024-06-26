import pygame as pg

from chess.pgn import Game
from chess import parse_square, Square, Move, WHITE
from board import BoardObject
from screen import Screen
from logging_config import get_logger


class GameObject:

    def __init__(self, debug_mode=False, default_board=True):
        self._logger = get_logger(__class__.__name__)
        self._game = Game()
        self._headers = NotImplemented
        self._board = BoardObject()
        self._screen = Screen()
        self._debug_mode = debug_mode
        self._default_board = default_board
        self._node = None
        self._start_sqaure: Square = None
        self._end_square: Square = None


    @property
    def headers(self):
        return self._headers
    
    @headers.setter
    def headers(self, headers_dict: dict) -> None:
        for key, value in headers_dict.items():
            self.game.headers[key] = value

    @property
    def board(self):
        return self._board
    
    @property
    def screen(self):
        return self._screen
    
    def start_game(self) -> None:
        self._screen.setup()
        self.screen.draw_pieces(self._board.board)


        while True:

            for event in pg.event.get():
                
                if self._debug_mode:
                    self._logger.info(pg.mouse.get_pos())

                if event.type == pg.QUIT:
                    pg.quit()
                    return
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mouse_down_triggered()

                    if self._start_sqaure and self._end_square:
                        self.make_move()

                    self._screen.setup()
                    self._screen.draw_pieces(self._board.board)

                    if self.check_terminations():
                        pg.quit()
                        return
                
                pg.display.update()


    def check_terminations(self) -> bool:
        if self._board.chess_board.is_checkmate():
            self._logger.info("game end by checkmate")
            winner = self._board.chess_board.outcome().winner
            self._logger.info(f"game winner is {'white' if winner is WHITE else 'black'}")
            self._logger.info(f"{self._game}")
            return True
        
        if self._board.chess_board.is_checkmate():
            self._logger.info("game end by stalemate")
            result = self._board.chess_board.outcome().result
            self._logger.info(f"game result: {result}")
            return True


    def make_move(self):
        move = Move(self._start_sqaure, self._end_square)
        self._logger.info(f"{move= }")

        is_succeed = self._board.make_move(move)
        self._logger.info(f"{is_succeed= }")

        if not is_succeed:
            self._start_sqaure = self._end_square = None
            self._logger.info(f"reseting squares, {self._start_sqaure= }, {self._end_square= }")
        
        if not self._node:
            self._node = self._game.add_variation(move.from_uci(move.uci()))
        else:
            self._node = self._node.add_variation(move.from_uci(move.uci()))

        self._start_sqaure = self._end_square = None
        self._logger.info(f"{self._game= }")

                
    def mouse_down_triggered(self):
        # Get start square
        square: Square = parse_square(self._board.get_pos_details(pg.mouse.get_pos()))
        self._logger.info(f"{square= }")

        if self._start_sqaure is None:
            self._start_sqaure = square
            self._logger.info(f"{self._start_sqaure= }")
            
        else:
            self._end_square = square
            self._logger.info(f"{self._end_square= }")

