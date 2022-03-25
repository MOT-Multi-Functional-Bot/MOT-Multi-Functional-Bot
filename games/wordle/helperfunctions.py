from datetime import datetime
from telegram import Update, Message


def log_input(update):
    print(f"[{datetime.now()}] {str(update.message.chat_id)} : '{update.message.text}'")


def send_message(update: Update, text: str) -> Message:
    return update.message.reply_text(text)
