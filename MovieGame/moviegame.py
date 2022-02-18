import requests
from telegram import Update, ForceReply, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters
from main_commands import log_input

PLAYMODE, GUESS = range(2)

def movieGuessingGame(update: Update, context: CallbackContext) -> int:
    """Movie guessing Game"""
    log_input(update)
    update.message.reply_text("You have started the movie guessing game!\n\n" "Which playmode do you chose?", reply_markup=ReplyKeyboardMarkup, one_time_keyboard = True, input_field_placeholder = "Easy or Hard Mode?")
    return PLAYMODE

def playMode(update: Update, context: CallbackContext) -> None:
    

