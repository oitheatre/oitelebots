from app.bot_template import bot_template

@bot_template.route('/')
def index():
    return 'blueprint hellooo'
