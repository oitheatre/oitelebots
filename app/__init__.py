import importlib
from flask import Flask
from config import FlaskConfig, TgBotConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(FlaskConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models


def register_bot(bot_name):
    try:
        bp_module = importlib.import_module(f'app.{bot_name}')
        bot_module = importlib.import_module(f'app.{bot_name}.bot')

        bot = bot_module.Bot()
        app.register_blueprint(bp_module.bp, url_prefix=f'/{bot.TOKEN}')
    except ImportError as err:
        print('Error: ', err)


register_bot(TgBotConfig().BOT_NAME)
