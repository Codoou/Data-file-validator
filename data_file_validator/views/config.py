from flask import render_template, Blueprint

config_page = Blueprint('config', __name__,
                    template_folder='templates',
                    url_prefix='/config')


@config_page.route('/')
def index():
    return render_template('config/index.html')