from main_commands import log_input, send_message
from telegram import Update
from zmq import Message
from telegram.ext import CallbackContext
from TicTacToe.TicTacToe_main import TicTacToe_Game



class GameMessage(TicTacToe_Game):
    def __init__(self, message: Message) -> None:
        super().__init__()
        self.err_msg = ""
        self.message = message

    def status(self):
        message = super().state()
        message+= f"\n\n{self.err_msg}"
        self.err_msg = ""
        return message

    def update_message(self):
        edit_message(self.message, self.status())

def edit_message(message: Message, text: str) -> Message:
    return message.edit_text(text)


# Register of all open games
running_games: "dict[int, GameMessage]" = {}


# Check if a game is running
def check_game_status(chat_id: int) -> bool:
    global running_games
    return running_games.get(chat_id) is not None



def TicTacToe(update: Update, context: CallbackContext) -> None:
    """ Play the TicTacToe game """
    log_input(update)
    global running_games

    if check_game_status(update.effective_chat.id):
        send_message(update, "Du hast das Spiel bereits gestartet!")
        return 
    
    running_games[update.effective_chat.id] = GameMessage(
        send_message(update, "Das Spiel TicTacToe wurde gestartet!")
    )


def stop(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    # check if there is an open game for the chat id
    if check_game_status(update.effective_chat.id):
        # remove chat id from running games
        del running_games[update.effective_chat.id]
        send_message(update, "Spiel gestoppt!")
        return

    # gets sent, if no game is running
    send_message(update, "Aktuell läuft noch kein Spiel!")


    #update.message.reply_text("You are trying to play TicTacToe Singleplayer!")
    #TicTacToe.TicTacToe_Singleplayer.TicTacToe.main(0,  update, CallbackContext)