from flask import Flask

# An instance of class Flask will be our WSGI application.
# The first argument is the name of the application's module or package.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def hello():
    return '<h1>Hello, World</h1>'

# To run the application:
# flask --app app run --host=0.0.0.0 --debug