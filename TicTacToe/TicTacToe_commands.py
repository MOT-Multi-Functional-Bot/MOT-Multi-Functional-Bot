from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
import TicTacToe.TicTacToe_Multiplayer.TicTacToeMultiplayer
import TicTacToe.TicTacToe_Singleplayer.AlphaBetaPruningMemoization


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def TicTacToe_Multiplayer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Multiplayer!")
    Board = {'0': ' ', '1': ' ', '2': ' ',
             '3': ' ', '4': ' ', '5': ' ',
             '6': ' ', '7': ' ', '8': ' '}

    board_keys = []

    for key in Board:
        board_keys.append(key)

    TicTacToe.TicTacToe_Multiplayer.TicTacToeMultiplayer.main(
        Board, board_keys, update, CallbackContext)


def TicTacToe_Single(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Singleplayer!")
    TicTacToe.TicTacToe_Singleplayer.AlphaBetaPruningMemoization.main(0,  update, CallbackContext)
