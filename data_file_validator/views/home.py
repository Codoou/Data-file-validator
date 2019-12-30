from flask import render_template, Blueprint

home_page = Blueprint('home', __name__,
                    template_folder='templates',
                    url_prefix='/home')


@home_page.route('/')
def index():
    return render_template('home/index.html')

@home_page.route('/<id>')
def i_index(id):
    print('test')
    return render_template('home/test.html', data={'name':str(id)})
