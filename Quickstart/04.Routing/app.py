from flask import Flask
from markupsafe import escape

# An instance of class Flask will be our WSGI application.
# The first argument is the name of the application's module or package.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    '''
    Todo.
    '''
    return 'Index page.'

@app.route('/hello')
def hello():
    """
    Todo.
    """
    return 'Hello, World'
# To run the application:
# flask --app app run --host=0.0.0.0 --debug