from app.oimailbot import bp

@bp.route('/')
def index():
    return 'mailbot hellooo'
