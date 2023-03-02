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
        # is used by Flask and extensions to keep data safe. It’s set to 'dev' to provide a convenient value during development, but it should be overridden with a random value when deploying.
        SECRET_KEY='dev',
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

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    # Unlike the auth blueprint, the blog blueprint does not have a url_prefix. So the index view will be at /, the create view at /create, and so on. The blog is the main feature of Flaskr, so it makes sense that the blog index will be the main index.
    app.add_url_rule('/', endpoint='index')

    return app
