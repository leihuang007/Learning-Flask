'''
Certain objects in Flask are global objects, but not of the usual kind. 
These objects are actually proxies to objects that are local to a specific context. What a mouthful. But that is actually quite easy to understand.
'''

from flask import Flask, request

app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'