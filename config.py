import os
import yaml

basedir = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TgBotConfig:
    def __init__(self):
        self.BOT_NAME = os.environ.get('BOT_NAME') or 'oitestbot'
        self.DEBUG_MODE = True if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'] == 'development' else False

        with open('bot_settings.yml') as f:
            bot_settings = yaml.safe_load(f)

            self.HOST_URL = bot_settings['HOST_URL']
            self.BOT_PORT = bot_settings['DEV_PORT'] if self.DEBUG_MODE else bot_settings['PRODUCTION_PORT']

            if not self.BOT_NAME in bot_settings:
                raise KeyError(f"Your bot_settings file don't have info about {self.BOT_NAME}")
            self.BOT_TOKEN = bot_settings[self.BOT_NAME]['BOT_TOKEN']

            if self.DEBUG_MODE:
                self.BOT_DEBUG_PORT = self.BOT_PORT + bot_settings[self.BOT_NAME]['NUMBER_ID']
