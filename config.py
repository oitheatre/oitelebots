import os
import yaml
basedir = os.path.abspath(os.path.dirname(__file__))

class FlaskConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TgBotConfig():
    def __init__(self):
        self.BOT_NAME = os.environ.get('BOT_NAME') or 'bot_template'
        with open('bot_settings.yml') as f:
            bot_settings = yaml.safe_load(f)

            self.BOT_TGNAME = bot_settings[self.BOT_NAME]['BOT_TGNAME']
            self.BOT_TOKEN = bot_settings[self.BOT_NAME]['BOT_TOKEN']
