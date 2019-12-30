from flask import render_template, Blueprint

from data_file_validator import app

home_page = Blueprint('home', __name__,
                      template_folder="templates")


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('home/index.html')
