from flask import Flask

from website.blueprints.page import page
from website.extensions import debug_toolbar

def create_app():
    """
    Create a Flask application

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)
    extensions(app)

    return app


def extensions(app):
    """
    Register extensions

    :param app: Flask app instance
    :return: None
    """
    debug_toolbar.init_app(app)

    return None