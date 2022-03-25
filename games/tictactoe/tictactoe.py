from telegram import Update, Message
from telegram.ext import CallbackContext
from .helperfunctions import log_input
import random


global gAllLines, gPlayers
gPlayers = [0, 1]


class tictactoeGameClass:
    def __init__(self) -> None:
        self.states = 0
        self.cache = {}


# Functions:


def set_bits(Bits):
    result = 0
    for b in Bits:
        result |= 1 << b
    return result


def set_bit(n):
    return 1 << n


gAllLines = [
    set_bits([0, 1, 2]),
    set_bits([3, 4, 5]),
    set_bits([6, 7, 8]),
    set_bits([0, 3, 6]),
    set_bits([1, 4, 7]),
    set_bits([2, 5, 8]),
    set_bits([0, 4, 8]),
    set_bits([2, 4, 6]),
]

# to_Board sets '⭕', '✖', '⬜' depending on the binary representation
def to_board(states):
    result = ""
    for cell in range(9):
        if states & (2**cell) != 0:
            result += "✖"
        elif states & (2 ** (cell + 9)) != 0:
            result += "⭕"
        else:
            result += "⬜"
        if (cell + 1) % 3 == 0:
            result += "\n"
    return result


# returns the set of empty fields
def empty(states):
    Free = {n for n in range(9)}
    Free -= {n for n in range(9) if states & (1 << n) != 0}
    Free -= {n for n in range(9) if states & (1 << (9 + n)) != 0}
    return Free


# calculate all possible next states, reachable from the current state, depending on the empty fields
def next_states(states, player):
    Empty = empty(states)
    Result = []
    for n in Empty:
        next_state = states | set_bit(player * 9 + n)
        Result.append(next_state)
    return Result


# returns wether the user or the computer wins
def utility(states):
    for mask in gAllLines:
        if states & mask == mask:
            return 1
        if (states >> 9) & mask == mask:
            return -1
    # bin(511) = '0b111111111' --> checks wether all fields are occupied and therefore wether the game is finished
    if (states & 511) | (states >> 9) != 511:
        return None
    return 0


# Is the game over in the current state
def finished(states):
    return utility(states) != None


# Gets the users input
# def get_move(state, update):
#     try:
#         row, col = input('Move eingeben bitte: ').split(',')
#         row, col = int(row), int(col)
#         mask = set_bit(9 + row * 3 + col)
#         if state & mask == 0:
#             return state | mask
#         update.message.reply_text("Nicht cheaten.")
#     except:
#         update.message.reply_text('Illegaler Input.')
#         update.message.reply_text(
#             'Reihen und Zeilen sind Elemente aus: {0,1,2}.')


def final_msg(states, update):
    if finished(states):
        if utility(states) == -1:
            update.message.reply_text("Du hast gewonnen!")
        elif utility(states) == 1:
            update.message.reply_text("Der Computer hat gewonnen")
        else:
            update.message.reply_text("Unentschieden")


def best_move(game):
    NS = next_states(game.states, gPlayers[0])
    bestValue = evaluate(game.states, game, maxValue, -1, 1)
    BestMoves = [s for s in NS if evaluate(s, game, minValue, -1, 1) == bestValue]
    BestState = random.choice(BestMoves)
    return bestValue, BestState


def evaluate(states, game, f, alpha=-1, beta=1):
    if states in game.cache:
        flag, v = game.cache[states]
        if flag == "=":
            return v
        if flag == "≤":
            if v <= alpha:
                return v
            elif alpha < v < beta:
                w = f(states, game, alpha, v)
                store_cache(game, states, alpha, v, w)
                return w
            else:
                w = f(states, game, alpha, beta)
                store_cache(game, states, alpha, beta, w)
                return w
        if flag == "≥":
            if beta <= v:
                return v
            elif alpha < v < beta:
                w = f(states, game, v, beta)
                store_cache(game, states, v, beta, w)
                return w
            else:
                w = f(states, game, alpha, beta)
                store_cache(game, states, alpha, beta, w)
                return w
    else:
        v = f(states, game, alpha, beta)
        store_cache(game, states, alpha, beta, v)
        return v


