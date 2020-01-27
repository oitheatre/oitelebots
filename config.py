import os
import yaml

basedir = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = 'localhost:5443'


class TgBotConfig():
    def __init__(self):
        self.BOT_NAME = os.environ.get('BOT_NAME') or 'bot_template'
        self.DEBUG_MODE = True if os.environ['FLASK_ENV'] == 'development' else False
        self.BOT_PORT = 8443 if self.DEBUG_MODE else 443

        with open('bot_settings.yml') as f:
            bot_settings = yaml.safe_load(f)

            self.BOT_TGNAME = bot_settings[self.BOT_NAME]['BOT_TGNAME']
            self.BOT_TOKEN = bot_settings[self.BOT_NAME]['BOT_TOKEN']
            if self.DEBUG_MODE:
                self.BOT_DEBUG_PORT = 8443 + bot_settings[self.BOT_NAME]['NUMBER_ID']
