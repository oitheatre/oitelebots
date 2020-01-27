import importlib
from flask import Flask
from config import FlaskConfig, TgBotConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


def register_bot(bot_name):
    try:
        bp_module = importlib.import_module(f'app.{bot_name}')
        bot_module = importlib.import_module(f'app.{bot_name}.bot')

        bot = bot_module.Bot()
        app.register_blueprint(bp_module.bp, url_prefix=f'/{bot.TOKEN}')
    except ImportError as err:
        print('Error: ', err)


bot_config = TgBotConfig()

app = Flask(__name__)
app.config.from_object(FlaskConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

register_bot(bot_config.BOT_NAME)

from app import routes, models
