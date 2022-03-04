from telegram import Update, ForceReply, Message
from telegram.ext import Updater, CallbackContext
from main_commands import send_message, log_input
from TicTacToe.TicTacToeBitboard import ticTac
from TicTacToe.exceptions import GameOverEx, GuessEx


# def log_input(update):
#     print(str(update.message.chat_id) + " entered: " + update.message.text)


# def TicTacToe_Single(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("You are trying to play TicTacToe Singleplayer!")
#     TicTacToe.TicTacToeBitboard.main(0,  update, CallbackContext)

running_games: "dict[int, GameMessage]" = {}


def ticTacToeGame(update: Update, context: CallbackContext) -> None:
    """Play the TicTacToe game"""
    log_input(update)
    global running_games

    if check_game_status(update.effective_chat.id):
        send_message(update, "You already started a game!")
        return

    running_games[update.effective_chat.id] = GameMessage(
        send_message(update, "The game has started! Use /guess '\{0-2\}},\{0-2\}}' to take a guess!")
    )


def check_game_status(chat_id: int) -> bool:
    global running_games
    return running_games.get(chat_id) is not None


def guess(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    # Check if a game is running
    if not check_game_status(update.effective_chat.id):
        send_message(update, "Start a game with /wordle")
        return

    # get player input
    print(f'\n\nContextShit = {context.args}\n\n')
    player_input = context.args[0]
    row, col = player_input.split(',')


    if player_input == "":
        send_message(update, "Guess a word by using /guess 'word'")
        return

    # get game info of playing player
    game = running_games[update.effective_chat.id]

    # run guess
    userid = str(update.message.chat_id)
    try:
        game.guess(row, col)

    # if error while guessing occurs display the error message to player
    except GuessEx as e:
        game.err_msg = str(e)

    # if game is over display the message to player
    except GameOverEx as e:
        game.err_msg = str(e)
        # Send Results to player
        update.message.reply_text(game.results())
        # delete running game from registry
        del running_games[update.effective_chat.id]

    game.update_message()


class GameMessage(ticTac):
    def __init__(self, message: Message):
        super().__init__()
        self.err_msg = ""
        self.message = message

    def status(self):
        message = super().State()
        message += f"\n\n{self.err_msg}"
        self.err_msg = ""
        return message
    
    # Update the statis message for the player
    def update_message(self):
        edit_message(self.message, self.status())




def edit_message(message: Message, text: str) -> Message:
    return message.edit_text(text)

# stop a running game
def stop(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    # check if there is an open game for the chat id
    if check_game_status(update.effective_chat.id):
        # remove chat id from running games
        del running_games[update.effective_chat.id]
        send_message(update, "Game stopped! Resume with /wordle!")
        return

    # gets sent, if no game is running
    send_message(update, "There is no game running!")