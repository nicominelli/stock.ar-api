import logging as log
from logging.config import dictConfig

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.serving import WSGIRequestHandler as WHandler

from config import app_config
from .utils.environment import get_env, Environment
from .utils.error_codes import ErrorCode
from .utils.error_handler import ErrorHandler
from .utils.error_handler import register_error_handler, register_login_handler

db = SQLAlchemy()
migrate = Migrate()


def logging_setup(level='DEBUG'):
    logger = log.getLogger('werkzeug')
    WHandler.log = lambda self, type, m, *args: \
        getattr(logger, type)('%s %s' % (self.address_string(), m % args))
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] [level:%(levelname)s] %(message)s',
            'datefmt': '%m/%d/%Y %I:%M:%S',
        }},
        'handlers': {'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }},
        'root': {
            'level': level,
            'handlers': ['console']
        }
    })


def create_app(env: Environment):
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    logging_setup(app.config['LOG_LEVEL'])
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.init_app(app)
        import app.utils.db_util as db_util
        db_util.check_db()

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    register_error_handler(app)

    return app


from app import models
