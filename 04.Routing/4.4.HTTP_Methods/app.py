'''
Web applications use different HTTP methods when accessing URLs. 
You should familiarize yourself with the HTTP methods as you work with Flask. 
By default, a route only answers to GET requests. 
You can use the methods argument of the route() decorator to handle different HTTP methods.
'''

from flask import Flask

# An instance of class Flask will be our WSGI application.
# The first argument is the name of the application's module or package.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    The example above keeps all methods for the route within one function, which can be useful if each part uses some common data.
    '''
    pass


@app.get('/login')
def login_get():
    '''
    You can also separate views for different methods into different functions. 
    Flask provides a shortcut for decorating such routes with get(), post(), etc. for each common HTTP method.
    '''
    pass


@app.post('/login')
def login_post():
    pass
