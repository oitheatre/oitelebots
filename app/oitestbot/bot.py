from app.BaseBot.BaseBot import BaseBot
from telegram.ext import (MessageHandler, Filters)


def echo(update, context):
    update.message.reply_text(update.message.text)


class Bot(BaseBot):
    def __init__(self):
        super().__init__()
        self.dp.add_handler(MessageHandler(Filters.text, echo))