def store_cache(game, states, alpha, beta, v):

    if v <= alpha:
        game.cache[states] = ("≤", v)
    elif v < beta:
        game.cache[states] = ("=", v)
    else:
        game.cache[states] = ("≥", v)


def maxValue(states, game, alpha, beta):
    if finished(states):
        return utility(states)
    if alpha >= beta:
        return alpha
    v = alpha
    for ns in next_states(states, gPlayers[0]):
        v = max(v, evaluate(ns, game, minValue, v, beta))
        if v >= beta:
            return v
    return v


def minValue(states, game, alpha, beta):
    if finished(states):
        return utility(states)
    if beta <= alpha:
        return beta
    v = beta
    for ns in next_states(states, gPlayers[1]):
        v = min(v, evaluate(ns, game, maxValue, alpha, v))
        if v <= alpha:
            return v
    return v


# ==========================================================================
# ==========================================================================
# ==========================================================================


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


class GameMessage(tictactoeGameClass):
    def __init__(self, message: Message):
        super().__init__()
        self.err_msg = ""
        self.message = message

    def status(self):
        # message = super().state()
        message = f"\n\n{self.err_msg}"
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
            "Let's start, I choose my Position! \nUse /pos 'Position [0-2],[0-2]' to start by setting your position!",
        )
    )


def pcPlay(update: Update):
    global running_games
    game = running_games[update.effective_chat.id]
    val, State = best_move(game)
    x = to_board(State)
    game.states = State
    update.message.reply_text(x)
    if finished(game.states):
        final_msg(game.states, update)
        del running_games[update.effective_chat.id]


def pos(update: Update, context: CallbackContext):
    log_input(update)
    global running_games

    if not check_game_status(update.effective_chat.id):
        send_message(update, "Start a game with /tic")
        return

    player_input = " ".join(context.args).split(",")

    if player_input == "":
        send_message(update, "Set your position with: /pos [0-2],[0-2]")
        return

    game = running_games[update.effective_chat.id]

    # userid = str(update.message.chat_id)

    try:
        row, col = player_input
        row, col = int(row), int(col)
        isValidInput(row, col, update)
        mask = set_bit(9 + row * 3 + col)
        mask2 = set_bit(row * 3 + col)
        print(f"MASKE = {bin(mask)}")
        if game.states & mask == 0 and game.states & mask2 == 0:
            x = game.states | mask
            game.states = x
            # update.message.reply_text(to_board(x))
            if finished(game.states):
                update.message.reply_text(final_msg(game.states, update))
                del running_games[update.effective_chat.id]

            else:
                pcPlay(update)
        else:
            raise update.message.reply_text("Nicht cheaten.")
    except:
        if not finished(game.states):
            update.message.reply_text("🚨 Cheater 🚨")
            update.message.reply_text(
                'A valid input would be "/pos [0-2],[0-2]"\nTry again :)'
            )


def isValidInput(row, col, update):
    if row > 2:
        update.message.reply_text(
            "Your input was invalid: your row should be in range of 0-2"
        )
        raise

    elif col > 2:
        update.message.reply_text(
            "Your input was invalid: your row should be in range of 0-2"
        )
        raise

    elif row < 0 or col < 0:
        update.message.reply_text(
            "Your input was invalid: row and col must be in range of 0-2"
        )
        raise


def stoptictactoe(update: Update, context: CallbackContext) -> None:
    log_input(update)
    global running_games

    if check_game_status(update.effective_chat.id):
        del running_games[update.effective_chat.id]
        send_message(update, "Game stopped! Start new game with /tic")
        return

    send_message(update, "There is no game running!")
