import os

from flask import Flask


def create_app(test_config=None):
    '''
    create_app is the application factory function.
    Create and configure the app
    '''
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder.
    # The instance folder is located outside the flaskr package and can hold local data that shouldn’t be committed to version control, such as configuration secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)
    # Set some default configuration that the app will use.
    app.config.from_mapping(
        SECRET_KEY='dev', # is used by Flask and extensions to keep data safe. It’s set to 'dev' to provide a convenient value during development, but it should be overridden with a random value when deploying.
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        # ensures that app.instance_path exists.
        os.makedirs(app.instance_path)
    except OSError:
            pass

    @app.route('/hello')
    def hello():
        return "Hello, World!"
    
    from . import db
    db.init_app(app)

    return app

