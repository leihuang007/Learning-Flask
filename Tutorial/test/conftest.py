import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture
def app():
    # tempfile.mkstemp() creates and opens a temporary file, returning the file descriptor and the path to it.
    db_fd, db_path = tempfile.mkstemp()

    # The DATABASE path is overridden so it points to this temporary path instead of the instance folder.
    # TESTING tells Flask that the app is in test mode. Flask changes some internal behavior so it’s easier to test, and other extensions can also use the flag to make testing them easier.
    app = create_app({"TESTING": True, "DATABASE": db_path})

    # After setting the path, the database tables are created and the test data is inserted.
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    # After the test is over, the temporary file is closed and removed.
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)
