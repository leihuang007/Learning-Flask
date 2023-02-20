from flask import Flask, request, render_template

app = Flask(__name__)


def valid_login(username: str, password: str) -> bool:
    """_summary_

    Args:
        username (str): _description_
        password (str): _description_

    Returns:
        bool: _description_
    """
    if username == 'Admin' and password == 'Admin':
        return True
    else:
        return False


def log_the_user_in(username: str) -> None:
    """_summary_

    Args:
        username (str): _description_
    """
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # To access parameters submitted in the URL(?key=value)
        # you can use the args attribute:
        # searchword = request.args.get('key', '')
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
