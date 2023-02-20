'''
To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:
'''
from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    # Note the 404 after the render_template() call.
    # This tells Flask that the status code of that page should be 404 which means not found.
    # By default 200 is assumed which translates to: all went well.
    return render_template('page_not_found.html'), 404
