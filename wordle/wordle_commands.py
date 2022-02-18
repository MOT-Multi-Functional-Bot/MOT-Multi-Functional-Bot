from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def wordle(update: Update, context: CallbackContext) -> None:
    """Play the wordle game"""
    log_input(update)
    update.message.reply_text("Guess words by using /guess 'word'")


def guess(update: Update, context: CallbackContext) -> None:
    pass
