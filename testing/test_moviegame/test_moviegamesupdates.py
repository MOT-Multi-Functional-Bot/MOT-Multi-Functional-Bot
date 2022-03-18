from testing.test_moviegame.test_moviegamesmessage import messagemovie
from testing.test_moviegame.test_moviegamechat import chatmovie

class Updatesmovie(messagemovie, chatmovie):
    def __init__(self, messagemovie, chatmovie) -> None:
        self.message = messagemovie 
        self.effective_chat = chatmovie

    