#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from conf import API_KEY
from main_commands import start, help_command, nudel, cat, echo

# from wordle_commands import wordle, guess
from MovieGame.moviegame import *

# Define a few command handlers. These usually take the two arguments update and
# context.


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # MovieGuessingGame Conversation Handler
    movie_Guessing_Game = ConversationHandler(
        entry_points=[CommandHandler("MovieGuessingGame", movieGuessingGame)],
        states={
            PLAYMODE: [MessageHandler(Filters.regex("^(Easy|Hard)$"), playMode)],
            GUESS: [MessageHandler(Filters.regex("^[\w*\s]*$"), movieGuess)],
        },
        fallbacks=[CommandHandler("stopgame", stopgame)],
    )

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("nudel", nudel))
    dispatcher.add_handler(CommandHandler("cat", cat))

    # MovieGuessingGame added Conversation_Handler
    dispatcher.add_handler(movie_Guessing_Game)

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
