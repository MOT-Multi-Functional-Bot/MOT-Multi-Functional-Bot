from telegram import Update
from telegram.ext import CallbackContext
from main_commands import log_input

running_games = {}  # list of all running games by chatid


def wordle(update: Update, context: CallbackContext) -> None:
    """Start the game"""
    log_input(update)
    update.message.reply_text("The Game has started! You can now use /guess start guessing!")
    running_games[update.message.chat_id] = 1


def guess(update: Update, context: CallbackContext) -> None:
    """Catch the user's guess"""
    log_input(update)

    # Check if user already started a game
    if not running_games.get(update.message.chat_id):
        update.message.reply_text("You need to start a game first! Start a game with /wordle")
        return

    user_input = "".join(context.args)  # Get User input
    # Check if user made a guess
    if user_input == "":
        update.message.reply_text("Guess a word by using /guess 'word' !")
        return
