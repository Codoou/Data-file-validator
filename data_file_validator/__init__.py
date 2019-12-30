import os
from flask import Flask
from .views.home import home_page
from .views.config import config_page
from .views.imports import import_page

app = Flask(__name__)
app.config.from_object('data_file_validator.default_settings')
app.config.from_envvar('DATA_FILE_VALIDATOR_SETTINGS')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'data_file_validator.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)



app.register_blueprint(home_page)
app.register_blueprint(import_page)
app.register_blueprint(config_page)

print(app.url_map)