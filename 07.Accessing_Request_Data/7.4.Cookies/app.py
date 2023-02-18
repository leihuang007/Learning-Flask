'''
To access cookies you can use the cookies attribute. 
To set cookies you can use the set_cookie method of response objects. 
The cookies attribute of request objects is a dictionary with all the cookies the client transmits. 
If you want to use sessions, do not use the cookies directly but instead use the Sessions in Flask that add some security on top of cookies for you.
'''
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f'Hello, {username}'
    else:
        return 'Nobody'


@app.route('/store_cookies')
def store_cookies():
    # resp = make_response(render_template('xxx.html'))
    resp = make_response('Cookes Set.')
    resp.set_cookie('username', 'John Doe')
    resp.set_cookie('password', 'secret')
    return resp
