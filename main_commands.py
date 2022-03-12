from datetime import datetime
from telegram import Message, Update
from telegram.ext import CallbackContext
import requests


def log_input(update):
    print(f"[{datetime.now()}] {str(update.message.chat_id)} used: '{update.message.text}'")


def send_message(update: Update, text: str) -> Message:
    return update.message.reply_text(text)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    log_input(update)
    user = update.effective_user
    msg = f"Hi {user['first_name']}, Welcome to the MOT-Bot!\n"
    msg += f"Use:\n"
    msg += f"- /wordle if you want to play wordle. \n"
    msg += f"- /numbergame if you want to do some number guessing. \n"
    msg += f"- /movieGuessingGame if you want to guess a movie title from a set of emojis.\n "
    msg += f"- /help if you want further instructions on each game."
    send_message(update, msg)


def help(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    log_input(update)
    msg = "Sorry, we don't care.\n\n"
    msg += "Just kidding! This Bot provides you with three games and some other entertainment features:\n\n"
    msg += "The /wordle game is a game, where the Bot chooses a word and you have 6 guesses to guess the right word.\n\n"
    msg += "When you choose the /numbergame the bot chooses a number that you have to guess. The bot will give you hints if the chosen number is higher or lower than your guess.\n\n"
    msg += "When playing the /movieGuessingGame, the bot will provide you a set of emojis and you have to guess the respective movie title. There are two playmodes you kann play in easy and hard.\n\n"
    msg += "For other entertainment you can use the /cat command and the Bot will send you a cute picture of a cat or the /noodle command to get attacked with a noodles :D\n\n"
    msg += "Have fun!"
    send_message(update, msg)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    log_input(update)
    send_message(update, f"{update.message.text}, thats weird isn't it ?")


def noodle(update: Update, context: CallbackContext) -> None:
    """Spam back at the user."""
    log_input(update)
    for i in range(10):
        send_message(update, "🍜🍜NOODLEATTACK!!🍜🍜")


def get_url():
    """ "Get a random cat"""
    contents = requests.get("https://cataas.com/cat?json=true").json()
    url = contents["url"]
    return "https://cataas.com/" + url


def cat(update: Update, context: CallbackContext) -> None:
    """Send cat pic."""
    log_input(update)
    url = get_url()
    update.message.reply_photo(url)
