from conf import API_KEY
from main_commands import cat, echo, help, noodle, start
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater
from games.wordle.wordle_commands import guess, howto, stats, stop, wordle
from games.MovieGame.moviegame import *
from games.numbergame.numbergame_commands import numb, stopnumbergame, numbergame, newnum


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

    # Main Commands
    dispatcher.add_handler(CommandHandler("cat", cat))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("noodle", noodle))
    dispatcher.add_handler(CommandHandler("start", start))

    # Wordle Commands
    dispatcher.add_handler(CommandHandler("guess", guess))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("wordle", wordle))
    dispatcher.add_handler(CommandHandler("stats", stats))
    dispatcher.add_handler(CommandHandler("howto", howto))

    # MovieGuessingGame added Conversation_Handler
    dispatcher.add_handler(movie_Guessing_Game)

    # MovieGuessingGame Conversation Handler
    movie_Guessing_Game = ConversationHandler(
        entry_points=[CommandHandler("MovieGuessingGame", movieGuessingGame)],
        states={
            PLAYMODE: [MessageHandler(Filters.regex("^(Easy|Hard)$"), playMode)],
            GUESS: [MessageHandler(Filters.regex("^[\w*\s]*$"), movieGuess)],
        },
        fallbacks=[CommandHandler("stopgame", stopgame)],
    )

    # MovieGuessingGame Commands
    dispatcher.add_handler(movie_Guessing_Game)

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
