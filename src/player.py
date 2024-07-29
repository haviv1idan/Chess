from src.utils import ColorEnum

class Player:

    def __init__(self, name: str, color: ColorEnum = None):
        self.name = name
        self.color = color