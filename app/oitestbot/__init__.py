from flask import Blueprint
bp = Blueprint('oitestbot', __name__, template_folder='templates')

from app.oitestbot import routes
