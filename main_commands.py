from telegram import Message, Update
from telegram.ext import CallbackContext
import requests


def log_input(update):
    print(f"{str(update.message.chat_id)} entered: '{update.message.text}'")


def send_message(update: Update, text: str) -> Message:
    return update.message.reply_text(text)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    log_input(update)
    user = update.effective_user
    send_message(update, f"Hi {user['first_name']}, Welcome to the MOT-Bot!")


def help(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    log_input(update)
    send_message(update, "Sorry, we don't care.")


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
