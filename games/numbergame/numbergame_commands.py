from telegram import Update, Message
from telegram.ext import CallbackContext
from .exceptions import GameOverEx, GuessEx
from .numbergame import numbergame
from .helperfunctions import log_input, send_message


class GameMessage(numbergame):
    def __init__(self, message: Message):
        super().__init__()
        self.err_msg = ""
        self.message = message

    def status(self):
        message = super().state()
        message += f"\n\n{self.err_msg}"
        self.err_msg = ""
        return message

    # Update the static message for the player
    def update_message(self):
        edit_message(self.message, self.status())


# function to edit messages
def edit_message(message: Message, text: str) -> Message:
    return message.edit_text(text)


# Register of all open games
running_games: "dict[int, GameMessage]" = {}


# Check if a game is running
def check_game_status(chat_id: int) -> bool:
    global running_games
    return running_games.get(chat_id) is not None


# Main command
def numbergame(update: Update, context: CallbackContext) -> None:
    """Play the numbergame"""
    log_input(update)
    global running_games

    if check_game_status(update.effective_chat.id):
        send_message(update, "You already started a game!")
        return

    running_games[update.effective_chat.id] = GameMessage(
        send_message(
            update,
            "I choose my number between 0-100! \nUse /numb 'Number' to start guessing!",
        )
    )


def numb(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    if not check_game_status(update.effective_chat.id):
        send_message(update, "Start a game with /numbergame")
        return

    player_input = " ".join(context.args).upper()

    if player_input == "":
        send_message(update, "Guess a number by using /numb 'number'")
        return

    game = running_games[update.effective_chat.id]

    userid = str(update.message.chat_id)

    try:
        game.numb(player_input, userid)

    except GuessEx as e:
        game.err_msg = str(e)
        update.message.reply_text(game.err_msg)

    except GameOverEx as e:
        game.err_msg = str(e)
        update.message.reply_text(game.results())
        del running_games[update.effective_chat.id]

    game.status()


def stopnumbergame(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    if check_game_status(update.effective_chat.id):
        del running_games[update.effective_chat.id]
        send_message(update, "Game stopped! Start new game with /numbergame")
        return

    send_message(update, "There is no game running!")


def newnum(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    if not check_game_status(update.effective_chat.id):
        send_message(update, "Start a game with /numbergame")
        return

    player_input = " ".join(context.args).upper()

    if player_input == "":
        send_message(
            update,
            "Set a new range with \n\n/newnum 'Number'. \n\nThe range is max 1.000.000.\nYou can only reset once a game.\nAnd your tries will be reset.",
        )
        return

    game = running_games[update.effective_chat.id]

    userid = str(update.message.chat_id)

    try:
        game.newnum(player_input, userid)

    except GuessEx as e:
        game.err_msg = str(e)
        update.message.reply_text(game.err_msg)

    game.status()
