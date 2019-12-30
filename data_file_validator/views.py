from flask import render_template

from data_file_validator import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('home/index.html')
