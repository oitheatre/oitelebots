from flask import Flask
from config import FlaskConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(FlaskConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app.bot_template import bot_template

app.register_blueprint(bot_template, url_prefix='/931254086:AAFfpBm-moEnm88BmHeuET2GzAs5j-EYEhg')

from app import routes, models