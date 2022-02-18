from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def numbers(update: Update, context: CallbackContext) -> None:
    """Play the Numbers game"""
    log_input(update)
    update.message.reply_text("start game with /number and a 'Number' for your guess range")


