import os
import yaml
basedir = os.path.abspath(os.path.dirname(__file__))

class FlaskConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TgBotConfig():
    def __init__(self, bot_name):
        with open('bot_settings.yml') as f:
            bot_settings = yaml.safe_load(f)

            self.BOT_TOKEN = bot_settings[bot_name]['BOT_TOKEN']
