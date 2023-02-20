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

# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name>
# as a keyword argument.
# Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>
# Converter types:
# string: (default)accepts any text without a slash
# int   : accepts positive integers
# float : accepts positive floating point values
# path  : like string but also accepts slashes
# uuid  : accepts UUID strings


@app.route('/user/<username>')
def show_user_profile(username):
    """
    Show the user profile for that user.
    """
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    '''
    show the post with the given id, the id is an integer.
    '''
    return f'Post {post_id}'

@app.route('/path/<path:sub_path>')
def show_subpath(sub_path):
    '''
    show the subpath after /path/
    '''
    return f'Subpath {escape(sub_path)}'
# To run the application:
# flask --app app run --host=0.0.0.0 --debug
