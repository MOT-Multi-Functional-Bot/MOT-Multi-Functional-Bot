from telegram import Update, Message
from telegram.ext import CallbackContext
from .exceptions import GameOverEx, GuessEx
from .tictactoe import tictactoeGame
from main_commands import log_input


def send_message(update: Update, text: str) -> Message:
    return update.message.reply_text(text)

    # function to edit messages


def edit_message(message: Message, text: str) -> Message:
    return message.edit_text(text)


# Register of all open games
running_games: "dict[int, GameMessage]" = {}


# Check if a game is running
def check_game_status(chat_id: int) -> bool:
    global running_games
    return running_games.get(chat_id) is not None


class GameMessage(tictactoeGame):
    def __init__(self, message: Message):
        super().__init__()
        self.err_msg = ""
        self.message = message

    def status(self):
        message = super().state()
        message += f"\n\n{self.err_msg}"
        self.err_msg = ""
        return message

    # Update the status message for the player
    def update_message(self):
        edit_message(self.message, self.status())


# Main command
def tictactoeGame(update: Update, context: CallbackContext) -> None:
    """Play the tictactoeGame"""
    log_input(update)
    global running_games

    if check_game_status(update.effective_chat.id):
        send_message(update, "You already started a game!")
        return

    running_games[update.effective_chat.id] = GameMessage(
        send_message(
            update,
            "Let's start, I choose my Position! \nUse /pos 'Position [0-8]' to start by setting your position!",
        )
    )

def pos(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    if not check_game_status(update.effective_chat.id):
        send_message(update, "Start a game with /tic")
        return

    player_input = " ".join(context.args).upper()

    if player_input == "":
        send_message(update, "Set your position with: /pos 'number [0-8]'")
        return

    game = running_games[update.effective_chat.id]

    userid = str(update.message.chat_id)

    try:
        game.pos(player_input, userid)

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
        send_message(update, "Game stopped! Start new game with /tic")
        return

    send_message(update, "There is no game running!")


