from flask import render_template, Blueprint

config_page = Blueprint('config', __name__,
                    template_folder='templates')


@config_page.route('/')
def index():
    return render_template('config/index.html')