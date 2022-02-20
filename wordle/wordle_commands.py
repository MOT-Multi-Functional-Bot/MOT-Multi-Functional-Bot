from telegram import Update
from telegram.ext import CallbackContext
from main_commands import log_input


def wordle(update: Update, context: CallbackContext) -> None:
    """Start the game"""
    log_input(update)
    update.message.reply_text("The Game has started! You can now use /guess start guessing!")


def guess(update: Update, context: CallbackContext) -> None:
    """Catch the user's guess"""
    log_input(update)
    update.message.reply_text("User Input: " + update.message.text)
