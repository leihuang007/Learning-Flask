'''
A common response format when writing an API is JSON. 
It's easy to get started writing such an API with Flask. 
If you return a dict or list from a view, it will be converted to a JSON response.
'''
import json
from flask import Flask, url_for

app = Flask(__name__)


class User:
    def __init__(self, username: str, theme: str, image: str) -> None:
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self):
        return json.dumps(self, ensure_ascii=False, default=lambda obj: obj.__dict__)


@app.route("/me")
def me_api():
    user = User('Easton Huang', 'Dark Bulue', 'abc.png')
    return {
        'username': user.username,
        'theme': user.theme,
        'image': url_for("user_image", filename=user.image)
    }


@app.route("/users")
def users():
    users = [User('Easton Huang', 'Dark Bulue', 'abc.png'),
             User('Easton Huang2', 'Dark Bulue2', 'abc2.png')]
    return [user.to_json() for user in users]


@app.route("/profile_image")
def user_image():
    pass
