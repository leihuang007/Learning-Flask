from flask import Flask
from markupsafe import escape

# An instance of class Flask will be our WSGI application.
# The first argument is the name of the application's module or package.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger our function.
# <name> in the route captures a value from the URL and passes it to the view function.
@app.route('/<name>')
def hello(name):
    '''
    When returning HTML(the default response type in Flask), any user-provided values rendered in the output must be
    escaped to protect from injection attacks. 
    HTML templates rendered with Jinja, introduced later, will do this automatically.
    '''
    return f'<h1>Hello, {escape(name)}</h1>'

# To run the application:
# flask --app app run --host=0.0.0.0 --debug