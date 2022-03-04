from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
import TicTacToe.TicTacToeBitboard


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def TicTacToe_Single(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Singleplayer!")
    TicTacToe.TicTacToeBitboard.main(0,  update, CallbackContext)
