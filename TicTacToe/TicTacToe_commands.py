from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
import TicTacToe.TicTacToe_Multiplayer.TicTacToeMultiplayer
import TicTacToe.TicTacToe_Singleplayer.AlphaBetaPruningMemoization


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def TicTacToe_Multiplayer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Multiplayer!")

    TicTacToe.TicTacToe_Multiplayer.TicTacToeMultiplayer.main(update, CallbackContext)


def TicTacToe_Single(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Singleplayer!")
    TicTacToe.TicTacToe_Singleplayer.TicTacToe.main(0,  update, CallbackContext)
