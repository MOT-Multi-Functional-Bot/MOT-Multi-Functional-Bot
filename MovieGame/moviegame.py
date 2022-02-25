import requests
from telegram import Update, ForceReply, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters
from main_commands import log_input
import random

PLAYMODE, GUESS = range(2)

def movieGuessingGame(update: Update, context: CallbackContext) -> int:
    """Movie guessing Game"""
    log_input(update)
    reply_keyboard = [['Easy', 'Hard']]
    update.message.reply_text("You have started the movie guessing game!\n\n" "Which playmode do you chose?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True, input_field_placeholder = "Easy or Hard Mode?"),)
    return PLAYMODE

def playMode(update: Update, context: CallbackContext) -> int:
    log_input(update)
    
    questions = [("👳‍♂️ 🚣 🐯",  "life of pi"), ("👧 🐸 👑" ,  "princess and the frog"), ("🚀 ✨ 👩 🌍",  "gravity"), ("5️⃣ 0️⃣ 0️⃣ 🌞 ❤️" ,  "500 days of summer"), ("🔪 👩 🚿" , "psycho"), ("👧 ❗ ❓ ✈️", "Airplane"), ("👨 👨 ❤️ 🏔️" , "Brokeback mountain"), ("🇯🇵 💣 🇺🇸 ⚓" , "pearl harbour"), ("👠 👰‍♀️ ⌚ 🌙" ,  "cinderella"), ("👦 🏠 👨 👨", "home alone"), ("👼 ⛪ 👹", "angels and demons"), ("🐀 🍲 🍛 🍝 🍜", "ratatouille"), ("✏️ 📔 💏" , "the notebook"), ("🐳 ➡️ 🌊", "free willy"), ("🌩️ 👨 🔨" , "thor"), ("🩸 💍" , "Blood diamond"), ("🎥 👣 👻" , "Scary Movie"), ("👨 ➡️ 🎅" , "Santa Clause"), ("🌍 🐒 🐒 🐒" , "Planet of the apes"), ("🐼 👊", "Kung Fu Panda"), ("👨 🧸 🍻" , "Ted"), ("👦 🍫 🏭" , "Charlie and the chocolate factory"), ("😈 👗 👠" , "The devil wears prada"), ("🚢 🧊 🏔️", "Titanic"), ("👦 💍 ➡️ 🌋", "Lord of the rings"), ("👽 📞 🔈 👦 🚲 🌕", "ET"), ("🍴 🙏 ❤️", "Eat Pray Love"), ("💇‍♀️ 🇫🇷 👸 🎶", "Les misérables"), ("👑 💬 🎤" , "The kings speech"), ("🌃 🏦 👨 🔦 🗿 🐒" , "night at the museum")]
    quiz = random.randint(0,len(questions))
    false1 = random.randint(0,len(questions))
    false2 = random.randint(0,len(questions))
    false3 = random.randint(0,len(questions))
    update.message.reply_text("You chose" + update.message.text +"mode")
    if update.message.text == "Easy":
        global playmodus
        playmodus = "Easy"
        update.message.reply_text("Easy Peasy Lemon Squeezy")
        global answer
        answer = questions[quiz][1]
        reply_keyboard = [[answer , questions[false1][1], questions[false2][1], questions[false3][1]]]
        update.message.reply_text("The movie you need to guess is:" + questions[quiz][0] , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True, input_field_placeholder = "A, B, C oder D?"),)
        
    return GUESS

def movieGuess(update: Update, context: CallbackContext) -> None:
    log_input(update)
    if playmodus == "Easy": 
        if update.message.text != answer:
            update.message.reply_text("Verdammt, knapp daneben, die richtige Antwort wäre " + answer)
        else:
            update.message.reply_text("Herzlichen Glückwunsch! Du hast gewonnen!")
    return ConversationHandler.END


def stopgame(update: Update, context: CallbackContext) -> int:
    log_input(update)
    update.message.reply_text("You ended the game")
    return ConversationHandler.END

