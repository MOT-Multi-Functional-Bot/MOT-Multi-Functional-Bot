class GameEx(Exception):
    pass


class GuessEx(GameEx):
    pass


class GameOverEx(GameEx):
    pass


class WinEx(GameOverEx):
    pass


class LoseEx(GameOverEx):
    pass