from flask import Flask

def create_app():
    """
    Create a Flask application

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def hello_world():
        """
        Render a Hello World reponse.

        :return: Flask response
        """
        return "Hello World"

    return app