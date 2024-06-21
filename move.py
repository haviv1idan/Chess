class Move:

    def __init__(self, start_pos: str = '', end_pos: str = ''):
        self._start_pos = start_pos
        self._end_pos = end_pos

    @property
    def start_pos(self):
        return self._start_pos

    @start_pos.setter
    def start_pos(self, pos: str):
        self._start_pos = pos

    @property
    def end_pos(self):
        return self._end_pos

    @end_pos.setter
    def end_pos(self, pos: str):
        self._end_pos = pos

    def uci_move(self) -> str:
        """returns the uci move

        Returns:
            str: uci_move
        """
        return self.start_pos + self.end_pos
