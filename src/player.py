from enum import Enum

class PlayerColor(Enum):
    WHITE = 0
    BLACK = 1


class Player:

    def __init__(self, name: str, color: Enum):
        self.name = name
        self.color = color
