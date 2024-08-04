from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src import Piece

    

class Move:

    def __init__(self, start_square: str, end_square: str, piece: 'Piece'):
        self.start_square = start_square
        self.end_square = end_square
        self.piece = piece

    
    def is_valid(self) -> bool:
        """
        returns if the move is valid

        Returns:
            bool: True if the move is valid, False otherwise
        """
        if self.start_square == self.end_square:
            return False
        
        if self.end_square not in self.piece.possible_moves():
            return False
        
        return True