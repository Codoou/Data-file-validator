from flask import render_template, Blueprint

home_page = Blueprint('home', __name__,
                    template_folder='templates')


@home_page.route('/')
def index():
    return render_template('home/index.html')
