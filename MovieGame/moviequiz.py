from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from main_commands import log_input
import random

# Quiz is a class that contains all the information on a MovieGuessingGame
# this class is necessary in order to differentiate the different games for the different users.

class Quiz:
    def __init__(self) -> None:

        # possible Quizzes
        self.questions = [
        ("👳‍♂️ 🚣 🐯", "life of pi"),
        ("👧 🐸 👑", "princess and the frog"),
        ("🚀 ✨ 👩 🌍", "gravity"),
        ("5️⃣ 0️⃣ 0️⃣ 🌞 ❤️", "500 days of summer"),
        ("🔪 👩 🚿", "psycho"),
        ("👧 ❗ ❓ ✈️", "Airplane"),
        ("👨 👨 ❤️ 🏔️", "Brokeback mountain"),
        ("🇯🇵 💣 🇺🇸 ⚓", "pearl harbour"),
        ("👠 👰‍♀️ ⌚ 🌙", "cinderella"),
        ("👦 🏠 👨 👨", "home alone"),
        ("👼 ⛪ 👹", "angels and demons"),
        ("🐀 🍲 🍛 🍝 🍜", "ratatouille"),
        ("✏️ 📔 💏", "the notebook"),
        ("🐳 ➡️ 🌊", "free willy"),
        ("🌩️ 👨 🔨", "thor"),
        ("🩸 💍", "Blood diamond"),
        ("🎥 👣 👻", "Scary Movie"),
        ("👨 ➡️ 🎅", "Santa Clause"),
        ("🌍 🐒 🐒 🐒", "Planet of the apes"),
        ("🐼 👊", "Kung Fu Panda"),
        ("👨 🧸 🍻", "Ted"),
        ("👦 🍫 🏭", "Charlie and the chocolate factory"),
        ("😈 👗 👠", "The devil wears prada"),
        ("🚢 🧊 🏔️", "Titanic"),
        ("👦 💍 ➡️ 🌋", "Lord of the rings"),
        ("👽 📞 🔈 👦 🚲 🌕", "ET"),
        ("🍴 🙏 ❤️", "Eat Pray Love"),
        ("💇‍♀️ 🇫🇷 👸 🎶", "Les misérables"),
        ("👑 💬 🎤", "The kings speech"),
        ("🌃 🏦 👨 🔦 🗿 🐒", "night at the museum"),
        ]

        # randomized choice of a quiz and optional choose options for Easy playmode
        self.quiz = random.randint(0, len(self.questions)-1)
        self.false1 = random.randint(0, len(self.questions)-1)
        self.false2 = random.randint(0, len(self.questions)-1)
        self.false3 = random.randint(0, len(self.questions)-1)

        # guesscount for hard mode
        self.guesscount = 0

        # setting the answer and the question of the Quiz with the previously randomly chosen self.quiz variable
        self.answer = self.questions[self.quiz][1]
        self.question = self.questions[self.quiz][0]

        # initializing the variable playmodus
        self.playmodus = None

        # setting the answer options for the Easy mode by using the previously randomly chosen self.false1, self.false2 and self.false3 variables
        self.option2 = self.questions[self.false1][1]
        self.option3 = self.questions[self.false2][1]
        self.option4 = self.questions[self.false3][1]