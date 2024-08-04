from chess import Move
from random import choice

class BotObject:

    def __init__(self):
        pass

    def make_move(self, legal_moves: list[Move]) -> Move:
        return choice(list(iter(legal_moves)))
