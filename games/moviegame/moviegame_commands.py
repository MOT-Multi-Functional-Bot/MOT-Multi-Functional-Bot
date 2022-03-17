from games.moviegame.moviequiz import Quiz
from main_commands import log_input
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler

PLAYMODE, GUESS = range(2)

# running_MovieGames: Dictionary --> saving running games
global running_MovieGames
running_MovieGames = {}

# movieguessinggame --> entry point for the ConversationHandler starts the Movie Guessing Game
def movieguessinggame(update: Update, context: CallbackContext) -> int:
    """Movie guessing Game"""
    log_input(update)
    if update.effective_chat.id in running_MovieGames.keys():
        update.message.reply_text(
            "There is already a game running, if you want to start a new game enter /stopgame and then /movieguessinggame."
        )
    else:
        reply_keyboard = [["Easy", "Hard"]]
        update.message.reply_text(
            "You have started the movie guessing game!\n\n"
            "Which playmode do you chose? Easy or Hard? \n\n If you want to stop the game send /stopgame.",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard,
                one_time_keyboard=True,
                input_field_placeholder="Easy or Hard Mode?",
            ),
        )
        return PLAYMODE


# playMode --> handles the users playMode choice and creates a Quiz object for the user which contains information on the users Movie Guessing Game
def playmode(update: Update, context: CallbackContext) -> int:
    log_input(update)

    running_MovieGames[update.effective_chat.id] = Quiz()
    update.message.reply_text("You chose " + update.message.text + " mode")
    if update.message.text == "Easy":
        running_MovieGames[update.effective_chat.id].playmodus = "Easy"
        update.message.reply_text("Easy Peasy Lemon Squeezy")
        reply_keyboard = [
            {
                running_MovieGames[update.effective_chat.id].answer,
                running_MovieGames[update.effective_chat.id].option1,
                running_MovieGames[update.effective_chat.id].option2,
                running_MovieGames[update.effective_chat.id].option3,
            }
        ]
        update.message.reply_text(
            "The movie you need to guess is:" + running_MovieGames[update.effective_chat.id].question,
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard,
                one_time_keyboard=True,
                input_field_placeholder="A, B, C oder D?",
            ),
        )
    else:
        running_MovieGames[update.effective_chat.id].playmodus = "Hard"
        update.message.reply_text("Wow! Good Luck!")
        update.message.reply_text(
            "The movie you need to guess is:" + running_MovieGames[update.effective_chat.id].question
        )
    return GUESS


# movieGuess --> handles the users guesses within their respective playmode and eventually ends the game
def movieguess(update: Update, context: CallbackContext) -> None:
    log_input(update)
    if running_MovieGames[update.effective_chat.id].playmodus == "Easy":
        if update.message.text != running_MovieGames[update.effective_chat.id].answer:
            update.message.reply_text(
                "Verdammt, knapp daneben, die richtige Antwort wäre "
                + running_MovieGames[update.effective_chat.id].answer
            )
        else:
            update.message.reply_text("Herzlichen Glückwunsch! Du hast gewonnen!")
        del running_MovieGames[update.effective_chat.id]
        return ConversationHandler.END
    elif running_MovieGames[update.effective_chat.id].playmodus == "Hard":
        if update.message.text.casefold() == running_MovieGames[update.effective_chat.id].answer.casefold():
            update.message.reply_text("Herzlichen Glückwunsch! Du hast gewonnen!")
            del running_MovieGames[update.effective_chat.id]
            return ConversationHandler.END

        else:
            running_MovieGames[update.effective_chat.id].guesscount += 1
            if running_MovieGames[update.effective_chat.id].guesscount < 5:
                update.message.reply_text(
                    "Das ist leider nicht richtig du hast noch "
                    + str(5 - running_MovieGames[update.effective_chat.id].guesscount)
                    + " Versuch(e)!"
                )
                return GUESS
            else:
                update.message.reply_text(
                    "Du hast leider verloren! Die richtige Antwort wäre "
                    + running_MovieGames[update.effective_chat.id].answer
                    + " gewesen."
                )
                del running_MovieGames[update.effective_chat.id]
                return ConversationHandler.END


# stopgame --> enables the user to stop the game even if it is not yet finished
def stopgame(update: Update, context: CallbackContext) -> int:
    log_input(update)
    update.message.reply_text("You ended the game")
    return ConversationHandler.END
