from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    safe_str = f'Hello, {escape(name)}!'
    unsafe_str = f'Hello, {name}!'
    return f'''Safe-str:{safe_str}<br>Unsafe-str:{unsafe_str}'''