from flask import Blueprint
bp = Blueprint('bot_template', __name__, template_folder='templates')

from app.bot_template import routes
