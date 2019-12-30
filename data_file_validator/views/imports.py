from flask import render_template, Blueprint

import_page = Blueprint('import', __name__,
                    template_folder='templates',
                    url_prefix='/import')


@import_page.route('/')
def index():
    return render_template('import/index.html')