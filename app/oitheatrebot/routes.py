from app.oitheatrebot import bp

@bp.route('/')
def index():
    return 'oitheatre hello'
