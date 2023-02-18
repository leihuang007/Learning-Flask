'''
To render a template you can use the render_template() method. 
All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. 
Flask will look for templates in the templates folder. 
So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<string:name>')
def hello(name=None):
    return render_template('hello.html', name=name)
