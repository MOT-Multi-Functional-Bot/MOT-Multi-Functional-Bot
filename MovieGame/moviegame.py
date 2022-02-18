import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
from main_commands import log_input

def movieGuessingGame(update: Update, context: CallbackContext) -> None:
    """Send cat pic."""
    log_input(update)
    update.message.reply_photo()