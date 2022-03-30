import unittest
from games.numbergame.numbergame import *
from games.numbergame.exceptions import *

class Test_WHAT_TO_TEST(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.numgame = numbergame()
        self.numbertoguess = numtoguess(2,False)

    def test_numb(self):
        self.numgame.selected_number = 42

        # guessed number is the correct number
        with self.assertRaises(WinEx) as context:
            self.numgame.numb("42","1")
        self.assertTrue(type(context.exception) == type(WinEx()))

        # guessed number is not the correct number
        with self.assertRaises(GuessEx) as context:
            self.numgame.numb("40","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

        # guessed number is not numeric
        with self.assertRaises(GuessEx) as context:
            self.numgame.numb("test","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

        # guessed number is to big/small
        with self.assertRaises(GuessEx) as context:
            self.numgame.numb("10000","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

    def test_newnum(self):
        self.numgame.reset = False
        # number was reset
        with self.assertRaises(GuessEx) as context:
            self.numgame.newnum("10000","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

        self.numgame.reset = True
        # number was already once reset
        with self.assertRaises(GuessEx) as context:
            self.numgame.numb("10000","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

        self.numgame.reset = False
        # number is not numeric
        with self.assertRaises(GuessEx) as context:
            self.numgame.numb("test","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

        self.numgame.reset = False
        # number is to big
        with self.assertRaises(GuessEx) as context:
            self.numgame.numb("10000000000","1")
        self.assertTrue(type(context.exception) == type(GuessEx()))

if __name__ == "__main__":
    unittest.main()


# HOW TO RUN THE TEST:
# python -m unittest testing/test_GAME.test_FILE.py
