from flask import Blueprint
bp = Blueprint('oimailbot', __name__, template_folder='templates')

from app.oimailbot import routes
