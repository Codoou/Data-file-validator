from flask import render_template, Blueprint

from data_file_validator.logic.import_logic import ImportLogic
import_page = Blueprint('import', __name__,
                    template_folder='templates',
                    url_prefix='/import')


@import_page.route('/')
def index():
    json = ImportLogic.GetImports()
    return render_template('import/index.html', data=json)