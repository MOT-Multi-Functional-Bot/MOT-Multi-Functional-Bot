from conf import API_KEY
from main_commands import start, help_command, nudel, cat, echo
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from games.numbergame.numbergame_commands import numb, stopnumbergame, numbergame, newnum


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Main Commands
    dispatcher.add_handler(CommandHandler("cat", cat))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("nudel", nudel))
    dispatcher.add_handler(CommandHandler("start", start))

    # Numbergame Commands
    dispatcher.add_handler(CommandHandler("numb", numb))
    dispatcher.add_handler(CommandHandler("stopnumbergame", stopnumbergame))
    dispatcher.add_handler(CommandHandler("numbergame", numbergame))
    dispatcher.add_handler(CommandHandler("newnum", newnum))

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
