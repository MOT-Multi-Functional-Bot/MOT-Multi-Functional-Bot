import random


class messagemovie:
    def __init__(self) -> None:
        self.text = None
        self.chat_id = random.randint(0, 100)

    def reply_text(self, text=None, reply_markup=None):
        pass
