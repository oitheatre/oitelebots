import abc
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram.ext import (Updater, CommandHandler)
from config import TgBotConfig

def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


class BaseBot(metaclass=abc.ABCMeta):
    def __init__(self):
        tgConfig = TgBotConfig()
        self.TOKEN = tgConfig.BOT_TOKEN
        self.BOT_NAME = tgConfig.BOT_NAME
        self.DEBUG_MODE = tgConfig.DEBUG_MODE

        # Start the Bot
        port = tgConfig.BOT_PORT
        url = 'https://{0}:{1}/{2}'.format(tgConfig.HOST_URL, port, self.TOKEN)

        if not self.DEBUG_MODE or not is_port_in_use(port):  # yes, this is weird; for FLASK_ENV development mode
            logger.info('Starting bot {0}{1}'.format(self.BOT_NAME, ' in development mode' if self.DEBUG_MODE else ''))
            updater = Updater(self.TOKEN, use_context=True)

            # Get the dispatcher to register handlers
            dp = updater.dispatcher

            # log all errors
            dp.add_error_handler(self.error)

            dp.add_handler(CommandHandler("start", self.start))

            updater.start_webhook(listen='0.0.0.0',
                                  port=port,
                                  url_path=self.TOKEN)
            updater.bot.set_webhook(url=url, certificate=open('telegram_ssl/cert.pem', 'rb'))

            self.dp = dp
            self.updater = updater

            logger.info('running bot {0} on {1} port, with TOKEN {2}, webhook url {3}'.format(self.BOT_NAME, port, self.TOKEN, url))
            logger.info('you can check your webhook status here https://api.telegram.org/bot{0}/getWebhookInfo'.format(self.TOKEN))

            if self.DEBUG_MODE:
                logger.info('do not forget to forward ports in development mode: ssh -i /path/to/private.key -R {0}:127.0.0.1:{1} -N tgbot@{2}'.format(tgConfig.BOT_DEBUG_PORT, tgConfig.BOT_PORT, tgConfig.HOST_URL))

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)

    @abc.abstractmethod
    def start(self, update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text('You have to change this text for yours')

