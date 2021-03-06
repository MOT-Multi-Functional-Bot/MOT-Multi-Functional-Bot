import unittest
from games.moviegame.moviegame_commands import *
from games.moviegame.moviequiz import *
from testing.test_moviegame.test_moviegamesupdates import *
from games.moviegame.runninggames import *


class Test_moviegame_commands(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.update = Updatesmovie(messagemovie, chatmovie)
        self.running_MovieGames = runninggames

    def test_movieguessinggame(self):
        # starting a game with no game running
        self.update.message.text = "movieguessinggame"
        self.update.effective_chat.id = 1
        self.update.message.chat_id = 1

        self.assertEqual(movieguessinggame(self.update, context=CallbackContext), 0)
        # starting a second game, with the game already running for this id
        self.running_MovieGames[1] = Quiz()
        self.assertEqual(movieguessinggame(self.update, context=CallbackContext), None)

    def test_playmode(self):
        # testing the choose playmode function
        self.update.message.text = "Easy"
        self.update.message.chat_id = 2
        self.assertEqual(playmode(self.update, context=CallbackContext), 1)
        self.update.message.text = "Easy"
        self.update.message.chat_id = 3
        self.assertEqual(playmode(self.update, context=CallbackContext), 1)

    def test_movieguess(self):
        # wrong answer in easy playmode
        self.update.message.text = "That is wrong"
        self.update.effective_chat.id = 2
        self.update.message.chat_id = 4
        self.running_MovieGames[2] = Quiz()
        self.running_MovieGames[2].playmodus = "Easy"
        self.assertEqual(movieguess(self.update, context=CallbackContext), ConversationHandler.END)

        # right answer in easy playmode
        self.update.effective_chat.id = 3
        self.update.message.chat_id = 5
        self.running_MovieGames[3] = Quiz()
        self.update.message.text = self.running_MovieGames[3].answer
        self.running_MovieGames[3].playmodus = "Easy"
        self.assertEqual(movieguess(self.update, context=CallbackContext), ConversationHandler.END)

        # wrong answer in hard playmode
        self.update.message.text = "That is wrong"
        self.update.message.chat_id = 6
        self.update.effective_chat.id = 4
        self.running_MovieGames[4] = Quiz()
        self.running_MovieGames[4].playmodus = "Hard"
        self.assertEqual(movieguess(self.update, context=CallbackContext), 1)

        # wrong answer in hard playmode exceeding the number of guesses allowed
        self.update.message.text = "That is wrong"
        self.update.message.chat_id = 7
        self.update.effective_chat.id = 5
        self.running_MovieGames[5] = Quiz()
        self.running_MovieGames[5].playmodus = "Hard"
        self.running_MovieGames[5].guesscount = 5
        self.assertEqual(movieguess(self.update, context=CallbackContext), ConversationHandler.END)

        # right answer in hard playmode
        self.update.effective_chat.id = 6
        self.update.message.chat_id = 8
        self.running_MovieGames[6] = Quiz()
        self.update.message.text = self.running_MovieGames[6].answer
        self.running_MovieGames[6].playmodus = "Hard"
        self.assertEqual(movieguess(self.update, context=CallbackContext), ConversationHandler.END)

    def test_stopgame(self):
        # testing the stopgame function
        self.update.message.text = "stopgame"
        self.update.message.chat_id = 9
        self.update.effective_chat.id = 7
        self.running_MovieGames[7] = Quiz()
        self.assertEqual(stopgame(self.update, context=CallbackContext), ConversationHandler.END)

        # testing the stopgame function
        self.update.message.text = "stopgame"
        self.update.message.chat_id = 10
        self.update.effective_chat.id = 8
        self.assertEqual(stopgame(self.update, context=CallbackContext), None)


if __name__ == "__main__":
    unittest.main()


# HOW TO RUN THE TEST:
# python -m unittest testing/test_moviegame.test_moviegame_commands.py
# Windows: python3 -m unittest .\testing\test_moviegame\test_moviegame_commands.py
