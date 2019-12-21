import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Blueprint
bot_template = Blueprint('bot_template', __name__, template_folder='templates')
from app.bot_template import routes

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
from config import TgBotConfig

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def bot():
    TOKEN = TgBotConfig('bot_template').BOT_TOKEN
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # log all errors
    dp.add_error_handler(error)

    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    port = 8443
    url = 'https://telegram.oitheatre.ru:{}/{}'.format(port, TOKEN)
    updater.start_webhook(listen='127.0.0.1',
                          port=port,
                          url_path=TOKEN)
    updater.bot.set_webhook(url=url, certificate=open('cert.pem', 'rb'))

    logger.info('running on {} port, TOKEN {}, url {}'.format(port, TOKEN, url))

    updater.idle()

bot()
