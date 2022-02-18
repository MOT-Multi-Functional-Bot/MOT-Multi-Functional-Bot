from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def numbergame(update: Update, context: CallbackContext) -> None:
    """Play the number game"""
    log_input(update)
    update.message.reply_text("Guess words by using /guess 'word'")


def guess(update: Update, context: CallbackContext) -> None:
    pass