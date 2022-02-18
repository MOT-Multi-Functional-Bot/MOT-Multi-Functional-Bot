from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext

def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)

def TicTacToe_main(update: Update, context:CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe!")
    

