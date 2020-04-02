from flask import Blueprint
bp = Blueprint('oitheatrebot', __name__, template_folder='templates')

from app.oitheatrebot import routes
