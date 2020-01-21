from app.bot_template import bp

@bp.route('/')
def index():
    return 'blueprint hellooo'
