from telegram import Update, ForceReply, Message
from telegram.ext import CallbackContext
import requests


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def send_message(update: Update, text: str) -> Message:
    return update.message.reply_text(text)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    log_input(update)
    user = update.effective_user
    update.message.reply_markdown_v2(
        rf"Hi {user.mention_markdown_v2()}\!",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    log_input(update)
    send_message(update, "HELP YOURSELVES!!eleven11!!")


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    log_input(update)
    send_message(update, update.message.text + " ?")


def nudel(update: Update, context: CallbackContext) -> None:
    """Spam back at the user."""
    log_input(update)
    for i in range(10):
        send_message(update, "🍜🍜NUDELATTACKE!!!!!🍜🍜")


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
