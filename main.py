#!/usr/bin/env python
# pylint: disable=C0116,W0613

import requests
from Games.wordle import *
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from conf import API_KEY


# Define a few command handlers. These usually take the two arguments update and
# context.


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    log_input(update)
    update.message.reply_text('HELP YOURSELVES!!eleven11!!')


def get_url():
    """"Get a random cat"""
    contents = requests.get('https://cataas.com/cat?json=true').json()
    url = contents['url']
    return "https://cataas.com/"+url


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    log_input(update)
    update.message.reply_text(update.message.text+" ?")


def nudel(update: Update, context: CallbackContext) -> None:
    """Spam back at the user."""
    log_input(update)
    for i in range(10):
        update.message.reply_text("🍜🍜NUDELATTACKE!!!!!🍜🍜")


def cat(update: Update, context: CallbackContext) -> None:
    """Send cat pic."""
    log_input(update)
    url = get_url()
    update.message.reply_photo(url)

def wordle(update: Update, context:CallbackContext) -> None:
    """Play the wordle game"""
    log_input(update)
    update.message.reply_text("Now you are playing Wordle\ntype in a Word with 5 letters:")
    print("Try executing worlde Game")
    wordle_game()
    



def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("nudel", nudel))
    dispatcher.add_handler(CommandHandler("cat", cat))
    dispatcher.add_handler(CommandHandler("wordle", wordle))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
