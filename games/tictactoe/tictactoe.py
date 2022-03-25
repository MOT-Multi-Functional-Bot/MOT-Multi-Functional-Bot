from .exceptions import GuessEx, WinEx

class tictactoeGameClass():
    def __init__(self) -> None:
        self.state = 0
        self.cache = {}


