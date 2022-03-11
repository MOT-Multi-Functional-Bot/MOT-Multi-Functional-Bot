from telegram import Message, Update
from telegram.ext import CallbackContext
import requests


def log_input(update):
    print(f"{str(update.message.chat_id)} entered: '{update.message.text}'")


def send_message(update: Update, text: str) -> Message:
    return update.message.reply_text(text)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    log_input(update)
    user = update.effective_user
    send_message(update, f"Hi {user['first_name']}, Welcome to the MOT-Bot! \nSend:\n-/wordle if you want to play the Wordle game. \n-/numbergame if you want to do some number guessing. \n-/movieGuessingGame if you want to guess a movie title from a set of emojis. \n-/help if you want further instructions on each game. ")



def help(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    log_input(update)
    send_message(update, "Sorry, we don't care. \n\nJust kidding! This Bot provides you with three games and some other entertainment features: \n\nThe /wordle game is a game, where the Bot chooses a word and you have 6 guesses to guess the right word. \n\nWhen you choose the /numbergame the bot chooses a number that you have to guess. The bot will give you hints if the chosen number is higher or lower than your guess. \n\nWhen playing the /movieGuessingGame, the bot will provide you a set of emojis and you have to guess the respective movie title. There are two playmodes you kann play in easy and hard. \n\nFor other entertainment you can use the /cat command and the Bot will send you cute pictures of cats or the /noodle command to get attacked with a 'Nudelattacke' :D \n\nHave fun! ")


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    log_input(update)
    send_message(update, f"{update.message.text}, thats weird isn't it ?")


def noodle(update: Update, context: CallbackContext) -> None:
    """Spam back at the user."""
    log_input(update)
    for i in range(10):
        send_message(update, "🍜🍜NOODLEATTACK!!🍜🍜")


def get_url():
    """ "Get a random cat"""
    contents = requests.get("https://cataas.com/cat?json=true").json()
    url = contents["url"]
    return "https://cataas.com/" + url


def cat(update: Update, context: CallbackContext) -> None:
    """Send cat pic."""
    log_input(update)
    url = get_url()
    update.message.reply_photo(url)
