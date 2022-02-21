from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
from TicTacToe.ticTac import game

def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)

def TicTacToe_main(update: Update, context:CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe!")
    Board   =  {'0': ' ' , '1': ' ' , '2': ' ' ,
            '3': ' ' , '4': ' ' , '5': ' ' ,
            '6': ' ' , '7': ' ' , '8': ' ' }

    board_keys = []

    for key in Board:
        board_keys.append(key)


    
    game(Board, board_keys, update, CallbackContext)


