from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from main_commands import log_input
import random

class Quiz:
    def __init__(self) -> None:
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

        self.quiz = random.randint(0, len(self.questions)-1)
        self.false1 = random.randint(0, len(self.questions)-1)
        self.false2 = random.randint(0, len(self.questions)-1)
        self.false3 = random.randint(0, len(self.questions)-1)
        self.guesscount = 0
        self.answer = self.questions[self.quiz][1]
        self.question = self.questions[self.quiz][0]
        self.playmodus = None
        self.option2 = self.questions[self.false1][1]
        self.option3 = self.questions[self.false2][1]
        self.option4 = self.questions[self.false3][1]