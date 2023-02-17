from flask import Flask
from markupsafe import escape

# An instance of class Flask will be our WSGI application.
# The first argument is the name of the application's module or package.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


@app.route('/')
def index():
    '''
    The index page.
    '''
    return 'Index page.'


@app.route('/projects/')
def projects():
    """
    Show the project page.
    If you access the URL without a trailing slash(/projects), Flask redirects you to the canonical URL with the trailing slash.
    """
    return 'The project page'


@app.route('/about')
def about():
    '''
    Show the about page.
    Access the URL with a trailing slash(/about/) produces a 404 "Not Found" error.
    This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
    '''
    return 'The about page'

# To run the application:
# flask --app app run --host=0.0.0.0 --debug
