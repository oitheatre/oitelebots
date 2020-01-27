from app.oitestbot import bp

@bp.route('/')
def index():
    return 'blueprint hellooo'
